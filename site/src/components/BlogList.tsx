"use client";
import { useEffect, useState } from "react";
import PostCard from "@/components/PostCard";
import type { PostMeta } from "@/lib/posts";

const ALL_CATEGORIES = [
  "전체",
  "운동",
  "다이어트",
  "건강식단",
  "생활습관",
  "멘탈케어",
  "건강해설",
];

function BlogContent({ allPosts }: { allPosts: PostMeta[] }) {
  const [activeCategory, setActiveCategory] = useState("전체");
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    const cat = new URLSearchParams(window.location.search).get("cat") || "전체";
    setActiveCategory(ALL_CATEGORIES.includes(cat) ? cat : "전체");
  }, []);

  const filtered = allPosts.filter((post) => {
    const matchesCategory = activeCategory === "전체" || post.category === activeCategory;
    const searchableText = `${post.title} ${post.excerpt} ${post.category}`.toLocaleLowerCase();
    return matchesCategory && searchableText.includes(searchTerm.trim().toLocaleLowerCase());
  });
  const visibleSlugs = new Set(filtered.map((post) => post.slug));

  function selectCategory(category: string) {
    setActiveCategory(category);
    const params = new URLSearchParams(window.location.search);
    if (category === "전체") {
      params.delete("cat");
    } else {
      params.set("cat", category);
    }
    const query = params.size ? `?${params.toString()}` : "";
    window.history.replaceState(null, "", `${window.location.pathname}${query}`);
  }

  return (
    <>
      {/* Category Filter */}
      <div className="category-nav">
        {ALL_CATEGORIES.map((cat) => (
          <button
            key={cat}
            className={`category-btn ${activeCategory === cat ? "active" : ""}`}
            aria-pressed={activeCategory === cat}
            onClick={() => selectCategory(cat)}
          >
            {cat}
          </button>
        ))}
      </div>

      <div className="blog-tools">
        <label className="blog-search">
          <span>글 검색</span>
          <input
            className="blog-search__input"
            type="search"
            value={searchTerm}
            onChange={(event) => setSearchTerm(event.target.value)}
            placeholder="제목과 요약 검색"
          />
        </label>
        <p className="blog-results" aria-live="polite">{filtered.length}개 글</p>
      </div>

      {/* Posts */}
      {allPosts.length > 0 ? (
        <div className="posts-grid">
          {allPosts.map((post) => (
            <div className="blog-result" hidden={!visibleSlugs.has(post.slug)} key={post.slug}>
              <PostCard post={post} />
            </div>
          ))}
        </div>
      ) : (
        <div className="empty-state">
          <p>아직 게시된 글이 없습니다.</p>
        </div>
      )}
      {allPosts.length > 0 && filtered.length === 0 && (
        <div className="empty-state"><p>검색 결과가 없습니다.</p></div>
      )}
    </>
  );
}

export default function BlogPage({ allPosts }: { allPosts: PostMeta[] }) {
  return <BlogContent allPosts={allPosts} />;
}
