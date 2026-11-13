# Radar IA

**Site:** https://valeriow.github.io/newsletter/

Newsletter de monitoramento diário de IA — IA agêntica, ferramentas e modelos open source, IA no setor público e IA aplicada em empresas. Voltada a estudantes e profissionais da área.

Site estático em Jekyll, hospedado no GitHub Pages.

- Cada edição é um arquivo em `_posts/AAAA-MM-DD-monitoramento-ia-HHh.md` (data e hora da edição, horário de Brasília).
- A publicação é feita automaticamente por uma tarefa agendada que faz commit e push neste repositório; o GitHub Pages reconstrói o site a cada push em `main`.
- Feed: https://valeriow.github.io/newsletter/feed.xml

## Podcast

- Roteiros em `_podcast/`; o áudio é gerado por `scripts/gerar_audio.py` (workflow `podcast-audio.yml`).
- Feed do podcast: https://valeriow.github.io/newsletter/podcast.xml
- Plataformas (configuradas em `podcast_plataformas` no `_config.yml`, usadas no site e no feed): [Spotify](https://open.spotify.com/show/12y2nAQdWSAWvWzJOHJIwW) · [YouTube Music](https://music.youtube.com/playlist?list=PLI7C95MfoASA) · [YouTube](https://www.youtube.com/playlist?list=PLI7C95MfoASA)
- O `gerar_audio.py` insere no encerramento uma chamada da Ana e do Leo para procurar o Radar IA no Spotify, YouTube e YouTube Music (pulada se o roteiro já citar o Spotify; desative com `--sem-chamada`). Só afeta áudios gerados a partir de agora.

Contato: valeriow@gmail.com
