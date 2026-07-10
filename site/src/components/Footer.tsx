import Link from "next/link";

export default function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className="footer">
      <div className="container">
        <div className="footer__inner">
          <div className="footer__brand">
            <h3>🌿 Wellbeing Health</h3>
            <p>
              운동, 다이어트, 건강식단, 생활습관, 멘탈케어까지
              <br />
              실생활에서 바로 쓸 수 있는 건강 정보를 전달합니다.
            </p>
          </div>

          <div className="footer__links">
            <h4>카테고리</h4>
            <ul>
              <li><Link href="/blog?cat=운동">운동</Link></li>
              <li><Link href="/blog?cat=다이어트">다이어트</Link></li>
              <li><Link href="/blog?cat=건강식단">건강식단</Link></li>
              <li><Link href="/blog?cat=생활습관">생활습관</Link></li>
              <li><Link href="/blog?cat=멘탈케어">멘탈케어</Link></li>
              <li><Link href="/blog?cat=전문가칼럼">전문가칼럼</Link></li>
            </ul>
          </div>

          <div className="footer__links">
            <h4>사이트</h4>
            <ul>
              <li><Link href="/">홈</Link></li>
              <li><Link href="/blog">전체 글</Link></li>
            </ul>
          </div>
        </div>

        <div className="footer__bottom">
          <span>© {year} Wellbeing Health. All rights reserved.</span>
          <span>건강 정보는 의료 상담을 대체하지 않습니다.</span>
        </div>
      </div>
    </footer>
  );
}
