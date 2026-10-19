import sys, pathlib, subprocess, shutil
from playwright.sync_api import sync_playwright
v, dur = sys.argv[1], float(sys.argv[2]); fps=30
p=pathlib.Path(__file__).parent; fr=p/f"frc_{v}"; shutil.rmtree(fr,ignore_errors=True); fr.mkdir()
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1350})
    pg.goto(f"file://{p}/cover.html?v={v}"); pg.wait_for_timeout(300)
    for i in range(int(dur*fps)):
        pg.evaluate(f"render({i/fps})"); pg.screenshot(path=str(fr/f"{i:04d}.png"))
    b.close()
subprocess.run(["ffmpeg","-v","error","-y","-framerate",str(fps),"-i",str(fr/"%04d.png"),"-f","lavfi","-i","anullsrc=r=44100:cl=stereo","-shortest",
 "-c:v","libx264","-preset","slow","-crf","16","-pix_fmt","yuv420p","-c:a","aac","-movflags","+faststart",str(p/"out"/f"capa_opcao_{v.upper()}.mp4")],check=True)
