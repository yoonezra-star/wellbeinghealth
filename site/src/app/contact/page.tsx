import type { Metadata } from "next";
import InfoPage from "@/components/InfoPage";
import { CONTACT_EMAIL } from "@/lib/site";

export const metadata: Metadata = {
  title: "문의하기",
  description: "콘텐츠 오류 제보, 저작권 및 운영 관련 문의 방법을 안내합니다.",
  alternates: { canonical: "/contact/" },
};

export default function ContactPage() {
  return (
    <InfoPage
      eyebrow="CONTACT"
      title="문의하기"
      description="콘텐츠 오류 제보, 출처 보완, 저작권 및 사이트 운영 관련 의견을 이메일로 받고 있습니다."
    >
      <section>
        <h2>연락처</h2>
        <p>
          이메일: <a href={`mailto:${CONTACT_EMAIL}`}>{CONTACT_EMAIL}</a>
        </p>
        <p>문의 내용과 관련 글 주소를 함께 보내면 확인에 도움이 됩니다.</p>
      </section>

      <section>
        <h2>문의 가능한 내용</h2>
        <ul>
          <li>본문의 사실 오류 또는 오래된 정보 제보</li>
          <li>출처 링크 오류와 추가 근거 제안</li>
          <li>이미지, 문장 인용과 저작권 관련 요청</li>
          <li>사이트 이용 중 발견한 기술적 문제</li>
          <li>광고 및 일반 제휴 문의</li>
        </ul>
      </section>

      <section>
        <h2>의료 상담은 제공하지 않습니다</h2>
        <p>
          이메일로 증상을 진단하거나 치료 방법, 약물 복용 여부를 안내하지 않습니다. 개인 건강 문제는
          의료기관 또는 자격을 갖춘 의료 전문가에게 상담해 주세요. 응급 상황이라면 즉시 119나 가까운
          응급의료기관을 이용해야 합니다.
        </p>
      </section>
    </InfoPage>
  );
}
