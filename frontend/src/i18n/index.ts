import i18n from "i18next";
import Backend from "i18next-http-backend";
import { initReactI18next } from "react-i18next";

export const AvailableLanguages = [
  { label: "English", value: "en" },
  { label: "日本語", value: "ja" },
  { label: "简体中文", value: "zh-CN" },
  { label: "繁體中文", value: "zh-TW" },
  { label: "한국어", value: "ko-KR" },
  { label: "Norsk", value: "no" },
  { label: "Arabic", value: "ar" },
  { label: "Deutsch", value: "de" },
  { label: "Français", value: "fr" },
  { label: "Italiano", value: "it" },
  { label: "Português", value: "pt" },
  { label: "Español", value: "es" },
  { label: "Türkçe", value: "tr" },
];

i18n
  .use(Backend)
  .use(initReactI18next)
  .init({
    lng: "ja",
    fallbackLng: "en",
    debug: import.meta.env.NODE_ENV === "development",
    load: "languageOnly",
  });

export default i18n;
