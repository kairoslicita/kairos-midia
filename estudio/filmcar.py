"""Renderiza um carrossel animado (slides 1080x1350, 6 s cada) e embute uma trilha contínua fatiada por slide.
Uso: python3 filmcar.py <trilha.wav> <pasta_saida> "nome|query" "nome|query" ...
Ex.: python3 filmcar.py musica/trilhas/carrossel_A_lofi.wav ../midia/x "c5_01_capa|s=c5capa&n=1/7"
"""
import sys, pathlib, subprocess, shutil
from playwright.sync_api import sync_playwright
track, outdir, items = sys.argv[1], pathlib.Path(sys.argv[2]), sys.argv[3:]
p=pathlib.Path(__file__).parent.resolve(); fps=30; D=6.0; outdir.mkdir(parents=True, exist_ok=True)
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1350})
    for k,it in enumerate(items):
        name,q=it.split('|'); fr=p/f"frcar_{name}"; shutil.rmtree(fr,ignore_errors=True); fr.mkdir()
        pg.goto(f"file://{p}/slides.html?{q}"); pg.wait_for_timeout(200)
        for i in range(int(D*fps)):
            pg.evaluate(f"render({i/fps})"); pg.screenshot(path=str(fr/f"{i:04d}.png"))
        subprocess.run(["ffmpeg","-v","error","-y","-framerate",str(fps),"-i",str(fr/"%04d.png"),
          "-ss",str(k*D),"-t",str(D),"-i",track,"-af","afade=t=in:d=0.04,afade=t=out:st=5.9:d=0.1",
          "-c:v","libx264","-preset","slow","-crf","16","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart",
          str(outdir/f"{name}.mp4")],check=True)
        shutil.rmtree(fr); print(name, flush=True)
    b.close()
