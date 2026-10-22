# 03 · Direção de arte

Complementa o `02` (o que já está aprovado) com as regras para criar coisas novas sem perder o padrão.

## Princípios
1. **Uma ideia por quadro.** Cada slide/cena tem um título, uma representação e uma frase de apoio. Se precisar de mais, divida.
2. **O sistema é o protagonista.** Sempre que possível, a ideia aparece numa tela remodelada do Kairos (celular ou painel `sys`), não em ícone genérico.
3. **Movimento com intenção.** Toda animação conta algo: valor caindo, robô cobrindo, limite segurando, status mudando. Nada de partículas ou efeitos decorativos.
4. **Contraste de estado:** coral = perda/risco/concorrente; lima = ganho/ok/robô; âmbar = atenção. Nunca inverter.
5. **Legível no celular:** título ≥ 88 px no carrossel e ≥ 100 px no Reel; texto ≥ 22 px; números mono ≥ 26 px. Testar reduzindo a 30%.

## Remodelagem das interfaces
- **Permitido:** reorganizar, ampliar, destacar, simplificar e estilizar telas; criar perspectiva, luz, profundidade, mockups; reimaginar layouts para comunicação.
- **Obrigatório:** manter a lógica real (stop loss por item, variação mínima, log de atividades, status perdendo/ganhando, um login com várias disputas). Valores sempre "de exemplo" e marcados.
- **Proibido:** botões ou funções que não existem; números de clientes ou resultados inventados; CNPJ, nomes ou dados reais sem autorização.
- **Marketing ≠ tutorial.** Peça conceitual leva "Telas ilustrativas". Tutorial ("como configurar") usa os passos reais. Se não houver gravação real, pedir ao dono uma gravação de tela do celular, sem dados sensíveis.

## Composição
- Margens laterais de 72 px no carrossel e 80 px no Reel. Grade: título no topo (y 136-420), conteúdo no meio (450-1150), apoio/CTA embaixo (1160-1260 no carrossel).
- Capas: manchete ocupa o terço superior; cartão de alerta de 500-520 px de altura; pílula "Arraste" em y≈1175.
- Reel: conteúdo entre y 220 e 1540; legenda cinética em y≈1290-1450.

## Movimento
- Entradas: ease-out cúbico de 0,3-0,5 s, atraso escalonado de 0,05-0,6 s.
- Cortes de Reel a cada 2-5 s, com "punch" de 0,22 s. Primeira cena sem animação de entrada (quadro 0 completo).
- Loops de carrossel em 6 s: o estado final precisa ficar legível pelo menos 1,5 s.
- Pulsar CTA com escala de ±3% numa senoide (não piscar).

## Capas (o que mais importa)
- Manchete com tensão concreta: número, perda, pergunta direta ("Perdeu o item por R$ 0,10?", "3 pregões no mesmo horário.", "Até onde dá para baixar?").
- Cartão animado que prova a manchete em 2-3 s.
- Teste: a capa precisa fazer sentido em 1 segundo, sem som e sem conhecer o Kairos.
