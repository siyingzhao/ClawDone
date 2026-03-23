const translations = {
  'zh-CN': {
    githubButton: 'GitHub',
    eyebrow: 'Phone · SSH · tmux · Agents',
    heroTitle: '更轻的远程控制台',
    heroText: '给 coding agents 派活。',
    primaryCta: 'GitHub',
    secondaryCta: '文档',
    pointOne: 'SSH',
    pointTwo: 'tmux',
    pointThree: 'Mobile'
  },
  en: {
    githubButton: 'GitHub',
    eyebrow: 'Phone · SSH · tmux · Agents',
    heroTitle: 'A lighter remote console',
    heroText: 'Dispatch work to coding agents.',
    primaryCta: 'GitHub',
    secondaryCta: 'Docs',
    pointOne: 'SSH',
    pointTwo: 'tmux',
    pointThree: 'Mobile'
  }
};

const languageButtons = document.querySelectorAll('[data-lang]');
const translatableNodes = document.querySelectorAll('[data-i18n]');

function applyLanguage(language) {
  const resolvedLanguage = translations[language] ? language : 'zh-CN';
  const dictionary = translations[resolvedLanguage];

  document.documentElement.lang = resolvedLanguage;
  document.title = resolvedLanguage === 'en' ? 'ClawDone' : 'ClawDone';

  translatableNodes.forEach((node) => {
    const key = node.dataset.i18n;
    if (dictionary[key]) node.textContent = dictionary[key];
  });

  languageButtons.forEach((button) => {
    button.classList.toggle('is-active', button.dataset.lang === resolvedLanguage);
  });

  localStorage.setItem('clawdone-language', resolvedLanguage);
}

const storedLanguage = localStorage.getItem('clawdone-language');
const browserLanguage = navigator.language.toLowerCase().startsWith('zh') ? 'zh-CN' : 'en';
applyLanguage(storedLanguage || browserLanguage);

languageButtons.forEach((button) => {
  button.addEventListener('click', () => applyLanguage(button.dataset.lang));
});
