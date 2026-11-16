import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
const root = new URL('../website/public/experiments/two-attractor-field/', import.meta.url);
const port = Number(process.env.PORT || 8788);
const types = { html: 'text/html', js: 'text/javascript', css: 'text/css', txt: 'text/plain' };
createServer(async (req, res) => {
  try {
    const pathname = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
    const file = new URL('.' + (pathname === '/' ? '/index.html' : pathname), root);
    if (!file.href.startsWith(root.href)) throw new Error('Invalid path');
    const body = await readFile(file);
    res.writeHead(200, { 'Content-Type': types[file.pathname.split('.').pop()] || 'application/octet-stream', 'Cache-Control': 'no-store' });
    res.end(body);
  } catch { res.writeHead(404);res.end('Not found'); }
}).listen(port, '127.0.0.1', () => console.log(`Two-attractor Three.js viewer: http://127.0.0.1:${port}/index.html`));
