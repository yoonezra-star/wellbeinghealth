import type { ReactNode } from "react";

interface InfoPageProps {
  eyebrow: string;
  title: string;
  description: string;
  updated?: string;
  children: ReactNode;
}

export default function InfoPage({
  eyebrow,
  title,
  description,
  updated = "2026년 8월 9일",
  children,
}: InfoPageProps) {
  return (
    <div className="info-page">
      <header className="info-page__header">
        <p className="info-page__eyebrow">{eyebrow}</p>
        <h1>{title}</h1>
        <p className="info-page__lead">{description}</p>
        <p className="info-page__updated">최종 업데이트: {updated}</p>
      </header>
      <div className="info-page__content">{children}</div>
    </div>
  );
}
