---
layout: default
title: Podcast
permalink: /podcast/
---
<section class="hero hero--compact">
  <h1 class="page__title">Podcast Radar IA</h1>
  <p class="hero__lead">As notícias de IA numa conversa entre dois apresentadores, Ana e Leo. Um <strong>episódio diário</strong> de ~20 minutos com a edição do dia e, aos domingos, um <strong>episódio semanal</strong> de ~60 minutos com o balanço da semana. As vozes são sintéticas.</p>
  <p class="podcast__assinar">Assine no seu app de podcast com o feed: <a href="{{ '/podcast.xml' | absolute_url }}">{{ '/podcast.xml' | absolute_url }}</a></p>
</section>
{% assign eps = site.podcast | sort: "date" | reverse %}
{% if eps.size == 0 %}
<p class="empty">Nenhum episódio publicado ainda.</p>
{% else %}
<ul class="list">
{% for e in eps %}
  {% assign id = e.episodio | default: e.semana | append: "-" | append: e.versao %}
  {% if e.episodio %}{% assign id = e.episodio %}{% endif %}
  {% assign a = site.data.audio[id] %}
  <li class="list__item episodio">
    <div class="list__link">
      <span class="list__date">{% if e.tipo == "semanal" %}<span class="badge badge--semanal">Semanal</span>{% elsif e.tipo == "diario" %}<span class="badge badge--diario">Diário</span>{% endif %} {{ e.periodo | default: e.date | date: "%d/%m/%Y" }} · {{ e.duracao }}</span>
      <span class="list__title">{{ e.title }}</span>
      {% if e.resumo %}<span class="list__excerpt">{{ e.resumo }}</span>{% endif %}
      <div class="episodio__versao">
        {% if a %}<audio controls preload="none" src="{{ a.url }}"></audio><span class="episodio__links"><a class="episodio__baixar" href="{{ a.url }}" download>Baixar MP3</a>{% if e.edicao %} · <a href="{{ e.edicao | relative_url }}">Ler a edição escrita</a>{% endif %}</span>{% else %}<span class="episodio__pendente">Áudio em preparação — costuma levar até uma hora após a edição.</span>{% if e.edicao %} <a href="{{ e.edicao | relative_url }}">Ler a edição escrita</a>{% endif %}{% endif %}
      </div>
    </div>
  </li>
{% endfor %}
</ul>
{% endif %}
