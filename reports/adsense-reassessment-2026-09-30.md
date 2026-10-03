# Wellbeing Health 애드센스 거절 후 재점검 및 업데이트 계획

점검일: 2026-09-30 (한국 시간)
대상: https://wellbeinghealth.co.kr/
보고서 범위: 공개 사이트 점검과 업데이트 계획. 아래 실행 기록은 이 보고서를 바탕으로 이어서 적용한 수정 사항을 기록한다.

후속 편집 기록은 2026-10-01부터 덧붙인다. 주제군 분류는 자동 1차 분류라 오탐이 있을 수 있으며, 편집 전 본문으로 확인한다.

## 1. 결론

**현재는 즉시 재신청보다 콘텐츠 정리와 핵심 글 재편집을 먼저 하는 편이 적절하다.**

글 수나 필수 페이지의 분량 부족만으로 설명하기 어렵다. 106개 글과 소개·편집정책 등의 기반은 있으나, 비슷한 주제의 글이 분산되어 있고 구체적인 건강 주장에 연결되는 근거가 부족한 사례가 남아 있다. 홈페이지의 운영 문구와 실제 발행·수정 기록 사이에도 간극이 있다.

이전의 제목 순화, 안전 안내, 공통 참고자료 추가는 유지할 만한 개선이다. 그러나 일반적인 건강 설명에 같은 안내문과 기관 링크를 덧붙이는 것만으로는 각 글의 고유한 가치를 충분히 만들기 어렵다. 다음 작업의 중심은 **중복 주제 정리, 주장별 근거 확인, 한국 독자가 실제로 이용할 수 있는 구체적인 자료**여야 한다.

이 판단은 공개 사이트와 소스에서 확인한 위험 요인을 바탕으로 한 편집적 진단이다. Google의 내부 심사 근거를 확인한 것은 아니며, 특정 문제가 단독 거절 원인이라고 확정하거나 승인을 보장할 수 없다.

## 2. 점검 범위와 확인된 수치

공개 홈·글 목록·대표 글·운영 안내 페이지, 브라우저 렌더링, 주요 HTTP 응답, 로컬의 전체 게시물 메타데이터와 공통 템플릿을 확인했다. 106개 글 모두의 의학적 주장과 외부 원문을 대조한 전수 사실검증은 아직 아니다.

| 항목 | 확인 결과 | 해석 |
| --- | --- | --- |
| 게시물 | 106개 | 더 많이 쓰는 것 자체가 우선 과제가 아님 |
| 본문에 HTTP(S) 링크가 없는 글 | 70개 | 원문 추적성 점검 대상. 공통 참고자료를 포함한 최종 페이지의 링크 수와는 다름 |
| 대표 이미지 메타데이터가 없는 글 | 68개 | 기본 이모지로 표시됨. 이미지가 없다는 사실 자체는 정책 위반이 아님 |
| 최근 최초 발행일 | 2026-07-01 | 홈은 최초 발행일 기준으로 최신 6개를 표시 |
| 최근 수정일 메타데이터 | 2026-08-10 | 내용의 실제 검토 여부나 외부 운영 활동까지 증명하는 값은 아님 |
| 제목에 '간헐적' 포함 | 6개 | 목적 구분 및 통합 검토 대상 |
| 제목에 '지중해' 포함 | 4개 | 식재료·한국식 적용·장보기 내용의 역할 구분 필요 |
| 제목에 '슈퍼푸드' 포함 | 7개 | 영양·면역·항산화 설명의 중첩 여부 점검 필요 |
| 사이트맵 | HTTP 200, URL 113개 | 사이트맵 존재와 Google 색인 완료는 별개 |

주제별 숫자는 제목 키워드 집계다. 해당 글이 모두 복제 콘텐츠라는 뜻은 아니다. 일부 개정 글은 기록표와 안전 조건처럼 목적이 이미 구분되어 있으므로 유지할 가치가 있다.

### 정상 확인된 기술 기반

- 루트 도메인 HTTPS 접속이 인증서 검증을 우회하지 않고 성공했고 홈은 HTTP 200이었다. 과거 인증서 오류는 이번 접속에서는 재현되지 않았다.
- `/blog/`, `/robots.txt`, `/sitemap.xml`, `/ads.txt`가 HTTP 200을 반환했다.
- robots.txt는 전체 접근을 허용하고 실제 도메인의 사이트맵을 안내한다.
- 존재하지 않는 테스트 경로는 HTTP 404를 반환했다.
- 요청했던 Google 소유권 확인 메타 태그가 운영 홈 HTML에 존재한다. Search Console 계정에서 확인 버튼을 눌러 소유권이 승인됐는지는 별도 확인 사항이다.
- ads.txt에는 Google 게시자 항목이 있다. 이것만으로 계정 일치나 AdSense 승인 상태까지 확인한 것은 아니다.

## 3. 주요 문제와 우선순위

### P0. 구체적인 연구·수치를 독자가 추적하기 어려움

[근력 운동 기본 원리 글](https://wellbeinghealth.co.kr/blog/2026-06-28-근력-운동의-모든-것-강한-몸을-위한-필수-가이드/)에는 연구 연도와 저널명, 단백질 섭취량, 운동 후 섭취 시간에 관한 주장이 있지만, 해당 논문을 식별할 수 있는 제목·저자·DOI 또는 직접 링크가 없다.

[지중해 식단 구성 글](https://wellbeinghealth.co.kr/blog/2026-06-16-건강과-맛을-동시에-지중해-식단의-모든-것/)의 심혈관 위험 30%, 비만 위험 20% 등의 설명도 원문·대상 집단·위험 수치의 의미를 검토해야 한다. 이번 점검에서 이 수치 자체를 의학적으로 참 또는 거짓으로 확정하지 않았다.

공통 참고자료는 `site/src/lib/references.ts`에서 제목·요약·카테고리로 자동 선택한다. 기관의 일반 안내 페이지는 개별 논문의 수치나 모든 본문 주장을 입증하지 않는다.

**수정:** 수치·질환 효과·인과 주장마다 원문을 확인하고 해당 문단에 연결한다. 원문을 찾지 못하거나 적용 범위를 설명할 수 없는 주장은 삭제하거나 근거가 확인되는 범위로 다시 쓴다. 일반 배경자료와 실제 인용자료를 분리한다. 안전 문구가 붙었다는 이유로 검증 완료 처리하지 않는다.

### P0. 글별로 해결하는 질문이 충분히 구분되지 않음

간헐적 단식, 지중해식단, 슈퍼푸드, 유산소 운동, 아침 루틴 관련 글이 여러 URL로 분산되어 있다. 제목만 달라지고 정의·효과·주의사항이 반복되는 글은 독자가 다른 페이지까지 읽어야 할 이유가 약하다.

**수정:** 전체 글을 유지·재작성·통합·발행 보류 검토로 분류한다. 같은 질문에 답하는 글은 대표 글로 통합하고, 기록표처럼 목적이 다른 글은 독립 유지한다. 제목 유사성만으로 삭제하지 않는다. 통합 시 원문·이미지를 보관하고 실제 대체 관계가 있는 URL에만 영구 리디렉션을 적용한다.

### P1. 운영 설명과 실제 노출 내용 사이의 불일치

[홈](https://wellbeinghealth.co.kr/)은 '매주 업데이트'를 표시하지만, 공개 글의 최신 발행일은 7월 1일이고 로컬 수정일 메타데이터의 최신 값은 8월 10일이다. 최근 개정 글도 최초 발행일이 오래되면 홈에 나타나지 않는다. 일부 카드의 요약은 문장 중간에서 끊겨 있다.

**수정:** 이행 여부를 확인할 수 없는 운영 약속은 실제 운영 방식에 맞춘다. 최초 발행일과 실질 수정일을 분리해 표시하고, 최근 검토한 핵심 글을 홈에 편집해서 배치한다. 날짜만 오늘로 바꾸지 않는다. 요약은 완결된 문장으로 작성한다.

### P1. 글 목록의 초기 HTML과 탐색 구조

[글 목록](https://wellbeinghealth.co.kr/blog/)의 서버 응답 HTML에는 게시물로 연결되는 `<a>`가 없고 '로딩 중' 상태가 있다. 실제 브라우저에서 JavaScript 실행 후에는 106개 목록이 표시되고 운동 필터도 작동했다. 따라서 '사이트가 비어 있다'거나 'Google이 색인할 수 없다'고 단정할 수는 없다.

원인은 클라이언트 검색 매개변수에 의존하는 목록과 Suspense 구성이다. 현재 목록에는 검색·페이지 나누기가 없고 카테고리는 쿼리 매개변수 필터 방식이다.

**수정:** 글 링크와 요약을 정적 HTML에 포함하고, 기존 스타일을 유지한 채 검색·페이지 나누기·주제별 탐색을 개선한다. 독립적인 안내 가치가 있는 카테고리 페이지를 제공한다면 빈 템플릿을 늘리지 말고 대표 글과 학습 순서를 함께 구성한다.

### P1. 편집 책임과 검토 이력을 더 구체적으로 보여줄 필요

소개·편집정책은 이미 존재하며, 단순히 길이를 늘릴 필요는 적다. 현재 저자는 공통 'Wellbeing Health 편집팀'으로 표시된다. 이는 그 자체로 위반은 아니지만, 건강정보의 작성·검증 책임을 독자가 판단할 단서가 제한적이다.

**수정:** 실제 운영 주체, 편집 책임, 자료 확인 방식, 오류 정정 경로를 일관되게 연결한다. 개인 실명·자격은 운영자가 실제로 공개할 수 있는 정보만 사용하고, 의료인 감수나 경력을 꾸며내지 않는다. '의학적 감수'와 '자료 대조 편집'을 구분한다.

### P2. 이미지와 표의 실용성이 부족한 부분

대표 이미지가 없는 글은 공통 이모지로 표시되고, 표로 읽혀야 할 일부 비교 정보는 줄글처럼 분리되어 있다. 이는 승인 요건의 이미지 수 문제라기보다 이해와 완성도의 문제다.

**수정:** 기존 사진·색상·폰트·레이아웃을 임의 교체하지 않는다. 원본 이관 자료와 현재 이미지 매핑을 먼저 비교한다. 근거가 있는 식품 표시 예시·기록표·운동 단계 자료처럼 이해에 기여하는 시각자료만 추가하고 출처·권리를 확인한다. 모바일에서는 표가 잘리거나 본문을 밀어내지 않도록 검증한다.

## 4. 실행 계획

아래 일정은 작업량을 나누기 위한 추정치이며 승인 기간이나 Google의 최소 요건이 아니다. 실제 사실검증 범위에 따라 연장될 수 있다.

| 단계 | 예상 작업량 | 실행 내용 | 완료 산출물 |
| --- | --- | --- | --- |
| 1. 목록화 | 1~2일 | 106개 글의 독자 질문·중복 주제·출처·이미지·수정 상태 조사. 실제 Search Console 데이터가 있으면 유입과 색인 상태를 함께 확인 | 전수 편집 대장, 통합 후보표, URL·이미지 보존 목록 |
| 2. 노출 문제 수정 | 1~2일 | 홈 상위 글의 근거 없는 주장 우선 처리, 운영 문구·요약 정리, 정적 글 목록, 깨진 표 수정 | 배포 전후 HTML·화면 비교, 회귀 점검 결과 |
| 3. 대표 콘텐츠 재편집 | 5~10일 | 첫 묶음 6~8개 핵심 자료를 근거 중심으로 재작성하고 중복 글의 역할 정리. 나머지 공개 글의 심각한 문제도 별도 처리 | 주장-출처 대조표, 대표 글, 통합 매핑, 수정 이력 |
| 4. 책임·운영 보강 | 1~2일 | 실제 운영자 정보 확인, 기사별 인용자료와 배경자료 분리, 정정 절차와 정기 검토 일정 정리 | 작성·검토 정보, 정정 기록 양식, 지속 운영 계획 |
| 5. 검증과 재신청 판단 | 기능 검증 후 관찰 | 링크·모바일·색인·실제 이용 흐름 점검, 핵심 글이 공개 배포본에 반영됐는지 확인 | 아래 완료 기준 점검표, 남은 이슈 목록 |

### 첫 번째 콘텐츠 묶음

1. 근력운동 기본 글: 연구·단백질·시간 주장 검증, 대상과 강도 구분, 초보자가 따라갈 수 있는 구체적인 예시 구성.
2. 지중해식단 대표 글: 4개 글의 역할 비교 후 통합 여부 결정. 한국 식재료 교체표와 장보기 예시 보강.
3. 간헐적 단식 안내: 기본 안내·시작 전 조건·기록표를 명확히 구분. 같은 설명을 반복하는 글은 통합 검토.
4. 슈퍼푸드·면역 식단: 특정 식품 효능 나열을 줄이고 실제 식사 구성과 주장 검토에 집중.
5. 저염식 글: 영양표시를 읽고 실제 섭취량을 계산하는 예시. 가상의 숫자는 예시임을 표시.
6. 수면 관련 글: 수면일지와 환경 점검 순서를 제공하고 비슷한 수면·아침 루틴 글의 역할 정리.

6~8개라는 숫자는 첫 작업 묶음의 크기일 뿐 승인 기준이 아니다. 대표 글만 개선하고 나머지 낮은 품질의 글을 방치한 상태를 완료로 간주하지 않는다.

도구를 추가한다면 인쇄 가능한 기록표 또는 기기 내 저장 방식부터 검토한다. 건강 기록을 분석 도구로 전송하거나 진단 결과처럼 표시하지 않는다. 도구 자체는 승인 필수 조건이 아니다.

## 5. 작업별 검증 기준

- 유지하는 각 글에 '누가 어떤 질문을 해결하는가'와 다른 글에는 없는 구체적 가치가 명시되어 있다.
- 중요한 건강 수치·효능·인과 주장은 확인한 원문과 연결되며, 미확인 주장은 정리되어 있다.
- 본문 인용과 자동 추천 배경자료를 구분한다. 링크 수만으로 검증 완료 표시를 하지 않는다.
- 중복 후보의 유지·통합 사유가 기록되고, 기존 URL과 이미지의 처리 이력이 남는다.
- 홈페이지 운영 문구와 실제 발행·검토 이력이 일치한다. 실제 내용 변경 없는 날짜 갱신은 하지 않는다.
- 글 목록의 초기 HTML에 실제 게시물 링크가 포함된다. 검색·필터·페이지 이동은 적용 범위대로 작동한다.
- 데스크톱·모바일에서 본문, 표, 이미지, 메뉴를 확인하고 깨진 링크 및 예상치 않은 빈 페이지가 없다.
- canonical, sitemap, robots, 리디렉션이 공개할 URL과 일치한다. 통합 후 사이트맵의 URL 수 감소는 정상일 수 있다.
- 운영자 정보와 검토 표시는 실제 사실과 일치하고 정정 연락 경로가 동작한다.
- 공개 사이트와 GitHub·Cloudflare 배포본의 변경이 일치하는지 실제 배포 후 확인한다.

## 6. 실제 이용과 재심사

이번에는 Search Console·GA4 계정의 비공개 실적을 열람하지 않았다. 트래픽 부족, 실제 이용자 부재, 색인 누락 규모는 현재 확정할 수 없다.

다음 실행 때 최근 28일·90일의 검색 노출·클릭·랜딩 페이지를 기준선으로 기록하고, GA4가 구성되어 있다면 참여 흐름도 함께 본다. 핵심 글을 읽은 독자가 다음 행동을 이해하는지 실제 피드백으로 확인한다. 데이터가 적다면 그 사실을 기록하며, 숫자를 만들어 채우지 않는다.

재신청은 위 수정과 배포 검증을 완료한 뒤 판단한다. 정해진 방문자 수·글자 수·게시물 수를 달성하면 승인된다는 전제는 두지 않는다. 유입 구매·봇 트래픽·클릭 유도는 사용하지 않는다. Search Console 색인 여부도 AdSense 승인을 대신하지 않는다.

## 7. 이전 점검표의 사용 범위

2026-10-01 갱신 자동 분류는 high 0 / review 36 / lower 70 / 본문 직접 링크 없음 0으로 집계됐다. 이는 특정 표현·수치·링크 패턴을 찾는 편집 우선순위용 휴리스틱이며, 의료 정확성 검증이나 원문 근거의 충분성, 고유 가치, AdSense 승인 가능성 점수가 아니다. 'high를 0으로 만들기'를 최종 목표로 삼지 않는다.

면책문·참고 링크·소개 페이지 분량을 계속 늘리는 방식보다, 글의 실제 문제 해결 능력을 검증하는 방식으로 완료 기준을 바꾼다. 승인 회피를 위한 일괄 비공개·무차별 삭제·noindex 추가도 해결책으로 삼지 않는다.

## 8. 근거 자료

- [Google 애드센스 콘텐츠 및 사용자 환경](https://support.google.com/adsense/answer/10015918?hl=ko): 고유한 가치, 유사 콘텐츠의 확장·통합, 이해하기 쉬운 탐색을 검토하는 기준.
- [Google 게시자 정책](https://support.google.com/adsense/answer/10502938?hl=ko): 광고가 게재되는 콘텐츠의 기본 정책. 사용자 제공 정책 주소가 이 문서로 연결됨.
- [유용하고 신뢰할 수 있는 사용자 중심 콘텐츠](https://developers.google.com/search/docs/fundamentals/creating-helpful-content?hl=ko): 출처·책임·독창적 기여·독자 중심성을 점검하는 검색 품질 참고자료. AdSense 승인 공식과 동일하지 않음.
- [Google 웹 검색 스팸 정책](https://developers.google.com/search/docs/essentials/spam-policies?hl=ko): 가치가 없는 대량 콘텐츠와 복제 관련 참고 기준. 이 사이트가 공식적으로 스팸 판정을 받았다고 단정한 것은 아님.
- [Search Console 직접 조치 보고서](https://support.google.com/webmasters/answer/9044175?hl=ko): 사용자가 제공한 빈약한 콘텐츠 링크의 상위 문서. AdSense 거절 통지만으로 Search Console 직접 조치가 존재한다고 볼 수 없음.

### 주요 구현 위치

- 홈·최신 글: `site/src/app/page.tsx`, `site/src/lib/posts.ts`
- 목록 렌더링: `site/src/components/BlogList.tsx`, `site/src/app/blog/page.tsx`
- 기사별 저자·참고자료: `site/src/app/blog/[slug]/page.tsx`, `site/src/lib/references.ts`
- 운영 정보: `site/src/lib/site.ts`, `site/src/app/about/page.tsx`
- 게시물 원문: `site/content/posts/`

## 실행 기록

- 1단계(전체 편집 대장): 완료. [106개 글 편집 대장](./adsense-editorial-inventory-2026-09-30.csv)을 만들었다. 주제군은 자동 1차 분류이며 글의 유지·통합 결정은 편집자가 본문을 비교한 뒤 내려야 한다.
- 2단계(홈·목록 노출): 완료. 68개 중간에서 끊긴 요약을 본문 첫 문장의 완결형으로 고쳤다. 홈에서 확인되지 않은 '매주 업데이트' 문구를 없애고 실제 수정일 기반 최신 글을 노출한다. 블로그 정적 HTML에 106개 글 링크가 생성되는 것을 빌드 결과에서 확인했다. 검색·카테고리 필터는 로컬 브라우저에서 동작을 확인했다.
- 3단계(대표 콘텐츠 재편집): 로컬 완료. 6개 대표 글을 새 제목·요약과 함께 다시 편집하고, 핵심 수치에 직접 연결되는 원문 링크 및 연구 범위를 추가했다. 수정한 글은 근력운동, PREDIMED, 간헐적 단식, 저염식, 수면, 아침 식사다. 기존 이미지가 연결된 글은 이미지와 URL을 그대로 유지했다. 전체 106개 글의 완전한 의학 사실검증 및 중복 통합은 미완료다.
- 4단계(책임·운영 보강): 완료 가능한 범위 점검. 소개·편집정책·면책·개인정보 페이지에 운영팀, 출처 우선순위, 전문가 검토 표기 기준, 정정 접수 경로가 이미 구체적으로 있어 허위 개인 이름·자격이나 확인되지 않은 운영주기를 추가하지 않았다. 본문 인용 원문과 자동 추천 일반 참고자료는 구분해 표시한다.
- 5단계(로컬 검증): 로컬 범위 완료. `npm run build`가 118개 정적 경로를 모두 생성했다. 빌드 산출물의 HTML 115개와 내부 링크 3,944개를 검사해 끊어진 내부 링크 0개를 확인했다. 정적 글 목록은 106개 글을 포함하고, 검색·카테고리 필터도 확인했다. 개정 대표 글에서 본문·수정일·개별 원문·관련 글이 표시되며 이미지가 없는 글의 큰 자리표시자는 제거했다. 후속 모바일 경로 점검은 아래 10차 기록에 추가했다. 원본 사이트 대비 이미지 누락 대조와 Core Web Vitals 실측은 미완료다.
- GitHub·Cloudflare 배포: 사용자 확인 후 `main`에 `5bad87b` (`Improve AdSense editorial readiness`)를 푸시하고, Cloudflare Pages `wellbeinghealth-site` Production에 정적 빌드를 배포했다. [Cloudflare 배포 기록](https://dash.cloudflare.com/6bde2d07259fb28c49f960364300fa23/pages/view/wellbeinghealth-site/0e508525-660e-42c8-a609-6b4e5965746f). 배포 직후 사용자 도메인 홈·글 목록·편집정책 및 개정한 PREDIMED 글이 HTTPS 200으로 응답하는 것을 확인했다. 공개 홈에서 '매주 업데이트'가 사라졌고, 공개 글 목록에는 정적 글 링크가 포함되며 '로딩 중' 안내가 없고, PREDIMED 글에서 새 제목·본문·직접 원문 참고자료가 확인된다.
- GitHub 자동 배포: `.github/workflows/deploy.yml`을 `main` 푸시 시 빌드·프로덕션 배포하도록 변경하고 `00c7aee`로 푸시했다. GitHub Actions 실행이 빌드와 배포 모두 성공했고 Cloudflare Production에서 해당 커밋을 확인했다. [GitHub Actions 실행 기록](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36732447972). 이는 기존 Pages 프로젝트에 연결된 GitHub Actions 방식의 자동 배포다. Cloudflare 대시보드의 Pages 네이티브 Git 연결 표시는 별개이며 직접 업로드 프로젝트 설정에 따라 'No Git connection'으로 남을 수 있다.
- AdSense 재심사: 제출하지 않았다. 전체 106개 글의 의학적 사실검증과 전체 모바일·이미지 원본 대조가 남아 있으므로, 이 작업 결과가 승인을 보장하지 않는다.
- 6단계(미개정 게시물 주제별 심층 점검): 진행 중. 간헐적 단식으로 자동 분류된 8개 글을 본문 기준으로 검토했다. 이 중 공복 운동 글은 단회 운동 중 지방 산화와 장기 체지방 변화의 차이를 직접 연구 자료로 설명하도록 전면 개정했고, 단식 방식 비교 글은 99개 무작위시험 메타분석의 결과·효과 크기·추적 기간 한계를 반영해 전면 개정했다. 나머지 글은 개요·안전 안내·실천 기록·12개월 임상시험 해석 등 역할이 구분되는지 확인했으나 이번 단계에서 모두 원문 대조를 끝낸 것은 아니다. 당뇨 전단계 식단 글은 단식 주제군 오분류를 바로잡는다. 전체 106개 글 검토는 계속 남아 있다.
- 6단계 1차 묶음 공개 배포: `98842a4`는 CI에서 `next/font/google`의 빌드 시 Google Fonts 요청 실패로 멈췄다. 화면 글꼴은 유지하면서 빌드 시 외부 다운로드를 요구하지 않도록 `1b84092`에서 폰트 선언을 수정했고, 118개 경로 빌드와 GitHub Actions/Cloudflare Production 배포가 성공했다. 공복 운동 및 단식 방식 비교 글 모두 사용자 도메인에서 HTTPS 200, 새 제목과 본문 연구 링크를 확인했다. [복구 후 GitHub Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36739112881).
- 6단계 2차 묶음(면역·슈퍼푸드): 편집 검토 완료, 로컬 빌드·배포 확인 중. 자동 분류된 11개 글을 본문으로 검토해 7개를 전면 개정하고 4개는 고유 역할·출처를 확인해 유지했다. 발효식품 글은 36명 규모 17주 연구의 미생물 다양성·염증 표지자 결과를 질환 예방 주장과 분리했다. ‘체온 1도’ 글의 체온 상승=면역 강화 주장을 바로잡았고, 슈퍼푸드 글들은 면역 영양소 기초, 근거 읽기, 식품별 주장 확인, 끼니 예시, 영양소 공급원 표와 보충제 한계로 역할을 나눴다. 상세 상태는 편집 대장에 반영했다. 이 묶음 역시 전체 게시물의 의학적 사실검증을 뜻하지 않는다.
- 6단계 3차 묶음(수면·아침 루틴): 완료. 자동 분류된 17개 글 가운데 실제로 수면·아침 주제를 다루는 글과 체중관리·번아웃·피로·폭식 등 다른 주제를 혼동한 6개를 분리했다. 수면·루틴 글 10개를 전면 개정하고, 출처가 있고 실용 목적이 분명한 수면일지 글 1개와 다른 주제의 기존 개정 글 6개는 유지·재분류했다. 개정은 성인 수면 권고, 아동 연령별 수면 권고, 불면증 CBT-I 지침, 수면무호흡 상담 신호, 수면제한과 식욕·체중 연구의 한계를 반영했다. 여러 유사한 아침 루틴 글은 5분 시작, 전날 준비, 개인 일정 설계, 7일 점검으로 각각의 독자 과제를 구분했다. `a0c0b02`를 `main`에 푸시했고 GitHub Actions 프로덕션 배포가 성공했다([Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36784585228)). 수정 글 10개의 기존 URL이 사용자 도메인에서 모두 HTTPS 200으로 응답하며 새 제목을 표시하는 것을 확인했다. 전체 게시물의 의학적 사실검증은 계속 남아 있다.
- 6단계 4차 묶음(유산소·심장): 완료. 자동 분류된 12개 글을 본문으로 재검토해 유산소 관련 글 9개를 전면 개정했다. 뱃살의 국소 감량 약속, HIIT 우월성, 운동 후 대사·질병예방 수치 등 근거를 과장하거나 조건을 생략한 표현을 걷어내고, 2024년 116개 무작위시험 메타분석과 WHO·CDC·미국심장협회 자료의 모집단·한계를 함께 제시했다. 심장 건강·혈압·초보자 4주 예시·일상 활동·체중 관리 등으로 글별 독자 질문을 구분했다. 계단 운동과 주간 유산소 가이드 2개는 구체적인 안전·계획 정보와 공식 자료가 있어 유지했고, 중장년 근력운동 글 1개는 오분류를 바로잡아 `근력·홈트`로 이동했다. `7424826`을 `main`에 푸시했고 GitHub Actions 프로덕션 배포가 성공했다([Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36791454375)). `npm run build`에서 정적 경로 118개를 생성하고 개정 글 9개의 내부 블로그 링크 오류 0개를 확인했다. 사용자 도메인에서 9개 기존 URL 모두 HTTPS 200과 개정 제목을 확인했고, 4월 2일 글의 대표 이미지도 유지했다. 이번 묶음도 전체 사이트 의학 검증이나 AdSense 승인을 뜻하지 않는다.
- 6단계 5차 묶음(명상·스트레스): 완료. 자동 분류된 13개 글 가운데 실제 스트레스·명상 관련 11개를 확인해 8개를 전면 개정하고, 기존 출처·실천 절차·중단 신호가 구체적인 3개는 유지했다. 항산화 식단 글과 탈모 안내 2개는 각 주제로 재분류했다. 가슴 답답함을 불안으로 단정하지 않도록 응급 평가 신호와 공황장애 CBT 근거를 명시하고, 마음챙김·요가·표현적 글쓰기는 가능한 효과의 범위와 근거 한계를 표시했다. 감정 기록과 관계 경계, 스트레스 시 식사 루틴은 자가관리로 한정하고 증상 악화 시 중단·전문가 상담을 안내한다. `e002112`를 `main`에 푸시했고 GitHub Actions 프로덕션 배포가 성공했다([Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36793846077)). `npm run build`가 정적 경로 118개를 생성했고, 개정 글 8개에서 내부 블로그 링크 오류 0개와 기존 대표 이미지 보존을 확인했다. 사용자 도메인의 8개 기존 URL 모두 HTTPS 200으로 응답하며 새 제목을 표시한다. 전체 사이트 검토와 AdSense 승인은 계속 남아 있다.
- 6단계 6차 묶음(질환·증상 해설): 완료. 대장에 자동 분류된 9개를 원문으로 대조해 6개(화면 눈 피로, 운동 카페인, 비염·감기, 허리 통증, 지속 피로/ME/CFS, 목 통증·자세)를 전면 개정하고 3개(무릎 운동, 우울감과 산책, 근골격 통증 개요)는 근거·실용성·안전 안내가 구체적이어서 유지했다. 카페인 글은 질환 안내가 아니라 운동 수행·영양 주제여서 분류를 바로잡았다. 개정본에는 Cochrane 블루라이트 렌즈 검토, FDA·NIH ODS 카페인 자료, CDC/NICE ME/CFS 및 PEM 안내, CDC·EPA 비염/감염·실내 습도 자료, NHS 척추 증상 자료를 본문 주장과 연결했다. 자세·습도·카페인으로 질환을 예방한다는 보장, 출처 불명의 위험 수치, 장기 피로만으로 ME/CFS를 진단하는 설명을 제거하고 상황별 진료 신호를 보강했다. `npm run build`가 정적 경로 118개를 생성했고, 수정 글 6개의 정적 HTML 제목·출처 및 기존 두 대표 이미지 파일을 확인했다. `278827c`를 `main`에 푸시했고 GitHub Actions 프로덕션 배포가 성공했다([Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36794990909)). 사용자 도메인에서 수정한 6개 URL 모두 HTTPS 200과 새 제목을 확인했다. 전체 사이트의 의학 검증 및 AdSense 승인 여부는 계속 별도 과제다.
- 6단계 7차 묶음(영양·보충제): 완료. 대장에 해당하는 10개 글을 원문과 출처로 대조해 4개(편의점 한 끼 구성, 영양제 필요성·안전, 식사와 근골격 통증 근거, 건강기능식품 표시 읽기)를 전면 개정하고 6개(고단백 식사, 채소 세척·보관, 저염식 계산, 칼슘·비타민 D, 견과류와 인지 건강, 대사증후군 검진)는 구체적인 독자 과제와 안전 안내가 있어 유지했다. 통증 글은 식재료 세척 주제와 분리하고 식단·보충제가 통증을 치료한다는 인과 주장을 제거해 `질환·증상 해설`로 분류했다. 편의점 글은 존재가 확인되지 않는 이용률·제품 평균 수치를 걷어내고 가상 예시 없이 제공량·나트륨·한 끼 조합 점검표를 제공한다. 영양제 두 편은 제품 선택과 복용 안전이라는 별도 목적을 갖도록 중복을 줄였다. FDA·NIH·USDA·식품안전나라·식약처 및 질환별 식이중재 체계적 고찰 원문을 연결하고 미국 규제 설명을 한국 제도와 구분했다. 기존 URL과 대표 이미지를 유지했다. `npm run build`에서 정적 경로 118개를 생성했고, 개정 글 4개의 정적 출력과 기존 대표 이미지 3개를 확인했다. `13306e8`을 `main`에 푸시했고 GitHub Actions 프로덕션 배포가 성공했다([Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36796522668)). 사용자 도메인의 수정 글 4개 URL 모두 HTTPS 200 및 새 제목을 확인했다. 전체 사이트 검토와 AdSense 승인 여부는 계속 별도 과제다.
- 6단계 8차 묶음(생활습관·운동·건강정보): 완료. 기타로 묶였던 16개를 원문 기준으로 다시 분류해 12개를 전면 개정하고 4개는 독자 과제·근거·실천성이 충분해 유지했다. 물 섭취가 기초대사량을 높인다는 인과, 스마트폰 사용시간만으로 중독을 진단하는 오해, 산후 체형 복귀 압박, 유연성만으로 낙상을 막는다는 단순화를 바로잡았다. 산후 회복·긴급 경고 신호, 스마트폰 사용 환경 조정, 의욕 저하 시 작은 행동과 도움 요청, 초보 산행·수영 안전, 필라테스 근거 범위, 건강수명 분기 점검, 아침 운동, 건강정보 판별, 식사·활동 7일 계획으로 각 글의 역할을 구분했다. 원래 URL과 있던 대표 이미지를 보존했다. 상세 제목·주제 분류·수정일·본문 단어 수·본문 링크 수 및 유지 근거를 편집 대장에 반영했다. `npm run build`가 정적 경로 118개를 생성했고, 12개 산출물의 새 제목·HTML 존재와 기존 대표 이미지 4개를 확인했다. `de1cb26`을 `main`에 푸시했으며 GitHub Actions 프로덕션 배포가 성공했다([Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36798017532)). 수정한 12개 기존 URL 모두 사용자 도메인에서 HTTPS 200과 새 제목을 표시한다. 이번 묶음은 전체 게시물의 의학적 검증이나 AdSense 승인을 뜻하지 않는다.
- 6단계 9차 묶음(홈트·요가·지중해식 식사): 완료. 미개정 4편을 본문 검토해 모두 전면 개정하고, 홈트 글 두 편은 좁은 공간의 무기구 순환 루틴과 집에서의 주 2회 점진적 근력훈련이라는 별도 독자 과제로 구분했다. 홈트 두 글의 출처 없는 트렌드·비용·부상 감소 통계와 센터 운동 대비 결과 보장을 삭제하고 동작 변형, 주간 계획, 점진적 부하, 중단 신호를 넣었다. 요가 글의 출처 불명 유연성·근력·스트레스 개선 백분율과 보편적 효과 단정을 걷어내고 15분 입문 순서, 자세 조정 및 NCCIH 안전 지침을 추가했다. 지중해식 글은 2013 PREDIMED 결과의 모집단과 무작위 배정 문제에 따른 철회·재출판을 명시하고 30% 단일 수치의 일반화, 근거 없는 질환 예방·치료 단정과 음주 권유를 제거했다. 한국 식탁 교체표, 3일 식사 예시, Cochrane 근거 한계를 보강하고 네 URL을 유지했다. 편집 대장의 제목·분류·수정일·단어 수·직접 링크 수를 갱신했다. `npm run build`에서 정적 경로 118개를 만들었고 네 개 산출물의 제목·본문 참고자료 및 식단표 HTML을 확인했다. `c216bde`를 `main`에 푸시했고 GitHub Actions 프로덕션 배포가 성공했다([Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36817213820)). 수정한 4개 기존 URL 모두 사용자 도메인에서 HTTPS 200과 새 제목을 표시한다. 이번 묶음은 전체 사이트 의학 검증이나 AdSense 승인을 뜻하지 않는다.

### 6단계 10차 묶음

- 생활습관·탈모·코어·기구 홈트 네 편에서 출처 없는 질환·성과·시장 수치와 보편적 효과 보장을 걷어내고, 생활습관 2주 기록표, 유형별 탈모 진료 준비, 저강도 코어 기초 동작, 밴드·덤벨 선택과 고정 안전 확인을 구성했다. WHO·CDC·KDCA·대한피부과학회·NICE·NHS·MedlinePlus 등 원문을 연결하고 기존 기구 홈트 대표 이미지를 보존했다. 편집 대장도 제목·분류·검토 이유·단어 수·직접 링크 수를 갱신했다.
- 자동 주장 점검은 106편에서 high 0 / review 36 / lower 70 / 직접 링크 누락 0으로 갱신됐으나 의학적 사실검증 점수는 아니다. 중복 제거한 외부 URL 155개를 HEAD로 확인하며 오래된 WHO 나트륨 링크 1개를 공식 sodium-reduction 자료로 교체했다. 일부 공식기관은 HEAD를 차단하거나 시간 초과했으므로 이를 깨진 링크로 단정하지 않는다.
- 모바일 점검은 기사 106개와 정보 경로 7개, 총 113개 URL을 320px·390px에서 검사했다. 수면 기록표 글의 7열 표가 좁은 화면에서 가로 넘침을 일으켜 전체 기록을 보존한 2열 표로 변경했다. 수정 후 226개 경로·화면 조합에서 가로 넘침 0건, 리소스 오류 0건을 확인했다. 검색 `수면` 결과 14개, 검색 초기화 후 `건강식단` 필터 22개, 모바일 메뉴 열기·닫기 및 목록 이동도 확인했다. 이는 로컬 빌드의 레이아웃·기능 점검이며 접근성 전수검사나 실사용 성능 측정은 아니다.
- 배포 및 공개 확인: `822f86f`를 `main`에 푸시했고 GitHub Actions `36819648164`의 Cloudflare 배포가 성공했다. 수정한 네 편과 수면 기록·저염식 글까지 6개 기존 URL이 사용자 도메인에서 HTTPS 200 및 새 제목을 반환한다. 다섯 핵심 글은 공개 사이트에서도 320px·390px 화면에서 가로 넘침 없이 열렸다. [GitHub Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36819648164).

### 6단계 11차 원문 대조

- 자동 우선순위 상위 네 글(면역 보충제 근거, 비염·감기, 유산소 운동, 수면 환경)의 핵심 주장을 공식 자료와 대조했다. [NIH ODS 면역 기능 자료](https://ods.od.nih.gov/factsheets/ImmuneFunction-Consumer/), [CDC 감기 안내](https://www.cdc.gov/common-cold/about/), [MedlinePlus 알레르기 비염](https://medlineplus.gov/ency/article/000813.htm), [EPA 실내 습기 지침](https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home), [CDC 가습기 위생 안내](https://www.cdc.gov/drinking-water/prevention/preventing-waterborne-germs-at-home.html), [WHO 신체활동 권고](https://www.who.int/news-room/fact-sheets/detail/physical-activity), [CDC 대화 테스트](https://www.cdc.gov/physicalactivity/basics/measuring/index.html), [CDC 수면 습관](https://www.cdc.gov/sleep/about/), [AASM 만성 불면증 행동치료 지침](https://pubmed.ncbi.nlm.nih.gov/33164742/)을 확인했다.
- 비염 글의 알레르기 증상·상대습도·가습기 위생 안내와 수면 환경 글의 수면 습관·CBT-I 근거는 원문과 부합해 유지했다. 면역 글에는 보충제 고용량 부작용과 약물 상호작용 주의, 복용 전 상담 기준을 추가했다. 유산소 글에는 중강도 대화 테스트의 CDC 직접 출처를 연결하고 4주 예시는 개인 처방이 아닌 입문 예시임을 분명히 했다. 해당 두 글의 수정일과 편집 대장 검토 결과를 반영했다.
- 이 묶음은 네 편의 특정 주장·출처를 대조한 것이며 사이트 전체 의료 사실 검증으로 확대 해석하지 않는다. 자동 점검은 106편에서 high 0 / review 36 / lower 70 / 직접 링크 누락 0으로 유지됐다.
- 배포 및 공개 확인: `ad2c4b9`를 `main`에 푸시했고 GitHub Actions `36822253530` 배포가 성공했다. 네 검토 글의 기존 URL이 사용자 도메인에서 모두 HTTPS 200 및 예상 제목을 표시하고, 두 보강 글의 신규 안내·CDC 출처가 공개 HTML에 반영됐다. [GitHub Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36822253530).

### 6단계 12차 원문·이미지 대조

- 간헐적 단식 안내 2편, 견과류와 인지 건강, 항산화 보충제 글의 핵심 주장을 [NIA 단식 근거 요약](https://www.nia.nih.gov/news/calorie-restriction-and-fasting-diets-what-do-we-know), [NIA 식단과 알츠하이머병 자료](https://www.nia.nih.gov/health/alzheimers-and-dementia/what-do-we-know-about-diet-and-prevention-alzheimers-disease), [NCCIH 항산화 보충제 자료](https://www.nccih.nih.gov/health/antioxidant-supplements-what-you-need-to-know)와 대조했다. 단식의 장기 효과·안전성은 확정되지 않았고 특정 견과류가 치매를 예방한다고 할 수 없다는 문구는 원문 범위에 부합했다. 항산화제 글에는 고용량 베타카로틴 보충제가 특히 흡연자·직업적 석면 노출자에게 폐암 위험을 높일 수 있다는 안전 주의를 추가했다.
- 이미지 보존 대조는 WordPress 복원 기준 커밋 `1adf4da`와 현재 게시물 106개의 대표 이미지 경로를 비교했다. 한 건의 불일치를 찾았다. 무릎 운동 글이 복원 당시 연결돼 있던 무릎 관절 이미지 `wp-64-featured.webp` 대신 도시락 이미지 `wp-85-featured.webp`를 사용하고 있어 원래 매핑으로 되돌렸다. 이제 저장소의 WordPress 이미지 38개가 38개 고유 로컬 참조와 모두 일치하고, 빠진 파일·미참조 파일·중복 바이트 파일은 없다.
- 빌드 및 공개 확인: `npm run build`가 정적 경로 118개를 생성했다. `890cd96`을 `main`에 푸시했고 GitHub Actions `36823429942`가 성공했다. 검토한 4개 글과 이미지 복구 글의 기존 주소는 HTTPS 200이며, 항산화 안전 안내와 무릎 이미지가 공개 페이지에 반영됐다. 무릎 이미지는 실제 브라우저에서 로드 완료(1024×1024)했고, 다섯 글 모두 320px 화면에서 문서 가로 넘침이 없었다. [GitHub Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36823429942).
- 이 비교는 저장소의 복원 기준본과 현재본 간 대조다. 운영 중인 `https://wellbeinghealth.co.kr/wp-json/wp/v2/posts`는 현재 Cloudflare Pages에서 404를 반환해 현행 원 WordPress 미디어 라이브러리와의 독립 비교는 할 수 없었다. 원본 백업 또는 WordPress 미디어 내보내기가 있으면 추가 대조할 수 있다.
- Core Web Vitals 실측은 이 환경에 Chrome DevTools MCP가 없어 수행하지 않았다. 도구 기반 측정값으로 가장하지 않으며, DevTools 성능 측정 도구 연결 후 LCP·CLS·INP 측정이 남아 있다.

### 6단계 13차 원문 대조

- 인터벌 운동, 초보자 요가, 항산화 식품과 염증, 간헐적 단식 안전 안내 네 편의 주장을 CDC·HHS·NCCIH·NIA·NIDDK 원문과 대조했다. 인터벌 강도 설명은 [CDC 대화 테스트](https://www.cdc.gov/physicalactivity/basics/measuring/index.html), 요가 초보자 안전 문구는 [NCCIH 안전 자료](https://www.nccih.nih.gov/health/yoga-effectiveness-and-safety), 항산화 보충제의 한계는 [NCCIH 자료](https://www.nccih.nih.gov/health/antioxidant-supplements-what-you-need-to-know), 단식 근거와 당뇨병 약물 주의는 [NIA](https://www.nia.nih.gov/news/calorie-restriction-and-fasting-diets-what-do-we-know)·[NIDDK](https://www.niddk.nih.gov/health-information/professionals/diabetes-discoveries-practice/fasting-safely-with-diabetes) 자료로 확인했다.
- 인터벌·요가 글의 안전 조정과 연구 한계는 원문과 일치해 유지했다. 항산화 식품 글에는 고용량 베타카로틴 보충제 관련 흡연자 및 직업적 석면 노출자 폐암 위험 주의를 보강했다. 간헐적 단식 글에는 당뇨병 환자의 저혈당·고혈당·탈수 위험, 약물 조절은 의료진과 정해야 한다는 NIDDK 근거를 추가했다. 두 글의 수정일과 편집 대장을 갱신했다.
- 자동 우선순위 집계는 106편 중 high 0 / review 36 / lower 70 / 직접 링크 누락 0으로 동일하다. 이 수치는 의학적 사실검증 점수가 아니며, 이 단계에서도 사이트 전체의 의학적 검토가 끝난 것은 아니다.
- 배포 검증: `41a859b`를 `main`에 푸시했고 GitHub Actions `36828374403`의 Cloudflare Pages 배포가 성공했다. wellbeinghealth.co.kr에서 이 네 글 모두 HTTPS 200 및 제목 일치를 확인했으며, 항산화 글의 석면 노출 주의와 단식 글의 NIDDK 링크가 공개 HTML에 반영됐다. [GitHub Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36828374403).

### 6단계 14차 원문 대조

- 혈압과 걷기, 허리 통증과 코어 운동, 가슴 답답함과 호흡 연습, 목 통증과 자세 네 편을 AHA·NICE·NHS·NIMH 원문과 대조했다. 혈압 글에는 검증된 자동 상완형 기기와 1분 간격 2회 측정·기록 방법을 추가했다. 허리 글의 활동 유지와 운동 선택은 NICE NG59에 부합하며, 회음부 감각·배뇨·배변 변화의 즉시 평가 권고를 NICE NG127 직접 링크로 덧붙였다.
- 흉부 불편을 공황으로 단정하지 않고 호흡 연습을 보조 수단으로 제한한 설명은 NHS·NIMH 자료와 부합해 유지했으며, NHS 흉통 원문 링크를 추가했다. 목 통증 글은 NHS 경추증 안내와 대조해 새로 생긴 보행·균형·협응 또는 대소변 기능 변화가 응급 평가 신호임을 구체화했다.
- 자동 우선순위 집계는 106편 중 high 0 / review 36 / lower 70 / 직접 링크 누락 0으로 유지됐다. 이는 휴리스틱 분류이며 의학적 사실검증 점수나 승인 예측이 아니다.
- 배포 확인: `e28ab98` 및 GitHub Actions `36832388882` 배포 성공. 수정한 네 페이지가 사용자 도메인에서 모두 HTTPS 200이며, 가정혈압 측정·NICE NG127·NHS 흉통·목 통증 응급 안내 문구가 공개 HTML에 반영됐다. [GitHub Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36832388882).

### 6단계 15차 원문 대조

- 칼슘·비타민 D, 중장년 근력운동, 지속 근골격 통증, 간헐적 단식 기록표 네 편을 NIAMS·NIH ODS·NIA·WHO·NHS·NIDDK 자료와 대조했다. 뼈 건강 보충제 중복·약물 상호작용, 근력운동 주 2일·점진적 증가, 단식 근거 한계에 대한 기존 설명은 공식 안내와 부합했다.
- 단식 기록표에는 당뇨병 또는 혈당강하제 복용 시 저혈당·고혈당·탈수 위험을 의료진과 검토하고 약물 계획을 임의로 바꾸지 말라는 문구와 NIDDK 직접 링크를 추가했다. 근골격 통증 글의 근거가 특정하지 않는 `30~60분마다`라는 고정 간격을 없애고 개인의 업무·증상에 맞춘 자세 변경으로 조정했으며 NHS 활동 유지 안내를 연결했다. 칼슘 글에는 NIH ODS 전문 자료를 추가했다.
- 자동 우선순위 집계는 106편 중 high 0 / review 36 / lower 70 / 직접 링크 누락 0이다. 이는 사실검증이나 승인 예측 점수가 아니다. `npm run build`에서 정적 경로 118개를 생성했다.
- 배포 확인: `741c051` 및 GitHub Actions `36833192876` Cloudflare Pages 배포 성공. 네 페이지 모두 사용자 도메인에서 HTTPS 200이며 수정 문구·출처가 공개 HTML에서 확인됐다. [GitHub Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36833192876).

### 6단계 16차 원문 대조

- 단기간 체중 감량, 수면 습관 점검, 독서와 인지 건강 세 편을 CDC·NIDDK·NIMH·AASM·NIA 원문과 대조했다. CDC의 연령별 수면 시간과 수면일지 항목, AASM의 만성 불면증 기준 및 CBT-I 강한 권고, NIA의 독서와 인지 건강 관찰연구·불확실성 설명은 본문과 부합해 유지했다.
- 단기간 빠른 감량과 담석 위험 설명에 NIDDK 직접 자료를 연결했다. 독서 글의 갑작스러운 혼란·언어 문제·편측 약화는 뇌졸중 응급 신호와 일치해 CDC 원문 링크를 추가했다. 체중·인지 건강 글의 수정일과 편집 대장을 갱신했다.
- 자동 우선순위 집계는 106편 중 high 0 / review 36 / lower 70 / 직접 링크 누락 0이며, 이는 사실검증이나 승인 예측 점수가 아니다. `npm run build`에서 정적 경로 118개를 생성했다.
- 배포 확인: `aaac5a5` 및 GitHub Actions `36835077361` 배포 성공. 세 페이지 모두 사용자 도메인에서 HTTPS 200을 반환했다. 체중 감량 글의 NIDDK 담석 출처, 독서 글의 CDC 뇌졸중 링크가 공개됐고, 수정 없이 유지한 수면 글의 제목·시간 기준·CBT-I 안내도 확인했다. [GitHub Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/36835077361).

### 6단계 17차 원문 대조

- 식사와 만성 근골격 통증, 아침 식사 구성, 우울감과 산책·빛, 제철 채소 세척·보관 네 편을 체계적 문헌고찰·WHO·NIMH·CDC·FDA 원문과 대조했다. 류마티스관절염 식이 메타분석의 매우 낮은 확실성, 섬유근육통·만성 통증 식이 연구의 제한과 이질성, WHO의 건강 식사 원칙은 본문 설명과 부합했다. ([RA 메타분석](https://pmc.ncbi.nlm.nih.gov/articles/PMC8706441/), [섬유근육통 고찰](https://pmc.ncbi.nlm.nih.gov/articles/PMC7551150/), [만성 근골격 통증 고찰](https://pmc.ncbi.nlm.nih.gov/articles/PMC9180920/), [WHO](https://www.who.int/news-room/fact-sheets/detail/healthy-diet))
- 우울감 글의 2주 이상 증상 평가, 계절성 우울증 광선치료의 별도 적용·주의, 자외선 보호 안내와 채소의 흐르는 물 세척·세제 금지·교차오염·냉장 보관 문구도 원문과 맞아 유지했다. ([NIMH 우울증](https://www.nimh.nih.gov/health/publications/depression), [NIMH 계절성 우울증](https://www.nimh.nih.gov/health/publications/seasonal-affective-disorder), [CDC 자외선 안전](https://www.cdc.gov/skin-cancer/sun-safety/), [FDA 농산물 안전](https://www.fda.gov/food/buy-store-serve-safe-food/selecting-and-serving-produce-safely))
- 자동 점검은 106편 중 high 0 / review 36 / lower 70 / 직접 링크 누락 0이다. 이는 사실 판정이나 승인 예측이 아니다. `npm run build`에서 정적 경로 118개를 생성했다.

### 6단계 18차 원문 대조

- 근력운동 시작, 대사증후군 검사·생활관리, 마음챙김, 발효식품·프로바이오틱스 네 편을 WHO·NIA·NHLBI·NCCIH 및 1차 연구와 대조했다. 성인 근력활동 주 2일 이상 권고는 인구 수준 지침으로 표현되어 있고, 운동 예시는 개인 처방과 분리되어 있어 유지했다. ([WHO 신체활동 지침](https://www.who.int/europe/news-room/fact-sheets/item/physical-activity), [NIA 근력·균형 운동](https://www.nia.nih.gov/health/four-types-exercise-can-improve-your-health-and-physical-ability))
- 대사증후군 글은 체중만으로 자가진단하지 않고 여러 위험요인의 검사·전문가 해석을 권하며 처방약 임의 조정을 금지한다. 마음챙김 글은 효과를 보장하지 않고 부정적 경험 시 중단, 기존 치료 대체 금지와 도움 요청을 설명한다. 두 글 모두 출처와 주의 문구가 원문에 부합해 유지했다. ([NHLBI 진단](https://www.nhlbi.nih.gov/health/metabolic-syndrome/diagnosis), [NHLBI 생활관리](https://www.nhlbi.nih.gov/health/metabolic-syndrome/treatment), [NCCIH 마음챙김 효과·안전](https://www.nccih.nih.gov/health/meditation-and-mindfulness-effectiveness-and-safety))
- 발효식품 글의 건강한 성인 36명·17주 무작위 식사 연구 설명은 연구의 범위를 넘지 않으며, 이를 특정 발효식품의 질환 예방이나 치료 증거로 확대하지 않는다. 보충제와 식품을 구분하고 중증 질환·면역저하 시 안전 확인을 권해 유지했다. ([Cell 연구 초록](https://pubmed.ncbi.nlm.nih.gov/34256014/), [NCCIH 프로바이오틱스 효과·안전](https://www.nccih.nih.gov/health/probiotics-usefulness-and-safety))
- 자동 주장 점검은 106편 중 high 0 / review 36 / lower 70 / 직접 링크 누락 0이었다. `npm run build`가 정적 경로 118개를 생성했다. 원문이 타당해 이번 차수는 본문 수정 없이 검증 기록만 갱신했다. 이 검증은 모든 의학적 주장에 대한 보증이나 AdSense 승인을 뜻하지 않는다.

### 6단계 19차 원문 대조

- 면역 영양소·감염 예방, 만성 불면증의 CBT-I, 보충제의 약물 상호작용·미국 FDA 규제, 스트레스와 소화불량 네 편을 NIH ODS·AASM·ACP·FDA·NIDDK 원문과 대조했다. 결핍이 없는 사람에게 보충제를 더 먹는다고 감염 예방이 보장되지 않는다는 설명과 면역 기능을 단일 수치로 나타내기 어렵다는 문구는 ODS 내용과 일치한다. ([NIH ODS 면역 기능 소비자 자료](https://ods.od.nih.gov/factsheets/ImmuneFunction-Consumer/))
- 불면증 글의 만성 불면증 CBT-I 권고 및 수면위생 단독치료의 한계는 AASM·ACP 안내와 일치한다. 보충제의 사전 승인·상호작용 설명도 FDA의 미국 규제 안내를 한국 제도와 분리해 서술했다. 두 글은 유지했다. ([AASM 권고](https://aasm.org/new-guideline-supports-behavioral-psychological-treatments-for-insomnia/), [ACP 권고](https://www.acponline.org/acp-newsroom/acp-recommends-cognitive-behavioral-therapy-as-initial-treatment-forchronic-insomnia), [FDA 보충제 규제·안전](https://www.fda.gov/consumers/consumer-updates/fda-101-dietary-supplements))
- 스트레스와 소화불량 글의 스트레스를 단일 원인으로 단정하지 않는 점과 진료 경고 신호는 NIDDK 설명에 부합한다. 독자가 증상·진료 필요 신호를 바로 확인하도록 해당 문단에 NIDDK 증상·원인 페이지 링크를 연결했다. ([NIDDK 소화불량 증상·원인](https://www.niddk.nih.gov/health-information/digestive-diseases/indigestion-dyspepsia/symptoms-causes))
- 자동 주장 점검은 106편 중 high 0 / review 36 / lower 70 / 직접 링크 누락 0이었다. `npm run build`가 정적 경로 118개를 생성했다. 이 차수는 면역·불면증·보충제 글은 유지하고, 소화불량 글의 NIDDK 출처 연결을 문맥에 맞게 보강했다. 편집·원문 대조는 AdSense 승인을 보장하지 않는다.

### 6단계 20차 원문 대조

- 면역 슈퍼푸드 광고 점검표, 탈모 진료 준비, 면역 영양소 식품표, 심장 건강 운동 네 편을 NCCIH·질병관리청·미국피부과학회·NIH ODS·WHO·미국심장협회 원문과 대조했다. 베리·채소·요거트·마늘을 감염 치료제로 제시하지 않는 설명과 탈모 원인별 평가·검사 안내는 근거 범위에 부합해 유지했다. ([NCCIH 마늘 근거·안전](https://www.nccih.nih.gov/health/garlic), [질병관리청 남성형 탈모](https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=2067), [질병관리청 원형탈모](https://health.kdca.go.kr/healthinfo/biz/health/gnrlzHealthInfo/gnrlzHealthInfo/gnrlzHealthInfoView.do?cntnts_sn=6700), [AAD 진단·치료](https://www.aad.org/public/diseases/hair-loss/treatment/diagnosis-treat))
- 면역 광고 글은 NCCIH가 마늘 보충제와 감기에 관한 근거를 소규모·한계 있는 두 연구로 설명하는 점과 출혈·항응고제 주의를 반영해 본문에 직접 연결했다. 비타민 C·D·아연 식품표는 ODS의 영양소별 공급원 자료를 추가해 독자가 각 표 항목을 교차 확인할 수 있도록 했다. ([ODS 비타민 C](https://ods.od.nih.gov/factsheets/VitaminC-Consumer/), [ODS 비타민 D](https://ods.od.nih.gov/factsheets/VitaminD-Consumer/), [ODS 아연](https://ods.od.nih.gov/factsheets/Zinc-Consumer/))
- 심장 운동 글의 성인 활동량, 대화 테스트, 점진적 시작과 중단·응급 신호는 WHO·AHA 안내와 부합했다. 자동 점검은 106편 중 high 0 / review 36 / lower 70 / 직접 링크 누락 0이며, `npm run build`가 정적 경로 118개를 생성했다. 이 대조는 글의 모든 의학적 내용을 보증하거나 AdSense 승인을 보장하지 않는다. ([WHO 신체활동](https://www.who.int/europe/news-room/fact-sheets/item/physical-activity), [AHA 활동 계획·경고 신호](https://www.heart.org/en/health-topics/cardiac-rehab/getting-physically-active/develop-a-physical-activity-plan-for-you))

### 6단계 21차 원문 대조

- 긍정 확언 글은 초기 실험과 후속 재현 연구를 함께 반영했다. 2009년 연구에서 자존감이 낮은 참여자에게 부정적 결과가 관찰된 점과 2020년 두 재현 연구에서 그 차이가 확인되지 않은 점을 나란히 설명해, 확언을 보편적 치료법 또는 보편적 위해로 단정하지 않도록 보강했다. ([Wood 등, 2009](https://doi.org/10.1111/j.1467-9280.2009.02370.x), [Flynn·Bordieri, 2020](https://doi.org/10.1016/j.jcbs.2020.03.003))
- 무릎 운동 글의 체중부하 곤란·심한 부종·열감 등 진료 신호와 운동 중 통증 시 중단 안내는 NHS·AAOS 자료에 부합해 유지했다. 7일 식사·움직임 계획은 치료·수명 연장 보장이 아닌 개인 일정에 맞춘 빈 계획 도구이며 WHO 식사 원칙과 CDC 주간 활동 권고에 맞아 유지했다. ([NHS 무릎 통증](https://www.nhs.uk/symptoms/knee-pain/), [AAOS 무릎 운동 프로그램](https://orthoinfo.aaos.org/globalassets/pdfs/2017-rehab_knee.pdf), [WHO 건강 식사](https://www.who.int/news-room/fact-sheets/detail/healthy-diet), [CDC 성인 활동 권고](https://www.cdc.gov/physical-activity-basics/guidelines/adults.html))
- 일상 유산소 활동 글의 WHO·CDC 주간 권고량과 주간 단위 기록 방식은 타당하다. 참고자료 중 CDC 주소 하나가 일반 홈페이지로 연결되어 최신 성인 활동 지침 페이지로 교체했다. 자동 주장 점검은 106편 중 high 0 / review 36 / lower 70 / 직접 링크 누락 0이며, `npm run build`는 정적 경로 118개를 생성했다. 배포 커밋 `f14b473`의 GitHub Actions `36957669246`이 성공했고, 두 공개 페이지 모두 HTTPS 200으로 연구 인용과 새 CDC 링크를 확인했다. 이 대조는 모든 주장에 대한 보증이나 AdSense 승인을 의미하지 않는다.

### 6단계 22차 원문 대조

- 알레르기 비염·감기 글의 알레르겐 관련 가려움·재채기·콧물, 감기의 바이러스성·전파와 증상, 습도 30~50%(가능하면 60% 미만) 및 가습기 물 비우기·세척·건조 안내를 MedlinePlus·CDC·EPA 원문과 대조했다. 본문은 진단을 단정하지 않고 고위험군과 악화 신호를 구분해 유지했다. ([MedlinePlus 알레르기 비염](https://medlineplus.gov/ency/article/000813.htm), [CDC 감기](https://www.cdc.gov/common-cold/about/), [EPA 습기·곰팡이 안내](https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home), [CDC 가습기 관리](https://www.cdc.gov/drinking-water/prevention/preventing-waterborne-germs-at-home.html))
- 유산소 운동 기본 가이드의 성인 주간 권고량, 중강도 대화 테스트, 짧은 활동부터 늘리기 문구는 WHO·CDC 지침에 부합했다. 침실 환경 글의 조용하고 편안하며 서늘한 환경, 취침 전 기기 사용 조절 및 불면증 치료 연결도 CDC·AASM 자료의 범위를 넘지 않아 유지했다. ([WHO 신체활동](https://www.who.int/news-room/fact-sheets/detail/physical-activity), [CDC 성인 권고](https://www.cdc.gov/physical-activity-basics/guidelines/adults.html), [CDC 강도 측정](https://www.cdc.gov/physicalactivity/basics/measuring/index.html), [CDC 수면 안내](https://www.cdc.gov/sleep/about/), [AASM 불면증 지침](https://pubmed.ncbi.nlm.nih.gov/33164742/))
- 항산화 식품·보충제 글은 NCCIH의 사람 대상 근거 한계와 베타카로틴 보충제 고위험군 주의를 재확인했다. 참고문헌의 이전 NCCIH URL이 현재 제목의 페이지로 리디렉션되어 최신 공식 주소로 교체했다. 자동 점검은 106편 중 high 0 / review 36 / lower 70 / 직접 링크 누락 0, 빌드는 정적 경로 118개 생성으로 통과했다. 커밋 `1605458`의 GitHub Actions `36958605849`가 성공했고, 네 공개 페이지 모두 HTTPS 200이며 최신 NCCIH 주소가 공개 HTML에서 확인됐다. 이번 원문 대조는 의학적 보증이나 AdSense 승인 보장이 아니다.

### 6단계 23차 원문 대조

- 간헐적 단식 안내와 2주 기록표는 NIA의 사람 대상 장기 효과·안전성 근거 한계, NIDDK의 당뇨병 환자 단식 시 저혈당·고혈당·탈수 및 의료진의 개별 약물 계획과 대조했다. 장시간 공복을 성공으로 보지 않고, 약 임의 조정 금지·중단 신호·개별 상담 안내를 유지했다. ([NIA 단식 연구 개요](https://www.nia.nih.gov/news/calorie-restriction-and-fasting-diets-what-do-we-know), [NIDDK 당뇨병과 단식 안전](https://www.niddk.nih.gov/health-information/professionals/diabetes-discoveries-practice/fasting-safely-with-diabetes))
- 견과류 글의 특정 식품이 알츠하이머병을 예방한다고 할 수 없다는 설명은 NIA의 최신 안내와 일치했다. 건강한 식사 패턴의 잠재성은 인정하되 근거가 혼재돼 있고 특정 식품의 예방 효과는 입증되지 않았다는 균형을 유지했다. ([NIA 식사와 알츠하이머 예방 근거](https://www.nia.nih.gov/health/alzheimers-and-dementia/what-do-we-know-about-diet-and-prevention-alzheimers-disease))
- 요가 입문 글의 초보자 거꾸로서기·강제호흡 회피, 임신·고혈압·녹내장·균형 문제에서의 수정 및 의료진 상담은 NCCIH 안내와 부합했다. 네 글 모두 본문 수정은 불필요해 유지했고 편집 대장에 재대조를 기록했다. ([NCCIH 요가 효과와 안전](https://www.nccih.nih.gov/health/yoga-effectiveness-and-safety))
- 자동 주장 점검은 106편 중 high 0 / review 36 / lower 70 / 직접 링크 누락 0이었고, 정적 빌드는 118개 경로를 생성했다. 커밋 `ad5304c`의 GitHub Actions `36960006071`이 성공했으며 네 공개 페이지 모두 HTTPS 200을 반환했다. 이번 대조는 개별 의료 조언이나 AdSense 승인 보장이 아니다.

### 6단계 24차 원문 대조

- 칼슘·비타민 D 글의 식품 공급원, 고용량·상한량 고려와 레보티록신·퀴놀론계 항생제 상호작용 주의는 NIH ODS·NIAMS 자료에 부합했다. 글은 연령별 상한량을 임의의 단일 수치로 일반화하지 않고 약사·의료진 확인을 권해 유지했다. ([NIH ODS 칼슘 소비자 자료](https://ods.od.nih.gov/factsheets/Calcium-Consumer/), [NIH ODS 칼슘 전문가 자료](https://ods.od.nih.gov/factsheets/Calcium-HealthProfessional/), [NIAMS 칼슘·비타민 D](https://www.niams.nih.gov/health-topics/calcium-and-vitamin-d-important-bone-health))
- 중장년 근력운동 안내의 주요 근육군 주 2일 이상, 점진적 시작, 균형·낙상 위험 고려와 동일 근육군 연속일 과훈련 회피는 NIA 안내와 부합했다. 허리 통증 글의 활동 유지 및 마미증후군 의심 시 새 배뇨·배변·성기능 변화 또는 회음부 감각 저하를 즉시 평가받으라는 기준은 NICE NG59·NG127과 부합했다. ([NIA 근력운동 유형](https://www.nia.nih.gov/health/exercise-and-physical-activity/three-types-exercise-can-improve-your-health-and-physical), [NICE 허리 통증 지침](https://www.nice.org.uk/guidance/ng59/chapter/Recommendations), [NICE 신경학적 증상·의뢰 지침](https://www.nice.org.uk/guidance/ng127/chapter/Recommendations-for-adults-aged-over-16))
- 단식 시작 안전 조건 글의 장기 근거 불확실성, 당뇨병 환자 저혈당·고혈당·탈수 주의 및 의료진과의 개인별 약물·혈당 계획은 NIA·NIDDK 원문과 부합했다. 네 편은 본문 수정 없이 유지하고 재대조 결과를 편집 대장에 반영했다. 자동 점검은 106편 중 high 0 / review 36 / lower 70 / 직접 링크 누락 0이었고, 빌드는 정적 경로 118개를 생성했다. 커밋 `d43795d`의 GitHub Actions `36991837917`이 성공했으며 네 공개 페이지 모두 HTTPS 200을 반환했다. 이번 대조는 의료 조언이나 AdSense 승인 보장이 아니다.

### 6단계 25차 원문 대조

- 단기간 감량 글은 CDC가 안내하는 완만한 감량의 일반적 유지 가능성과 NIDDK의 빠른 감량·장시간 금식 시 담석 위험을 재확인했다. 글은 주당 감량 수치를 보편 처방으로 제시하지 않고 개인차·안전 조건을 구분한다. ([CDC 감량 단계](https://www.cdc.gov/healthy-weight-growth/losing-weight/index.html), [NIDDK 담석과 식이](https://www.niddk.nih.gov/health-information/digestive-diseases/gallstones/dieting))
- 독서 글은 NIA가 인지 자극 활동의 잠재 이점을 언급하면서도 관찰연구가 인과성을 입증하지 않는다고 구분한 설명과 부합했다. 식사·취미를 치매 예방 보장으로 제시하지 않는 문구를 유지했다. ([NIA 알츠하이머 예방 근거](https://www.nia.nih.gov/health/alzheimers-and-dementia/preventing-alzheimers-disease-what-do-we-know))
- 수면 습관 글의 만성 불면증 기준에 ‘충분한 수면 기회와 적절한 환경에도 불구하고’라는 핵심 조건을 보태고 NHLBI 진단 원문을 연결했다. 주 3회 이상·3개월 이상과 낮 기능 영향은 전문가가 종합 판단하는 정보로 구분했다. AASM의 성인 만성 불면증 CBT-I 강한 권고와 수면위생 단독치료의 한계 설명은 지침에 부합한다. ([NHLBI 불면증 진단](https://www.nhlbi.nih.gov/health/insomnia/diagnosis), [AASM 임상 지침 원문](https://pubmed.ncbi.nlm.nih.gov/33164742/))
- 만성 근골격 통증 글은 류마티스관절염 식이 메타분석의 매우 낮은 근거 확실성과 섬유근육통 식이 연구의 표본·방법 이질성 및 편향을 과장 없이 기술했다. 특정 식품·식단을 일반 통증 치료제로 제시하지 않아 유지했다. ([류마티스관절염 체계적 고찰](https://pubmed.ncbi.nlm.nih.gov/34959772/), [섬유근육통 식이 체계적 고찰](https://pubmed.ncbi.nlm.nih.gov/32878326/))
- 자동 점검은 106편 중 high 0 / review 36 / lower 70 / 직접 링크 누락 0이었고, 빌드는 정적 경로 118개를 생성했다. 커밋 `b16f425`의 GitHub Actions `37101931476`이 성공했으며 네 공개 페이지가 HTTPS 200을 반환했다. 수면 글의 보완 문장과 NHLBI 링크도 공개 HTML에서 확인했다. 대조와 수정은 개별 진단·치료 조언이나 AdSense 승인을 보장하지 않는다.

### 6단계 26차 원문 대조

- 가슴 답답함·호흡 연습 글은 NHS의 부드럽고 무리하지 않는 호흡 안내와 흉통·심한 호흡곤란 응급 신호, NIMH의 공황장애 증상·치료 안내와 대조했다. 증상을 공황으로 단정하지 않고 호흡 연습을 보조 수단으로 한정한 기존 설명이 부합해 유지했다. ([NHS 호흡 연습](https://www.nhs.uk/mental-health/self-help/guides-tools-and-activities/breathing-exercises-for-stress/), [NHS 흉통·심장마비 응급 신호](https://www.nhs.uk/conditions/heart-attack/), [NIMH 공황장애 안내](https://www.nimh.nih.gov/health/publications/panic-disorder-when-fear-overwhelms))
- 근력운동 시작 글의 성인 주요 근육군 근력활동 주 2일 이상은 WHO의 공중보건 권고와 일치한다. 본문은 이를 개인 운동 처방과 구분하고, 작은 단계로 시작해 증상에 따라 조절하도록 안내해 유지했다. ([WHO 신체활동 권고](https://www.who.int/initiatives/behealthy/physical-activity))
- 대사증후군 글은 허리둘레만으로 진단하지 않고 혈압 및 혈당·지질 검사와 의료진의 종합 평가를 권한다. 이는 NHLBI 진단 안내와 부합하며, 처방약 임의 변경 금지와 응급 증상 안내도 유지했다. ([NHLBI 진단](https://www.nhlbi.nih.gov/health/metabolic-syndrome/diagnosis), [NHLBI 치료·생활관리](https://www.nhlbi.nih.gov/health/metabolic-syndrome/treatment))
- 면역 식품 글의 결핍과 정상 면역 기능을 구분하고, 결핍이 없는 상태에서 보충제를 늘려도 대개 감염 예방·회복 이점이 없다는 설명은 NIH ODS 소비자 자료와 부합한다. 실험실 표지자와 감염 같은 임상 결과를 구분한 점도 유지했다. ([NIH ODS 소비자 자료](https://ods.od.nih.gov/factsheets/ImmuneFunction-Consumer/), [NIH ODS 전문가 자료](https://ods.od.nih.gov/factsheets/ImmuneFunction-HealthProfessional/))
- 네 편은 원문 수정 없이 재대조 기록만 추가했다. 106개 게시물 기준 자동 점검은 high 0 / review 36 / lower 70 / 본문 직접 링크 누락 0으로 확인했다. 이 휴리스틱 집계는 의료 사실검증 점수나 애드센스 승인 예측이 아니다. 이번 차수의 원문 대조 역시 개별 의료 조언이나 승인 보장이 아니다.

### 6단계 27차 원문 대조

- 상위 review 후보 중 알레르기 비염·감기, 성인 유산소 운동, 수면 환경 글은 이전 차수의 대조 기록이 있어 그 결과를 반복 검토로 표시했다. MedlinePlus의 비염 증상, CDC의 감기 전파·증상, EPA의 습도 관리와 WHO의 성인 주간 활동 권고는 유지했다. 침실의 조용하고 편안하며 서늘한 환경과 취침 전 기기 조절 역시 CDC 안내 및 만성 불면증의 CBT-I 지침을 대체하지 않는다는 문구와 부합해 그대로 두었다. ([MedlinePlus 비염](https://medlineplus.gov/ency/article/000813.htm), [CDC 감기](https://www.cdc.gov/common-cold/about/), [EPA 습기·곰팡이](https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home), [WHO 신체활동](https://www.who.int/news-room/fact-sheets/detail/physical-activity), [CDC 수면 습관](https://www.cdc.gov/sleep/about/))
- 비염 글의 코 세척은 멸균수·증류수·끓였다 식힌 물 사용 외에 수돗물 금지와 세척 기기의 세척·건조를 명시하고 FDA 직접 안내를 연결했다. ([FDA 코 세척 안전](https://www.fda.gov/consumers/consumer-updates/rinsing-your-sinuses-neti-pots-safe))
- 2주 단식 기록표는 NIA의 사람 대상 장기 효과·안전성 불확실성 및 NIDDK의 당뇨병 단식 위험과 대조했다. 2주를 검증된 안전성 시험기간처럼 읽지 않도록 한계를 명시하고, 근거가 특정되지 않은 30~60분 공복 연장 권고를 제거했다. 이미 있는 16:8 개요 글은 방식·시간표 설명, 시작 전 안전 글은 위험군 상담, 이 글은 증상과 일상 기능 기록이라는 독자 역할을 각각 유지했다. ([NIA 단식 근거](https://www.nia.nih.gov/news/calorie-restriction-and-fasting-diets-what-do-we-know), [NIDDK 당뇨병과 단식 안전](https://www.niddk.nih.gov/health-information/professionals/diabetes-discoveries-practice/fasting-safely-with-diabetes))
- 유산소 운동 글의 WHO 150~300분 중강도 또는 75~150분 고강도 권고와 CDC의 활동 분할·적은 양부터 시작 원칙을 재확인하고, CDC 링크를 성인 활동 지침 페이지로 교체했다. ([WHO 신체활동](https://www.who.int/news-room/fact-sheets/detail/physical-activity), [CDC 성인 활동 지침](https://www.cdc.gov/physical-activity-basics/guidelines/adults.html))
- 자동 점검은 106편 중 high 1 / review 35 / lower 70 / 본문 직접 링크 누락 0으로 표시됐다. 유일한 high 항목인 단식 기록표는 규칙이 `장기적인` 안의 `기적`, `불확실한` 안의 `확실한`, 부정문 `반드시 늘릴 필요는 없습니다`를 각각 보장 표현으로 오인한 명백한 휴리스틱 오탐이다. 원문 수동 확인에서는 과장 주장을 찾지 못했으며, 이 점수 자체는 의학적 사실 판정이 아니다. 수정한 세 글의 갱신일·단어 수·링크 수를 편집대장에 반영했다. `npm run build`가 통과해 정적 경로 118개를 생성했고, 생성 HTML에서 단식 기록기간 경계, FDA 코 세척 안전문, 새 CDC 링크를 확인했다.
- 배포 확인: `f85c959`의 GitHub Actions `37108150626` Cloudflare Pages 배포가 성공했다. 네 기존 URL 모두 `wellbeinghealth.co.kr`에서 HTTPS 200을 반환했고, 단식 기록기간 안내, FDA 코 세척 수돗물 금지 안내와 출처, 새 CDC 성인 활동 지침 링크를 공개 HTML에서 확인했다. [GitHub Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/37108150626). 원문 대조는 의료 조언이나 애드센스 승인을 보장하지 않는다.

### 6단계 28차 콘텐츠 중복·탐색 점검

- 면역·슈퍼푸드 관련 게시물을 원문 단위로 비교했다. 5월 21일 글은 연구 주장 평가법, 6월 6일 글은 베리·마늘·잎채소·요거트의 구체 주장, 6월 8일 글은 영양소 공급원 표, 6월 5일 글은 하루 끼니 예시, 5월 17일 글은 면역 식사와 보충제의 기본 원칙으로 독자 질문이 나뉜다. 이를 ‘면역 식품과 근거 읽기’ 주제 흐름으로 묶었다.
- 가장 큰 중복은 일반 식단 구성 글(5월 23일)과 슈퍼푸드 선택 기준(6월 10일)이었다. 기존 URL 및 그 글을 참조하는 링크를 보존하면서 5월 23일 글을 열량 처방이 아닌 빈 주간 계획표·장보기 점검 도구로 전환했다. 6월 10일은 식품 선택 원칙, 6월 5일은 메뉴 예시로 역할을 명확히 했다. 두 항산화 글은 식품과 염증 설명 및 고용량 보충제 안전성으로 나뉘므로 별도 항산화 근거 흐름에 배치했다. 게시물을 삭제하거나 리디렉션하지 않았다.
- 자동 점검기는 `장기적인` 안의 `기적`, `불확실한` 안의 `확실한`, 부정문 속 `반드시`를 단정 표현으로 세던 오탐을 제외하고, 실제 긍정형 `예방한다`는 계속 검출하도록 회귀 단언을 추가했다. 점검 결과는 106개 중 high 0 / review 32 / lower 74 / 직접 링크 누락 0이다. 이는 문장 위험도를 가늠하는 휴리스틱일 뿐 의료 사실검증이나 AdSense 승인 예측이 아니다.
- `npm run build`가 통과해 정적 경로 118개를 생성했다. 정적 내보내기 검사는 게시물 106개 전체의 필수 마크업 통과, 내부 링크 오류 0, 필수 파일 누락 0을 반환했다. 이전 감사 스크립트가 찾던 구형 문구를 현재 템플릿의 `주제별 일반 참고자료`로 교체하고 블로그 목록 페이지를 글 수에 포함하지 않도록 바로잡았다. 세 주제 흐름과 새 계획표가 생성 HTML에 표시됨을 확인했다.
- 배포 확인: 커밋 `070dd4e`의 GitHub Actions `37111215442` Cloudflare Pages 배포 성공. 주간 계획표, 식품 선택·계획 가이드, 면역 근거 가이드, 항산화 근거 가이드 네 페이지가 사용자 도메인에서 모두 HTTPS 200을 반환하고 기대한 주제 탐색 제목을 표시한다. [GitHub Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/37111215442).

### 6단계 29차 유산소 콘텐츠 중복·안전 점검

- 유산소 주제 9편을 원문과 주제 가이드에서 비교했다. 대표 글은 권고량·강도·목표별 원칙, 5월 22일 글은 독자가 직접 채우는 주간 계획표, 5월 28일 글은 4주간 활동·회복 기록과 다음 행동 결정, 6월 4일 글은 일상 일정에 활동을 붙이는 방법으로 역할을 나눴다. 나머지는 심장 중단 신호, 혈압 기록, 과체중·비만 성인 연구 해석, 일반 건강 이점의 근거 범위, 복부 국소감량 오해라는 독자 질문으로 구분했다. 기존 URL과 대표 이미지 메타데이터를 보존했으며 글을 삭제하거나 새 글로 중복 발행하지 않았다.
- 대표 가이드의 구체적인 4주 진도표는 전용 기록 글과 내용이 겹쳐 간결한 개인별 조정 원칙으로 바꾸고 두 실용 도구로 연결했다. 주간 계획표는 보편적인 첫 주 목표를 정하지 않고 실제 가능한 요일·시간, 활동 및 회복 메모를 작성하게 했다. 4주 표도 자동 증량 처방이 아니라 계획을 유지·줄임·쉼 중 선택하는 점검 도구로 구성했다.
- WHO의 성인 주간 활동 권고, CDC 대화 검사 및 성인 활동 지침과 AHA 운동 중 경고 신호 안내를 대조했다. 강도 대화 검사는 의료 평가가 아닌 참고법으로 한정했고, 가슴 통증·실신할 듯한 어지럼·비정상적 호흡곤란 등 중단 및 의료 도움 신호를 유지했다. ([WHO 신체활동](https://www.who.int/europe/news-room/fact-sheets/item/physical-activity), [CDC 대화 검사](https://www.cdc.gov/physicalactivity/basics/measuring/index.html), [CDC 성인 활동 지침](https://www.cdc.gov/physical-activity-basics/guidelines/adults.html), [AHA 활동 중 경고 신호](https://www.heart.org/en/health-topics/cardiac-rehab/getting-physically-active/develop-a-physical-activity-plan-for-you))
- 자동 주장 점검은 106편 중 high 0 / review 32 / lower 74 / 본문 직접 링크 누락 0이다. 정적 내보내기 검사는 게시물 106편 전체 필수 마크업, 내부 링크 오류 0, 필수 파일 누락 0으로 통과했고, `npm run build`에서 정적 경로 118개를 생성했다. 휴리스틱 점수는 의료 사실검증 결과나 AdSense 승인 예측이 아니다.
- 배포 확인: 콘텐츠 커밋 `7f850e8`의 GitHub Actions `37113546213`이 Build와 Cloudflare Pages Deploy 모두 성공했다. 계획표·4주 기록표·대표 가이드의 기존 URL 세 곳이 사용자 도메인에서 모두 HTTPS 200을 반환했고, 새 제목과 각 표가 공개 HTML에 반영됐다. [GitHub Actions 실행](https://github.com/yoonezra-star/wellbeinghealth/actions/runs/37113546213).

### 미확인 범위

전체 논문의 의학적 사실 대조는 계속 진행 중이며, 외부 링크는 155개를 자동 확인했지만 HEAD를 차단하거나 시간 초과한 원문은 브라우저 확인이 필요하다. 현행 원 WordPress 미디어와의 대조, Core Web Vitals 실측, 실제 이용자 데이터는 미확인이다. 저장소 복원 기준본과 비교한 로컬 이미지 매핑은 106개 글 모두 완료했다. 113개 모바일 경로 전체 점검은 앞선 빌드에서 수행했고, 이번 변경 글 다섯 편은 공개본에서 320px 레이아웃을 재확인했다. 이 점검들은 모든 글의 정확성이나 AdSense 승인을 뜻하지 않는다.
