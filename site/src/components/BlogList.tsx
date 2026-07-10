"use client";
import { useState, useEffect, Suspense } from "react";
import { useSearchParams } from "next/navigation";
import PostCard from "@/components/PostCard";
import { CATEGORIES } from "@/lib/posts";
import type { PostMeta } from "@/lib/posts";

const ALL_CATEGORIES = CATEGORIES;

function BlogContent({ allPosts }: { allPosts: PostMeta[] }) {
  const searchParams = useSearchParams();
  const initialCat = searchParams.get("cat") || "전체";
  const [activeCategory, setActiveCategory] = useState(initialCat);

  useEffect(() => {
    const cat = searchParams.get("cat") || "전체";
    setActiveCategory(cat);
  }, [searchParams]);

  const filtered =
    activeCategory === "전체"
      ? allPosts
      : allPosts.filter((p) => p.category === activeCategory);

  return (
    <>
      {/* Category Filter */}
      <div className="category-nav">
        {ALL_CATEGORIES.map((cat) => (
          <button
            key={cat}
            className={`category-btn ${activeCategory === cat ? "active" : ""}`}
            onClick={() => setActiveCategory(cat)}
          >
            {cat}
          </button>
        ))}
      </div>

      {/* Posts */}
      {filtered.length > 0 ? (
        <div className="posts-grid">
          {filtered.map((post) => (
            <PostCard key={post.slug} post={post} />
          ))}
        </div>
      ) : (
        <div className="empty-state">
          <div className="empty-state__icon">📝</div>
          <p>이 카테고리에는 아직 게시된 글이 없습니다.</p>
        </div>
      )}
    </>
  );
}

export default function BlogPage({ allPosts }: { allPosts: PostMeta[] }) {
  return (
    <Suspense fallback={<div style={{ padding: "80px", textAlign: "center", color: "var(--text-muted)" }}>로딩 중...</div>}>
      <BlogContent allPosts={allPosts} />
    </Suspense>
  );
}
