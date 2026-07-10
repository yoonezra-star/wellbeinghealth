import { getAllPostSlugs, getPostData } from "@/lib/posts";
import Link from "next/link";
import type { Metadata } from "next";

interface Props {
  params: Promise<{ slug: string }>;
}

export async function generateStaticParams() {
  return getAllPostSlugs();
}

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  const decodedSlug = decodeURIComponent(slug);
  const post = await getPostData(decodedSlug);
  return {
    title: post.title,
    description: post.metaDescription || post.excerpt,
    keywords: post.focusKeyword ? [post.focusKeyword] : [],
    openGraph: {
      title: post.title,
      description: post.metaDescription || post.excerpt,
      type: "article",
      publishedTime: post.date,
    },
  };
}

const CATEGORY_EMOJI: Record<string, string> = {
  운동: "🏃",
  다이어트: "🥗",
  건강식단: "🥦",
  생활습관: "🌅",
  멘탈케어: "🧘",
  전문가칼럼: "👨‍⚕️",
  건강: "💚",
};

function formatDate(dateStr: string) {
  if (!dateStr) return "";
  const d = new Date(dateStr);
  return `${d.getFullYear()}년 ${d.getMonth() + 1}월 ${d.getDate()}일`;
}

export default async function PostPage({ params }: Props) {
  const { slug } = await params;
  const decodedSlug = decodeURIComponent(slug);
  const post = await getPostData(decodedSlug);
  const emoji = CATEGORY_EMOJI[post.category] || "💚";

  return (
    <div className="article-wrap">
      {/* Breadcrumb */}
      <nav className="breadcrumb">
        <Link href="/">홈</Link>
        <span>›</span>
        <Link href="/blog">블로그</Link>
        <span>›</span>
        <span>{post.category}</span>
      </nav>

      {/* Article Header */}
      <header className="article-header">
        <span className={`article-category cat-${post.category}`}>
          {emoji} {post.category}
        </span>
        <h1 className="article-title">{post.title}</h1>
        <div className="article-meta">
          <span>📅 {formatDate(post.date)}</span>
          {post.focusKeyword && (
            <span>🔑 {post.focusKeyword}</span>
          )}
        </div>
      </header>

      {/* Thumbnail placeholder */}
      <div
        style={{
          width: "100%",
          aspectRatio: "16/9",
          background: "linear-gradient(135deg, var(--bg-card) 0%, #263348 100%)",
          borderRadius: "var(--radius)",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          fontSize: "4rem",
          marginBottom: "40px",
        }}
      >
        {emoji}
      </div>

      {/* Content */}
      <article
        className="article-content"
        dangerouslySetInnerHTML={{ __html: post.contentHtml }}
      />

      {/* Back link */}
      <div style={{ marginTop: "60px", paddingTop: "32px", borderTop: "1px solid var(--border)" }}>
        <Link
          href="/blog"
          style={{
            display: "inline-flex",
            alignItems: "center",
            gap: "8px",
            color: "var(--primary)",
            fontWeight: 500,
          }}
        >
          ← 전체 아티클로 돌아가기
        </Link>
      </div>
    </div>
  );
}
