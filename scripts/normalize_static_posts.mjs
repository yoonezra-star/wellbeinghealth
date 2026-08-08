import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const postsDirectory = path.join(scriptDirectory, "..", "site", "content", "posts");

const namedEntities = new Map([
  ["nbsp", " "],
  ["amp", "&"],
  ["quot", '"'],
  ["apos", "'"],
  ["lt", "<"],
  ["gt", ">"],
  ["hellip", "..."],
  ["ndash", "-"],
  ["mdash", "-"],
  ["lsquo", "'"],
  ["rsquo", "'"],
  ["ldquo", '"'],
  ["rdquo", '"'],
]);

function decodeEntities(value) {
  return value
    .replace(/&#(\d+);/g, (_, code) => String.fromCodePoint(Number(code)))
    .replace(/&#x([0-9a-f]+);/gi, (_, code) => String.fromCodePoint(parseInt(code, 16)))
    .replace(/&([a-z]+);/gi, (entity, name) => namedEntities.get(name.toLowerCase()) ?? entity);
}

let entityFiles = 0;
let headingFiles = 0;

for (const fileName of fs.readdirSync(postsDirectory).filter((name) => name.endsWith(".md"))) {
  const filePath = path.join(postsDirectory, fileName);
  const original = fs.readFileSync(filePath, "utf8");
  let normalized = decodeEntities(original);

  if (normalized !== original) entityFiles += 1;

  const frontmatterEnd = normalized.indexOf("---", 3);
  const header = normalized.slice(0, frontmatterEnd + 3);
  let body = normalized.slice(frontmatterEnd + 3);

  if (!/^##\s+/m.test(body) && /^###\s+/m.test(body)) {
    body = body.replace(/^(#{3,6})\s+/gm, (_, hashes) => `${hashes.slice(1)} `);
    headingFiles += 1;
  }

  normalized = `${header}${body}`;
  if (normalized !== original) fs.writeFileSync(filePath, normalized, "utf8");
}

console.log(`Normalized entities in ${entityFiles} files and heading levels in ${headingFiles} files.`);
