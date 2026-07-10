import type { Metadata } from "next";
import { Noto_Sans_KR } from "next/font/google";
import "./globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

const notoSansKR = Noto_Sans_KR({
  subsets: ["latin"],
  weight: ["300", "400", "500", "700"],
  display: "swap",
});

export const metadata: Metadata = {
  title: {
    default: "Wellbeing Health — 건강한 삶을 위한 웰빙 가이드",
    template: "%s | Wellbeing Health",
  },
  description:
    "운동, 다이어트, 건강식단, 생활습관, 멘탈케어까지 — 실생활에서 바로 쓸 수 있는 건강 정보를 전달합니다.",
  keywords: ["웰빙", "건강", "다이어트", "운동", "건강식단", "멘탈케어"],
  authors: [{ name: "웰빙코치" }],
  creator: "Wellbeing Health",
  openGraph: {
    type: "website",
    locale: "ko_KR",
    url: "https://wellbeinghealth.co.kr",
    siteName: "Wellbeing Health",
    title: "Wellbeing Health — 건강한 삶을 위한 웰빙 가이드",
    description:
      "운동, 다이어트, 건강식단, 생활습관, 멘탈케어까지 — 실생활에서 바로 쓸 수 있는 건강 정보를 전달합니다.",
  },
  robots: {
    index: true,
    follow: true,
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ko">
      <body className={notoSansKR.className}>
        <Header />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
