import { getSortedPostsData } from "@/lib/posts";
import PostCard from "@/components/PostCard";
import Link from "next/link";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Wellbeing Health — 건강한 삶을 위한 웰빙 가이드",
  description:
    "운동, 다이어트, 건강식단, 생활습관, 멘탈케어까지 — 실생활에서 바로 쓸 수 있는 건강 정보를 전달합니다.",
};

export default function HomePage() {
  const allPosts = getSortedPostsData();
  const latestPosts = allPosts.slice(0, 6);

  const stats = [
    { label: "전문 아티클", value: `${allPosts.length}+` },
    { label: "카테고리", value: "6" },
    { label: "매주 업데이트", value: "✓" },
  ];

  return (
    <>
      {/* Hero */}
      <section className="hero">
        <div className="container">
          <div className="hero__tag">🌿 웰빙 건강 정보</div>
          <h1 className="hero__title">
            건강한 삶을 위한
            <br />
            <span>웰빙 가이드</span>
          </h1>
          <p className="hero__desc">
            운동, 다이어트, 건강식단, 생활습관, 멘탈케어까지
            <br />
            실생활에서 바로 쓸 수 있는 건강 정보를 전달합니다.
          </p>
          <Link href="/blog" className="hero__cta">
            전체 글 보기 →
          </Link>

          {/* Stats */}
          <div
            style={{
              display: "flex",
              gap: "40px",
              justifyContent: "center",
              marginTop: "48px",
              flexWrap: "wrap",
            }}
          >
            {stats.map((s) => (
              <div key={s.label} style={{ textAlign: "center" }}>
                <div
                  style={{
                    fontSize: "1.8rem",
                    fontWeight: 700,
                    color: "var(--primary)",
                    marginBottom: "4px",
                  }}
                >
                  {s.value}
                </div>
                <div style={{ fontSize: "0.85rem", color: "var(--text-muted)" }}>
                  {s.label}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Latest Posts */}
      <section className="posts-section">
        <div className="container">
          <div className="section-header">
            <h2 className="section-title">최신 아티클</h2>
            <Link href="/blog" className="section-link">
              전체 보기 →
            </Link>
          </div>

          {latestPosts.length > 0 ? (
            <div className="posts-grid">
              {latestPosts.map((post) => (
                <PostCard key={post.slug} post={post} />
              ))}
            </div>
          ) : (
            <div className="empty-state">
              <div className="empty-state__icon">📝</div>
              <p>아직 게시된 글이 없습니다.</p>
            </div>
          )}
        </div>
      </section>
    </>
  );
}
