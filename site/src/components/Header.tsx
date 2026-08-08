"use client";
import Link from "next/link";
import { useState } from "react";

export default function Header() {
  const [menuOpen, setMenuOpen] = useState(false);

  const closeMenu = () => setMenuOpen(false);

  return (
    <header className="header">
      <div className="container">
        <div className="header__inner">
          <Link href="/" className="header__logo" onClick={closeMenu}>
            <div className="header__logo-icon">🌿</div>
            <span>Wellbeing Health</span>
          </Link>

          <nav className="header__nav" aria-label="주 메뉴">
            <Link href="/blog">블로그</Link>
            <Link href="/blog?cat=운동">운동</Link>
            <Link href="/blog?cat=다이어트">다이어트</Link>
            <Link href="/blog?cat=건강식단">건강식단</Link>
            <Link href="/blog?cat=멘탈케어">멘탈케어</Link>
          </nav>
          <button
            type="button"
            className="header__menu"
            aria-label="메뉴 열기"
            aria-expanded={menuOpen}
            aria-controls="mobile-navigation"
            onClick={() => setMenuOpen((open) => !open)}
          >
            ☰
          </button>
        </div>
        {menuOpen && (
          <nav id="mobile-navigation" className="header__mobile-nav" aria-label="모바일 메뉴">
            <Link href="/blog" onClick={closeMenu}>블로그</Link>
            <Link href="/blog?cat=운동" onClick={closeMenu}>운동</Link>
            <Link href="/blog?cat=다이어트" onClick={closeMenu}>다이어트</Link>
            <Link href="/blog?cat=건강식단" onClick={closeMenu}>건강식단</Link>
            <Link href="/blog?cat=생활습관" onClick={closeMenu}>생활습관</Link>
            <Link href="/blog?cat=멘탈케어" onClick={closeMenu}>멘탈케어</Link>
            <Link href="/blog?cat=전문가칼럼" onClick={closeMenu}>전문가칼럼</Link>
          </nav>
        )}
      </div>
    </header>
  );
}
