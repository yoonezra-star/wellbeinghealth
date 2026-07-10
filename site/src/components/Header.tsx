"use client";
import Link from "next/link";
import { useState } from "react";

export default function Header() {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <header className="header">
      <div className="container">
        <div className="header__inner">
          <Link href="/" className="header__logo">
            <div className="header__logo-icon">🌿</div>
            <span>Wellbeing Health</span>
          </Link>

          <nav className="header__nav">
            <Link href="/blog">블로그</Link>
            <Link href="/blog?cat=운동">운동</Link>
            <Link href="/blog?cat=다이어트">다이어트</Link>
            <Link href="/blog?cat=건강식단">건강식단</Link>
            <Link href="/blog?cat=멘탈케어">멘탈케어</Link>
          </nav>
        </div>
      </div>
    </header>
  );
}
