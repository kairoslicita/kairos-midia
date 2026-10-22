# 02 · KAIROS · PADRÃO VISUAL APROVADO

Este é o piso de qualidade. Toda peça nova é comparada com as referências abaixo (miniaturas em `assets/referencias/`, arquivos completos em `midia/` no repo). **Não recomeçar a direção de arte.**

## Histórico de aprovação (o que o dono disse)
| Data | Peça | Retorno | O que isso fixou |
|---|---|---|---|
| 18-19/10 | 1ª versão animada (claro + verde e coral) | "Houve uma melhora absurda" | Direção: fundo creme, verde-floresta, coral e lima; sistema remodelado; movimento |
| 19/10 | Capas A (alerta escuro) e B (órbita) | "Gostei muito da capa A" | **Capa = fundo escuro + manchete enorme em 3 linhas + cartão de alerta animado** |
| 19/10 | Carrossel 1 "Como o robô decide", Reel "Reunião às 9h", Carrossel 2 "7 erros" | "Ficou excelente!" | Slides internos claros com painel `sys` escuro, cartão "como evitar", fios tracejados, telas do celular |
| 19/10 | Ajuste de copy | Pediu "milissegundos", stop loss, servidor | Precisão do produto faz parte do padrão |
| 22/10 | Semana 27-30/10 (C3 preço mínimo, Reel desligou, C4 modos) | Aprovado | Calculadora animada, comparativo lado a lado, linha do tempo |
| 22/10 | Prompt mestre V2 | "Remodelagem do sistema ficou muito boa e está aprovada" | Interfaces reimaginadas são desejadas, com fidelidade à lógica |

Alerta do dono: "não sair muito do layout do sistema, para não descaracterizar".

## Tokens
- **Cores:** creme `#f2ede3` (fundo claro) · creme 2 `#e9e2d4` · cartão `#fbf8f2` · linha `#d8cfbf` · verde-floresta `#0b2219` (fundo escuro, texto) · floresta 2 `#10291f` / `#123024` (painéis) · borda escura `#24463a` · coral `#ff5f3c` (destaque, perda, CTA) · coral texto `#ff8a6d` / `#d1401f` · lima `#b9ee4f` (ganho, ok, número positivo) · lima cartão `#c9f26c` · âmbar `#ffcf73` (atenção) · texto secundário `#56645b` (claro) / `#8fa699` (escuro). Legenda cinética de Reel: amarelo `#ffe94d`.
- **Tipografia:** manchetes Inter Display 900, entrelinha 0,9, tracking −0,045em (capa 112-120px; título interno 88-104px; Reel 100-150px). Texto Inter 25-40px. Números, rótulos e logs em DejaVu Sans Mono (rótulos em CAIXA ALTA com tracking +0,06-0,08em).
- **Logo:** "Kairos" Inter Display 800 com ponto coral ("Kairos**.**"). Topo esquerdo; contador "n/7" em pílula mono no topo direito.
- **Ícones:** traço 2,2px, cantos arredondados, conjunto próprio (box, truck, pct, up, srv, live, pause, lock, key, shield, list, cal).

## Componentes aprovados (em `estudio/slides.html` e `estudio/reels2.html`)
- **Capa de carrossel (`bgd`)**: fundo floresta com brilho coral; manchete de 3 linhas (2 creme + 1 coral); cartão grande coral (perda) ou lima (ganho) com animação em loop (contagem, cronômetro, barra de progresso, carimbo); pílula creme "Arraste…" com chevrons animados.
- **Slide interno (`bg`)**: fundo creme; rótulo mono coral ("erro 4 de 7", "passo 2 de 4"); título de 2 linhas (floresta + coral); painel `sys` escuro com a representação do sistema; cartão `fix` creme com selo lima ("como evitar", "na prática", "em detalhe"); número-fantasma gigante `#e6dece` no canto; nota "Telas ilustrativas, com valores de exemplo."
- **Celular**: 430x880, raio 66, ilha dinâmica, barra 5G, cabeçalho "Robô de lances" com "● ao vivo" piscando, painéis, linhas de log mono com pílulas (perdendo coral, ganhando lima, abre hoje âmbar, ok cinza).
- **Fios tracejados coral** animados ligando cartões ao celular, com pontos viajando.
- **CTA "Comenta PREGÃO"**: pílula coral pulsando + caixa de comentário digitando "PREGÃO" + bolha de Direct com o PDF do Kit.
- **Reel**: fundo floresta com brilho radial; cortes secos com "punch" de zoom (1,05 → 1); manchetes enormes; cartões coral (perdendo) e lima (ganhando); toast de notificação "Kairos · item 1"; etiqueta lima "PREGÃO · COMPRAS.GOV.BR" no anúncio; legenda palavra a palavra opcional.
- **Áudio**: trilha original sintetizada (lofi/tech/eletrônica 84-124 BPM) com virada sincronizada ao clímax, efeitos (tique, whoosh, carimbo, moeda). Carrossel: uma trilha contínua fatiada em 6 s por slide.

## Formatos
- Carrossel: 1080x1350, 7-9 slides de vídeo de 6 s em loop, trilha embutida. Capa sempre escura; internos claros; CTA no último.
- Reel: 1080x1920, 15-22 s, 30 fps, H.264 CRF 16-17, AAC 192k. Área segura: conteúdo entre y=220 e y=1540; nada importante nos 140 px da direita entre y=1100 e 1700 (botões do app).

## Pode mudar (melhoria incremental bem-vinda)
Novas cenas e visualizações do sistema; ângulos, profundidade e luz nos mockups; ritmo e duração; legendas cinéticas; variações de CTA; capas com outro tipo de animação dentro da mesma estrutura.

## Não pode (exige autorização)
Trocar paleta ou tipografia; fotos de banco ou rostos; templates genéricos; slides só de texto corrido; capas claras; inventar funções; prints crus no lugar da remodelagem (exceto em tutorial real); música de terceiros sem licença comercial.

## Lições de regressão (já aconteceram)
- Quadro 0 vazio (fade do preto, uma palavra só): **o primeiro quadro precisa ter o gancho completo**.
- Texto sobreposto a cartões e títulos quebrando em 3 linhas: conferir quadros-chave antes de entregar.
- Afirmações erradas ("segura quando está na frente", "lances em segundos", "login caiu", "só acompanha pelo celular"): checar contra `01_contexto_kairos.md`.
