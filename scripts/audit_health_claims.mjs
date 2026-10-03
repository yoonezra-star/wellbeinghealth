import fs from "node:fs";
import path from "node:path";
import assert from "node:assert/strict";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const rootDirectory = path.join(scriptDirectory, "..");
const siteDirectory = path.join(rootDirectory, "site");
const postsDirectory = path.join(siteDirectory, "content", "posts");
const reportsDirectory = path.join(rootDirectory, "reports");
const require = createRequire(path.join(siteDirectory, "package.json"));
const matter = require("gray-matter");

const clinicalPattern =
  /(암|당뇨|치매|골다공증|우울증|공황|비염|불면증|탈모|디스크|혈압|혈당|콜레스테롤|호르몬|면역|염증|만성피로|통증)/g;
const guaranteePattern =
  /(완치|치료한다|예방한다|없애준다|잡아준다|해독|독소 배출|기적|극대화|반드시|확실한|무조건|100%|과학이 증명|입증되었다)/g;
const personalPattern = /(저는|제가|저도|제 경험|직접 경험|경험했습니다)/g;
const statisticPattern = /\d+(?:\.\d+)?\s*(?:%|배|kg|g|mg|분|시간)/g;
const carePattern = /(의료진|의료기관|진료|응급|중단|의사|약사|임상영양사)/g;
const linkPattern = /https?:\/\/[^)\s]+/g;
const generated = new Intl.DateTimeFormat("en-CA", {
  timeZone: "Asia/Seoul",
}).format(new Date());

function countMatches(value, pattern) {
  return (value.match(pattern) || []).length;
}

function countGuaranteeClaims(value) {
  let count = 0;
  for (const match of value.matchAll(guaranteePattern)) {
    const previousCharacter = value.slice(Math.max(0, match.index - 1), match.index);
    const followingText = value.slice(match.index + match[0].length, match.index + match[0].length + 24);

    if (match[0] === "기적" && previousCharacter === "장") continue;
    if (match[0] === "확실한" && previousCharacter === "불") continue;
    if (match[0] === "반드시" && /(필요(?:는)?\s*없|않|아니|없|못)/.test(followingText)) continue;
    count += 1;
  }
  return count;
}

assert.equal(
  countGuaranteeClaims("장기적인 효과는 불확실하며, 공복 시간을 반드시 늘릴 필요는 없습니다."),
  0
);
assert.equal(countGuaranteeClaims("이 식품은 감염을 예방한다."), 1);

const results = fs
  .readdirSync(postsDirectory)
  .filter((fileName) => fileName.endsWith(".md"))
  .map((fileName) => {
    const parsed = matter(fs.readFileSync(path.join(postsDirectory, fileName), "utf8"));
    const title = String(parsed.data.title || fileName);
    const content = parsed.content;
    const links = countMatches(content, linkPattern);
    const clinical = countMatches(`${title}\n${content}`, clinicalPattern);
    const guarantees = countGuaranteeClaims(`${title}\n${content}`);
    const personal = countMatches(content, personalPattern);
    const statistics = countMatches(content, statisticPattern);
    const careSignals = countMatches(content, carePattern);

    let score = Math.min(clinical, 6);
    score += Math.min(guarantees * 2, 12);
    score += Math.min(personal, 3);
    score += statistics > 0 ? 2 : 0;
    score += links === 0 ? 5 : links === 1 ? 2 : 0;
    score += clinical > 0 && careSignals === 0 ? 4 : 0;

    const level = score >= 15 ? "high" : score >= 8 ? "review" : "lower";
    return {
      fileName,
      title,
      score,
      level,
      clinical,
      guarantees,
      personal,
      statistics,
      links,
      careSignals,
    };
  })
  .sort((a, b) => b.score - a.score || a.title.localeCompare(b.title, "ko"));

const summary = {
  audited: results.length,
  high: results.filter((result) => result.level === "high").length,
  review: results.filter((result) => result.level === "review").length,
  lower: results.filter((result) => result.level === "lower").length,
  noDirectLinks: results.filter((result) => result.links === 0).length,
};

const tableRows = results
  .map(
    (result) =>
      `| ${result.score} | ${result.level} | ${result.title.replaceAll("|", "\\|")} | ${result.links} | ${result.careSignals} | \`${result.fileName}\` |`
  )
  .join("\n");

const markdown = `# 건강 주장 자동 점검 보고서

생성일: ${generated}

이 보고서는 질환명, 보장성 표현, 수치 주장, 직접 링크와 안전 문구를 기준으로 편집 우선순위를 정하는 휴리스틱 점검입니다. 점수는 의학적 오류 판정이나 애드센스 승인 보장을 뜻하지 않습니다.

## 요약

- 점검 글: ${summary.audited}개
- 우선 수정(high): ${summary.high}개
- 검토 필요(review): ${summary.review}개
- 낮은 우선순위(lower): ${summary.lower}개
- 본문 직접 링크 없음: ${summary.noDirectLinks}개

## 판정 기준

- 질환·증상 용어가 많을수록 검토 점수 증가
- 완치, 예방 보장, 해독, 기적 등 단정 표현에 높은 가중치
- 출처 링크가 없거나 안전·진료 문구가 없으면 가중치 추가
- 개인 경험과 구체적인 수치 주장이 있으면 직접 근거 확인 필요

## 전체 우선순위

| 점수 | 단계 | 글 제목 | 직접 링크 | 안전 신호 | 파일 |
| ---: | --- | --- | ---: | ---: | --- |
${tableRows}
`;

fs.mkdirSync(reportsDirectory, { recursive: true });
fs.writeFileSync(
  path.join(reportsDirectory, "health-claims-audit.json"),
  `${JSON.stringify({ generated, summary, results }, null, 2)}\n`,
  "utf8"
);
fs.writeFileSync(path.join(reportsDirectory, "health-claims-audit.md"), markdown, "utf8");

console.log(JSON.stringify(summary, null, 2));
