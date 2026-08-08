import type { Metadata } from "next";
import Link from "next/link";
import InfoPage from "@/components/InfoPage";

export const metadata: Metadata = {
  title: "사이트 소개",
  description: "Wellbeing Health의 운영 목적과 콘텐츠 제작 원칙을 안내합니다.",
  alternates: { canonical: "/about/" },
};

export default function AboutPage() {
  return (
    <InfoPage
      eyebrow="ABOUT US"
      title="일상에서 이해하고 실천할 수 있는 건강 정보"
      description="Wellbeing Health는 운동, 식생활, 생활습관과 마음 건강에 관한 자료를 읽기 쉬운 한국어로 정리하는 건강 정보 매거진입니다."
    >
      <section>
        <h2>운영 목적</h2>
        <p>
          건강 정보는 많지만, 출처를 확인하기 어렵거나 누구에게나 같은 방법을 권하는 글도 많습니다.
          Wellbeing Health는 공공기관과 보건기관의 자료를 우선 확인하고, 독자가 자신의 상황에 맞게
          판단할 수 있도록 적용 조건과 주의사항을 함께 전달하는 것을 목표로 합니다.
        </p>
      </section>

      <section>
        <h2>콘텐츠를 만드는 사람</h2>
        <p>
          콘텐츠는 <strong>Wellbeing Health 편집팀</strong> 명의로 작성하고 관리합니다. 현재 이 사이트는
          의료기관이 아니며, 의료인에 의한 진료나 개인별 처방을 제공하지 않습니다. 의료 전문가가 실제로
          검토한 글만 별도로 검토자와 자격을 표시하며, 확인되지 않은 전문 자격을 표기하지 않습니다.
        </p>
      </section>

      <section>
        <h2>자료 선정 원칙</h2>
        <ul>
          <li>질병관리청, 보건복지부, WHO 등 공공 보건기관의 자료를 우선합니다.</li>
          <li>건강 효과를 단정하지 않고 대상, 한계, 주의할 상황을 함께 설명합니다.</li>
          <li>출처가 바뀌거나 새로운 근거가 확인되면 내용을 수정하고 업데이트 일자를 표시합니다.</li>
          <li>독자의 실제 진단과 치료 결정은 의료 전문가의 상담을 우선하도록 안내합니다.</li>
        </ul>
      </section>

      <section>
        <h2>자동화 도구 사용</h2>
        <p>
          자료 정리, 문장 초안과 교정 과정에서 자동화 또는 인공지능 도구를 사용할 수 있습니다. 도구가 만든
          결과를 그대로 전문적 판단으로 간주하지 않으며, 발행 전 편집 과정에서 문맥, 표현, 출처 연결과
          안전 고지를 확인합니다. 자세한 기준은 <Link href="/editorial-policy">편집정책</Link>에서 확인할 수 있습니다.
        </p>
      </section>

      <section>
        <h2>의견과 정정 요청</h2>
        <p>
          내용 오류, 오래된 링크 또는 부정확한 표현을 발견했다면 <Link href="/contact">문의하기</Link>를 통해
          알려주세요. 확인이 필요한 내용은 근거를 다시 검토한 뒤 수정합니다.
        </p>
      </section>
    </InfoPage>
  );
}
