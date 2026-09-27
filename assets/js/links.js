// Abre em nova janela apenas os links externos (outro domínio).
// Navegação interna, âncoras, e-mail e telefone continuam na mesma aba.
(function () {
  document.querySelectorAll('a[href]').forEach(function (a) {
    if (a.hasAttribute('download')) return;
    if (a.protocol !== 'http:' && a.protocol !== 'https:') return;
    if (a.hostname === window.location.hostname) return;
    a.setAttribute('target', '_blank');
    a.setAttribute('rel', 'noopener noreferrer');
  });
})();
