(function () {
  var VELOCIDADES = [0.75, 1, 1.5, 2];
  var CHAVE = 'radar-ia-velocidade';
  var audios = document.querySelectorAll('audio');
  if (!audios.length) return;

  var atual = 1;
  try {
    var salva = parseFloat(localStorage.getItem(CHAVE));
    if (VELOCIDADES.indexOf(salva) !== -1) atual = salva;
  } catch (e) {}

  var grupos = [];

  function rotulo(v) {
    return String(v).replace('.', ',') + '×';
  }

  function marcar() {
    grupos.forEach(function (g) {
      g.querySelectorAll('button').forEach(function (b) {
        var ativo = parseFloat(b.dataset.v) === atual;
        b.setAttribute('aria-checked', ativo ? 'true' : 'false');
        b.tabIndex = ativo ? 0 : -1;
      });
    });
  }

  function aplicar(v) {
    atual = v;
    try { localStorage.setItem(CHAVE, String(v)); } catch (e) {}
    audios.forEach(function (a) { a.playbackRate = v; });
    marcar();
  }

  audios.forEach(function (audio) {
    audio.playbackRate = atual;
    // Alguns navegadores redefinem a velocidade ao carregar a mídia.
    audio.addEventListener('loadedmetadata', function () { audio.playbackRate = atual; });

    var wrap = document.createElement('div');
    wrap.className = 'player__velocidade';

    var titulo = document.createElement('span');
    titulo.className = 'player__velocidade-titulo';
    titulo.textContent = 'Velocidade';
    wrap.appendChild(titulo);

    var grupo = document.createElement('div');
    grupo.className = 'player__pilulas';
    grupo.setAttribute('role', 'radiogroup');
    grupo.setAttribute('aria-label', 'Velocidade de reprodução');

    VELOCIDADES.forEach(function (v) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'player__pilula';
      b.dataset.v = String(v);
      b.setAttribute('role', 'radio');
      b.textContent = rotulo(v);
      b.addEventListener('click', function () { aplicar(v); });
      grupo.appendChild(b);
    });

    // Setas do teclado movem a seleção, como em qualquer grupo de opções.
    grupo.addEventListener('keydown', function (ev) {
      var i = VELOCIDADES.indexOf(atual);
      if (ev.key === 'ArrowRight' || ev.key === 'ArrowUp') i = Math.min(i + 1, VELOCIDADES.length - 1);
      else if (ev.key === 'ArrowLeft' || ev.key === 'ArrowDown') i = Math.max(i - 1, 0);
      else return;
      ev.preventDefault();
      aplicar(VELOCIDADES[i]);
      grupo.querySelector('[data-v="' + VELOCIDADES[i] + '"]').focus();
    });

    wrap.appendChild(grupo);
    grupos.push(grupo);
    audio.insertAdjacentElement('afterend', wrap);
  });

  marcar();
})();
