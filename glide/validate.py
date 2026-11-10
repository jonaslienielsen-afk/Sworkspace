"""Leave-one-out check of the prediction model in predict.py.

For each test, hide it, score its products from the other tests, rank the
entries that were actually in the hidden test, and see how the real result
compares. Questions answered:
  - Top-1 hit: is the real winner the model's #1 pick?
  - Top-3 hit: is the real winner among the model's top 3 picks?
  - Pick points: placing points (3/2/1/0) the model's #1 pick actually got.
Ties in predicted score are broken at random (expected value is used), so a
model that scores everything 0 gets exactly the random baseline.

An entry's predicted score is the mean of its products' scores (combinations
like "Swix PS6 + Toko HP Blue" average their parts).

Compared methods:
  random        - no information
  overall form  - all other tests weighted equally (ignores conditions)
  same class    - only tests in the same condition class (A/B/C)
  model s/h     - the kernel model with snow-temp scale s C and humidity scale h %

Two set-ups:
  leave-one-out - all other tests are used (past and future)
  forward       - only earlier tests are used, as in real use

Run: python3 validate.py
"""
import math
from collections import defaultdict
from itertools import product as grid

from glide_data import TESTS, POINTS, components, condition_class, hum_mid, podium_places


def entries(t):
    out = [(n, POINTS[p]) for p, n, *_ in podium_places(t)]
    out += [(n, 0) for n in t["others"]]
    return out


def product_scores(train, weight_fn):
    """Expected placing points per product: sum(w * pts) / sum(w)."""
    score = defaultdict(float)
    total = 0.0
    for t in train:
        w = weight_fn(t)
        if w <= 0:
            continue
        total += w
        best = {}
        for name, pts in entries(t):
            for c in components(name):
                best[c] = max(best.get(c, 0), pts)
        for c, pts in best.items():
            score[c] += w * pts
    return {c: v / total for c, v in score.items()} if total else {}


def evaluate_test(t, scores):
    ents = entries(t)
    pred = [sum(scores.get(c, 0.0) for c in components(n)) / len(components(n)) for n, _ in ents]
    actual = [pts for _, pts in ents]
    n = len(ents)
    top_pts = max(actual)
    # Top-k hit probability with random tie-breaking, for the best-predicted winner.
    def hit(k):
        best = 0.0
        for i in range(n):
            if actual[i] != top_pts:
                continue
            above = sum(1 for j in range(n) if pred[j] > pred[i])
            equal = sum(1 for j in range(n) if pred[j] == pred[i]) - 1
            p = 0.0 if above >= k else min(1.0, (k - above) / (equal + 1))
            best = max(best, p)
        return best
    # Expected actual points of the model's #1 pick (random among tied top scores).
    m = max(pred)
    tops = [actual[i] for i in range(n) if pred[i] == m]
    pick = sum(tops) / len(tops)
    known_winner = any(actual[i] == top_pts and pred[i] > 0 for i in range(n))
    return hit(1), hit(3), pick, n, known_winner


def run(weight_maker, forward=False):
    tests = sorted(TESTS, key=lambda t: (t["date"], t["id"]))
    res = []
    for i, t in enumerate(tests):
        train = tests[:i] if forward else tests[:i] + tests[i + 1:]
        if forward and len(train) < 5:
            continue
        scores = product_scores(train, weight_maker(t))
        res.append(evaluate_test(t, scores))
    k = len(res)
    return dict(n=k,
                top1=sum(r[0] for r in res) / k,
                top3=sum(r[1] for r in res) / k,
                pick=sum(r[2] for r in res) / k,
                known=sum(r[4] for r in res) / k)


def kernel(s_scale, h_scale):
    def maker(target):
        def w(t):
            d = math.hypot((target["snow"] - t["snow"]) / s_scale,
                           (hum_mid(target) - hum_mid(t)) / h_scale)
            return math.exp(-d * d / 2)
        return w
    return maker


def same_class(target):
    c = condition_class(target)
    return lambda t: 1.0 if condition_class(t) == c else 0.0


def overall(target):
    return lambda t: 1.0


def random_baseline(forward=False):
    tests = sorted(TESTS, key=lambda t: (t["date"], t["id"]))
    if forward:
        tests = tests[5:]
    r = [evaluate_test(t, {}) for t in tests]
    k = len(r)
    return dict(n=k, top1=sum(x[0] for x in r) / k, top3=sum(x[1] for x in r) / k,
                pick=sum(x[2] for x in r) / k, known=0.0)


def fmt(name, r):
    return (f"{name:<26} {r['top1']*100:6.0f}%  {r['top3']*100:6.0f}%  {r['pick']:9.2f}   "
            f"{r['known']*100:5.0f}%")


def main():
    header = f"{'Method':<26} {'Top-1':>7}  {'Top-3':>7}  {'Pick pts':>9}   {'Winner known':>5}"
    for forward in (False, True):
        title = "FORWARD (only earlier tests, first 5 skipped)" if forward else "LEAVE-ONE-OUT (all other tests)"
        rb = random_baseline(forward)
        print(f"\n{title} - {rb['n']} tests predicted\n{header}")
        print(fmt("random", rb))
        print(fmt("overall form", run(overall, forward)))
        print(fmt("same condition class", run(same_class, forward)))
        print(fmt("model 3C / 12% (default)", run(kernel(3, 12), forward)))
        rows = []
        for s, h in grid([1, 2, 3, 5, 8, 1000], [5, 8, 12, 20, 30, 1000]):
            rows.append(((s, h), run(kernel(s, h), forward)))
        rows.sort(key=lambda x: (-x[1]["top3"], -x[1]["pick"]))
        print("  best scales on this data (beware: tuned on the same 29 tests):")
        for (s, h), r in rows[:5]:
            sl = "inf" if s == 1000 else s
            hl = "inf" if h == 1000 else h
            print(fmt(f"  model {sl}C / {hl}%", r))
    print("\nTop-1/Top-3: share of tests where the real winner was the model's #1 / in its top 3.")
    print("Pick pts: average placing points (3/2/1/0) the model's #1 pick actually got.")
    print("Winner known: share of tests where the winner had a podium in the training tests (otherwise no model can rank it).")


if __name__ == "__main__":
    main()
