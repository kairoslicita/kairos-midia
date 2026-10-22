import sys, pathlib, subprocess, shutil
from playwright.sync_api import sync_playwright
q, dur, name = sys.argv[1], float(sys.argv[2]), sys.argv[3]; fps=30
p=pathlib.Path(__file__).parent; fr=p/f"fr_{name}"; shutil.rmtree(fr,ignore_errors=True); fr.mkdir()
page = sys.argv[4] if len(sys.argv)>4 else "slides.html"
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1350})
    pg.goto(f"file://{p}/{page}?{q}"); pg.wait_for_timeout(300)
    for i in range(int(dur*fps)):
        pg.evaluate(f"render({i/fps})"); pg.screenshot(path=str(fr/f"{i:04d}.png"))
    b.close()
out=p/"final"; out.mkdir(exist_ok=True)
subprocess.run(["ffmpeg","-v","error","-y","-framerate",str(fps),"-i",str(fr/"%04d.png"),"-f","lavfi","-i","anullsrc=r=44100:cl=stereo","-shortest",
 "-c:v","libx264","-preset","slow","-crf","16","-pix_fmt","yuv420p","-c:a","aac","-movflags","+faststart",str(out/f"{name}.mp4")],check=True)
shutil.rmtree(fr)
print(name)
