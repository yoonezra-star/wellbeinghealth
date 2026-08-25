import type { Metadata } from "next";
import { Noto_Sans_KR } from "next/font/google";
import "./globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Script from "next/script";
import {
  ADSENSE_PUBLISHER_ID,
  EDITOR_NAME,
  SITE_DESCRIPTION,
  SITE_NAME,
  SITE_URL,
} from "@/lib/site";

const notoSansKR = Noto_Sans_KR({
  subsets: ["latin"],
  weight: ["300", "400", "500", "700"],
  display: "swap",
});

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: "Wellbeing Health — 건강한 삶을 위한 웰빙 가이드",
    template: "%s | Wellbeing Health",
  },
  description: SITE_DESCRIPTION,
  keywords: ["웰빙", "건강", "다이어트", "운동", "건강식단", "멘탈케어"],
  authors: [{ name: EDITOR_NAME, url: "/about/" }],
  creator: EDITOR_NAME,
  publisher: SITE_NAME,
  alternates: { canonical: "/" },
  openGraph: {
    type: "website",
    locale: "ko_KR",
    url: SITE_URL,
    siteName: SITE_NAME,
    title: "Wellbeing Health — 건강한 삶을 위한 웰빙 가이드",
    description:
      "운동, 다이어트, 건강식단, 생활습관, 멘탈케어까지 — 실생활에서 바로 쓸 수 있는 건강 정보를 전달합니다.",
  },
  robots: {
    index: true,
    follow: true,
  },
  verification: {
    google: "S_AkLU9rcMzWW3XJrzqolc4EGk9DyLBiSYcOx-7agnM",
  },
  other: {
    "google-adsense-account": ADSENSE_PUBLISHER_ID,
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const organizationJsonLd = {
    "@context": "https://schema.org",
    "@type": "Organization",
    name: SITE_NAME,
    url: SITE_URL,
    email: "mailto:replyleaders@naver.com",
  };

  const websiteJsonLd = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    name: SITE_NAME,
    url: SITE_URL,
    inLanguage: "ko-KR",
    publisher: { "@id": `${SITE_URL}/#organization` },
  };

  return (
    <html lang="ko">
      <body className={notoSansKR.className}>
        <Script
          id="adsense-script"
          async
          strategy="beforeInteractive"
          crossOrigin="anonymous"
          src={`https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${ADSENSE_PUBLISHER_ID}`}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify([
              { ...organizationJsonLd, "@id": `${SITE_URL}/#organization` },
              websiteJsonLd,
            ]).replace(/</g, "\\u003c"),
          }}
        />
        <Header />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
