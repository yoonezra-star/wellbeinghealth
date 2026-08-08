import type { Metadata } from "next";
import Link from "next/link";
import InfoPage from "@/components/InfoPage";

export const metadata: Metadata = {
  title: "건강정보 면책",
  description: "Wellbeing Health 콘텐츠의 적용 범위와 의료 면책 사항을 안내합니다.",
  alternates: { canonical: "/disclaimer/" },
};

export default function DisclaimerPage() {
  return (
    <InfoPage
      eyebrow="HEALTH DISCLAIMER"
      title="건강정보 이용 전 확인하세요"
      description="사이트의 모든 콘텐츠는 일반적인 정보 제공을 위한 것이며 개인별 진단이나 치료를 대신하지 않습니다."
    >
      <section>
        <h2>의학적 진단과 치료가 아닙니다</h2>
        <p>
          글에 소개된 운동, 식단, 생활습관 정보는 일반적인 교육 목적입니다. 증상, 검사 결과, 약물 복용,
          치료 시작이나 중단에 관한 결정은 의사, 약사 등 자격을 갖춘 전문가와 상의해야 합니다.
        </p>
      </section>

      <section>
        <h2>개인에 따라 결과가 다릅니다</h2>
        <p>
          같은 방법도 연령, 건강 상태, 임신 여부, 알레르기, 복용 약과 운동 경험에 따라 효과와 위험이 달라질
          수 있습니다. 특정 결과를 보장하지 않으며, 불편한 증상이 생기면 중단하고 전문가의 도움을 받아야 합니다.
        </p>
      </section>

      <section>
        <h2>응급 상황</h2>
        <p>
          가슴 통증, 호흡 곤란, 의식 변화, 갑작스러운 마비, 심한 출혈 등 응급 증상이 있다면 사이트 정보를
          기다리지 말고 즉시 119 또는 가까운 응급의료기관에 연락하세요.
        </p>
      </section>

      <section>
        <h2>외부 링크</h2>
        <p>
          참고를 위해 외부 기관 링크를 제공하지만 해당 사이트의 내용, 변경 또는 이용 결과를 통제하지 않습니다.
          링크가 현재 근거와 맞지 않는다면 <Link href="/contact">문의하기</Link>로 알려주세요.
        </p>
      </section>
    </InfoPage>
  );
}
