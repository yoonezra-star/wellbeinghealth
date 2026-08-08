import type { ReactNode } from "react";

interface InfoPageProps {
  eyebrow: string;
  title: string;
  description: string;
  updated?: string;
  toc?: Array<{ id: string; label: string }>;
  children: ReactNode;
}

export default function InfoPage({
  eyebrow,
  title,
  description,
  updated = "2026년 8월 9일",
  toc,
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
      {toc && toc.length > 0 && (
        <nav className="info-page__toc" aria-label="페이지 목차">
          <p>페이지 안내</p>
          <ol>
            {toc.map((item) => (
              <li key={item.id}>
                <a href={`#${item.id}`}>{item.label}</a>
              </li>
            ))}
          </ol>
        </nav>
      )}
      <div className="info-page__content">{children}</div>
    </div>
  );
}
