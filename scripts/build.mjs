// Builds the static app into dist/: copies src/ and the OCR/barcode libraries
// from node_modules so the app works fully offline (no CDN needed).
import { cpSync, mkdirSync, rmSync, readdirSync, readFileSync, writeFileSync, statSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { join, relative } from 'node:path';

const root = new URL('..', import.meta.url).pathname;
const src = join(root, 'src');
const dist = join(root, 'dist');
const nm = join(root, 'node_modules');

rmSync(dist, { recursive: true, force: true });
cpSync(src, dist, { recursive: true });

const vendor = {
  'vendor/tesseract.min.js': 'tesseract.js/dist/tesseract.min.js',
  'vendor/worker.min.js': 'tesseract.js/dist/worker.min.js',
  // LSTM-only cores (with embedded wasm); tesseract.js picks the right one for the device.
  'vendor/core/tesseract-core-lstm.wasm.js': 'tesseract.js-core/tesseract-core-lstm.wasm.js',
  'vendor/core/tesseract-core-simd-lstm.wasm.js': 'tesseract.js-core/tesseract-core-simd-lstm.wasm.js',
  'vendor/core/tesseract-core-relaxedsimd-lstm.wasm.js': 'tesseract.js-core/tesseract-core-relaxedsimd-lstm.wasm.js',
  'vendor/lang/eng.traineddata.gz': '@tesseract.js-data/eng/4.0.0_best_int/eng.traineddata.gz',
  'vendor/zxing-library.min.js': '@zxing/library/umd/index.min.js',
  'vendor/zxing-browser.min.js': '@zxing/browser/umd/zxing-browser.min.js',
};
for (const [to, from] of Object.entries(vendor)) {
  mkdirSync(join(dist, to, '..'), { recursive: true });
  cpSync(join(nm, from), join(dist, to));
}

// Fill in the service worker's precache list and a content-based cache version.
const walk = (dir) => readdirSync(dir).flatMap((f) => {
  const p = join(dir, f);
  return statSync(p).isDirectory() ? walk(p) : [p];
});
const files = walk(dist).filter((p) => !p.endsWith('sw.js'));
const hash = createHash('sha256');
for (const f of files) hash.update(readFileSync(f));
const precache = ['./', ...files.map((f) => relative(dist, f)).filter((f) => !/core\/tesseract-core-(simd|relaxedsimd)/.test(f))];
const sw = readFileSync(join(dist, 'sw.js'), 'utf8')
  .replace('__VERSION__', hash.digest('hex').slice(0, 12))
  .replace('__FILES__', JSON.stringify(precache, null, 2));
writeFileSync(join(dist, 'sw.js'), sw);

console.log(`Built ${files.length + 1} files into dist/`);
