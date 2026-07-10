const fs = require('fs');
const path = require('path');
const https = require('https');

const WP_URL = 'https://wellbeinghealth.co.kr/wp-json/wp/v2/posts?per_page=100';
const POSTS_DIR = path.join(__dirname, 'site', 'content', 'posts');

if (!fs.existsSync(POSTS_DIR)) {
  fs.mkdirSync(POSTS_DIR, { recursive: true });
}

function stripHtml(html) {
  return html.replace(/<[^>]*>?/gm, '').trim();
}

function fetchPosts(url) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve(JSON.parse(data)));
    }).on('error', reject);
  });
}

async function migrate() {
  console.log('Fetching WordPress posts...');
  try {
    const posts = await fetchPosts(WP_URL);
    console.log(`Found ${posts.length} posts.`);

    posts.forEach(post => {
      const title = post.title.rendered.replace(/"/g, '\\"');
      const date = post.date.split('T')[0];
      const slug = post.slug;
      const content = post.content.rendered;
      // Convert HTML to simple markdown for paragraphs
      let markdownContent = content
        .replace(/<h[1-6][^>]*>(.*?)<\/h[1-6]>/gi, '### $1\n\n')
        .replace(/<p[^>]*>(.*?)<\/p>/gi, '$1\n\n')
        .replace(/<li[^>]*>(.*?)<\/li>/gi, '- $1\n')
        .replace(/<br\s*\/?>/gi, '\n')
        .replace(/<[^>]*>?/gm, '');

      // Decode HTML entities simply
      markdownContent = markdownContent.replace(/&#8211;/g, '-').replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&');
      
      const excerpt = stripHtml(post.excerpt.rendered).substring(0, 120).replace(/"/g, '\\"');
      
      const frontmatter = `---
title: "${title}"
date: "${date}"
category: "전체"
excerpt: "${excerpt}"
---

${markdownContent}
`;
      const filePath = path.join(POSTS_DIR, `${date}-${slug}.md`);
      fs.writeFileSync(filePath, frontmatter);
      console.log(`Saved: ${filePath}`);
    });
    console.log('✅ Migration complete!');
  } catch (err) {
    console.error('Migration failed:', err);
  }
}

migrate();
