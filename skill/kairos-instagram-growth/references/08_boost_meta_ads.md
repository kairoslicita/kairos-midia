# 08 · Boost e Meta Ads com R$ 150/mês

Claude cuida de estratégia, escolha do criativo, plano, acompanhamento e otimização. **Ativar, pagar, ampliar verba ou mudar campanha exige "aprovado" explícito do dono**, e quem clica é ele.

## Custos reais (conferidos em 22/10/2026; reconfirmar a cada mês)
- **Impostos no Brasil:** desde jan/2026 a Meta repassa PIS/Cofins (9,25%) + ISS (2,9%) = **~12,15% sobre o valor veiculado** (fonte: Tecnoblog, comunicado oficial da Meta). Teto de R$ 150 de custo total ≈ **R$ 133,75 de mídia**.
- **Taxa da Apple:** impulsionar **pelo app do Instagram/Facebook no iPhone** soma a comissão de **30% da Apple**. Fazer pelo **navegador (Safari)** evita a taxa (orientação da própria Meta; fontes: Tecnoblog 19/02/2024, Hardware.com.br). O dono usa iPhone, então: **sempre pelo Safari**, em instagram.com, facebook.com ou business.facebook.com (Meta Business Suite).
- **Mínimo diário:** referência de R$ 3/dia para engajamento/tráfego/alcance (Trafius, 2026). A Meta valida o mínimo na ativação.

## Onde criar
| Via | Quando |
|---|---|
| **Impulsionar pelo navegador** (Meta Business Suite ou instagram.com no Safari) | Padrão. Simples, usa o post original (comentários e ManyChat continuam funcionando no mesmo post). |
| **Gerenciador de Anúncios** (adsmanager no navegador) | Só quando precisar de controle extra: excluir seguidores atuais, objetivo de leads/mensagens com formulário, testar 2 criativos no mesmo conjunto. Requer conta de anúncios ligada a uma Página do Facebook. |

Dependência: se o Instagram não estiver ligado a uma Página do Facebook/portfólio empresarial, o Business Suite pede para conectar na primeira vez.

## Objetivos e quando usar
| Objetivo (no Impulsionar) | Uso no Kairos |
|---|---|
| **Visitas ao perfil** | Padrão para crescer seguidores qualificados. Métrica: custo por visita e seguidores na semana. |
| Mensagens (Direct/WhatsApp) | Quando o funil de atendimento estiver pronto e o dono tiver tempo de responder no mesmo dia. |
| Visitas ao site | Só com UTM e com o site atualizado (hoje o site ainda fala em notebook ligado). |
Alcance ou visualizações sozinhos não são objetivo: não trazem cliente.

## Público
- Interesses de nicho na Meta são escassos e mudam. **Nunca inventar interesse.** Na hora de criar, buscar "licitação", "compras públicas", "pregão", "fornecedor do governo"; usar só os que aparecerem.
- Recomendação para conta pequena: **Brasil, 25-60 anos, interesses amplos (empreendedorismo, pequenas e médias empresas) + os de licitação que existirem, com expansão automática (Advantage+) ligada**. O próprio criativo filtra: a etiqueta "PREGÃO · COMPRAS.GOV.BR" e o gancho afastam quem não é do nicho.
- Nacional, não estadual: o produto é digital e o Compras.gov.br é federal.

## Criativos elegíveis
- Reels com **trilha original** (não usar música da biblioteca do app em post que vai ser impulsionado: algumas faixas bloqueiam o Boost).
- Gancho completo no quadro 0; 12-16 s; legenda na tela; sem enquetes ou figurinhas interativas.
- Sem promessa de resultado ("ganhe licitações"), sem preço em destaque no anúncio.

## Plano experimental (ciclo de 30 dias)
- **Teste 1** (até R$ 40 de custo total): R$ 8,90/dia × 4 dias ≈ R$ 35,60 + impostos ≈ R$ 39,93.
- **Teste 2** (até R$ 40): mesma estrutura, outra peça/hipótese, **depois** do teste 1 (não em paralelo).
- **Reserva** (até R$ 70): só para reforçar o vencedor com evidência. Sem evidência, **não gastar**.

## Regras de parada e de vitória (heurísticas iniciais, não benchmarks)
- Parar antes do fim se, com ≥ R$ 15 gastos: 0 visitas ao perfil, ou frequência > 2,5, ou comentários negativos sobre o produto.
- Considerar "promissor" se: custo por visita ao perfil ≤ R$ 0,60 **e** pelo menos 1 seguidor novo a cada R$ 10 **ou** ≥ 3 comentários "PREGÃO".
- Amostras pequenas: não declarar vencedor com menos de ~R$ 30 gastos ou ~1.000 impressões. Comparar sempre custo por resultado, nunca curtidas.

## Registro obrigatório
Cada impulso vira uma linha em `operacao/controle_boost.csv` (ID, post, objetivo, público, janela, orçamento aprovado, gasto, alcance pago, impressões, frequência, visitas, seguidores, comentários PREGÃO, cliques, leads, testes, custo por resultado, leitura, próxima ação) e um experimento em `registro_experimentos.csv`. Dados pagos: Metricool (`IGRE14/16/17/18/20` em Reels; `IGPO17/19/22/23/26` em posts) ou print do painel do anúncio enviado pelo dono.
