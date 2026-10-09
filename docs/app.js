'use strict';
(() => {
  const en = document.documentElement.lang === 'en';
  const menuButton = document.getElementById('menu-toggle');
  const menu = document.getElementById('mobile-nav');
  const closeMenu = () => {
    menu.hidden = true;
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', en ? 'Open menu' : 'Abrir menú');
  };
  menuButton.addEventListener('click', () => {
    const expanded = menuButton.getAttribute('aria-expanded') === 'true';
    menu.hidden = expanded;
    menuButton.setAttribute('aria-expanded', String(!expanded));
    menuButton.setAttribute('aria-label', expanded ? (en ? 'Open menu' : 'Abrir menú') : (en ? 'Close menu' : 'Cerrar menú'));
  });
  menu.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && !menu.hidden) { closeMenu(); menuButton.focus(); }
  });
  window.matchMedia('(min-width: 851px)').addEventListener('change', event => { if (event.matches) closeMenu(); });
  const form = document.getElementById('inquiry-form');
  const panel = document.getElementById('message-panel');
  const status = document.getElementById('status');
  const vehicle = document.getElementById('vehicle');
  let preparedMessage = '';
  const whatsappNumber = window.JBCARS_CONFIG?.whatsappNumber || '';
  const whatsappReady = /^\d{8,15}$/.test(whatsappNumber);
  if (whatsappReady) document.querySelectorAll('[data-whatsapp]').forEach(button => {
    button.disabled = false;
    button.querySelector('[data-whatsapp-pending]')?.remove();
    button.addEventListener('click', event => {
      event.preventDefault();
      const message = button.dataset.whatsapp === 'inquiry' ? preparedMessage : (en ? 'Hi Jesús! I would like to discuss my next car in Miami.' : '¡Hola, Jesús! Me gustaría hablar sobre mi próximo carro en Miami.');
      window.open(`https://wa.me/${whatsappNumber}?text=${encodeURIComponent(message)}`, '_blank', 'noopener,noreferrer');
    });
  });
  document.querySelectorAll('[data-vehicle]').forEach(button => button.addEventListener('click', () => {
    vehicle.value = button.dataset.vehicle;
    panel.hidden = true;
    form.hidden = false;
    document.getElementById('contacto').scrollIntoView({behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth'});
    status.textContent = en ? `${vehicle.selectedOptions[0].text} selected. Complete your inquiry.` : `${vehicle.selectedOptions[0].text} seleccionado. Completa tu consulta.`;
    document.getElementById('name').focus({preventScroll:true});
  }));
  form.addEventListener('submit', event => {
    event.preventDefault();
    const name = document.getElementById('name');
    name.setCustomValidity(name.value.trim() ? '' : (en ? 'Please enter your name.' : 'Escribe tu nombre.'));
    if (!form.reportValidity()) return;
    const selectedText = id => document.getElementById(id).selectedOptions[0].text;
    const lines = en ? [
      `Hi Jesús! I'm ${name.value.trim()}. I'd like to discuss my next car.`,
      '', `Vehicle: ${selectedText('vehicle')}`, `Approximate budget: ${selectedText('budget')}`, `Timing: ${selectedText('timing')}`
    ] : [
      `¡Hola, Jesús! Soy ${name.value.trim()}. Me gustaría hablar de mi próximo carro.`,
      '', `Tipo de carro: ${selectedText('vehicle')}`, `Presupuesto aproximado: ${selectedText('budget')}`, `Plazo: ${selectedText('timing')}`
    ];
    const extra = document.getElementById('message').value.trim();
    if (extra) lines.push('', extra);
    lines.push('', en ? 'Inquiry prepared on the JB Cars Miami website.' : 'Consulta preparada en la web de JB Cars Miami.');
    const message = lines.join('\n');
    preparedMessage = message;
    document.getElementById('message-preview').textContent = message;
    if (whatsappReady) document.getElementById('send-whatsapp').href = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(message)}`;
    document.getElementById('send-email').href = `mailto:jbcarsadvisor@gmail.com?subject=${encodeURIComponent(en ? 'My next car · JB Cars Miami' : 'Mi próximo carro · JB Cars Miami')}&body=${encodeURIComponent(message)}`;
    form.hidden = true;
    panel.hidden = false;
    const heading = panel.querySelector('h3');
    heading.tabIndex = -1;
    heading.focus({preventScroll:true});
    status.textContent = en ? 'Your inquiry is prepared, but has not been sent.' : 'Tu consulta está preparada, pero todavía no se ha enviado.';
  });
  document.getElementById('name').addEventListener('input', event => event.target.setCustomValidity(''));
  document.getElementById('edit-inquiry').addEventListener('click', () => {
    form.hidden = false;
    panel.hidden = true;
    document.getElementById('name').focus({preventScroll:true});
  });
  document.getElementById('year').textContent = String(new Date().getFullYear());
})();
