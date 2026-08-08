import type { Metadata } from "next";
import InfoPage from "@/components/InfoPage";
import { CONTACT_EMAIL } from "@/lib/site";

export const metadata: Metadata = {
  title: "개인정보처리방침",
  description: "Wellbeing Health의 개인정보, 접속 정보, 쿠키, 광고 서비스 처리와 이용자 선택 방법을 안내합니다.",
  alternates: { canonical: "/privacy/" },
};

const toc = [
  { id: "overview", label: "방침의 적용 범위" },
  { id: "direct-data", label: "직접 수집하는 정보" },
  { id: "automatic-data", label: "자동 처리 정보" },
  { id: "purposes", label: "처리 목적" },
  { id: "services", label: "외부 서비스" },
  { id: "ads-cookies", label: "Google 광고와 쿠키" },
  { id: "choices", label: "쿠키 관리와 선택권" },
  { id: "retention", label: "보유 및 삭제" },
  { id: "rights", label: "이용자 권리" },
  { id: "children", label: "아동의 개인정보" },
  { id: "security", label: "보안과 외부 링크" },
  { id: "changes", label: "방침 변경 및 문의" },
];

export default function PrivacyPage() {
  return (
    <InfoPage
      eyebrow="PRIVACY POLICY"
      title="개인정보처리방침"
      description="Wellbeing Health 이용 과정에서 어떤 정보가 처리될 수 있고, 어떤 서비스가 관여하며, 이용자가 어떻게 선택할 수 있는지 안내합니다."
      toc={toc}
    >
      <section id="overview">
        <h2>1. 방침의 적용 범위</h2>
        <p>
          이 방침은 wellbeinghealth.co.kr에서 제공하는 웹페이지와 이메일 문의 과정에 적용됩니다. 외부 링크를
          통해 이동한 다른 사이트에는 해당 사이트의 개인정보처리방침이 적용됩니다.
        </p>
        <p>
          Wellbeing Health는 회원가입, 댓글, 결제 또는 온라인 상담 기능을 운영하지 않습니다. 사이트에서 이름,
          전화번호, 주소, 건강정보를 직접 입력받는 별도 양식도 제공하지 않습니다.
        </p>
      </section>

      <section id="direct-data">
        <h2>2. 직접 수집하는 정보</h2>
        <p>
          이용자가 이메일로 문의하는 경우 발신 이메일 주소, 이메일에 적은 이름 또는 소속, 문의 내용과 첨부파일이
          전달될 수 있습니다. 이 정보는 문의 확인, 회신, 오류 정정, 권리 관계 확인과 처리 기록 관리를 위해
          사용합니다.
        </p>
        <p>
          문의에 필요하지 않은 주민등록번호, 금융정보, 비밀번호, 진료기록, 검사 결과와 같은 민감정보를 보내지
          마세요. 실수로 불필요한 정보가 전달된 경우 삭제를 요청할 수 있습니다.
        </p>
      </section>

      <section id="automatic-data">
        <h2>3. 자동으로 처리될 수 있는 정보</h2>
        <p>
          사이트 접속과 전송 과정에서 IP 주소, 브라우저 및 기기 종류, 운영체제, 접속 시각, 요청한 URL, 이전
          페이지, 오류 기록, 쿠키 또는 유사한 식별자가 호스팅·보안·광고 서비스에 의해 자동으로 처리될 수
          있습니다.
        </p>
        <p>
          이러한 접속 정보는 일반적으로 특정 독자의 이름을 직접 확인하기 위한 용도로 사용하지 않습니다. 다만
          외부 서비스 제공자는 자체 정책과 설정에 따라 쿠키, 웹 비콘, IP 주소 또는 기타 식별자를 이용할 수
          있습니다.
        </p>
      </section>

      <section id="purposes">
        <h2>4. 정보 처리 목적</h2>
        <ul>
          <li>웹페이지 전송과 기기·브라우저에 맞는 콘텐츠 제공</li>
          <li>비정상 접속, 자동화 공격, 부정 광고 활동과 보안 위협 방지</li>
          <li>서버 오류 확인과 사이트 안정성 유지</li>
          <li>문의 내용 확인, 답변, 정정 및 권리 요청 처리</li>
          <li>광고 제공, 광고 빈도 조정과 광고 성과 측정</li>
          <li>관련 법령 또는 정당한 권리 보호를 위해 필요한 기록 유지</li>
        </ul>
      </section>

      <section id="services">
        <h2>5. 외부 서비스</h2>
        <p>사이트 운영 과정에서 다음 외부 서비스가 정보를 처리할 수 있습니다.</p>
        <ul>
          <li>
            <strong>Cloudflare Pages</strong>: 웹페이지 전송, DNS, 보안, 성능 최적화와 접속·오류 로그 처리
          </li>
          <li>
            <strong>Google AdSense</strong>: 광고 요청, 광고 제공, 부정 사용 방지, 빈도 관리와 성과 측정
          </li>
          <li>
            <strong>이메일 서비스 제공자</strong>: 이용자가 보낸 문의 메일의 전송과 보관
          </li>
        </ul>
        <p>
          외부 서비스는 각 회사의 인프라에서 정보를 처리하며, 처리 장소가 이용자의 국가와 다를 수 있습니다.
          자세한 내용은
          <a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noreferrer"> Cloudflare 개인정보처리방침</a>과
          <a href="https://policies.google.com/privacy" target="_blank" rel="noreferrer"> Google 개인정보처리방침</a>에서
          확인할 수 있습니다.
        </p>
      </section>

      <section id="ads-cookies">
        <h2>6. Google 광고와 쿠키</h2>
        <p>
          사이트에는 Google AdSense 광고 코드가 포함되어 있습니다. Google을 포함한 제3자 광고사업자는 광고를
          제공하는 과정에서 이용자의 브라우저에 쿠키를 저장하거나 기존 쿠키를 읽을 수 있으며, 웹 비콘, IP 주소
          또는 기타 식별자를 이용해 정보를 수집할 수 있습니다.
        </p>
        <p>
          Google과 그 파트너는 이용자가 이 사이트 또는 다른 웹사이트를 방문한 기록을 바탕으로 광고를 제공할 수
          있습니다. 광고 쿠키는 관련성 있는 광고 제공, 같은 광고가 과도하게 반복되지 않도록 하는 빈도 관리,
          부정 사용 방지와 광고 성과 측정에 사용될 수 있습니다.
        </p>
        <p>
          Google이 파트너 사이트에서 정보를 사용하는 방법은
          <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noreferrer"> Google 파트너 사이트 정보 처리 안내</a>에서
          확인할 수 있습니다.
        </p>
      </section>

      <section id="choices">
        <h2>7. 쿠키 관리와 이용자 선택권</h2>
        <p>
          이용자는 브라우저 설정에서 쿠키를 확인, 삭제, 차단하거나 사이트별 저장 권한을 변경할 수 있습니다.
          쿠키를 제한해도 일반 콘텐츠는 읽을 수 있지만 일부 광고 또는 보안 기능의 동작이 달라질 수 있습니다.
        </p>
        <ul>
          <li>
            Google 맞춤 광고 설정 및 해제:
            <a href="https://adssettings.google.com/" target="_blank" rel="noreferrer"> Google 광고 설정</a>
          </li>
          <li>
            여러 광고사업자의 맞춤 광고 선택 관리:
            <a href="https://optout.aboutads.info/" target="_blank" rel="noreferrer"> AboutAds 선택 도구</a>
          </li>
        </ul>
        <p>
          특정 지역에서 동의 관리 메시지가 제공되는 경우 이용자는 해당 메시지에서 광고 목적의 데이터 사용에
          관한 선택을 변경할 수 있습니다.
        </p>
      </section>

      <section id="retention">
        <h2>8. 보유 및 삭제</h2>
        <p>
          이메일 문의 내용은 문의 해결, 후속 확인과 분쟁 방지에 필요한 기간 동안 보관한 뒤 목적이 끝나면
          정리합니다. 관련 법령에 따라 보존할 필요가 있거나 권리 침해 대응이 진행 중인 경우에는 필요한 범위에서
          더 오래 보관할 수 있습니다.
        </p>
        <p>
          Cloudflare와 Google이 처리하는 접속 로그, 식별자와 쿠키의 보유 기간은 이용자의 설정과 각 서비스의
          정책에 따라 달라집니다. 이용자는 브라우저에서 저장된 쿠키를 직접 삭제할 수 있습니다.
        </p>
      </section>

      <section id="rights">
        <h2>9. 이용자 권리와 요청 방법</h2>
        <p>
          이용자는 자신이 이메일 문의로 제공한 정보에 대해 열람, 정정 또는 삭제를 요청할 수 있습니다. 요청은
          <a href={`mailto:${CONTACT_EMAIL}`}> {CONTACT_EMAIL}</a>로 보내주세요. 요청 대상과 기존 문의를 확인할 수
          있는 최소한의 정보를 포함해야 하며, 다른 사람의 개인정보 보호를 위해 필요한 확인을 요청할 수 있습니다.
        </p>
        <p>
          외부 광고 서비스가 자체적으로 보유한 정보는 해당 서비스의 개인정보 관리 화면 또는 문의 절차를 통해
          관리해야 할 수 있습니다.
        </p>
      </section>

      <section id="children">
        <h2>10. 아동의 개인정보</h2>
        <p>
          사이트는 아동을 대상으로 회원가입이나 개인정보 입력을 요구하지 않습니다. 아동이 문의 과정에서 불필요한
          개인정보를 제공한 사실을 보호자가 알게 된 경우 이메일로 삭제를 요청할 수 있습니다.
        </p>
      </section>

      <section id="security">
        <h2>11. 보안과 외부 링크</h2>
        <p>
          사이트는 HTTPS 연결과 호스팅 서비스의 보안 기능을 사용합니다. 다만 인터넷을 통한 전송이나 저장 방식을
          절대적으로 안전하다고 보장할 수는 없습니다. 이용자는 이메일로 비밀번호와 민감한 의료·금융정보를 보내지
          않아야 합니다.
        </p>
        <p>
          기사에 포함된 외부 기관 링크를 방문하면 해당 사이트가 별도의 쿠키와 개인정보처리방침을 적용할 수
          있습니다. Wellbeing Health의 방침은 외부 사이트의 정보 처리에는 적용되지 않습니다.
        </p>
      </section>

      <section id="changes">
        <h2>12. 방침 변경 및 문의</h2>
        <p>
          서비스 구성, 광고 도구 또는 관련 기준이 변경되면 이 방침을 수정하고 상단의 최종 업데이트 날짜를
          갱신합니다. 개인정보 처리에 관한 질문이나 요청은
          <a href={`mailto:${CONTACT_EMAIL}`}> {CONTACT_EMAIL}</a>로 보내주세요.
        </p>
      </section>
    </InfoPage>
  );
}
