(function () {
  var VELOCIDADES = [0.75, 1, 1.25, 1.5, 1.75, 2];
  var CHAVE = 'radar-ia-velocidade';
  var audios = document.querySelectorAll('audio');
  if (!audios.length) return;

  var atual = 1;
  try {
    var salva = parseFloat(localStorage.getItem(CHAVE));
    if (VELOCIDADES.indexOf(salva) !== -1) atual = salva;
  } catch (e) {}

  var selects = [];

  function aplicar(v, origem) {
    atual = v;
    try { localStorage.setItem(CHAVE, String(v)); } catch (e) {}
    audios.forEach(function (a) { a.playbackRate = v; });
    selects.forEach(function (s) { if (s !== origem) s.value = String(v); });
  }

  audios.forEach(function (audio) {
    audio.playbackRate = atual;
    // Alguns navegadores redefinem a velocidade ao carregar a mídia.
    audio.addEventListener('loadedmetadata', function () { audio.playbackRate = atual; });

    var label = document.createElement('label');
    label.className = 'player__velocidade';
    label.appendChild(document.createTextNode('Velocidade '));
    var select = document.createElement('select');
    select.setAttribute('aria-label', 'Velocidade de reprodução');
    VELOCIDADES.forEach(function (v) {
      var o = document.createElement('option');
      o.value = String(v);
      o.textContent = v + '×';
      if (v === atual) o.selected = true;
      select.appendChild(o);
    });
    select.addEventListener('change', function () { aplicar(parseFloat(select.value), select); });
    label.appendChild(select);
    selects.push(select);
    audio.insertAdjacentElement('afterend', label);
  });
})();
