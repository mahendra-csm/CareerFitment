// node print.js in.html out.pdf  - auto-fits each page's content, then prints an A4 PDF with Chromium
const { chromium } = require('playwright');
(async () => {
  const [inp, out] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 794, height: 1123 } });
  await p.goto('file://' + inp, { waitUntil: 'load', timeout: 300000 });
  await p.evaluate(() => document.fonts.ready);
  const report = await p.evaluate(() => {
    const res = [];
    document.querySelectorAll('.page:not(.cover):not(.divider):not(.back):not(.full):not(.nofit) > .pc').forEach((pc) => {
      const zi = document.createElement('div'); zi.className = 'zi';
      while (pc.firstChild) zi.appendChild(pc.firstChild);
      pc.appendChild(zi);
      const H = pc.clientHeight, W = pc.clientWidth;
      const natural = () => { zi.style.minHeight = ''; const h = zi.scrollHeight; return h; };
      let h = natural(), z = 1;
      if (h < H * 0.97) {
        // grow until it fills the page (cap 1.3)
        let lo = 1, hi = 1.12;
        for (let i = 0; i < 14; i++) { const m = (lo + hi) / 2; zi.style.zoom = m; zi.style.width = (W / m) + 'px'; if (zi.scrollHeight * m <= H * 0.985) lo = m; else hi = m; }
        z = lo;
      } else if (h > H) {
        let lo = 0.6, hi = 1;
        for (let i = 0; i < 14; i++) { const m = (lo + hi) / 2; zi.style.zoom = m; zi.style.width = (W / m) + 'px'; if (zi.scrollHeight * m <= H) lo = m; else hi = m; }
        z = lo;
      }
      zi.style.zoom = z; zi.style.width = (W / z) + 'px'; zi.style.minHeight = (H / z) + 'px';
      const n = pc.parentElement.dataset.n;
      if (z < 0.97) res.push(`page ${n}: overflow, shrunk to ${z.toFixed(2)}`);
    });
    return res;
  });
  report.forEach((r) => console.log(r));
  await p.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await b.close();
})();
