import Link from "next/link";
import { PostMeta } from "@/lib/posts";

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
  return `${d.getFullYear()}.${String(d.getMonth() + 1).padStart(2, "0")}.${String(
    d.getDate()
  ).padStart(2, "0")}`;
}

export default function PostCard({ post }: { post: PostMeta }) {
  const emoji = CATEGORY_EMOJI[post.category] || "💚";

  return (
    <Link href={`/blog/${post.slug}`} className="post-card">
      <div className="post-card__thumbnail-placeholder">{emoji}</div>
      <div className="post-card__body">
        <span className={`post-card__category cat-${post.category}`}>
          {post.category}
        </span>
        <h2 className="post-card__title">{post.title}</h2>
        {post.excerpt && (
          <p className="post-card__excerpt">{post.excerpt}</p>
        )}
        <div className="post-card__footer">
          <span className="post-card__date">{formatDate(post.date)}</span>
          <span className="post-card__read">읽기 →</span>
        </div>
      </div>
    </Link>
  );
}
