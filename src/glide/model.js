// Glide Picker model: similarity-weighted placing points (same as glide/predict.py).
//
// Each past test gets a weight from how close its snow temperature and snow
// humidity are to the day you are waxing for:
//   d = sqrt(((snow - snow_i) / SNOW_SCALE)^2 + ((hum - hum_i) / HUM_SCALE)^2)
//   w = exp(-d^2 / 2)
// A product scores 3/2/1 points for 1st/2nd/3rd (ties share the place) and 0
// when tested off the podium; a combination gives its points to every product
// in it. Score = sum(w * points) / sum(w over all tests), i.e. expected placing
// points on a day like this (0-3).
// If a snow type is chosen, w is also multiplied by how alike the snow types are
// (cond.typeSim: a row of the similarity table in data.json, e.g. new vs wet 0.1).

export const SNOW_SCALE = 2;   // degrees C
export const HUM_SCALE = 30;   // snow-humidity percentage points

/** Snow can't be warmer than 0 C; in the tests it was ~1 C colder than the air when below 0. */
export function estimateSnowTemp(air) {
  return Math.min(0, Math.round((air - 1) * 2) / 2);
}

/** Condition class, same rule as glide_data.condition_class. hum may be null (unknown). */
export function conditionClass(snow, hum) {
  if (hum != null && hum >= 55) return 'C';
  if (snow <= -4.5 || (hum != null && hum < 25 && snow <= -3)) return 'A';
  return 'B';
}

export const CLASS_LABELS = {
  A: 'Cold / dry',
  B: 'Medium / transformed',
  C: 'Wet',
};

/**
 * Similarity weight of test t for conditions {snow, hum, typeSim}.
 * hum null ignores humidity; typeSim null (snow type unknown) ignores snow type.
 */
export function weight(t, { snow, hum, typeSim = null }) {
  const ds = (snow - t.snow) / SNOW_SCALE;
  const dh = hum == null ? 0 : (hum - t.hum) / HUM_SCALE;
  const type = typeSim ? (typeSim[t.snowCat] ?? 1) : 1;
  return Math.exp(-(ds * ds + dh * dh) / 2) * type;
}

/** Each product's best result in test t: Map(product -> {points, entry}). */
export function bestPerProduct(t) {
  const best = new Map();
  const consider = (entry, points) => {
    for (const p of entry.products) {
      const cur = best.get(p);
      if (!cur || points > cur.points) best.set(p, { points, entry });
    }
  };
  for (const e of t.podium) consider(e, e.points);
  for (const e of t.others) consider(e, 0);
  return best;
}

/**
 * Rank products for the given conditions.
 * Returns [{product, score, podiumRate, evidence, tests, wins, how}] sorted by score.
 * `how` is the podium entry (with its test and weight) that contributed most,
 * which tells how Bull applied the product in the most similar good result.
 */
export function rankProducts(tests, cond) {
  const rows = new Map();
  let total = 0;
  for (const t of tests) {
    const w = weight(t, cond);
    total += w;
    for (const [product, { points, entry }] of bestPerProduct(t)) {
      let r = rows.get(product);
      if (!r) {
        r = { product, sum: 0, testedW: 0, podiumW: 0, tests: 0, wins: [], how: null, howW: -1 };
        rows.set(product, r);
      }
      r.sum += w * points;
      r.testedW += w;
      r.tests += 1;
      if (points > 0) {
        r.podiumW += w;
        if (w * points > r.howW) { r.howW = w * points; r.how = { test: t, entry, weight: w }; }
      }
      if (points === 3) r.wins.push(t.date);
    }
  }
  return [...rows.values()]
    .map((r) => ({
      product: r.product,
      score: total ? r.sum / total : 0,
      podiumRate: r.testedW ? r.podiumW / r.testedW : 0,
      evidence: r.testedW,
      tests: r.tests,
      wins: r.wins,
      how: r.how,
    }))
    .sort((a, b) => b.score - a.score || b.podiumRate - a.podiumRate || a.product.localeCompare(b.product));
}

/** Most similar tests, with their weights. */
export function similarTests(tests, cond, n = 5) {
  return tests
    .map((t) => ({ test: t, weight: weight(t, cond) }))
    .sort((a, b) => b.weight - a.weight)
    .slice(0, n);
}

/** Evidence label for a product's summed similarity weight. */
export function evidenceLabel(e) {
  if (e >= 3) return 'strong';
  if (e >= 1.5) return 'some';
  return 'thin';
}

/** All-condition product statistics (per product, combinations split). */
export function productStats(tests) {
  const rows = new Map();
  for (const t of tests) {
    for (const [product, { points }] of bestPerProduct(t)) {
      let r = rows.get(product);
      if (!r) {
        r = { product, tests: 0, wins: 0, second: 0, third: 0, points: 0, A: 0, B: 0, C: 0, byType: {} };
        rows.set(product, r);
      }
      r.tests += 1;
      r.points += points;
      r[t.cls[0]] += points;
      const bt = (r.byType[t.snowCat] ??= { tests: 0, points: 0 });
      bt.tests += 1;
      bt.points += points;
      if (points === 3) r.wins += 1;
      else if (points === 2) r.second += 1;
      else if (points === 1) r.third += 1;
    }
  }
  return [...rows.values()]
    .map((r) => ({ ...r, perTest: r.points / r.tests, podiumRate: (r.wins + r.second + r.third) / r.tests }))
    .sort((a, b) => b.points - a.points || b.perTest - a.perTest || a.product.localeCompare(b.product));
}
