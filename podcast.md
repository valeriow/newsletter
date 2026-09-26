---
layout: default
title: Podcast
permalink: /podcast/
---
<section class="hero hero--compact">
  <h1 class="page__title">Podcast Radar IA</h1>
  <p class="hero__lead">Roteiros semanais com as principais notícias da semana, em formato de conversa entre dois apresentadores: uma versão curta (~20 min) e uma completa (~60 min). Gerados aos domingos a partir das edições diárias.</p>
</section>
{% assign eps = site.podcast | sort: "date" | reverse | group_by: "semana" %}
{% if eps.size == 0 %}
<p class="empty">Nenhum roteiro publicado ainda.</p>
{% else %}
<ul class="list">
{% for g in eps %}
  {% assign first = g.items | first %}
  <li class="list__item episodio">
    <div class="list__link">
      <span class="list__date">Semana {{ g.name }} · {{ first.periodo }}</span>
      <span class="list__title">{{ first.titulo_semana | default: first.title }}</span>
      {% if first.resumo %}<span class="list__excerpt">{{ first.resumo }}</span>{% endif %}
      <span class="episodio__versoes">
      {% assign ordenados = g.items | sort: "ordem" %}
      {% for e in ordenados %}<a class="episodio__link" href="{{ e.url | relative_url }}">{{ e.versao | capitalize }} · {{ e.duracao }}</a>{% endfor %}
      </span>
    </div>
  </li>
{% endfor %}
</ul>
{% endif %}
