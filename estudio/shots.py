import sys, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image
p=pathlib.Path(__file__).parent; out=sys.argv[1]; items=sys.argv[2:]  # "query@t"
ims=[]
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1350})
    for it in items:
        q,t=it.split('@'); pg.goto(f"file://{p}/slides.html?{q}"); pg.wait_for_timeout(150); pg.evaluate(f"render({t})")
        f=p/'tmp_shot.png'; pg.screenshot(path=str(f)); ims.append(Image.open(f).resize((432,540)).copy())
    b.close()
W=Image.new('RGB',(432*len(ims),540)); [W.paste(im,(i*432,0)) for i,im in enumerate(ims)]; W.save(out); print(out)
