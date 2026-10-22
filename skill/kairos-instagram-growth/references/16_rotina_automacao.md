# 16 · Rotina e automação

Uma skill não roda sozinha. O que roda sem o dono são **tarefas agendadas** do Claude (cada execução abre uma sessão nova, lê o repo e usa esta skill) e o **Metricool** (publica o que foi agendado). Nada monitora 24/7.

## Tarefas agendadas existentes (conta do dono)
| Nome | Quando | Faz |
|---|---|---|
| Instagram Kairos: pauta semanal | Qui 08h58 | Prepara a semana seguinte (peças, legendas, LEIA-ME), pede aprovação; agenda só depois de "aprovado" |
| Instagram Kairos: relatório semanal | Seg 08h54 | Números da semana, leitura, decisões e proposta de Boost |
| Lembretes do dia do post | 10h05 nos dias de publicação | Lembra o dono: ManyChat, Story, responder comentários |

Toda execução agendada: ler `operacao/ESTADO.md` → fazer a tarefa → atualizar CSVs/ESTADO → commit → mensagem curta ao dono.

## Integrações e permissões
| Item | Situação | O que destrava |
|---|---|---|
| Metricool (leitura e agendamento) | Conectado | Cota de 20 posts/mês |
| GitHub `kairoslicita/kairos-midia` | Conectado (público) | Hospeda mídia e operação. Por ser público, nada de dado pessoal ou credencial |
| Meta Business Suite / Gerenciador de Anúncios | **Sem acesso do Claude** | Dono ativa o Boost pelo Safari; manda print dos resultados ou o Metricool lê os dados pagos |
| ManyChat | Conta do dono, plano grátis | Dono cria um gatilho por post |
| Insights nativos do Instagram (visitas ao perfil, % não seguidores) | Só pelo app | Print do dono quando for decisivo |
| Site (UTM/Analytics) | Sem acesso ao código | Pedir a quem mantém o site |

## Comando para a próxima semana (sem repetir o briefing)
"Prepare a próxima semana." A skill lê ESTADO + calendário, produz as peças planejadas, confere a qualidade, entrega o pacote e pede "Aprova a semana?".
