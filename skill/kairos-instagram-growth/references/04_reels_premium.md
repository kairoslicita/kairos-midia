# 04 · Reels premium

## Três tipos de Reel
| Tipo | Duração | Objetivo | Estrutura |
|---|---|---|---|
| Descoberta (educação/dor) | 15-20 s | Alcance de não seguidores, salvamentos | Gancho de dor → explicação visual → regra/ação → CTA leve |
| Demonstração | 18-25 s | Visitas ao perfil, confiança | Situação real → tela do Kairos agindo → resultado → CTA |
| Anúncio (variante Boost) | 12-16 s | Visitas/comentários pagos | **Gancho completo no quadro 0** + etiqueta do nicho → conflito → robô resolve → oferta do Kit |

Não abrir todo Reel como propaganda do robô. Pelo menos metade começa por um problema do licitante.

## Banco de ganchos (testados ou prontos para teste)
- "Perdeu o item por R$ 0,10?" (anúncio, lote V2)
- "Esse lance parece bom… mas dá prejuízo." (lote V2)
- "POV: você esqueceu do pregão." (lote V2)
- "Reunião às 9h. Pregão também." (publicado 21/10)
- "Desligou o computador? O robô, não." (28/10)
- "Três pregões no mesmo horário. Como você acompanha tudo?"
- "Até onde vale baixar o preço?"
- "O pregoeiro chamou no chat. Você viu?"
- "Aberto ou aberto e fechado? Muda a hora do seu lance."

## Entregáveis por Reel
Objetivo e persona · hipótese · gancho · roteiro · storyboard com tempos · direção de arte e telas · texto na tela e legendas sincronizadas · trilha original · animações e cortes · CTA · capa (quadro indicado) · legenda do post e palavras-chave · critérios de validação · variante Boost se aplicável. Usar `assets/templates/briefing_audiovisual.md`.

## Narração
Padrão: **sem voz**. O dono não pode usar a própria voz e não há locução sintética natural e estável disponível. A narrativa vai no texto na tela (manchetes por cena e, quando útil, legenda palavra a palavra). Se um dia houver voz licenciada, ela entra só com aprovação, e a mesma voz deve ser usada em toda a série.

## Pipeline (repo `estudio/`)
1. Cenas em `reels2.html` (modos `#r2`, `#r3`, `#r4`). Para um Reel novo, criar um modo novo reaproveitando `bg`, `tag`, `head`, `toast`, celular e cartões.
2. Prova visual: renderizar quadros-chave (0 s, meio, CTA) e conferir sobreposição, área segura e quadro 0.
3. Trilha: `musica/synth_reels2.py` → função `build(nome, duração, cortes, drop, bpm, ticks, stamps, coins, alerts)`. Alinhar o drop ao clímax visual.
4. Render: `python3 filmr2.py <modo> ../midia/<pasta>/<arquivo>.mp4 <duração>`.
5. Conferir: duração, volume (−18 a −22 dB médio), folha de contato.

## Postagem
- Arquivo já tem trilha e efeitos: **não adicionar música do app**.
- Capa: escolher o quadro indicado no LEIA-ME.
- Não marcar localização. Selo de IA: desligado (não é imagem realista gerada por IA).
- Depois de publicar: dono cria a automação do ManyChat para o post e compartilha no Story.

## Validação mínima
Tempo de leitura: cada texto principal fica na tela pelo menos (palavras ÷ 3) + 1 s; nunca manchete e detalhe entrando juntos; no máximo 2 camadas de texto por cena.
Quadro 0 com gancho completo · nada na área dos botões · texto lido em 1 s por cena · números coerentes entre cenas · fato do produto conferido · nota "valores de exemplo" quando houver valores · CTA único e claro.
