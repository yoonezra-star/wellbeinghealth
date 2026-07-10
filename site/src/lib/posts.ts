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

  const processedContent = await remark()
    .use(remarkGfm)
    .use(remarkHtml, { sanitize: false })
    .process(content);

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
    contentHtml,
  };
}

export const CATEGORIES = [
  "전체",
  "운동",
  "다이어트",
  "건강식단",
  "생활습관",
  "멘탈케어",
  "전문가칼럼",
];
