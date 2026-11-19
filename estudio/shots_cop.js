const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + __dirname + '/reels_cop.html'); await p.waitForTimeout(300);
  for (const t of [0, 4.6, 8.8, 13.0, 17.2, 20.6]) { await p.evaluate((t) => render(t), t); await p.screenshot({ path: `/tmp/claude-0/-home-claude/df052ad1-0f12-5b0c-9cf6-7985f56b8916/scratchpad/prop16/rc_${t}.jpg`, type: 'jpeg', quality: 80 }); }
  await b.close(); })();
