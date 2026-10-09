'use strict';
(() => {
  const button = document.getElementById('menu-toggle');
  const menu = document.getElementById('mobile-nav');
  const close = () => {
    menu.hidden = true;
    button.setAttribute('aria-expanded', 'false');
    button.setAttribute('aria-label', 'Abrir menú');
  };
  button.addEventListener('click', () => {
    const open = button.getAttribute('aria-expanded') !== 'true';
    menu.hidden = !open;
    button.setAttribute('aria-expanded', String(open));
    button.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
  });
  menu.querySelectorAll('a').forEach(link => link.addEventListener('click', close));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && !menu.hidden) { close(); button.focus(); }
  });
  matchMedia('(min-width: 851px)').addEventListener('change', event => { if (event.matches) close(); });
  document.getElementById('year').textContent = String(new Date().getFullYear());
})();
