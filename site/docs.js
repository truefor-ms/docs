(() => {
  'use strict';
  document.documentElement.classList.add('enhanced');
  document.querySelectorAll('[data-print]').forEach(b => b.addEventListener('click', () => window.print()));
  const menu = document.querySelector('.site-navigation');
  const toc = document.querySelector('.page-toc');
  const narrow = window.matchMedia('(max-width: 760px)');
  const compact = window.matchMedia('(max-width: 1200px)');
  const adapt = () => { if(menu) menu.open = !narrow.matches; if(toc) toc.open = !compact.matches; };
  adapt(); narrow.addEventListener('change', adapt); compact.addEventListener('change', adapt);
  const input = document.querySelector('#nav-search');
  const pages = [...document.querySelectorAll('[data-nav-page]')];
  const records = document.querySelector('.source-records');
  if(records && records.querySelector('[aria-current="page"]')) records.open = true;
  input?.addEventListener('input', () => {
    const terms = input.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    pages.forEach(a => { a.hidden = !terms.every(t => a.dataset.search.includes(t)); });
    document.querySelectorAll('[data-nav-group]').forEach(g => { g.hidden = ![...g.querySelectorAll('[data-nav-page]')].some(a => !a.hidden); });
    if(records) { records.hidden = ![...records.querySelectorAll('[data-nav-page]')].some(a => !a.hidden); records.open = terms.length > 0 || !!records.querySelector('[aria-current="page"]'); }
    document.querySelector('#nav-empty').hidden = pages.some(a => !a.hidden);
  });
  const anchors = [...document.querySelectorAll('.page-toc a')];
  if('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      const current = entries.find(e => e.isIntersecting);
      if(!current) return;
      anchors.forEach(a => { if(a.hash === '#'+current.target.id) a.setAttribute('aria-current','location'); else a.removeAttribute('aria-current'); });
    }, {rootMargin:'-90px 0px -55% 0px'});
    document.querySelectorAll('.article h2[id]').forEach(h => observer.observe(h));
  }
})();
