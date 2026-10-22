# 05 · Carrosséis premium (animados)

## Estrutura padrão (7-9 slides de 6 s)
1. **Capa escura** com manchete de 3 linhas e cartão animado que prova a tensão (ver `02`).
2. **Problema** visual (o que dá errado na disputa).
3-6. **Passos / erros / perguntas**: um por slide, com painel `sys`, cartão `fix` e rótulo "n de N".
7. **Kairos na prática** (opcional): como o robô resolve, sem exagero.
último. **CTA** "Comenta PREGÃO" (ou variação aprovada) + teste grátis em segundo plano.

## Tipos de slide prontos em `estudio/slides.html`
`ecapa`/`erro` (lista de erros), `pmcapa`/`passo`/`pconta`/`perrado` (calculadora), `mcapa`/`medital`/`maberto`/`mfechado`/`mlance`/`mdica` (linha do tempo), `limite`, `monitor`, `orbita`, `multi`, `seguranca` (sistema), `c5capa`/`c5abas`/`c5itens` (vários pregões), `c6capa`/`faq` (perguntas e respostas), `cta`, `pcta`, `c6cta`. Variar um slide existente com `.replace()` em vez de copiar.

## Render
```
cd estudio
python3 shots.py prova.png "s=c6capa&n=1/7@2" "s=faq&q=0&n=2/7@4.5"   # prova visual
python3 filmcar.py musica/trilhas/carrossel_B_minimal_tech.wav ../midia/<pasta> "c6_01_capa|s=c6capa&n=1/7" ...
```
A trilha é fatiada em blocos de 6 s na ordem dos slides, então deslizar entre slides parece contínuo.

## Postagem (manual ou Metricool)
- Instagram: + > Publicação > selecionar vários **na ordem dos números**. Recusar "transformar em Reel". Não adicionar música.
- Metricool: tipo POST com a lista de URLs raw na ordem.

## Legenda
Gancho na 1ª linha (repete a capa com outra palavra) → 1-2 linhas de valor → "Salve para…" → CTA → nota de veracidade quando houver regra ou valores → 5-8 hashtags de nicho (#licitacoes #pregaoeletronico #comprasgovbr #licitacao #comprasnet #fornecedor #mei #pequenasempresas).

## Conteúdo regulatório
Carrossel que ensina regra (prazos, modos de disputa, documentos) precisa de fonte normativa conferida na data (Lei 14.133/2021, IN SEGES/ME 73/2022 etc.) e a frase "Confira sempre o edital".
