# Lote V3 · 3 Reels (pedido de 28/10/2026)

Status: **aguardando aprovação**. Nada agendado nem publicado.
Arquivos: `midia/lote_v3_reels/`. Cenas: `estudio/reels3.html` (modos r7, r8, r9 e Boost r7b, r8b, r9b). Trilhas: `estudio/musica/synth_reels3.py`. Render: `python3 filmr3.py <modo> <saída.mp4> <duração>`.

## Fatos conferidos antes do render
| Função citada | Fonte | Resultado |
|---|---|---|
| Pesquisa de preços e fabricantes (escolha de marca) | 01 ("a confirmar") → dono, 28/10 20h48 | **Existe hoje** (confirmado pelo dono) |
| Documentos e validades, download em ZIP | 01 ("a confirmar") → dono, 28/10 20h48 | **Existe hoje** (confirmado pelo dono) |
| Gestão da informação | 01: "Meus leilões" (status do dia), itens da compra (Órbita), log de atividades | Real; o Reel mostra só esses três |
| Robô | 01 + memória do dono | Cobre em milissegundos só acima do stop loss, nunca abaixo; roda no servidor; tudo pelo celular; **configurado só no dia da disputa** |

Limite de texto adotado: o Kairos **pesquisa** fabricantes e preços; quem **confere o edital** é o fornecedor. Nenhuma cena diz que o Kairos lê ou valida o edital. Também não se fala em "aviso de vencimento" (só "validade à vista").

---

## V3-R7 · "Sua primeira dispensa ou pregão, com ajuda desde o começo"
- **Arquivo:** `reel_r7_primeira_dispensa_ou_pregao.mp4` · 1080x1920 · 33 s · trilha original `reel_r7.wav` (118 BPM, virada em 3,2 s).
- **Objetivo:** demonstração para iniciante (salvamentos e visitas ao perfil). **Persona:** quem vai disputar a primeira dispensa ou pregão no ComprasNet.
- **Hipótese:** mostrar o caminho completo, com um exemplo concreto por etapa, convence o iniciante de que não vai estar sozinho, sem virar lista de funções.
- **Capa:** quadro 0 (frase + tela de bloqueio com a 1ª notificação).

| Tempo | Cena | Texto na tela | Exemplo prático |
|---|---|---|---|
| 0-3,2 s | Gancho (v3 · P4, escolhido pelo dono em 28/10 22h28) | Como o Kairos pode ajudar você a ganhar sua licitação. | POV da tela de bloqueio às 10:42; notificações caem com vibração: "Kairos · Disputa de hoje carregada · item 1 às 10h" → "Kairos · Robô cobriu: R$ 1.289,90 → R$ 1.289,80" → "Compras.gov.br · Item 1: você está em 1º lugar" (verde). Rodapé "Exemplo ilustrativo." |
| 3,2-9,0 s | 1/4 Marcas | Escolha a marca antes de ofertar. | Tela "Pesquisa de preços": 3 fabricantes com preço de referência. Cartão "Trecho do edital · item 1: impressora laser, frente e verso, mínimo de 30 páginas por minuto" → "Fabricante B atende. É essa que você oferta." |
| 9,0-14,6 s | 2/4 Documentos | Nenhum documento vencido no dia. | Tela "Documentos": FGTS "vence em 3 dias" (coral) vira "renovada"; botão "Baixar tudo em ZIP" |
| 14,6-21,8 s | 3/4 Disputa | No dia da disputa, o robô cobre em milissegundos. | Tela "Disputa hoje · 09:00": digita o stop loss, liga o robô; depois cobre 4 lances com log. Nota: configurado no dia, só acima do stop loss, servidor, celular |
| 21,8-27,0 s | 4/4 Informação | Tudo da disputa em um só lugar. | "Meus leilões": dispensa abre hoje 14h, pregão ganhando, pregão perdendo; itens; log |
| 27,0-33,0 s | CTA | Do preparo à disputa, com você. / Comenta PREGÃO / Teste 7 dias grátis, sem cartão | Kit do Pregão no Direct |

**Legenda:**
```
Sua primeira dispensa ou pregão no Compras.gov.br não precisa começar no escuro.

Antes de ofertar: pesquise fabricantes e preços do item e confira o que o edital pede.
Antes da disputa: seus documentos com a validade à vista, tudo em ZIP.
No dia da disputa: você define o stop loss e o robô cobre os lances em milissegundos, só acima do seu limite. Roda no servidor, e você controla tudo pelo celular.
Durante e depois: disputas, itens e histórico em um só lugar.

Comenta PREGÃO e receba o Kit do Pregão no Direct.
Teste o Kairos grátis por 7 dias, sem cartão. Link na bio.

Valores e datas de exemplo.
#dispensaeletronica #pregaoeletronico #licitacoes #comprasgovbr #licitacao #fornecedor
```
**Variante Boost (`reel_r7b_boost_...mp4`):** mesmas cenas dentro da área 4:5 (y 285-1635); CTA principal "Siga o Kairos", "Comenta PREGÃO" secundário. Observação: 33 s é longo para anúncio frio; se for impulsionar, o R8 é o candidato natural.

---

## V3-R8 · "Perdi por 1 centavo" (compartilhável, com loop)
- **Arquivo:** `reel_r8_perdi_por_1_centavo.mp4` · 18,4 s · trilha `reel_r8.wav` (128 BPM, virada em 9,4 s).
- **Objetivo:** envios e marcações (alcance orgânico). **Persona:** quem já dá lance manual.
- **Hipótese:** a dor de perder por R$ 0,01 + "marque quem ainda dá lance no dedo" gera envios; o loop aumenta o tempo assistido.
- **Capa:** quadro 0.

| Tempo | Cena | Texto na tela | Representação |
|---|---|---|---|
| 0-2,4 s | Gancho | Você perdeu o pregão por R$ 0,01. | Placar encerrado: 1º concorrente R$ 1.279,89 · 2º você R$ 1.279,90 · "Simulação com valores ilustrativos" |
| 2,4-7,0 s | Disputa | O lance no dedo. | Sala de disputa (modo aberto) 00:05 → 00:00; você digita R$ 1.279,88 e não dá tempo: "Lance não registrado: a disputa encerrou." Nota: encerra após 2 min sem lances |
| 7,0-9,4 s | Corte seco | Seu dedo: segundos. / O robô do Kairos: milissegundos. | Tipografia pura, dois carimbos |
| 9,4-14,6 s | Robô | Cobre em milissegundos. Nunca abaixo do seu stop loss. | Robô cobre 3 lances; o 4º lance do concorrente (R$ 1.249,00) fica abaixo do stop loss (R$ 1.250,00) e o log mostra "Não cobriu: abaixo do stop loss". Nota: servidor, celular, configurado no dia |
| 14,6-18,4 s | CTA + loop | Marque quem ainda dá lance no dedo. / Comenta PREGÃO / Teste 7 dias grátis, sem cartão | Nos 0,6 s finais o CTA some e volta o placar do quadro 0 (loop sem emenda) |

**Legenda (curta):**
```
Perder por R$ 0,01 dói. Marque aquele colega de licitação que ainda dá lance no dedo.

O robô do Kairos cobre em milissegundos, só acima do seu stop loss. Roda no servidor e você controla pelo celular.

Comenta PREGÃO e receba o Kit do Pregão no Direct. Teste 7 dias grátis, sem cartão. Link na bio.

Simulação com valores ilustrativos.
#pregaoeletronico #licitacoes #comprasgovbr #robodelances #licitacao
```
**Variante Boost (`reel_r8b_boost_...mp4`):** área 4:5, CTA "Siga o Kairos" + "Comenta PREGÃO". É a melhor candidata a Boost do lote (curta, gancho de dor, loop).

---

## V3-R9 · "3 erros que fazem iniciante perder a primeira dispensa"
- **Arquivo:** `reel_r9_3_erros_primeira_dispensa.mp4` · 29,6 s · trilha `reel_r9.wav` (120 BPM, virada em 16,6 s).
- **Objetivo:** salvamentos e descoberta (dor primeiro). **Persona:** iniciante em dispensa eletrônica.
- **Hipótese:** erros concretos geram identificação; a virada que transforma cada ✗ em ✓ apresenta o produto sem virar lista de funções.
- **Capa:** quadro 0 (gancho + 3 erros numerados).

| Tempo | Cena | Texto na tela | Representação |
|---|---|---|---|
| 0-3,0 s | Gancho (v2, 28/10 21h) | 3 erros que fazem iniciante perder a primeira dispensa. | Fundo coral; três ✗ batem nos erros (0,35 / 0,85 / 1,35 s) com tremida e carimbo sonoro; "Você comete algum deles?" |
| 3,0-7,6 s | Erro 1 | Marca escolhida sem checar o edital. | Proposta: "Edital pede: frente e verso ✓" × "Modelo ofertado: só frente ✗" → carimbo RECUSADA |
| 7,6-12,0 s | Erro 2 | Documento vencido. | Habilitação: CRF FGTS "venceu ontem" → "Pode custar a sua habilitação." |
| 12,0-16,6 s | Erro 3 | Sem tempo para o lance. | Notificações: reunião 10h → perdeu a 1ª posição → novo lance → "Disputa encerrada · você ficou em 2º" (sem cronômetro, para não depender da regra de tempo da dispensa) |
| 16,6-24,4 s | Virada | O Kairos ajuda do preparo à disputa. | 4 cartões ✗ → ✓: Marca (pesquise fabricantes e preços) · Documento (validades à vista, ZIP) · Lance (no dia, o robô cobre em ms, só acima do stop loss) · Informação (disputas, itens e histórico). Nota: tudo pelo celular; robô configurado no dia |
| 24,4-29,6 s | CTA | Sua primeira dispensa, mais preparada. / Comenta PREGÃO / Teste 7 dias grátis, sem cartão | Kit do Pregão no Direct |

**Legenda:**
```
3 erros que fazem iniciante perder a primeira dispensa:

1. Ofertar uma marca sem checar o que o edital pede.
2. Deixar um documento vencer ou atrasar o envio.
3. Não ter tempo para o lance na hora da disputa.

O Kairos ajuda do preparo à disputa: pesquisa de fabricantes e preços, documentos com a validade à vista e, no dia da disputa, o robô que cobre em milissegundos, só acima do seu stop loss. Tudo pelo celular.

Salve para revisar antes da sua próxima dispensa.
Comenta PREGÃO e receba o Kit do Pregão no Direct. Teste 7 dias grátis, sem cartão. Link na bio.

Exemplos ilustrativos.
#dispensaeletronica #licitacoes #comprasgovbr #licitacao #fornecedor #pregaoeletronico
```
**Variante Boost (`reel_r9b_boost_...mp4`):** área 4:5, CTA "Siga o Kairos" + "Comenta PREGÃO".

---

## Para todos
- Publicar sem música do app (a trilha é original), sem localização, capa = quadro 0.
- ManyChat por post (PREGÃO, PREGAO, pregão, pregao) e repost no Story.
- Cota do Metricool em novembro: 3/20 usados; estes 3 Reels cabem (ficariam 6/20).
- Sem preço, sem promessa de vitória ou lucro. Valores, datas e marcas são de exemplo ("Fabricante A/B/C").

## V3-R9 v2 (30/10 23h) · versão vigente
Arquivos: `midia/lote_v3_reels/reel_r9_3_erros_primeira_dispensa_v2.mp4` (31,4 s) e `reel_r9b_boost_3_erros_primeira_dispensa_v2.mp4` (área 4:5, CTA "Siga o Kairos"). Modos `reels3.html#r9v` / `#r9vb`, trilha `reel_r9v.wav`.
- Gancho com os 3 erros trancados (cadeados) + "Você comete algum deles?" (sugestão da avaliadora).
- Cada cena de erro começa com o cartão destravando (3,0 / 8,2 / 13,2 s); contador "ERRO n/3" com pontos de progresso.
- Fim de cada erro: "Já cometeu esse? Comenta 1/2/3". CTA: "Qual você já cometeu? 1 2 3 · Comenta o número" + "Comenta PREGÃO · Kit no Direct" + teste 7 dias.
- Loop: últimos 0,3 s voltam aos cadeados do quadro 0.
- ManyChat: além de PREGÃO/PREGAO/pregão/pregao, opcional criar gatilho para "1", "2", "3" (resposta: "Boa! O Kairos ajuda exatamente nisso. Quer o Kit do Pregão? Comenta PREGÃO.").

Legenda v2:
```
3 erros que fazem iniciante perder a primeira dispensa. Qual deles você já cometeu? Comenta 1, 2 ou 3 👇

1. Ofertar uma marca sem checar o que o edital pede.
2. Deixar um documento vencer ou atrasar o envio.
3. Não ter tempo para o lance na hora da disputa.

O Kairos ajuda do preparo à disputa: pesquisa de fabricantes e preços, documentos com a validade à vista e, no dia da disputa, o robô que cobre em milissegundos, só acima do seu stop loss. Tudo pelo celular.

Comenta PREGÃO e receba o Kit do Pregão no Direct. Teste 7 dias grátis, sem cartão. Link na bio.

Exemplos ilustrativos.
#dispensaeletronica #licitacoes #comprasgovbr #licitacao #fornecedor #pregaoeletronico
```

## V3-R9 v3 (31/10 07h) · versão vigente — ritmo de leitura
`reel_r9_3_erros_primeira_dispensa_v3.mp4` e `reel_r9b_boost_3_erros_primeira_dispensa_v3.mp4` (30,3 s, modos `#r9w`/`#r9wb`, trilha `reel_r9w.wav`). Sem "Comenta n" por cena (só no CTA); virada só com títulos (✓ Marca · ✓ Documento · ✓ Lance · ✓ Informação); cenas de erro mais lentas.
