"""Renderiza o R10 (voo.html#r10) com a trilha musica/trilhas/reel_r10.wav. Quadros reais em voo/ (bash voo/extrair.sh dentro de voo/)."""
import pathlib, subprocess, shutil, sys
from playwright.sync_api import sync_playwright
p=pathlib.Path(__file__).parent.resolve(); mode=sys.argv[1]; out=sys.argv[2]; T=float(sys.argv[3]) if len(sys.argv)>3 else 18.5; fps=30
fr=p/f"fr_{mode}"; fr.mkdir(exist_ok=True)  # retoma quadros já renderizados
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    pg.goto(f"file://{p}/voo.html#{mode}"); pg.wait_for_timeout(300)
    for i in range(int(T*fps)):
        f=fr/f"{i:04d}.png"
        if f.exists() and f.stat().st_size>0 and (fr/f"{i+1:04d}.png").exists(): continue
        pg.evaluate(f"render({i/fps})"); pg.evaluate("Promise.all(Array.from(document.images).map(i=>i.decode().catch(()=>0)))"); pg.screenshot(path=str(f))
    b.close()
pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
subprocess.run(["ffmpeg","-v","error","-y","-framerate","30","-i",str(fr/"%04d.png"),"-i",str(p/"musica"/"trilhas"/f"reel_{mode}.wav"),"-c:v","libx264","-preset","slow","-crf","17","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart",out],check=True)
shutil.rmtree(fr); print("done",out)
