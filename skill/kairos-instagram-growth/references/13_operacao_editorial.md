# 13 · Operação editorial

## Estados de cada tarefa ou peça
planejado → em criação → (aguardando materiais) → em revisão → aguardando aprovação → aprovado → agendado → publicado → em análise → concluído. Exceção: bloqueado (dizer por quê e o que destrava). Nunca pular para "publicado" sem confirmação (Metricool retornou publicado ou o dono confirmou).

## Semana-tipo
| Quando | Quem | O quê |
|---|---|---|
| Qui 08h58 | Claude (tarefa agendada) | Pauta e produção da semana seguinte → envia peças + LEIA-ME → "Aprova a semana?" |
| Após "aprovado" | Claude | Agenda no Metricool (se houver cota) ou prepara pacote manual; cria lembretes das 10h05 |
| Dia do post 10h | Metricool ou dono | Publicação |
| Dia do post 10h05 | Dono (lembrete) | ManyChat da peça + repost no Story + responder comentários |
| Seg 08h54 | Claude (tarefa agendada) | Relatório semanal + proposta de Boost |
| Diário (20-30 min) | Dono | Comentários úteis em perfis do nicho, respostas, Stories |

## Cota do Metricool (plano grátis)
20 publicações por mês, zera no dia 1º. Antes de agendar, contar as já publicadas e agendadas no mês (`getScheduledPosts` + posts publicados). Stories não vão para o Metricool. Sem cota: entregar arquivos + legendas para publicação manual e dizer isso claramente.

## Agendamento no Metricool
- Mídias com URL raw: `https://raw.githubusercontent.com/kairoslicita/kairos-midia/main/midia/<pasta>/<arquivo>.mp4`.
- Carrossel: tipo POST com a lista de vídeos na ordem. Reel: tipo REEL com `videoCoverMilliseconds` do quadro de capa. `autoPublish: true`.
- Ao atualizar um post agendado, o id muda (o uuid não).

## Arquivos e nomes
- `midia/AAAA-MM-DD_<formato>_<tema>/` com `c<n>_<nn>_<slide>.mp4` ou `reel_<tema>.mp4`; `midia/LEIA-ME_semana_<dd>a<dd>-<mm>.txt` com legenda, capa, ManyChat e ordem.
- Lotes ainda sem data: `midia/lote_v2_*`.
- Nunca sobrescrever arquivo publicado; versão nova ganha sufixo `_v2`.

## Aprovações
Registro em `assets/templates/aprovacoes_campanhas.md` (cópia viva em `operacao/aprovacoes.md`): o que foi aprovado, por quem, quando e com qual escopo. "Aprovado" vale só para o escopo descrito.
