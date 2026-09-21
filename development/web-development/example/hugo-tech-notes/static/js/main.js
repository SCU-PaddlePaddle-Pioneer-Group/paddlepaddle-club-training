(() => {
  const root = document.documentElement;
  const button = document.querySelector('.theme-toggle');
  if (!button) return;

  const savedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const initialTheme = savedTheme || (prefersDark ? 'dark' : 'light');

  root.dataset.theme = initialTheme;
  button.setAttribute('aria-pressed', String(initialTheme === 'dark'));

  button.addEventListener('click', () => {
    const nextTheme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = nextTheme;
    localStorage.setItem('theme', nextTheme);
    button.setAttribute('aria-pressed', String(nextTheme === 'dark'));
  });
})();
