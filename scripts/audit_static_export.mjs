import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.join(path.dirname(fileURLToPath(import.meta.url)), "..", "site", "out");

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
const articleFiles = htmlFiles.filter((file) => file.includes(`${path.sep}blog${path.sep}`));
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

  if (file.includes(`${path.sep}blog${path.sep}`) && file.endsWith("index.html")) {
    const required = [
      'rel="canonical"',
      "건강정보 이용 안내",
      "편집팀 참고자료",
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
  articleFiles: articleFiles.filter((file) => file.endsWith("index.html")).length,
  fullyMarkedArticles: articleChecks,
  brokenInternalLinks: brokenLinks,
  missingRequiredFiles: requiredFiles,
};

console.log(JSON.stringify(report, null, 2));

if (brokenLinks.length || requiredFiles.length || articleChecks !== 106) process.exitCode = 1;
