---
layout: default
title: Podcast
permalink: /podcast/
---
<section class="hero hero--compact">
  <h1 class="page__title">Podcast Radar IA</h1>
  <p class="hero__lead">As principais notícias da semana em IA numa conversa entre dois apresentadores, Ana e Leo. Duas versões por semana: <strong>resumo</strong> (~20 min) e <strong>completa</strong> (~60 min), publicadas aos domingos a partir da edição semanal. As vozes são sintéticas.</p>
  <p class="podcast__assinar">Assine no seu app de podcast com o feed: <a href="{{ '/podcast.xml' | absolute_url }}">{{ '/podcast.xml' | absolute_url }}</a></p>
</section>
{% assign eps = site.podcast | sort: "date" | reverse | group_by: "semana" %}
{% if eps.size == 0 %}
<p class="empty">Nenhum episódio publicado ainda.</p>
{% else %}
<ul class="list">
{% for g in eps %}
  {% assign first = g.items | first %}
  <li class="list__item episodio">
    <div class="list__link">
      <span class="list__date">{{ first.periodo }}</span>
      <span class="list__title">{{ first.titulo_semana | default: first.title }}</span>
      {% if first.resumo %}<span class="list__excerpt">{{ first.resumo }}</span>{% endif %}
      {% if first.edicao %}<a class="episodio__edicao" href="{{ first.edicao | relative_url }}">Ler a edição escrita →</a>{% endif %}
      {% assign ordenados = g.items | sort: "ordem" %}
      {% for e in ordenados %}
      {% assign a = site.data.audio[e.semana][e.versao] %}
      <div class="episodio__versao">
        <span class="episodio__rotulo">{% if e.versao == "curto" %}Resumo{% else %}Completo{% endif %} · {{ e.duracao }}</span>
        {% if a %}<audio controls preload="none" src="{{ a.url }}"></audio><a class="episodio__baixar" href="{{ a.url }}" download>Baixar MP3</a>{% else %}<span class="episodio__pendente">Áudio em preparação</span>{% endif %}
      </div>
      {% endfor %}
    </div>
  </li>
{% endfor %}
</ul>
{% endif %}
