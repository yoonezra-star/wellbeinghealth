import Link from "next/link";

export default function NotFound() {
  return (
    <div className="not-found">
      <p className="info-page__eyebrow">404</p>
      <h1>페이지를 찾을 수 없습니다</h1>
      <p>주소가 변경되었거나 삭제된 페이지입니다.</p>
      <div className="not-found__links">
        <Link href="/">홈으로 이동</Link>
        <Link href="/blog">전체 글 보기</Link>
      </div>
    </div>
  );
}
