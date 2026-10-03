import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.join(path.dirname(fileURLToPath(import.meta.url)), "..", "site", "out");
const postsRoot = path.join(path.dirname(root), "content", "posts");

function walk(directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const target = path.join(directory, entry.name);
    return entry.isDirectory() ? walk(target) : [target];
  });
}

function routeTarget(href) {
  const pathname = decodeURIComponent(href.split(/[?#]/)[0]);
  if (!pathname || pathname === "/") return path.join(root, "index.html");
  const relative = pathname.replace(/^\//, "");
  return path.extname(relative)
    ? path.join(root, relative)
    : path.join(root, relative, "index.html");
}

const htmlFiles = walk(root).filter((file) => file.endsWith(".html"));
const blogRoot = path.join(root, "blog");
const articleFiles = htmlFiles.filter(
  (file) =>
    file.startsWith(`${blogRoot}${path.sep}`) &&
    file !== path.join(blogRoot, "index.html") &&
    path.basename(file) === "index.html"
);
const articleFileSet = new Set(articleFiles);
const expectedArticleCount = fs
  .readdirSync(postsRoot)
  .filter((file) => file.endsWith(".md")).length;
const brokenLinks = [];
let articleChecks = 0;

for (const file of htmlFiles) {
  const html = fs.readFileSync(file, "utf8");
  const hrefs = [...html.matchAll(/href="([^"]+)"/g)].map((match) => match[1]);

  for (const href of hrefs) {
    if (/^(https?:|mailto:|#)/.test(href)) continue;
    const target = routeTarget(href);
    if (!fs.existsSync(target)) brokenLinks.push({ file: path.relative(root, file), href });
  }

  if (articleFileSet.has(file)) {
    const required = [
      'rel="canonical"',
      "건강정보 이용 안내",
      "주제별 일반 참고자료",
      "관련 아티클",
      '"@type":"BlogPosting"',
      'google-adsense-account',
    ];
    if (required.every((marker) => html.includes(marker))) articleChecks += 1;
  }
}

const requiredFiles = ["ads.txt", "robots.txt", "sitemap.xml"].filter(
  (file) => !fs.existsSync(path.join(root, file))
);

const report = {
  htmlFiles: htmlFiles.length,
  articleFiles: articleFiles.length,
  expectedArticleCount,
  fullyMarkedArticles: articleChecks,
  brokenInternalLinks: brokenLinks,
  missingRequiredFiles: requiredFiles,
};

console.log(JSON.stringify(report, null, 2));

if (brokenLinks.length || requiredFiles.length || articleChecks !== expectedArticleCount) {
  process.exitCode = 1;
}
