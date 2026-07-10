# AdSense 신청 직전 체크리스트

점검일: 2026-07-03  
사이트: https://wellbeinghealth.co.kr

## 현재 신청 가능 상태

승인 준비도: 91 / 100

현재 큰 기술 리스크는 대부분 정리되었습니다. 남은 것은 Search Console에서 sitemap을 제출하고, 신청 후 며칠 동안 자동 대량 발행을 하지 않는 운영 안정화입니다.

## 완료된 항목

- `ads.txt`: https://wellbeinghealth.co.kr/ads.txt 200 OK
- `robots.txt`: sitemap_index.xml 명시 확인
- `sitemap_index.xml`: 200 OK
- 홈 noindex 없음
- 홈에서 AdSense publisher/client 감지
- 개인정보처리방침 공개 페이지 1개
- 사이트 소개, 문의하기, 면책 조항, 개인정보처리방침 노출
- 최근 60개 공개 글 중 중복 제목 0건
- 최근 60개 공개 글 중 범용 제목 신호 0건
- 최근 60개 공개 글 중 표 포함 글 31개
- 최근 60개 공개 글 중 안전 고지 포함 글 51개
- 최근 30개 공개 글에 공식 참고자료 추가
- 대표 글 20개에 편집자 요약, 체크리스트, 적용 기준 표 추가
- 대표 글 20개 모두 공식 참고자료, 안전 고지, 핵심 범위 블록 보유
- 자동 발행 크론은 주석 처리 상태
- 오래된 자동화 프롬프트의 가상 경험담/플레이스홀더 이미지 지시 제거

## Search Console에서 할 일

1. Google Search Console에 접속합니다.
2. 속성 `https://wellbeinghealth.co.kr/`을 선택합니다.
3. `Sitemaps` 메뉴로 이동합니다.
4. 아래 sitemap을 제출합니다.
   - `https://wellbeinghealth.co.kr/sitemap_index.xml`
5. 제출 후 `post-sitemap.xml`, `page-sitemap.xml`, `category-sitemap.xml`이 발견되는지 확인합니다.
6. URL 검사에서 아래 페이지를 각각 검사하고 색인 생성 요청합니다.
   - https://wellbeinghealth.co.kr/
   - https://wellbeinghealth.co.kr/%ec%82%ac%ec%9d%b4%ed%8a%b8-%ec%86%8c%ea%b0%9c/
   - https://wellbeinghealth.co.kr/%eb%ac%b8%ec%9d%98%ed%95%98%ea%b8%b0/
   - https://wellbeinghealth.co.kr/%ea%b0%9c%ec%9d%b8%ec%a0%95%eb%b3%b4%ec%b2%98%eb%a6%ac%eb%b0%a9%ec%b9%a8/
   - https://wellbeinghealth.co.kr/%eb%a9%b4%ec%b1%85-%ec%a1%b0%ed%95%ad/

## AdSense 신청 전 운영 규칙

- 신청 전후 3~7일 동안 자동 대량 발행을 하지 않습니다.
- 새 글을 올려야 한다면 하루 0~1개만 수동 검수 후 발행합니다.
- 신청 직후 제목, 메뉴, 정책 페이지를 대량 수정하지 않습니다.
- 건강/식단/운동 글에는 안전 고지와 공식 참고자료를 유지합니다.
- 실제처럼 보이는 가상 경험담, 치료·완치 단정, 가짜 출처 URL은 사용하지 않습니다.

## 최종 권장 순서

1. Search Console sitemap 제출
2. 대표 페이지 URL 검사 및 색인 요청
3. 24~48시간 대기
4. AdSense 사이트 검토 신청
5. 신청 후 자동 발행 중지 상태 유지

