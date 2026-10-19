import pathlib, subprocess, shutil
from playwright.sync_api import sync_playwright
p=pathlib.Path(__file__).parent; fr=p/"fr_reel"; shutil.rmtree(fr,ignore_errors=True); fr.mkdir(); fps=30
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920})
    pg.goto(f"file://{p}/reel.html"); pg.wait_for_timeout(300)
    for i in range(int(21.5*fps)):
        pg.evaluate(f"render({i/fps})"); pg.screenshot(path=str(fr/f"{i:04d}.png"))
    b.close()
subprocess.run(["ffmpeg","-v","error","-y","-framerate","30","-i",str(fr/"%04d.png"),"-i",str(p/"sfx.wav"),"-c:v","libx264","-preset","slow","-crf","17","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart",str(p/"final"/"reel_reuniao_pregao.mp4")],check=True)
shutil.rmtree(fr); print("done")
