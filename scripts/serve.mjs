// Tiny static server for local testing: node scripts/serve.mjs [port]
// Note: phones only allow the live camera on https:// (or localhost).
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { join, extname, normalize } from 'node:path';

const dist = new URL('../dist', import.meta.url).pathname;
const port = Number(process.argv[2] || process.env.PORT || 8080);
const types = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css',
  '.svg': 'image/svg+xml', '.png': 'image/png', '.csv': 'text/csv', '.gz': 'application/gzip',
  '.webmanifest': 'application/manifest+json', '.wasm': 'application/wasm', '.json': 'application/json',
};

createServer(async (req, res) => {
  let path = normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname)).replace(/^(\.\.[/\\])+/, '');
  if (path.endsWith('/')) path += 'index.html';
  try {
    const body = await readFile(join(dist, path));
    res.writeHead(200, { 'Content-Type': types[extname(path)] || 'application/octet-stream' });
    res.end(body);
  } catch {
    res.writeHead(404).end('Not found');
  }
}).listen(port, () => console.log(`Serving dist/ on http://localhost:${port}`));
