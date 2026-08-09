import fs from "fs";
import path from "path";
import matter from "gray-matter";
import { remark } from "remark";
import remarkGfm from "remark-gfm";
import remarkHtml from "remark-html";

const postsDirectory = path.join(process.cwd(), "content/posts");

export interface PostMeta {
  slug: string;
  title: string;
  date: string;
  category: string;
  excerpt: string;
  focusKeyword?: string;
  metaDescription?: string;
  thumbnail?: string;
  updated?: string;
}

export interface Post extends PostMeta {
  contentHtml: string;
}

export function getSortedPostsData(): PostMeta[] {
  if (!fs.existsSync(postsDirectory)) {
    return [];
  }

  const fileNames = fs.readdirSync(postsDirectory);
  const allPostsData: PostMeta[] = fileNames
    .filter((name) => name.endsWith(".md"))
    .map((fileName) => {
      const slug = fileName.replace(/\.md$/, "");
      const fullPath = path.join(postsDirectory, fileName);
      const fileContents = fs.readFileSync(fullPath, "utf8");
      const { data } = matter(fileContents);

      return {
        slug,
        title: data.title || slug,
        date: data.date || "",
        category: data.category || "건강",
        excerpt: data.excerpt || data.metaDescription || "",
        focusKeyword: data.focusKeyword || "",
        metaDescription: data.metaDescription || "",
        thumbnail: data.thumbnail || "",
        updated: data.updated || "",
      };
    });

  return allPostsData.sort((a, b) => (a.date < b.date ? 1 : -1));
}

export function getPostsByCategory(category: string): PostMeta[] {
  const all = getSortedPostsData();
  if (category === "전체") return all;
  return all.filter((post) => post.category === category);
}

export function getAllPostSlugs() {
  if (!fs.existsSync(postsDirectory)) return [];
  const fileNames = fs.readdirSync(postsDirectory);
  return fileNames
    .filter((name) => name.endsWith(".md"))
    .map((fileName) => ({ slug: fileName.replace(/\.md$/, "") }));
}

export async function getPostData(slug: string): Promise<Post> {
  const fullPath = path.join(postsDirectory, `${slug}.md`);
  const fileContents = fs.readFileSync(fullPath, "utf8");
  const { data, content } = matter(fileContents);

  const normalizedContent = content
    .replace(/&#(\d+);/g, (_, code: string) => String.fromCodePoint(Number(code)))
    .replace(/&#x([0-9a-f]+);/gi, (_, code: string) => String.fromCodePoint(parseInt(code, 16)))
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&");

  const processedContent = await remark()
    .use(remarkGfm)
    .use(remarkHtml, { sanitize: false })
    .process(normalizedContent);

  const contentHtml = processedContent.toString();

  return {
    slug,
    title: data.title || slug,
    date: data.date || "",
    category: data.category || "건강",
    excerpt: data.excerpt || data.metaDescription || "",
    focusKeyword: data.focusKeyword || "",
    metaDescription: data.metaDescription || "",
    thumbnail: data.thumbnail || "",
    updated: data.updated || "",
    contentHtml,
  };
}

export function getRelatedPosts(post: PostMeta, limit = 3): PostMeta[] {
  return getSortedPostsData()
    .filter((candidate) => candidate.slug !== post.slug)
    .sort((a, b) => {
      const categoryScoreA = a.category === post.category ? 2 : 0;
      const categoryScoreB = b.category === post.category ? 2 : 0;
      return categoryScoreB - categoryScoreA || (a.date < b.date ? 1 : -1);
    })
    .slice(0, limit);
}

export const CATEGORIES = [
  "전체",
  "운동",
  "다이어트",
  "건강식단",
  "생활습관",
  "멘탈케어",
  "건강해설",
];
