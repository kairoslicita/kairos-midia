"""Renderiza os Reels do lote V2 (reels2.html#r2|r3|r4) com a trilha original de musica/trilhas/reel_<modo>.wav.
Uso: python3 filmr2.py r4 ../midia/lote_v2_reels/reel_anuncio_perdeu_010.mp4 15.5
Trilhas: python3 musica/synth_reels2.py (gera musica/trilhas/reel_r2|r3|r4.wav)."""
import pathlib, subprocess, shutil, sys
from playwright.sync_api import sync_playwright
p=pathlib.Path(__file__).parent.resolve(); mode=sys.argv[1]; out=sys.argv[2]; T=float(sys.argv[3]) if len(sys.argv)>3 else 18.5; fps=30
fr=p/f"fr_{mode}"; shutil.rmtree(fr,ignore_errors=True); fr.mkdir()
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    pg.goto(f"file://{p}/reels2.html#{mode}"); pg.wait_for_timeout(300)
    for i in range(int(T*fps)):
        pg.evaluate(f"render({i/fps})"); pg.screenshot(path=str(fr/f"{i:04d}.png"))
    b.close()
pathlib.Path(out).parent.mkdir(parents=True, exist_ok=True)
subprocess.run(["ffmpeg","-v","error","-y","-framerate","30","-i",str(fr/"%04d.png"),"-i",str(p/"musica"/"trilhas"/f"reel_{mode}.wav"),"-c:v","libx264","-preset","slow","-crf","17","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart",out],check=True)
shutil.rmtree(fr); print("done",out)
