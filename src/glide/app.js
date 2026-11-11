import {
  estimateSnowTemp, rankProducts, similarTests, evidenceLabel, productStats,
} from './model.js';

const $ = (id) => document.getElementById(id);
const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const fmtT = (v) => `${v > 0 ? '+' : ''}${v} °C`;
const place = (p) => ['', '1st', '2nd', '3rd'][p] || `${p}th`;
const fmtDate = (d) => new Date(`${d}T12:00:00`).toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' });

let TESTS = [];
let SNOW = { order: [], labels: {}, sim: {} };
const state = { mode: 'snow', snow: -3, air: -2, hum: 35, humUnknown: false, snowType: '' };
const STORE = 'glide-picker-v1';

function load() {
  try { Object.assign(state, JSON.parse(localStorage.getItem(STORE) || '{}')); } catch { /* storage unavailable */ }
}
function save() {
  try { localStorage.setItem(STORE, JSON.stringify(state)); } catch { /* storage unavailable */ }
}

function conditions() {
  const snow = state.mode === 'snow' ? state.snow : estimateSnowTemp(state.air);
  return {
    snow,
    hum: state.humUnknown ? null : state.hum,
    typeSim: state.snowType ? SNOW.sim[state.snowType] : null,
  };
}

// ---------------------------------------------------------------- inputs
function syncInputs() {
  const isSnow = state.mode === 'snow';
  $('modeSnow').classList.toggle('on', isSnow);
  $('modeAir').classList.toggle('on', !isSnow);
  $('modeSnow').setAttribute('aria-checked', isSnow);
  $('modeAir').setAttribute('aria-checked', !isSnow);
  const temp = $('temp');
  temp.min = isSnow ? -15 : -20;
  temp.max = isSnow ? 0 : 12;
  temp.value = isSnow ? state.snow : state.air;
  $('tempLabel').textContent = isSnow ? 'Snow temperature' : 'Air temperature';
  $('tempOut').textContent = fmtT(Number(temp.value));
  const hint = $('tempHint');
  hint.hidden = isSnow;
  if (!isSnow) hint.textContent = `Estimated snow temperature: ${fmtT(estimateSnowTemp(state.air))}`;

  $('hum').value = state.hum;
  $('hum').disabled = state.humUnknown;
  $('humOut').textContent = state.humUnknown ? 'unknown' : `${state.hum} %`;
  $('humUnknown').checked = state.humUnknown;
  for (const b of $('humChips').children) b.classList.toggle('on', !state.humUnknown && Number(b.dataset.hum) === state.hum);
  $('humChips').classList.toggle('disabled', state.humUnknown);

  $('typeOut').textContent = state.snowType ? SNOW.labels[state.snowType] : 'Not sure';
  for (const b of $('typeChips').children) b.classList.toggle('on', b.dataset.type === state.snowType);
}

function setTemp(v) {
  const t = $('temp');
  v = Math.min(Number(t.max), Math.max(Number(t.min), Math.round(v * 2) / 2));
  if (state.mode === 'snow') state.snow = v; else state.air = v;
  update();
}
function setHum(v) {
  state.hum = Math.min(100, Math.max(10, Math.round(v)));
  state.humUnknown = false;
  update();
}

function bindInputs() {
  $('modeSnow').onclick = () => { state.mode = 'snow'; update(); };
  $('modeAir').onclick = () => { state.mode = 'air'; update(); };
  $('temp').oninput = (e) => setTemp(Number(e.target.value));
  $('hum').oninput = (e) => setHum(Number(e.target.value));
  $('humUnknown').onchange = (e) => { state.humUnknown = e.target.checked; update(); };
  for (const b of document.querySelectorAll('.step')) {
    b.onclick = () => {
      const step = Number(b.dataset.step);
      if (b.dataset.target === 'temp') setTemp(Number($('temp').value) + step);
      else setHum((state.humUnknown ? 35 : state.hum) + step);
    };
  }
  for (const b of $('humChips').children) b.onclick = () => setHum(Number(b.dataset.hum));
  $('typeChips').innerHTML = [['', 'Not sure'], ...SNOW.order.map((k) => [k, SNOW.labels[k]])]
    .map(([k, label]) => `<button data-type="${k}">${esc(label)}</button>`).join('');
  for (const b of $('typeChips').children) b.onclick = () => { state.snowType = b.dataset.type; update(); };
}

// ---------------------------------------------------------------- pick tab
function testConditions(t) {
  const hum = t.humMin === t.humMax ? `${t.humMin} %` : `${t.humMin}–${t.humMax} %`;
  return `Snow ${fmtT(t.snow)}${t.snowEst ? ' (est.)' : ''} · air ${fmtT(t.air)} · humidity ${hum}`;
}

function podiumHtml(t) {
  return `<ol class="podium">${t.podium.map((e) => `
    <li><span class="medal m${e.place}">${e.place}</span>
      <div><strong>${esc(e.name)}</strong>
        <div class="muted small">${esc(e.type)} · ${esc(e.apply)} · ${esc(e.remove)}</div></div></li>`).join('')}
  </ol>`;
}

function testCard(t, extra = '') {
  const others = t.others.map((o) => esc(o.name)).join(', ');
  return `<details class="card test">
    <summary>
      <div class="test-head">
        <div><strong>${fmtDate(t.date)}</strong> <span class="pill small st-${t.snowCat}">${esc(SNOW.labels[t.snowCat])}</span>${extra}</div>
        <div class="muted small">${esc(testConditions(t))}</div>
        <div class="muted small">${esc(t.snowType)}${t.weather ? ` · ${esc(t.weather)}` : ''}</div>
        <div class="winner">🥇 ${esc(t.podium.filter((e) => e.place === 1).map((e) => e.name).join(' = '))}</div>
      </div>
    </summary>
    <div class="test-body">
      <div class="muted small">${esc(t.title)} — ${esc(t.kind)}</div>
      ${podiumHtml(t)}
      ${others ? `<p class="small"><strong>Also tested:</strong> ${others}</p>` : ''}
      ${t.bestFeel ? `<p class="small"><strong>Best feel:</strong> ${esc(t.bestFeel)}</p>` : ''}
      ${t.distance ? `<p class="small"><strong>Distance:</strong> ${esc(t.distance)}</p>` : ''}
      <p class="small">${esc(t.notes)}</p>
    </div>
  </details>`;
}

// The product's own record on the chosen snow type, e.g. "New snow: 0 pts in 1 test".
function typeRecord(product) {
  if (!state.snowType) return '';
  const b = STATS_BY_PRODUCT.get(product)?.byType[state.snowType];
  const label = { new: 'New snow', fine: 'Fine-grained', new_over_old: 'New on old', transformed: 'Transformed', wet: 'Wet' }[state.snowType];
  if (!b) return `<span class="tag">${esc(label)}: not tested</span>`;
  const cls = b.points === 0 ? 'ev-thin' : 'ev-strong';
  const icon = b.points === 0 ? '⚠ ' : '';
  return `<span class="tag ${cls}">${icon}${esc(label)}: ${b.points} pts in ${b.tests} test${b.tests === 1 ? '' : 's'}</span>`;
}

function renderResults(cond) {
  const ranked = rankProducts(TESTS, cond).filter((r) => r.score > 0).slice(0, 8);
  const max = Math.max(ranked[0]?.score || 1, 0.01);
  $('results').innerHTML = ranked.map((r, i) => {
    const ev = evidenceLabel(r.evidence);
    const how = r.how;
    const howHtml = how ? `
      <div class="how">
        <div class="small"><strong>How Bull applied it</strong> — ${place(how.entry.place)} on ${fmtDate(how.test.date)}
          (snow ${fmtT(how.test.snow)}, ${how.test.hum.toFixed(0)} %, ${esc(SNOW.labels[how.test.snowCat].toLowerCase())})${how.entry.name !== r.product ? ` as part of <em>${esc(how.entry.name)}</em>` : ''}</div>
        <div class="small">On: ${esc(how.entry.apply)}</div>
        <div class="small">Off: ${esc(how.entry.remove)}</div>
        ${how.test.bestFeel && how.test.bestFeel.includes(r.product) ? '<div class="small">⭐ Best feel that day</div>' : ''}
      </div>` : '';
    const wins = r.wins.length ? `Won ${r.wins.length}× (${r.wins.map(fmtDate).join(', ')})` : 'No wins yet';
    return `<li class="card result">
      <details>
        <summary>
          <span class="rank">${i + 1}</span>
          <div class="result-main">
            <div class="result-name">${esc(r.product)}</div>
            <div class="bar"><span style="width:${Math.max(4, (r.score / max) * 100).toFixed(0)}%"></span></div>
            <div class="tags">
              <span class="tag">Score ${r.score.toFixed(2)}</span>
              <span class="tag">Podium ${(r.podiumRate * 100).toFixed(0)} %</span>
              <span class="tag ev-${ev}">Evidence: ${ev}</span>
              ${typeRecord(r.product)}
            </div>
          </div>
        </summary>
        <div class="result-body">
          ${howHtml}
          <div class="small muted">${wins} · in ${r.tests} test${r.tests === 1 ? '' : 's'} overall</div>
        </div>
      </details>
    </li>`;
  }).join('') || '<li class="muted">No data.</li>';
}

function renderSimilar(cond) {
  $('similar').innerHTML = similarTests(TESTS, cond, 5)
    .map(({ test, weight }) => testCard(test, ` <span class="pill small">${(weight * 100).toFixed(0)} % match</span>`))
    .join('');
}

function update() {
  syncInputs();
  const cond = conditions();
  renderResults(cond);
  renderSimilar(cond);
  save();
}

// ---------------------------------------------------------------- tests tab
let typeFilter = '';
function renderTests() {
  const q = $('testSearch').value.trim().toLowerCase();
  const list = [...TESTS].reverse().filter((t) => {
    if (typeFilter && t.snowCat !== typeFilter) return false;
    if (!q) return true;
    const hay = [t.date, t.title, t.snowType, SNOW.labels[t.snowCat], t.weather, t.notes, t.bestFeel, t.distance,
      ...t.podium.map((e) => e.name), ...t.others.map((o) => o.name)].join(' ').toLowerCase();
    return hay.includes(q);
  });
  $('testCount').textContent = `${list.length} of ${TESTS.length} tests`;
  $('testList').innerHTML = list.map((t) => testCard(t)).join('');
}

// ---------------------------------------------------------------- products tab
let STATS = [];
let STATS_BY_PRODUCT = new Map();
let sortKey = 'points';
let sortDir = -1;
function renderProducts() {
  const q = $('prodSearch').value.trim().toLowerCase();
  const podiumOnly = $('prodPodiumOnly').checked;
  const rows = STATS
    .filter((r) => (!podiumOnly || r.points > 0) && (!q || r.product.toLowerCase().includes(q)))
    .sort((a, b) => {
      const x = a[sortKey]; const y = b[sortKey];
      const c = typeof x === 'string' ? x.localeCompare(y) : x - y;
      return c * sortDir || b.points - a.points;
    });
  $('prodTable').querySelector('tbody').innerHTML = rows.map((r) => `<tr>
    <td class="left">${esc(r.product)}</td><td>${r.tests}</td><td>${r.wins || ''}</td><td>${r.second || ''}</td>
    <td>${r.third || ''}</td><td><strong>${r.points}</strong></td><td>${r.perTest.toFixed(2)}</td>
    ${SNOW.order.map((k) => {
      const b = r.byType[k];
      return `<td>${b ? `${b.points} <span class="muted">(${b.tests})</span>` : ''}</td>`;
    }).join('')}</tr>`).join('');
  for (const th of $('prodTable').querySelectorAll('th')) {
    th.classList.toggle('sorted', th.dataset.sort === sortKey);
    th.dataset.dir = th.dataset.sort === sortKey ? (sortDir > 0 ? '▲' : '▼') : '';
  }
}

// ---------------------------------------------------------------- tabs + init
function showTab(name) {
  for (const b of document.querySelectorAll('.tabbar button')) {
    const on = b.dataset.tab === name;
    b.classList.toggle('active', on);
    b.setAttribute('aria-selected', on);
  }
  for (const s of document.querySelectorAll('.tab')) {
    const on = s.id === `tab-${name}`;
    s.hidden = !on;
    s.classList.toggle('active', on);
  }
  window.scrollTo(0, 0);
}

async function init() {
  load();
  const res = await fetch('data.json');
  const data = await res.json();
  TESTS = data.tests;
  SNOW = data.snowTypes;
  STATS = productStats(TESTS).map((r) => {
    for (const k of SNOW.order) r[`t_${k}`] = r.byType[k]?.points ?? -1;
    return r;
  });
  STATS_BY_PRODUCT = new Map(STATS.map((r) => [r.product, r]));
  const first = TESTS[0].date.slice(0, 7);
  const last = TESTS[TESTS.length - 1].date.slice(0, 7);
  $('dataBadge').textContent = `${TESTS.length} tests`;
  $('dataBadge').title = `${first} – ${last}`;
  $('aboutData').insertAdjacentHTML('beforeend', ` Currently ${TESTS.length} tests from ${fmtDate(TESTS[0].date)} to ${fmtDate(TESTS[TESTS.length - 1].date)}.`);

  bindInputs();
  for (const b of document.querySelectorAll('.tabbar button')) b.onclick = () => showTab(b.dataset.tab);
  $('testSearch').oninput = renderTests;
  $('typeFilter').innerHTML = [['', 'All'], ...SNOW.order.map((k) => [k, SNOW.labels[k]])]
    .map(([k, label]) => `<button data-type="${k}"${k ? '' : ' class="on"'}>${esc(label)}</button>`).join('');
  for (const b of $('typeFilter').children) {
    b.onclick = () => {
      typeFilter = b.dataset.type;
      for (const x of $('typeFilter').children) x.classList.toggle('on', x === b);
      renderTests();
    };
  }
  $('prodSearch').oninput = renderProducts;
  $('prodPodiumOnly').onchange = renderProducts;
  for (const th of $('prodTable').querySelectorAll('th')) {
    th.onclick = () => {
      if (sortKey === th.dataset.sort) sortDir = -sortDir;
      else { sortKey = th.dataset.sort; sortDir = th.dataset.sort === 'product' ? 1 : -1; }
      renderProducts();
    };
  }
  update();
  renderTests();
  renderProducts();
}

init().catch((e) => {
  $('dataBadge').textContent = 'Error';
  $('results').innerHTML = `<li class="card">Could not load the test data: ${esc(e.message)}</li>`;
});
