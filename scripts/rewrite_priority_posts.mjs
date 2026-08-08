import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const siteDirectory = path.join(scriptDirectory, "..", "site");
const postsDirectory = path.join(siteDirectory, "content", "posts");
const require = createRequire(path.join(siteDirectory, "package.json"));
const matter = require("gray-matter");

const priorityPosts = new Map([
  [
    "2026-03-15-굶지-않고-살-빼는-고단백-다이어트-식단-근육-유지의.md",
    {
      title: "고단백 다이어트 식단: 근육 유지를 위한 구성 원칙",
      description: "고단백 식단을 구성할 때 필요한 단백질, 탄수화물, 지방의 역할과 근육 손실을 줄이기 위한 실천 기준을 정리합니다.",
    },
  ],
  [
    "2026-03-15-내-몸의-청소-시간-간헐적-단식-다이어트-조절법과-주.md",
    {
      title: "간헐적 단식 조절법과 주의사항: 식사 시간과 안전 기준",
      description: "간헐적 단식의 기본 방식과 적용할 때 살펴야 할 영양, 수분 섭취, 중단 신호와 주의 대상을 정리합니다.",
    },
  ],
  [
    "2026-03-15-체중계-숫자보다-체지방-감량-집중하는-다이어트-성.md",
    {
      title: "체중보다 체지방 변화에 집중하는 건강한 감량 전략",
      description: "체중의 일시적인 변화와 체지방 감소를 구분하고, 무리하지 않는 식사와 운동 기록 방법을 알아봅니다.",
    },
  ],
  [
    "2026-03-16-나이-들수록-중요한-근력-강화-운동-기초-대사량-증진.md",
    {
      title: "중장년 근력 강화 운동: 기초 원리와 안전한 시작법",
      description: "나이가 들수록 중요한 근력 운동의 기본 원칙과 초보자가 강도를 안전하게 조절하는 방법을 정리합니다.",
    },
  ],
  [
    "2026-03-16-무릎-아프지-않게-운동-관절-보호-수칙과-올바른-자세.md",
    {
      title: "무릎 부담을 줄이는 운동 자세와 관절 보호 수칙",
      description: "무릎 부담을 줄이는 운동 자세와 강도 조절, 운동을 멈추고 진료를 고려해야 하는 증상을 정리합니다.",
    },
  ],
  [
    "2026-03-16-헬스장-안-가도-몸짱-되는-홈트레이닝-운동-기구-활용.md",
    {
      title: "집에서 시작하는 홈트레이닝: 기구 활용과 안전 수칙",
      description: "집에서 운동할 때 활용할 수 있는 기본 기구와 공간 구성, 부상 위험을 줄이는 운동 순서를 안내합니다.",
    },
  ],
]);

const personalClaimPattern =
  /[^.!?\n]*(?:저 역시|저 또한|제가|저는|저도|저의 경험|제 실전 경험|제 경험|제 모습|제 몸|아버지|동료)[^.!?\n]*[.!?]\s*/g;

function removePersonalClaims(content) {
  return content
    .split("\n")
    .map((line) => {
      if (/^(#|\s*[-*]\s|\s*\d+\.\s)/.test(line)) return line;
      return line.replace(personalClaimPattern, "").trim();
    })
    .join("\n")
    .replace(/\n{3,}/g, "\n\n");
}

let updatedFiles = 0;

for (const [fileName, editorial] of priorityPosts) {
  const filePath = path.join(postsDirectory, fileName);
  const parsed = matter(fs.readFileSync(filePath, "utf8"));
  let content = removePersonalClaims(parsed.content);

  content = content
    .replace(
      /내 몸의 청소 시간 간헐적 단식 다이어트 조절법과 주의사항은 단순히 굶는 것이 아니라 우리 몸이 스스로를 치유할 수 있는 귀중한 여유를 허락하는 지혜로운 습관입니다\./g,
      "간헐적 단식은 하루 중 식사 가능한 시간을 제한하는 식사 패턴입니다. 체중과 대사 지표에 미치는 영향은 전체 섭취량, 식사의 질, 활동량과 개인 건강 상태에 따라 달라질 수 있습니다."
    )
    .replace(
      /간헐적 단식은 우리 몸속의 세포들이 쌓인 노폐물을 청소하고 에너지를 효율적으로 재배치하는 ‘오토파지’ 현상을 활성화하는 가장 자연스러운 방법입니다\./g,
      "단식과 세포 대사에 관한 연구가 진행되고 있지만, 사람에게서 특정 단식 시간이 세포 청소 효과를 보장한다고 단정하기는 어렵습니다."
    )
    .replace(
      /하지만 마지막 식사 후 약 12시간이 지나면 혈중 포도당이 소진되면서 우리 몸은 비축해둔 ‘지방’을 꺼내 쓰기 시작합니다\./g,
      "공복이 길어지면 저장된 에너지를 사용하는 비율이 달라질 수 있지만, 전환 시점은 이전 식사와 활동량 등 개인 조건에 따라 다릅니다."
    )
    .replace(
      /16시간 이상 공복을 유지하면 지방 연소 효율이 극대화되며, 몸속의 낡은 단백질을 재활용하는 오토파지 시스템이 가동됩니다\./g,
      "사람 대상 연구만으로 16시간이라는 기준이 지방 연소나 오토파지를 극대화한다고 확정할 수는 없습니다."
    )
    .replace(
      /지방 세포 속에 저장되어 있던 독소들이 지방이 타면서 함께 배출되기 때문이죠\./g,
      "체중 변화만으로 염증이나 피부 상태가 개선된다고 단정할 수 없으며, 이른바 독소 배출이라는 표현도 의학적으로 명확한 개념이 아닙니다."
    )
    .replace(
      /단식 시간이 길어질수록 성장 호르몬 수치가 치솟아 근육 손실을 방지하고 체지방 위주의 감량을 돕습니다\./g,
      "단식 시간이 지나치게 길거나 단백질과 전체 열량이 부족하면 근육량 유지에 불리할 수 있습니다."
    )
    .replace(
      /당분이 섞인 음료는 아주 소량이라도 인슐린을 자극해 지방 연소 모드를 즉시 중단시킨다는 점을 명심해야 합니다\./g,
      "열량이 있는 음료는 단식 중 섭취량에 포함되므로 목표와 건강 상태에 맞춰 선택해야 합니다."
    )
    .replace(/체중 1kg당 단백질 1\.5~2g 목표/g, "개인 상태에 맞는 단백질 필요량 확인")
    .replace(
      /두통이 심할 때는 물에 천일염을 한 꼬집 섞어 마시면 전해질 불균형이 해소되어 금세 가라앉기도 합니다\./g,
      "두통이나 심한 무기력감이 계속되면 단식을 중단하고 수분을 섭취한 뒤, 증상이 낫지 않으면 의료 전문가와 상담해야 합니다. 소금이나 보충제를 임의로 추가하는 것은 혈압과 복용 약에 따라 문제가 될 수 있습니다."
    )
    .replace(
      /건강한 일반인의 경우 체중 1kg당 1\.5~2g 정도의 단백질 섭취는 큰 문제가 되지 않습니다\./g,
      "필요한 단백질 양은 연령, 활동량, 전체 섭취 열량과 건강 상태에 따라 달라지므로 하나의 수치를 모든 사람에게 적용할 수 없습니다."
    )
    .replace(
      /만약 이 중 3개 이상에 해당한다면 즉시 운동 강도를 낮추고 전문의의 진단을 받아야 합니다\./g,
      "항목 수와 관계없이 통증이 지속되거나 붓기, 열감, 관절의 불안정성이 있다면 운동 강도를 낮추고 의료기관에서 원인을 확인하는 편이 안전합니다."
    )
    .replace(
      /가장 대표적인 증상은 ‘키토 플루’라고 불리는 두통, 무기력증, 구취 등입니다\. 이는 몸이 탄수화물 연소 체질에서 지방 연소 체질로 변하는 과도기적 현상입니다\./g,
      "식사 시간을 크게 바꾼 뒤 두통, 무기력감이나 구취를 경험하는 사람이 있지만 원인은 수분 부족, 카페인 섭취 변화, 부족한 영양 섭취 등 다양할 수 있습니다. 이를 단순한 적응 과정으로 단정해서는 안 됩니다."
    );

  const data = {
    ...parsed.data,
    title: editorial.title,
    excerpt: editorial.description,
    metaDescription: editorial.description,
    updated: "2026-08-09",
  };

  fs.writeFileSync(filePath, matter.stringify(content.trimStart(), data), "utf8");
  updatedFiles += 1;
}

console.log(`Rewrote ${updatedFiles} priority posts.`);
