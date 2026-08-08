export const SITE_URL = "https://wellbeinghealth.co.kr";
export const SITE_NAME = "Wellbeing Health";
export const SITE_DESCRIPTION =
  "운동, 다이어트, 건강식단, 생활습관, 멘탈케어 정보를 근거와 함께 쉽게 전달하는 건강 정보 매거진입니다.";
export const EDITOR_NAME = "Wellbeing Health 편집팀";
export const CONTACT_EMAIL = "replyleaders@naver.com";
export const ADSENSE_PUBLISHER_ID = "ca-pub-1441018945572157";

export function absoluteUrl(path = "/") {
  return new URL(path, SITE_URL).toString();
}
