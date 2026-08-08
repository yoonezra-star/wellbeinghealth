import type { Metadata } from "next";
import InfoPage from "@/components/InfoPage";
import { CONTACT_EMAIL } from "@/lib/site";

export const metadata: Metadata = {
  title: "개인정보처리방침",
  description: "Wellbeing Health의 개인정보와 쿠키 처리 방침을 안내합니다.",
  alternates: { canonical: "/privacy/" },
};

export default function PrivacyPage() {
  return (
    <InfoPage
      eyebrow="PRIVACY POLICY"
      title="개인정보처리방침"
      description="Wellbeing Health는 서비스 운영에 필요한 범위에서 방문 정보와 쿠키가 어떻게 처리될 수 있는지 공개합니다."
    >
      <section>
        <h2>1. 직접 수집하는 개인정보</h2>
        <p>
          사이트에는 회원가입, 댓글, 온라인 문의 양식이 없습니다. 따라서 이름, 전화번호, 주소 등을 사이트에서
          직접 입력받거나 저장하지 않습니다. 이메일로 문의하면 발신 주소와 문의 내용은 답변과 기록 관리에
          필요한 기간 동안 이메일 서비스에 보관될 수 있습니다.
        </p>
      </section>

      <section>
        <h2>2. 자동으로 처리될 수 있는 정보</h2>
        <p>
          사이트 접속 과정에서 IP 주소, 브라우저 종류, 접속 시각, 요청 URL과 쿠키 정보가 호스팅·보안·통계
          또는 광고 서비스에 의해 처리될 수 있습니다. 이러한 정보는 사이트 안정성, 방문 통계와 광고 운영을
          위해 사용될 수 있습니다.
        </p>
      </section>

      <section>
        <h2>3. 외부 서비스</h2>
        <ul>
          <li>Cloudflare Pages: 사이트 전송, 보안과 접속 로그 처리</li>
          <li>Google AdSense: 광고 제공, 부정 사용 방지와 광고 성과 측정</li>
        </ul>
        <p>
          Google을 포함한 제3자 공급업체는 쿠키를 사용해 이전 방문 기록을 바탕으로 광고를 제공할 수 있습니다.
          Google의 정보 처리 방식은 <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noreferrer">Google 파트너 사이트 개인정보 안내</a>에서,
          광고 개인 최적화 설정은 <a href="https://adssettings.google.com/" target="_blank" rel="noreferrer">Google 광고 설정</a>에서 확인할 수 있습니다.
        </p>
      </section>

      <section>
        <h2>4. 쿠키 관리</h2>
        <p>
          이용자는 브라우저 설정에서 쿠키를 삭제하거나 저장을 제한할 수 있습니다. 쿠키를 제한하면 일부 광고
          또는 사이트 기능이 정상적으로 동작하지 않을 수 있습니다.
        </p>
      </section>

      <section>
        <h2>5. 보유 기간과 문의</h2>
        <p>
          사이트가 직접 보관하는 문의 이메일은 문의 처리 목적이 끝난 뒤 합리적인 기간 내 정리합니다. 외부
          서비스의 로그와 쿠키 보유 기간은 각 서비스의 정책을 따릅니다. 개인정보 관련 문의는
          <a href={`mailto:${CONTACT_EMAIL}`}> {CONTACT_EMAIL}</a>로 보내주세요.
        </p>
      </section>

      <section>
        <h2>6. 방침 변경</h2>
        <p>서비스 또는 관련 법령이 변경되면 이 방침을 수정하고 상단의 최종 업데이트 날짜를 갱신합니다.</p>
      </section>
    </InfoPage>
  );
}
