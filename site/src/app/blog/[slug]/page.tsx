import { getAllPostSlugs, getPostData, getRelatedPosts, getSortedPostsData } from "@/lib/posts";
import { getEditorialReferences } from "@/lib/references";
import { getTopicGuide } from "@/lib/topicGuides";
import { absoluteUrl, EDITOR_NAME, SITE_NAME, SITE_URL } from "@/lib/site";
import PostCard from "@/components/PostCard";
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
    authors: [{ name: EDITOR_NAME, url: "/about/" }],
    alternates: { canonical: `/blog/${post.slug}/` },
    openGraph: {
      title: post.title,
      description: post.metaDescription || post.excerpt,
      type: "article",
      publishedTime: post.date,
      modifiedTime: post.updated || post.date,
      authors: [absoluteUrl("/about/")],
      url: absoluteUrl(`/blog/${post.slug}/`),
      images: post.thumbnail ? [{ url: post.thumbnail, alt: post.title }] : undefined,
    },
  };
}

const CATEGORY_EMOJI: Record<string, string> = {
  운동: "🏃",
  다이어트: "🥗",
  건강식단: "🥦",
  생활습관: "🌅",
  멘탈케어: "🧘",
  건강해설: "📚",
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
  const references = getEditorialReferences(post);
  const relatedPosts = getRelatedPosts(post);
  const topicGuide = getTopicGuide(post.slug);
  const allPosts = topicGuide ? getSortedPostsData() : [];
  const topicPosts = topicGuide
    ? topicGuide.postSlugs
        .map((topicSlug) => allPosts.find((candidate) => candidate.slug === topicSlug))
        .filter((candidate): candidate is NonNullable<typeof candidate> => Boolean(candidate))
    : [];
  const articleUrl = absoluteUrl(`/blog/${post.slug}/`);
  const imageUrl = post.thumbnail ? absoluteUrl(post.thumbnail) : undefined;
  const jsonLd = [
    {
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      headline: post.title,
      description: post.metaDescription || post.excerpt,
      datePublished: post.date,
      dateModified: post.updated || post.date,
      inLanguage: "ko-KR",
      articleSection: post.category,
      mainEntityOfPage: articleUrl,
      image: imageUrl ? [imageUrl] : undefined,
      author: {
        "@type": "Organization",
        name: EDITOR_NAME,
        url: absoluteUrl("/about/"),
      },
      publisher: {
        "@type": "Organization",
        name: SITE_NAME,
        url: SITE_URL,
      },
      isAccessibleForFree: true,
    },
    {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      itemListElement: [
        { "@type": "ListItem", position: 1, name: "홈", item: `${SITE_URL}/` },
        { "@type": "ListItem", position: 2, name: "블로그", item: `${SITE_URL}/blog/` },
        { "@type": "ListItem", position: 3, name: post.title, item: articleUrl },
      ],
    },
  ];

  return (
    <div className="article-wrap">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd).replace(/</g, "\\u003c") }}
      />
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
          <span>작성: <Link href="/about">{EDITOR_NAME}</Link></span>
          {post.updated && <span>수정: {formatDate(post.updated)}</span>}
        </div>
      </header>

      {post.thumbnail && (
        <img className="article-thumbnail" src={post.thumbnail} alt={post.title} />
      )}

      <aside className="health-notice" aria-label="건강정보 이용 안내">
        <strong>건강정보 이용 안내</strong>
        <p>
          이 글은 일반적인 건강정보를 정리한 자료이며 진단이나 치료를 대신하지 않습니다. 기저질환이 있거나
          약을 복용 중이라면 식단과 운동을 바꾸기 전에 의료 전문가와 상담하세요.
        </p>
      </aside>

      <article
        className="article-content"
        dangerouslySetInnerHTML={{ __html: post.contentHtml }}
      />

      {topicGuide && (
        <nav className="topic-guide" aria-labelledby={`topic-guide-${topicGuide.id}`}>
          <div className="article-section-heading">
            <p>주제 탐색</p>
            <h2 id={`topic-guide-${topicGuide.id}`}>{topicGuide.label}</h2>
          </div>
          <p className="topic-guide__description">
            {topicGuide.description} 현재 글이 세부 주제라면 대표 가이드에서 전체 기준을 먼저 확인할 수 있습니다.
          </p>
          <ul className="topic-guide__links">
            {topicPosts.map((topicPost) => (
              <li key={topicPost.slug}>
                <Link
                  href={`/blog/${topicPost.slug}`}
                  aria-current={topicPost.slug === post.slug ? "page" : undefined}
                >
                  <span>{topicPost.slug === topicGuide.pillarSlug ? "대표 가이드" : "세부 글"}</span>
                  <strong>{topicPost.title}</strong>
                </Link>
              </li>
            ))}
          </ul>
        </nav>
      )}

      <section className="article-references" aria-labelledby="article-references-title">
        <div className="article-section-heading">
          <p>주제별 일반 참고자료</p>
          <h2 id="article-references-title">추가로 살펴볼 자료</h2>
        </div>
        <ul>
          {references.map((reference) => (
            <li key={reference.url}>
              <a href={reference.url} target="_blank" rel="noreferrer">
                <strong>{reference.title}</strong>
                <span>{reference.publisher}</span>
              </a>
            </li>
          ))}
        </ul>
        <p className="article-references__note">
          이 자료는 주제별 기본 안내이며 본문 개별 수치나 연구의 직접 인용을 대신하지 않습니다. 구체적인
          연구 결과는 해당 문단에 연결된 원문을 확인하세요.
        </p>
      </section>

      <section className="article-author" aria-labelledby="article-author-title">
        <div>
          <p className="article-author__label">작성 및 편집</p>
          <h2 id="article-author-title">{EDITOR_NAME}</h2>
          <p>
            공공기관과 보건기관 자료를 바탕으로 일상 건강정보를 정리합니다. 의료기관이 아니며 확인되지 않은
            전문 자격을 표시하지 않습니다.
          </p>
        </div>
        <Link href="/editorial-policy">편집정책 보기</Link>
      </section>

      <section className="related-posts" aria-labelledby="related-posts-title">
        <div className="article-section-heading">
          <p>함께 읽기</p>
          <h2 id="related-posts-title">관련 아티클</h2>
        </div>
        <div className="posts-grid">
          {relatedPosts.map((relatedPost) => (
            <PostCard key={relatedPost.slug} post={relatedPost} />
          ))}
        </div>
      </section>

      <div className="article-back">
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
