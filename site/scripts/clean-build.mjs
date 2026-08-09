import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const siteDirectory = path.dirname(path.dirname(fileURLToPath(import.meta.url)));

for (const directoryName of [".next", "out"]) {
  const target = path.join(siteDirectory, directoryName);
  fs.rmSync(target, { recursive: true, force: true });
}

console.log("Removed stale Next.js build output.");
