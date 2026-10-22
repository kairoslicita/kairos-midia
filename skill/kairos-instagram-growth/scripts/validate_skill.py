#!/usr/bin/env python3
"""Valida a skill kairos-instagram-growth: frontmatter, estrutura obrigatória, links internos,
templates preenchidos e cobertura dos 10 comandos-padrão.
Uso: python3 scripts/validate_skill.py [pasta_da_skill]   (código de saída 0 = ok)"""
import sys, re, csv, pathlib

root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parents[1])
errors, notes = [], []

skill = (root / "SKILL.md").read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
if not m:
    errors.append("SKILL.md sem frontmatter YAML")
else:
    fm = dict(l.split(":", 1) for l in m.group(1).splitlines() if ":" in l)
    name = fm.get("name", "").strip()
    desc = fm.get("description", "").strip()
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name): errors.append(f"name inválido: {name!r}")
    if name != root.name: errors.append(f"name ({name}) diferente da pasta ({root.name})")
    if not (20 <= len(desc) <= 1024): errors.append(f"description com {len(desc)} caracteres")
    if "<" in desc or ">" in desc: errors.append("description com < ou >")

refs = ["01_contexto_kairos","02_padrao_visual_aprovado","03_direcao_de_arte","04_reels_premium","05_carrosseis_premium",
        "06_stories_e_comunidade","07_crescimento_organico","08_boost_meta_ads","09_publico_personas","10_inteligencia_competitiva",
        "11_funil_conversao","12_metricas_analytics","13_operacao_editorial","14_qualidade_validacao","15_economia_de_recursos",
        "16_rotina_automacao","17_aprendizados_historicos"]
for r in refs:
    f = root / "references" / f"{r}.md"
    if not f.exists(): errors.append(f"falta references/{r}.md"); continue
    words = len(f.read_text(encoding="utf-8").split())
    if words < 120: errors.append(f"references/{r}.md muito curto ({words} palavras)")
    if r not in skill: errors.append(f"SKILL.md não cita {r}")

tpl = ["calendario_editorial.csv","controle_conteudos.csv","controle_boost.csv","dashboard_kpis.csv","banco_ideias.csv",
       "registro_experimentos.csv","briefing_audiovisual.md","checklist_qualidade.md","aprovacoes_campanhas.md"]
for t in tpl:
    f = root / "assets" / "templates" / t
    if not f.exists(): errors.append(f"falta assets/templates/{t}"); continue
    if t.endswith(".csv"):
        rows = list(csv.reader(f.open(encoding="utf-8")))
        if len(rows) < 2: errors.append(f"{t} sem linhas preenchidas")
        elif any(len(r) != len(rows[0]) for r in rows): errors.append(f"{t} com número de colunas inconsistente")
        else: notes.append(f"{t}: {len(rows)-1} linhas")
    elif len(f.read_text(encoding="utf-8").split()) < 80: errors.append(f"{t} quase vazio")

# caminhos relativos citados entre crases que apontam para dentro da skill
for f in [root / "SKILL.md", *(root / "references").glob("*.md")]:
    for p in re.findall(r"`((?:references|assets|scripts)/[^`*<>|\s]+)`", f.read_text(encoding="utf-8")):
        if not (root / p).exists(): errors.append(f"{f.name}: caminho inexistente {p}")

commands = ["Assuma o Instagram do Kairos hoje", "Prepare a próxima semana", "Qual Reel devemos impulsionar",
            "Analise o Boost", "Crie um Reel premium", "Faça um carrossel mantendo nossa identidade",
            "Estamos crescendo pouco", "Analise os concorrentes", "Como gerar clientes pelo Instagram", "Prepare os próximos 30 dias"]
for c in commands:
    if c not in skill: errors.append(f"comando sem rota no SKILL.md: {c}")

refs_dir = root / "assets" / "referencias"
imgs = list(refs_dir.glob("*.jpg")) if refs_dir.exists() else []
if len(imgs) < 5: errors.append("menos de 5 referências visuais em assets/referencias")
else: notes.append(f"referências visuais: {len(imgs)}")

for n in notes: print("ok  ", n)
for e in errors: print("ERRO", e)
print("RESULTADO:", "aprovado" if not errors else f"{len(errors)} erro(s)")
sys.exit(1 if errors else 0)
