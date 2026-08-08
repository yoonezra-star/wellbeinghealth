const { execFileSync } = require("child_process");
const fs = require("fs");
const path = require("path");
const matter = require(path.join(__dirname, "..", "site", "node_modules", "gray-matter"));

const SITE_DIR = path.join(__dirname, "..", "site");
const POSTS_DIR = path.join(SITE_DIR, "content", "posts");
const IMAGES_DIR = path.join(SITE_DIR, "public", "images", "wordpress");
const WP_HOST = process.env.WP_HOST || "wellbeinghealth.co.kr";
const WP_ORIGIN_IP = process.env.WP_ORIGIN_IP || "";

const CATEGORY_BY_ID = {
  3: "운동",
  4: "다이어트",
  5: "생활습관",
  6: "멘탈케어",
  7: "전문가칼럼",
  8: "건강식단",
};

const NAMED_ENTITIES = {
  amp: "&", apos: "'", gt: ">", hellip: "...", ldquo: "\"", lsquo: "'",
  lt: "<", mdash: "-", nbsp: " ", ndash: "-", quot: "\"", rdquo: "\"", rsquo: "'",
};

function decodeHtml(value) {
  return String(value || "").replace(/&(#x[0-9a-f]+|#\d+|[a-z]+);/gi, (match, entity) => {
    const lower = entity.toLowerCase();
    if (lower.startsWith("#x")) return String.fromCodePoint(parseInt(lower.slice(2), 16));
    if (lower.startsWith("#")) return String.fromCodePoint(parseInt(lower.slice(1), 10));
    return NAMED_ENTITIES[lower] || match;
  });
}

function stripHtml(value) {
  return decodeHtml(String(value || "").replace(/<[^>]*>/g, "").replace(/\s+/g, " ")).trim();
}

function requestJson(url) {
  const args = ["-fsSL"];
  if (WP_ORIGIN_IP) args.push("--resolve", `${WP_HOST}:443:${WP_ORIGIN_IP}`);
  args.push(url);
  return JSON.parse(execFileSync("curl.exe", args, { encoding: "utf8", maxBuffer: 16 * 1024 * 1024 }));
}

function getExtension(url) {
  const extension = path.extname(new URL(url).pathname).toLowerCase();
  return /^\.(avif|gif|jpe?g|png|webp)$/.test(extension) ? extension : ".webp";
}

function downloadImage(url, name) {
  if (!url) return "";
  const targetName = `${name}${getExtension(url)}`;
  const targetPath = path.join(IMAGES_DIR, targetName);
  if (!fs.existsSync(targetPath)) {
    const args = ["-fsSL"];
    if (WP_ORIGIN_IP) args.push("--resolve", `${WP_HOST}:443:${WP_ORIGIN_IP}`);
    args.push(url, "-o", targetPath);
    execFileSync("curl.exe", args, { stdio: "inherit" });
  }
  return `/images/wordpress/${targetName}`;
}

function getImageSource(post) {
  const images = post.featured_image_url || {};
  return images.large || images.medium_large || images.full || images.medium || images.thumbnail || "";
}

function htmlToMarkdown(html, postId) {
  let imageIndex = 0;
  let output = String(html || "").replace(/<figure[^>]*>\s*<img\b[^>]*>\s*<\/figure>/gi, "");
  output = output.replace(/<img\b([^>]*)>/gi, (match, attributes) => {
    const srcMatch = attributes.match(/\bsrc=["']([^"']+)["']/i);
    if (!srcMatch) return "";
    const altMatch = attributes.match(/\balt=["']([^"']*)["']/i);
    const imagePath = downloadImage(decodeHtml(srcMatch[1]), `wp-${postId}-inline-${imageIndex++}`);
    return imagePath ? `\n\n![${decodeHtml(altMatch ? altMatch[1] : "")}](${imagePath})\n\n` : "";
  });
  output = output
    .replace(/<h2[^>]*>([\s\S]*?)<\/h2>/gi, (_, text) => `\n\n## ${stripHtml(text)}\n\n`)
    .replace(/<h3[^>]*>([\s\S]*?)<\/h3>/gi, (_, text) => `\n\n### ${stripHtml(text)}\n\n`)
    .replace(/<h(?:1|[4-6])[^>]*>([\s\S]*?)<\/h[1-6]>/gi, (_, text) => `\n\n### ${stripHtml(text)}\n\n`)
    .replace(/<li[^>]*>([\s\S]*?)<\/li>/gi, (_, text) => `- ${stripHtml(text)}\n`)
    .replace(/<p[^>]*>([\s\S]*?)<\/p>/gi, (_, text) => `\n\n${stripHtml(text)}\n\n`)
    .replace(/<br\s*\/?>/gi, "\n")
    .replace(/<[^>]*>/g, "");
  return decodeHtml(output).replace(/\n{3,}/g, "\n\n").trim();
}

function normalizedTitle(value) {
  return stripHtml(value).replace(/\s+/g, " ").trim();
}

function getCategory(post) {
  return post.categories.map((id) => CATEGORY_BY_ID[id]).find(Boolean) || "건강";
}

function trimLineEnds(value) {
  if (typeof value !== "string") return value;
  return value.split(/\r?\n/).map((line) => line.trimEnd()).join("\n");
}

function main() {
  fs.mkdirSync(IMAGES_DIR, { recursive: true });
  const firstPage = requestJson(`https://${WP_HOST}/wp-json/wp/v2/posts?per_page=100&page=1`);
  const secondPage = requestJson(`https://${WP_HOST}/wp-json/wp/v2/posts?per_page=100&page=2`);
  const posts = [...firstPage, ...secondPage];
  const localPosts = new Map();

  for (const fileName of fs.readdirSync(POSTS_DIR).filter((name) => name.endsWith(".md"))) {
    const fullPath = path.join(POSTS_DIR, fileName);
    const parsed = matter(fs.readFileSync(fullPath, "utf8"));
    localPosts.set(normalizedTitle(parsed.data.title), { fullPath, parsed });
  }

  let updated = 0;
  let added = 0;
  for (const post of posts) {
    const title = normalizedTitle(post.title.rendered);
    const thumbnail = downloadImage(getImageSource(post), `wp-${post.id}-featured`);
    const existing = localPosts.get(title);

    if (existing) {
      const expectedPath = path.join(POSTS_DIR, `${post.date.slice(0, 10)}-${decodeURIComponent(post.slug)}.md`);
      if (existing.fullPath !== expectedPath) {
        fs.renameSync(existing.fullPath, expectedPath);
        existing.fullPath = expectedPath;
      }
      const data = Object.fromEntries(
        Object.entries({ ...existing.parsed.data, category: getCategory(post), thumbnail })
          .map(([key, value]) => [key, trimLineEnds(value)])
      );
      const content = existing.parsed.content.trim().replace(/[ \t]+$/gm, "");
      fs.writeFileSync(existing.fullPath, matter.stringify(content + "\n", data));
      updated += 1;
      continue;
    }

    const date = post.date.slice(0, 10);
    const data = {
      title,
      date,
      category: getCategory(post),
      excerpt: stripHtml(post.excerpt.rendered).slice(0, 180),
      metaDescription: stripHtml(post.excerpt.rendered).slice(0, 160),
      thumbnail,
    };
    const filePath = path.join(POSTS_DIR, `${date}-${decodeURIComponent(post.slug)}.md`);
    fs.writeFileSync(filePath, matter.stringify(`${htmlToMarkdown(post.content.rendered, post.id)}\n`, data));
    added += 1;
  }
  console.log(`Synced ${posts.length} WordPress posts: ${updated} updated, ${added} added.`);
}

main();
