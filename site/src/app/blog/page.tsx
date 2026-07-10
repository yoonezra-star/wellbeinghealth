import { getSortedPostsData } from "@/lib/posts";
import BlogList from "@/components/BlogList";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "블로그 — 전체 아티클",
  description:
    "Wellbeing Health의 모든 건강 아티클을 카테고리별로 탐색하세요. 운동, 다이어트, 건강식단, 생활습관, 멘탈케어.",
};

export default function BlogPage() {
  const allPosts = getSortedPostsData();

  return (
    <div className="blog-page">
      <div className="container">
        <div className="blog-page__header">
          <h1 className="blog-page__title">전체 아티클</h1>
          <p className="blog-page__desc">
            총 <strong style={{ color: "var(--primary)" }}>{allPosts.length}개</strong>의 건강 정보 아티클
          </p>
        </div>
        <BlogList allPosts={allPosts} />
      </div>
    </div>
  );
}
