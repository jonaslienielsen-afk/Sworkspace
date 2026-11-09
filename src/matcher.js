// Pure logic for parsing serial-number lists and matching scanned values.
// No DOM access, so it can be unit-tested in Node.

/** Uppercase and strip everything except letters and digits. */
export function normalize(value) {
  return String(value ?? '')
    .toUpperCase()
    .replace(/[^A-Z0-9]/g, '');
}

// Characters OCR commonly mixes up, folded to one representative.
const CONFUSABLE = { O: '0', Q: '0', D: '0', I: '1', L: '1', Z: '2', S: '5', B: '8', G: '6' };

/** A looser key where look-alike characters (O/0, I/1, S/5, ...) are treated as equal. */
export function confusableKey(value) {
  return normalize(value).replace(/[OQDILZSBG]/g, (c) => CONFUSABLE[c]);
}

/** Split one CSV/TSV line, honouring double-quoted fields. */
function splitLine(line, delimiter) {
  const out = [];
  let cur = '';
  let quoted = false;
  for (let i = 0; i < line.length; i++) {
    const ch = line[i];
    if (quoted) {
      if (ch === '"' && line[i + 1] === '"') { cur += '"'; i++; }
      else if (ch === '"') quoted = false;
      else cur += ch;
    } else if (ch === '"') quoted = true;
    else if (ch === delimiter) { out.push(cur.trim()); cur = ''; }
    else cur += ch;
  }
  out.push(cur.trim());
  return out;
}

function detectDelimiter(lines) {
  const sample = lines.slice(0, 20).join('\n');
  const counts = { '\t': 0, ';': 0, ',': 0 };
  for (const d of Object.keys(counts)) counts[d] = sample.split(d).length - 1;
  const best = Object.entries(counts).sort((a, b) => b[1] - a[1])[0];
  return best[1] > 0 ? best[0] : null;
}

const SERIAL_HEADER = /(serial|serie|s\/?n\b|^sn$|nummer|number|^nr\.?$|^no\.?$|^id$)/i;

/**
 * Parse pasted text or a CSV/TSV/TXT file into rows.
 * Returns { columns, rows, serialCol, hasHeader }.
 * - Single-column input: every non-empty line is a serial number.
 * - Multi-column input: a header row is detected if it names a serial column.
 */
export function parseList(text) {
  const lines = String(text ?? '')
    .replace(/^﻿/, '')
    .split(/\r?\n/)
    .filter((l) => l.trim() !== '');
  if (lines.length === 0) return { columns: ['Serial'], rows: [], serialCol: 0, hasHeader: false };

  const delimiter = detectDelimiter(lines);
  let table = delimiter ? lines.map((l) => splitLine(l, delimiter)) : lines.map((l) => [l.trim()]);
  const width = Math.max(...table.map((r) => r.length));
  table = table.map((r) => (r.length < width ? [...r, ...Array(width - r.length).fill('')] : r));

  const first = table[0];
  let serialCol = first.findIndex((c) => SERIAL_HEADER.test(c));
  // A header is a first row that names a serial column, or (multi-column) contains no digits at all.
  const hasHeader = serialCol >= 0 || (width > 1 && first.every((c) => !/\d/.test(c)));
  const columns = hasHeader ? first.map((c, i) => c || `Column ${i + 1}`) : first.map((_, i) => (width === 1 ? 'Serial' : `Column ${i + 1}`));
  const rows = hasHeader ? table.slice(1) : table;

  if (serialCol < 0) serialCol = guessSerialColumn(rows, width);
  return { columns, rows, serialCol, hasHeader };
}

/** Pick the column whose values look most like serial numbers (contain digits, mostly unique). */
function guessSerialColumn(rows, width) {
  let best = 0;
  let bestScore = -1;
  for (let c = 0; c < width; c++) {
    const vals = rows.map((r) => normalize(r[c])).filter(Boolean);
    if (!vals.length) continue;
    const withDigits = vals.filter((v) => /\d/.test(v) && v.length >= 4).length / vals.length;
    const unique = new Set(vals).size / vals.length;
    const score = withDigits * 2 + unique;
    if (score > bestScore) { bestScore = score; best = c; }
  }
  return best;
}

/** Build lookup maps from rows. */
export function buildIndex(rows, serialCol) {
  const exact = new Map();
  const loose = new Map();
  for (const row of rows) {
    const key = normalize(row[serialCol]);
    if (!key) continue;
    if (!exact.has(key)) exact.set(key, []);
    exact.get(key).push(row);
    const lk = confusableKey(key);
    if (!loose.has(lk)) loose.set(lk, []);
    loose.get(lk).push(row);
  }
  return { exact, loose, serialCol, size: exact.size };
}

/** Levenshtein distance, bailing out early once it exceeds `max`. */
export function editDistance(a, b, max = Infinity) {
  if (Math.abs(a.length - b.length) > max) return max + 1;
  let prev = Array.from({ length: b.length + 1 }, (_, i) => i);
  for (let i = 1; i <= a.length; i++) {
    const cur = [i];
    let rowMin = i;
    for (let j = 1; j <= b.length; j++) {
      cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
      rowMin = Math.min(rowMin, cur[j]);
    }
    if (rowMin > max) return max + 1;
    prev = cur;
  }
  return prev[b.length];
}

/**
 * Check a scanned/typed value against the index.
 * status: 'found'    – exact match (ignoring case, spaces and dashes)
 *         'possible' – matches only when look-alike characters are treated as equal,
 *                      or is one character away from a listed serial
 *         'not_found'
 */
export function check(index, input) {
  const key = normalize(input);
  if (!key) return { status: 'empty', key, matches: [] };
  if (index.exact.has(key)) return { status: 'found', key, matches: index.exact.get(key) };

  const loose = index.loose.get(confusableKey(key));
  if (loose) return { status: 'possible', key, reason: 'look-alike characters', matches: loose };

  if (key.length >= 5 && index.size <= 200000) {
    const near = [];
    for (const [k, rows] of index.exact) {
      if (editDistance(key, k, 1) <= 1) near.push(...rows);
      if (near.length >= 5) break;
    }
    if (near.length) return { status: 'possible', key, reason: 'one character differs', matches: near };
  }
  return { status: 'not_found', key, matches: [] };
}

/**
 * Turn raw OCR text into likely serial-number candidates, best first.
 * Candidates are alphanumeric tokens of 4+ characters that contain at least one digit;
 * runs of adjacent tokens are also joined, since serials are often printed with spaces.
 */
export function extractCandidates(text, index = null) {
  const lines = String(text ?? '').toUpperCase().split(/\n+/);
  const seen = new Set();
  const out = [];
  const add = (v) => {
    const n = normalize(v);
    if (n.length >= 4 && /\d/.test(n) && !seen.has(n)) { seen.add(n); out.push(n); }
  };
  for (const line of lines) {
    const tokens = line.split(/[^A-Z0-9-]+/).filter(Boolean);
    // Every run of up to 4 adjacent tokens ("20 123 456" -> "20123456").
    for (let i = 0; i < tokens.length; i++) {
      for (let j = i + 1; j <= Math.min(tokens.length, i + 4); j++) add(tokens.slice(i, j).join(''));
    }
  }
  const rank = (c) => {
    let s = 0;
    if (index) {
      const r = check(index, c).status;
      s += r === 'found' ? 1000 : r === 'possible' ? 500 : 0;
    }
    s += (c.replace(/\D/g, '').length / c.length) * 10; // mostly digits
    s += Math.min(c.length, 14);
    return s;
  };
  return out.sort((a, b) => rank(b) - rank(a)).slice(0, 8);
}
