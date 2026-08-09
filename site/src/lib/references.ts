import type { PostMeta } from "@/lib/posts";

export interface EditorialReference {
  title: string;
  publisher: string;
  url: string;
}

const REFERENCES = {
  kdca: {
    title: "국가건강정보포털",
    publisher: "질병관리청",
    url: "https://health.kdca.go.kr/healthinfo/",
  },
  healthyDiet: {
    title: "Healthy diet",
    publisher: "World Health Organization",
    url: "https://www.who.int/news-room/fact-sheets/detail/healthy-diet",
  },
  physicalActivity: {
    title: "Physical activity",
    publisher: "World Health Organization",
    url: "https://www.who.int/news-room/fact-sheets/detail/physical-activity",
  },
  cdcActivity: {
    title: "About Physical Activity",
    publisher: "Centers for Disease Control and Prevention",
    url: "https://www.cdc.gov/physical-activity/php/about/index.html",
  },
  mentalHealth: {
    title: "Mental health: strengthening our response",
    publisher: "World Health Organization",
    url: "https://www.who.int/news-room/fact-sheets/detail/mental-health-strengthening-our-response",
  },
  stress: {
    title: "Doing What Matters in Times of Stress",
    publisher: "World Health Organization",
    url: "https://www.who.int/publications/i/item/9789240003927",
  },
  sleep: {
    title: "About Sleep",
    publisher: "Centers for Disease Control and Prevention",
    url: "https://www.cdc.gov/sleep/about/index.html",
  },
  supplements: {
    title: "Dietary Supplements: What You Need to Know",
    publisher: "NIH Office of Dietary Supplements",
    url: "https://ods.od.nih.gov/factsheets/WYNTK-Consumer/",
  },
  diabetes: {
    title: "Diabetes Basics",
    publisher: "Centers for Disease Control and Prevention",
    url: "https://www.cdc.gov/diabetes/about/index.html",
  },
  obesity: {
    title: "Obesity and overweight",
    publisher: "World Health Organization",
    url: "https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight",
  },
  fasting: {
    title: "Calorie Restriction and Fasting Diets: What Do We Know?",
    publisher: "National Institute on Aging",
    url: "https://www.nia.nih.gov/news/calorie-restriction-and-fasting-diets-what-do-we-know",
  },
  mediterranean: {
    title: "What is the Mediterranean Diet?",
    publisher: "American Heart Association",
    url: "https://www.heart.org/en/healthy-living/healthy-eating/eat-smart/nutrition-basics/mediterranean-diet",
  },
  heart: {
    title: "Preventing Heart Disease",
    publisher: "Centers for Disease Control and Prevention",
    url: "https://www.cdc.gov/heart-disease/prevention/index.html",
  },
} satisfies Record<string, EditorialReference>;

const KEYWORD_REFERENCES: Array<[RegExp, EditorialReference]> = [
  [/간헐적\s*단식|공복/, REFERENCES.fasting],
  [/지중해/, REFERENCES.mediterranean],
  [/수면|숙면|불면/, REFERENCES.sleep],
  [/스트레스|번아웃|명상|마음챙김/, REFERENCES.stress],
  [/영양제|보충제|비타민/, REFERENCES.supplements],
  [/당뇨|혈당/, REFERENCES.diabetes],
  [/비만|체지방|다이어트|감량/, REFERENCES.obesity],
  [/심혈관|심장|혈압/, REFERENCES.heart],
];

const CATEGORY_REFERENCES: Record<string, EditorialReference[]> = {
  운동: [REFERENCES.physicalActivity, REFERENCES.cdcActivity],
  다이어트: [REFERENCES.healthyDiet, REFERENCES.obesity],
  건강식단: [REFERENCES.healthyDiet, REFERENCES.kdca],
  생활습관: [REFERENCES.kdca, REFERENCES.sleep],
  멘탈케어: [REFERENCES.mentalHealth, REFERENCES.stress],
  건강해설: [REFERENCES.kdca, REFERENCES.healthyDiet],
  건강: [REFERENCES.kdca, REFERENCES.healthyDiet],
};

export function getEditorialReferences(post: PostMeta): EditorialReference[] {
  const searchable = `${post.title} ${post.excerpt} ${post.focusKeyword || ""}`;
  const candidates = [
    ...KEYWORD_REFERENCES.filter(([pattern]) => pattern.test(searchable)).map(([, reference]) => reference),
    ...(CATEGORY_REFERENCES[post.category] || CATEGORY_REFERENCES.건강),
    REFERENCES.kdca,
  ];

  return candidates
    .filter((reference, index, all) => all.findIndex((item) => item.url === reference.url) === index)
    .slice(0, 3);
}
