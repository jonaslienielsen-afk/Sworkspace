import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import {
  estimateSnowTemp, conditionClass, weight, rankProducts, similarTests, productStats, bestPerProduct,
} from '../src/glide/model.js';

const { tests, snowTypes } = JSON.parse(readFileSync(new URL('../src/glide/data.json', import.meta.url)));

test('data has all tests with podiums', () => {
  assert.ok(tests.length >= 29);
  for (const t of tests) {
    assert.ok(t.podium.length >= 3, t.id);
    assert.equal(typeof t.snow, 'number');
    assert.equal(typeof t.hum, 'number');
  }
});

test('estimateSnowTemp never goes above 0', () => {
  assert.equal(estimateSnowTemp(8), 0);
  assert.equal(estimateSnowTemp(-5), -6);
});

test('conditionClass matches the Python rule', () => {
  assert.equal(conditionClass(0, 70), 'C');
  assert.equal(conditionClass(-6, 30), 'A');
  assert.equal(conditionClass(-4, 22), 'A');
  assert.equal(conditionClass(-1, 22), 'B');
  for (const t of tests) assert.equal(conditionClass(t.snow, t.hum), t.cls[0], t.id);
});

test('weight is 1 for identical conditions and falls off with distance', () => {
  const t = tests[0];
  assert.equal(weight(t, { snow: t.snow, hum: t.hum }), 1);
  assert.ok(weight(t, { snow: t.snow - 2, hum: t.hum }) < 0.61);
  assert.equal(weight(t, { snow: t.snow, hum: null }), 1);
});

test('ties share points and combinations credit every product', () => {
  const t = tests.find((x) => x.id === '2024-01-25');
  const best = bestPerProduct(t);
  assert.equal(best.get('Toko HP Yellow').points, 3);
  assert.equal(best.get('Vauhti LDR New Snow liquid').points, 3);
  const c = tests.find((x) => x.id === '2026-02-19');
  const b2 = bestPerProduct(c);
  assert.equal(b2.get('Skigo Booster Cold').points, 3);
  assert.equal(b2.get('Vola NSD2319').points, 3);
});

test('same ranking as glide/predict.py (snow -3 C, humidity 35%)', () => {
  const r = rankProducts(tests, { snow: -3, hum: 35 });
  assert.equal(r[0].product, 'Skigo LDQ');
  assert.ok(Math.abs(r[0].score - 0.77) < 0.01, String(r[0].score));
  assert.equal(r[1].product, 'HWK UHX Red');
  assert.ok(r[0].how && r[0].how.entry.apply);
});

test('cold dry and wet days pick different products', () => {
  assert.equal(rankProducts(tests, { snow: -8, hum: 25 })[0].product, 'Toko HP Blue');
  const wet = rankProducts(tests, { snow: 0, hum: 85 }).slice(0, 3).map((r) => r.product);
  assert.ok(wet.includes('Toko Prototype liquid') || wet.includes('Skigo FFR Yellow'), wet.join());
});

test('similarTests sorts by weight', () => {
  const s = similarTests(tests, { snow: -10, hum: 30 }, 3);
  assert.equal(s.length, 3);
  assert.ok(s[0].weight >= s[1].weight && s[1].weight >= s[2].weight);
});

test('productStats totals', () => {
  const s = productStats(tests);
  const ldq = s.find((r) => r.product === 'Skigo LDQ');
  assert.equal(ldq.wins, 4);
  assert.equal(s[0].product, 'Skigo LDQ');
});

test('every test has a snow type and the similarity table is complete', () => {
  for (const t of tests) assert.ok(snowTypes.order.includes(t.snowCat), t.id);
  for (const a of snowTypes.order) {
    for (const b of snowTypes.order) assert.equal(typeof snowTypes.sim[a][b], 'number');
    assert.equal(snowTypes.sim[a][a], 1);
  }
});

test('snow type changes the pick: Skigo LDQ drops on new snow, leads on transformed', () => {
  const base = { snow: -3, hum: 30 };
  const onNew = rankProducts(tests, { ...base, typeSim: snowTypes.sim.new }).slice(0, 5).map((r) => r.product);
  assert.ok(!onNew.includes('Skigo LDQ'), onNew.join());
  const onOld = rankProducts(tests, { ...base, typeSim: snowTypes.sim.transformed });
  assert.equal(onOld[0].product, 'Skigo LDQ');
});

test('productStats splits points by snow type', () => {
  const ldq = productStats(tests).find((r) => r.product === 'Skigo LDQ');
  assert.deepEqual(ldq.byType.new, { tests: 1, points: 0 });
  assert.equal(ldq.byType.transformed.points, 13);
});
