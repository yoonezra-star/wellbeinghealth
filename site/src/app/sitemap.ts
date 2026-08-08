import type { MetadataRoute } from "next";
import { getSortedPostsData } from "@/lib/posts";
import { SITE_URL } from "@/lib/site";

export const dynamic = "force-static";

export default function sitemap(): MetadataRoute.Sitemap {
  const staticPages = [
    "",
    "/blog",
    "/about",
    "/editorial-policy",
    "/contact",
    "/privacy",
    "/disclaimer",
  ].map((path) => ({
    url: `${SITE_URL}${path}/`,
    lastModified: new Date("2026-08-09"),
    changeFrequency: path === "" || path === "/blog" ? ("weekly" as const) : ("monthly" as const),
    priority: path === "" ? 1 : path === "/blog" ? 0.9 : 0.5,
  }));

  const posts = getSortedPostsData().map((post) => ({
    url: `${SITE_URL}/blog/${encodeURIComponent(post.slug)}/`,
    lastModified: new Date(post.updated || post.date),
    changeFrequency: "monthly" as const,
    priority: 0.7,
  }));

  return [...staticPages, ...posts];
}
