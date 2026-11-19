const { chromium } = require('playwright'); const { spawn } = require('child_process');
const OUT = process.argv[2], T = 21.5, FPS = 30;
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + __dirname + '/reels_cop.html'); await p.waitForTimeout(300);
  const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', '30', '-c:v', 'mjpeg', '-i', '-', '-i', __dirname + '/musica/trilhas/reel_cop.wav', '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', OUT + '.tmp.mp4'], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let i = 0; i < Math.round(T * FPS); i++) { await p.evaluate((t) => render(t), i / FPS); const buf = await p.screenshot({ type: 'jpeg', quality: 93 }); if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once('drain', r)); }
  ff.stdin.end(); await new Promise((r) => ff.on('close', r)); require('fs').renameSync(OUT + '.tmp.mp4', OUT); await b.close(); console.log('ok', OUT); })();
