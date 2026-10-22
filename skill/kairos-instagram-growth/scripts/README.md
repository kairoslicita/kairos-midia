# Scripts

| Script | O que faz | Testado |
|---|---|---|
| `scripts/validate_skill.py` | Confere frontmatter, as 17 referências, templates preenchidos, caminhos internos, rotas dos 10 comandos e referências visuais. `python3 scripts/validate_skill.py` | 22/10/2026 |
| `assets/estudio/filmcar.py` | Renderiza carrossel animado (6 s por slide) e embute a trilha fatiada. | 22/10/2026 (C5, C6) |
| `assets/estudio/filmr2.py` | Renderiza Reels do `reels2.html` (#r2, #r3, #r4) com trilha original. | 22/10/2026 (R2, R3, R4) |
| `assets/estudio/shots.py` | Prova visual: vários quadros de slides num PNG. | 22/10/2026 |
| `assets/estudio/films.py`, `filmr.py` | Render dos lotes anteriores (carrossel sem trilha; Reel v1). | 19/10/2026 |
| `assets/estudio/musica/synth*.py` | Trilhas originais (numpy/scipy) e efeitos. `synth_reels2.py` gera `musica/trilhas/reel_r2/r3/r4.wav`. | 19-22/10/2026 |

Requisitos: Python 3, Playwright com Chromium, ffmpeg, numpy, scipy; fontes Inter, Inter Display e DejaVu Sans Mono instaladas. A cópia em `assets/estudio/` é de referência; a versão em uso fica em `estudio/` no repo `kairoslicita/kairos-midia` (os scripts esperam `slides.html`, `reels2.html` e `musica/trilhas/` ao lado).
