import { normalize, parseList, buildIndex, check, extractCandidates } from './matcher.js';

const $ = (id) => document.getElementById(id);
const LIST_KEY = 'ssc.list.v1';
const HISTORY_KEY = 'ssc.history.v1';
const MAX_HISTORY = 1000;

// ---------- storage (wrapped: storage can be unavailable in private mode) ----------
const store = {
  get(key, fallback) {
    try { const v = localStorage.getItem(key); return v ? JSON.parse(v) : fallback; } catch { return fallback; }
  },
  set(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); return true; } catch { return false; }
  },
  remove(key) { try { localStorage.removeItem(key); } catch { /* ignore */ } },
};

// ---------- state ----------
let list = store.get(LIST_KEY, null); // { name, columns, rows, serialCol, loadedAt }
let index = list ? buildIndex(list.rows, list.serialCol) : null;
let history = store.get(HISTORY_KEY, []);

// ---------- tabs ----------
document.querySelectorAll('.tabbar button').forEach((btn) => {
  btn.addEventListener('click', () => showTab(btn.dataset.tab));
});
function showTab(name) {
  document.querySelectorAll('.tabbar button').forEach((b) => b.setAttribute('aria-selected', String(b.dataset.tab === name)));
  document.querySelectorAll('.tab').forEach((s) => { s.hidden = s.id !== `tab-${name}`; });
  if (name !== 'scan') stopCamera();
  if (name === 'list') renderList();
  if (name === 'history') renderHistory();
}

// ---------- list management ----------
function setList(parsed, name) {
  list = { name, columns: parsed.columns, rows: parsed.rows, serialCol: parsed.serialCol, loadedAt: Date.now() };
  index = buildIndex(list.rows, list.serialCol);
  if (!store.set(LIST_KEY, list)) alert('The list is too large to be saved on this device. It will work until you close the app.');
  renderBadge();
  renderList();
}

function loadText(text, name) {
  const parsed = parseList(text);
  if (!parsed.rows.length) { alert('No serial numbers found in that list.'); return; }
  setList(parsed, name);
}

$('fileInput').addEventListener('change', async (e) => {
  const file = e.target.files[0];
  if (!file) return;
  loadText(await file.text(), file.name);
  e.target.value = '';
});
$('pasteBtn').addEventListener('click', () => {
  const text = $('pasteArea').value;
  if (!text.trim()) return;
  loadText(text, 'Pasted list');
  $('pasteArea').value = '';
  $('pasteArea').closest('details').open = false;
});
$('sampleBtn').addEventListener('click', async () => {
  const res = await fetch('sample-list.csv');
  loadText(await res.text(), 'Sample list');
});
$('columnSelect').addEventListener('change', (e) => {
  if (!list) return;
  list.serialCol = Number(e.target.value);
  index = buildIndex(list.rows, list.serialCol);
  store.set(LIST_KEY, list);
  renderBadge();
  renderList();
});
$('clearList').addEventListener('click', () => {
  if (!confirm('Remove the serial number list from this phone?')) return;
  list = null; index = null;
  store.remove(LIST_KEY);
  renderBadge();
  renderList();
});
$('listFilter').addEventListener('input', () => renderList());

function renderBadge() {
  $('listBadge').textContent = index ? `${index.size.toLocaleString()} serials` : 'No list';
}

function seenSerials() {
  return new Set(history.filter((h) => h.status === 'found').map((h) => h.key));
}

function renderList() {
  const has = !!list;
  $('listCard').hidden = !has;
  $('columnPick').hidden = !has || list.columns.length < 2;
  if (!has) { $('listSummary').textContent = 'No list loaded yet.'; return; }

  const seen = seenSerials();
  const seenCount = [...index.exact.keys()].filter((k) => seen.has(k)).length;
  $('listSummary').textContent =
    `${list.name}: ${index.size.toLocaleString()} serial numbers` +
    ` · ${seenCount.toLocaleString()} scanned` +
    ` · loaded ${new Date(list.loadedAt).toLocaleString()}`;

  const sel = $('columnSelect');
  sel.innerHTML = '';
  list.columns.forEach((c, i) => sel.add(new Option(c, String(i), false, i === list.serialCol)));

  const q = normalize($('listFilter').value);
  const rows = q ? list.rows.filter((r) => r.some((c) => normalize(c).includes(q))) : list.rows;
  const LIMIT = 200;
  const table = $('listTable');
  table.innerHTML = '';
  const head = table.createTHead().insertRow();
  list.columns.forEach((c) => { const th = document.createElement('th'); th.textContent = c; head.appendChild(th); });
  const body = table.createTBody();
  for (const r of rows.slice(0, LIMIT)) {
    const tr = body.insertRow();
    if (seen.has(normalize(r[list.serialCol]))) tr.className = 'seen';
    r.forEach((c, i) => {
      const td = tr.insertCell();
      td.textContent = c;
      if (i === list.serialCol) td.className = 'serial-col';
    });
  }
  $('listMore').textContent = rows.length > LIMIT ? `Showing ${LIMIT} of ${rows.length.toLocaleString()} – search to narrow down.` : '';
}

// ---------- checking ----------
let lastAuto = { key: '', at: 0 };

$('checkForm').addEventListener('submit', (e) => {
  e.preventDefault();
  runCheck($('serialInput').value, 'manual');
});

function runCheck(value, source) {
  const key = normalize(value);
  if (!key) return;
  $('serialInput').value = key;
  if (!index) {
    showResult({ status: 'nolist', key });
    return;
  }
  const r = check(index, key);
  showResult(r);
  feedback(r.status);
  addHistory({ key, status: r.status, source, at: Date.now() });
}

function showResult(r) {
  const el = $('result');
  el.hidden = false;
  el.className = `result ${r.status === 'nolist' ? 'possible' : r.status}`;
  el.innerHTML = '';
  const h = document.createElement('h3');
  const s = document.createElement('div');
  s.className = 'serial';
  s.textContent = r.key;

  if (r.status === 'nolist') {
    h.textContent = 'No list loaded';
    el.append(h, s, para('Import a list under the “List” tab first.'));
    return;
  }
  h.textContent = { found: '✔ In the list', possible: '? Possible match', not_found: '✘ Not in the list' }[r.status];
  el.append(h, s);

  if (r.status === 'possible') {
    el.append(para(`Not an exact match (${r.reason}). Compare with the ski before confirming:`));
  }
  for (const row of r.matches.slice(0, 5)) {
    const box = document.createElement('div');
    box.className = 'match';
    const dl = document.createElement('dl');
    list.columns.forEach((c, i) => {
      if (!row[i]) return;
      const dt = document.createElement('dt'); dt.textContent = c;
      const dd = document.createElement('dd'); dd.textContent = row[i];
      dl.append(dt, dd);
    });
    box.append(dl);
    if (r.status === 'possible') {
      const b = document.createElement('button');
      b.className = 'secondary small-btn';
      b.textContent = `Yes, it is ${normalize(row[list.serialCol])}`;
      b.addEventListener('click', () => runCheck(row[list.serialCol], 'confirmed'));
      box.append(b);
    }
    el.append(box);
  }
  el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function para(text) { const p = document.createElement('p'); p.className = 'small'; p.textContent = text; return p; }

let audioCtx;
function feedback(status) {
  try { navigator.vibrate?.(status === 'found' ? 80 : [60, 60, 60, 60, 200]); } catch { /* ignore */ }
  try {
    audioCtx ??= new (window.AudioContext || window.webkitAudioContext)();
    const o = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    o.frequency.value = status === 'found' ? 1046 : status === 'possible' ? 660 : 220;
    g.gain.setValueAtTime(0.15, audioCtx.currentTime);
    g.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.25);
    o.connect(g).connect(audioCtx.destination);
    o.start();
    o.stop(audioCtx.currentTime + 0.25);
  } catch { /* ignore */ }
}

// ---------- history ----------
function addHistory(entry) {
  history.unshift(entry);
  if (history.length > MAX_HISTORY) history.length = MAX_HISTORY;
  store.set(HISTORY_KEY, history);
}

const STATUS_LABEL = { found: 'In list', possible: 'Possible', not_found: 'Not in list' };

function renderHistory() {
  const ul = $('historyList');
  ul.innerHTML = '';
  const counts = { found: 0, possible: 0, not_found: 0 };
  history.forEach((h) => { counts[h.status] = (counts[h.status] || 0) + 1; });
  $('historySummary').textContent = history.length
    ? `${history.length} scans · ${counts.found} in list · ${counts.not_found} not in list · ${counts.possible} possible`
    : 'Nothing scanned yet.';
  for (const h of history.slice(0, 300)) {
    const li = document.createElement('li');
    const left = document.createElement('div');
    const s = document.createElement('div'); s.className = 's'; s.textContent = h.key;
    const t = document.createElement('div'); t.className = 't'; t.textContent = `${new Date(h.at).toLocaleString()} · ${h.source}`;
    left.append(s, t);
    const pill = document.createElement('span');
    pill.className = `pill ${h.status}`;
    pill.textContent = STATUS_LABEL[h.status] || h.status;
    li.append(left, pill);
    li.addEventListener('click', () => { showTab('scan'); runCheck(h.key, 'history'); });
    ul.append(li);
  }
}

$('clearHistory').addEventListener('click', () => {
  if (!confirm('Clear the scan history?')) return;
  history = [];
  store.set(HISTORY_KEY, history);
  renderHistory();
});

$('exportHistory').addEventListener('click', () => {
  const esc = (v) => `"${String(v ?? '').replace(/"/g, '""')}"`;
  const lines = [['Serial', 'Result', 'Time', 'Source'].map(esc).join(',')];
  for (const h of history) lines.push([h.key, STATUS_LABEL[h.status] || h.status, new Date(h.at).toISOString(), h.source].map(esc).join(','));
  const blob = new Blob([lines.join('\n')], { type: 'text/csv' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `ski-scans-${new Date().toISOString().slice(0, 10)}.csv`;
  a.click();
  setTimeout(() => URL.revokeObjectURL(a.href), 1000);
});

// ---------- camera ----------
const video = $('video');
const frame = $('frame');
let stream = null;
let scanTimer = null;
let barcodeBusy = false;
let ocrBusy = false;
let barcodeDetector = null;
let zxingReader = null;

function camStatus(text) {
  $('camStatus').hidden = !text;
  $('camStatus').textContent = text || '';
}

$('startCam').addEventListener('click', startCamera);
$('stopCam').addEventListener('click', stopCamera);

async function startCamera() {
  if (!navigator.mediaDevices?.getUserMedia) {
    alert('Live camera is not available here (the app must be opened over https). Use “Use a photo” instead.');
    return;
  }
  try {
    stream = await navigator.mediaDevices.getUserMedia({
      audio: false,
      video: { facingMode: { ideal: 'environment' }, width: { ideal: 1920 }, height: { ideal: 1080 } },
    });
  } catch (err) {
    alert(`Could not open the camera: ${err.message}`);
    return;
  }
  video.srcObject = stream;
  await video.play();
  $('camera').classList.add('live');
  $('camControls').hidden = false;
  setupTorch();
  await setupBarcode();
  scanTimer = setInterval(scanBarcodeFrame, 300);
}

function stopCamera() {
  clearInterval(scanTimer);
  scanTimer = null;
  stream?.getTracks().forEach((t) => t.stop());
  stream = null;
  video.srcObject = null;
  $('camera').classList.remove('live');
  $('camControls').hidden = true;
  $('barcodeHint').hidden = true;
  camStatus('');
}

function setupTorch() {
  const track = stream.getVideoTracks()[0];
  const caps = track.getCapabilities?.() || {};
  const btn = $('torchBtn');
  btn.hidden = !caps.torch;
  btn.onclick = async () => {
    const on = btn.getAttribute('aria-pressed') !== 'true';
    try { await track.applyConstraints({ advanced: [{ torch: on }] }); btn.setAttribute('aria-pressed', String(on)); } catch { /* ignore */ }
  };
}

async function setupBarcode() {
  if (barcodeDetector || zxingReader) { $('barcodeHint').hidden = !stream; return; }
  try {
    if ('BarcodeDetector' in window) {
      const formats = await window.BarcodeDetector.getSupportedFormats();
      if (formats.length) barcodeDetector = new window.BarcodeDetector({ formats });
    }
  } catch { barcodeDetector = null; }
  if (!barcodeDetector && window.ZXingBrowser) zxingReader = new window.ZXingBrowser.BrowserMultiFormatReader();
  $('barcodeHint').hidden = !stream || !(barcodeDetector || zxingReader);
}

/** Try to read a barcode/QR code from a canvas. Returns the text or null. */
async function decodeBarcode(canvas) {
  try {
    if (barcodeDetector) {
      const codes = await barcodeDetector.detect(canvas);
      return codes[0]?.rawValue || null;
    }
    if (zxingReader) return zxingReader.decodeFromCanvas(canvas).getText();
  } catch { /* nothing found */ }
  return null;
}

async function scanBarcodeFrame() {
  if (barcodeBusy || ocrBusy || !video.videoWidth || !(barcodeDetector || zxingReader)) return;
  barcodeBusy = true;
  try {
    const scale = Math.min(1, 1280 / video.videoWidth);
    frame.width = Math.round(video.videoWidth * scale);
    frame.height = Math.round(video.videoHeight * scale);
    frame.getContext('2d', { willReadFrequently: true }).drawImage(video, 0, 0, frame.width, frame.height);
    const text = await decodeBarcode(frame);
    if (text) handleBarcode(text);
  } finally {
    barcodeBusy = false;
  }
}

function handleBarcode(text) {
  const key = normalize(text);
  if (!key) return;
  const now = Date.now();
  if (key === lastAuto.key && now - lastAuto.at < 4000) return; // same code still in view
  lastAuto = { key, at: now };
  flash();
  $('candidates').hidden = true;
  runCheck(key, 'barcode');
}

function flash() {
  $('camera').classList.add('flash');
  setTimeout(() => $('camera').classList.remove('flash'), 400);
}

/** The part of the video frame that is inside the guide box, in video pixel coordinates. */
function guideCropRect() {
  const vw = video.videoWidth, vh = video.videoHeight;
  const vr = video.getBoundingClientRect();
  const gr = $('guide').getBoundingClientRect();
  const scale = Math.max(vr.width / vw, vr.height / vh); // object-fit: cover
  const offX = (vr.width - vw * scale) / 2;
  const offY = (vr.height - vh * scale) / 2;
  const pad = 0.04; // a little margin around the box
  let x = (gr.left - vr.left - offX) / scale;
  let y = (gr.top - vr.top - offY) / scale;
  let w = gr.width / scale;
  let h = gr.height / scale;
  x -= w * pad; y -= h * pad * 2; w *= 1 + pad * 2; h *= 1 + pad * 4;
  x = Math.max(0, x); y = Math.max(0, y);
  return { x, y, w: Math.min(w, vw - x), h: Math.min(h, vh - y) };
}

$('ocrBtn').addEventListener('click', async () => {
  if (!video.videoWidth || ocrBusy) return;
  const r = guideCropRect();
  const c = document.createElement('canvas');
  c.width = Math.round(r.w); c.height = Math.round(r.h);
  c.getContext('2d').drawImage(video, r.x, r.y, r.w, r.h, 0, 0, c.width, c.height);
  flash();
  await ocrAndCheck(c, 'camera');
});

$('photoInput').addEventListener('change', async (e) => {
  const file = e.target.files[0];
  e.target.value = '';
  if (!file) return;
  const bmp = await createImageBitmap(file, { imageOrientation: 'from-image' }).catch(() => null);
  if (!bmp) { alert('Could not read that image.'); return; }
  const scale = Math.min(1, 2000 / Math.max(bmp.width, bmp.height));
  const c = document.createElement('canvas');
  c.width = Math.round(bmp.width * scale); c.height = Math.round(bmp.height * scale);
  c.getContext('2d').drawImage(bmp, 0, 0, c.width, c.height);
  await setupBarcode();
  const code = await decodeBarcode(c);
  if (code) { runCheck(code, 'photo barcode'); return; }
  await ocrAndCheck(c, 'photo');
});

// ---------- OCR ----------
let workerPromise = null;
function getWorker() {
  if (!window.Tesseract) return Promise.reject(new Error('Text recognition failed to load.'));
  workerPromise ??= (async () => {
    const abs = (p) => new URL(p, location.href).href;
    const worker = await window.Tesseract.createWorker('eng', 1, {
      workerPath: abs('vendor/worker.min.js'),
      corePath: abs('vendor/core'),
      langPath: abs('vendor/lang'),
      gzip: true,
    });
    await worker.setParameters({
      tessedit_char_whitelist: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-/ ',
      tessedit_pageseg_mode: '6',
      preserve_interword_spaces: '1',
    });
    return worker;
  })().catch((err) => { workerPromise = null; throw err; });
  return workerPromise;
}

/** Grayscale + contrast stretch, upscaled so text is ~tall enough for Tesseract. Optionally inverted. */
function preprocess(src, invert) {
  const targetH = Math.max(src.height, 160);
  const scale = Math.min(3, targetH / src.height);
  const c = document.createElement('canvas');
  c.width = Math.round(src.width * scale); c.height = Math.round(src.height * scale);
  const ctx = c.getContext('2d', { willReadFrequently: true });
  ctx.imageSmoothingQuality = 'high';
  ctx.drawImage(src, 0, 0, c.width, c.height);
  const img = ctx.getImageData(0, 0, c.width, c.height);
  const d = img.data;
  let min = 255, max = 0;
  const gray = new Uint8ClampedArray(d.length / 4);
  for (let i = 0, j = 0; i < d.length; i += 4, j++) {
    const g = 0.299 * d[i] + 0.587 * d[i + 1] + 0.114 * d[i + 2];
    gray[j] = g;
    if (g < min) min = g;
    if (g > max) max = g;
  }
  const range = Math.max(1, max - min);
  for (let i = 0, j = 0; i < d.length; i += 4, j++) {
    let v = ((gray[j] - min) / range) * 255;
    if (invert) v = 255 - v;
    d[i] = d[i + 1] = d[i + 2] = v;
  }
  ctx.putImageData(img, 0, 0);
  return c;
}

async function ocrAndCheck(canvas, source) {
  ocrBusy = true;
  $('ocrBtn').disabled = true;
  camStatus('Reading text…');
  try {
    const worker = await getWorker();
    let candidates = [];
    let raw = '';
    // Serials can be dark-on-light or light-on-dark; try both.
    for (const invert of [false, true]) {
      const { data } = await worker.recognize(preprocess(canvas, invert));
      raw += `\n${data.text}`;
      candidates = extractCandidates(raw, index);
      if (index && candidates.some((c) => check(index, c).status === 'found')) break;
    }
    camStatus('');
    showCandidates(candidates, source);
  } catch (err) {
    camStatus('');
    alert(err.message || 'Text recognition failed.');
  } finally {
    ocrBusy = false;
    $('ocrBtn').disabled = false;
  }
}

function showCandidates(candidates, source) {
  const box = $('candidates');
  const chips = $('candidateChips');
  chips.innerHTML = '';
  if (!candidates.length) {
    box.hidden = false;
    chips.append(para('No serial number recognised. Move closer, hold steady, turn on the light – or type it in below.'));
    return;
  }
  for (const c of candidates) {
    const b = document.createElement('button');
    const st = index ? check(index, c).status : '';
    b.className = `chip ${st}`;
    b.textContent = c;
    b.addEventListener('click', () => runCheck(c, `${source} text`));
    chips.append(b);
  }
  box.hidden = candidates.length < 2;
  runCheck(candidates[0], `${source} text`);
}

// ---------- init ----------
renderBadge();
if (!index) showTab('list');

if ('serviceWorker' in navigator && location.protocol === 'https:') {
  navigator.serviceWorker.register('sw.js').catch(() => { /* offline support is optional */ });
}
