import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const siteDirectory = path.join(scriptDirectory, "..", "site");
const postsDirectory = path.join(siteDirectory, "content", "posts");
const require = createRequire(path.join(siteDirectory, "package.json"));
const matter = require("gray-matter");

const mismatchedSummaryFiles = new Set([
  "2026-05-25-지방을-태우는-고강도-운동의-비밀-최적의-다이어트.md",
  "2026-06-19-유산소-운동의-모든-것-건강을-위한-필수-가이드.md",
  "2026-06-13-유산소-운동의-놀라운-효과-건강한-삶을-위한-필수-요.md",
  "2026-06-04-일상-속-유산소-운동-건강을-위한-작은-변화.md",
  "2026-05-30-코어-강화를-위한-효과적인-운동-루틴.md",
  "2026-05-28-유산소-운동의-놀라운-건강-혜택과-시작하는-방법-2.md",
]);

const titleReplacements = new Map([
  [
    "만성피로: 전문가의 시각과 최신 연구로 본 실질적 분석",
    "만성피로를 이해하는 핵심 관점: 원인과 확인할 신호",
  ],
  [
    "영양제, 독이 될 수 있다? 전문가가 전하는 오남용의 위험과 성분 분석",
    "영양제 오남용 위험과 성분표 확인 기준",
  ],
  [
    "비만보다 더 심각한 대사 질환, 전문가가 제안하는 예방 및 치료 전략",
    "대사질환 위험을 낮추는 생활관리 원칙",
  ],
  [
    "우리 아이 키 성장의 비밀: 전문가의 인사이트와 환경 개선 전략",
    "아이 성장에 영향을 주는 수면·영양·활동 환경",
  ],
  [
    "현대인의 불면증: 전문가가 제안하는 효과적인 숙면 솔루션",
    "현대인의 불면증: 숙면 환경과 진료가 필요한 신호",
  ],
  [
    "두피 검사와 탈모 치료의 골든타임: 전문가가 제안하는 최적의 접근법",
    "두피 검사와 탈모 치료 시기: 조기 평가가 중요한 이유",
  ],
  [
    "명상으로 스트레스를 극복하는 혁신적 접근법: 최신 연구와 전문가 팁",
    "명상으로 스트레스를 관리하는 방법: 실천 순서와 주의점",
  ],
]);

const repeatedStrengthPackage =
  /## 편집자 핵심 요약[\s\S]*?## 실천 전 체크리스트[\s\S]*?## 한눈에 보는 적용 기준[\s\S]*?(?=\n## )/;

let updatedFiles = 0;
let renamedCategories = 0;
let revisedTitles = 0;
let removedPackages = 0;
let correctedGuidelines = 0;

for (const fileName of fs.readdirSync(postsDirectory).filter((name) => name.endsWith(".md"))) {
  const filePath = path.join(postsDirectory, fileName);
  const parsed = matter(fs.readFileSync(filePath, "utf8"));
  const data = { ...parsed.data };
  let content = parsed.content;
  let changed = false;

  if (data.category === "전문가칼럼") {
    data.category = "건강해설";
    renamedCategories += 1;
    changed = true;
  }

  const replacementTitle = titleReplacements.get(data.title);
  if (replacementTitle) {
    data.title = replacementTitle;
    revisedTitles += 1;
    changed = true;
  }

  if (mismatchedSummaryFiles.has(fileName) && repeatedStrengthPackage.test(content)) {
    content = content.replace(repeatedStrengthPackage, "").replace(/\n{3,}/g, "\n\n");
    removedPackages += 1;
    changed = true;
  }

  const correctedContent = content.replace(
    "하루 최소 150분의 중간 강도의 운동",
    "일주일에 총 150분의 중간 강도 운동"
  );
  if (correctedContent !== content) {
    content = correctedContent;
    correctedGuidelines += 1;
    changed = true;
  }

  if (!changed) continue;

  data.updated = "2026-08-09";
  fs.writeFileSync(filePath, matter.stringify(content.trimStart(), data), "utf8");
  updatedFiles += 1;
}

console.log(
  JSON.stringify(
    { updatedFiles, renamedCategories, revisedTitles, removedPackages, correctedGuidelines },
    null,
    2
  )
);
