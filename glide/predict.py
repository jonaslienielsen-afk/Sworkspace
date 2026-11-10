"""Predict the best fluor-free glide wax for a given day, from the Bull Superski
glide tests (glide_data.py).

Method (nearest-neighbour weighting):
  1. Each past test gets a similarity weight from how close its snow
     temperature and snow humidity are to the forecast day:
         d = sqrt(((snow - snow_i) / 3)^2 + ((hum - hum_i) / 12)^2)
         w = exp(-d^2 / 2)
     So a test 3 C or 12 humidity points away counts ~60%, twice that ~14%.
  2. In each test a product scores 3 (1st), 2 (2nd), 1 (3rd), 0 (tested, not on
     the podium); tied products share the place's points. A combination gives
     its points to each product in it.
  3. Score = sum(w * points) / sum(w over ALL tests). This is the expected
     placing points on a day like this. Products never tested in similar
     conditions get ~0, so the score rewards proven results, not lucky one-offs.
  4. "Podium rate" = weighted share of the similar tests the product was in
     where it finished top 3.

Usage:
  python3 predict.py --snow-temp -2 --humidity 35
  python3 predict.py --air-temp 3 --humidity 70      # snow temp estimated
"""
import argparse
import math
from collections import defaultdict

from glide_data import TESTS, POINTS, components, hum_mid, podium_places

SNOW_SCALE = 3.0   # degrees C
HUM_SCALE = 12.0   # humidity percentage points


def weights(snow, hum):
    out = []
    for t in TESTS:
        d = math.hypot((snow - t["snow"]) / SNOW_SCALE, (hum - hum_mid(t)) / HUM_SCALE)
        out.append((t, math.exp(-d * d / 2)))
    return out


def entries(t):
    for place, name, *_ in podium_places(t):
        yield name, POINTS[place]
    for name in t["others"]:
        yield name, 0


def predict(snow, hum, top=10):
    ws = weights(snow, hum)
    total_w = sum(w for _, w in ws)
    score = defaultdict(float)
    tested_w = defaultdict(float)
    podium_w = defaultdict(float)
    wins = defaultdict(list)
    for t, w in ws:
        seen = {}
        for name, pts in entries(t):
            for c in components(name):
                seen[c] = max(seen.get(c, 0), pts)  # best result of the product in this test
        for c, pts in seen.items():
            score[c] += w * pts
            tested_w[c] += w
            if pts > 0:
                podium_w[c] += w
            if pts == 3:
                wins[c].append(t["date"])
    rows = []
    for c in score:
        rows.append(dict(product=c, score=score[c] / total_w,
                         podium_rate=podium_w[c] / tested_w[c] if tested_w[c] else 0,
                         evidence=tested_w[c], wins=wins[c]))
    rows.sort(key=lambda r: (-r["score"], -r["podium_rate"]))
    nearest = sorted(ws, key=lambda x: -x[1])[:5]
    return rows[:top], nearest


def estimate_snow_temp(air):
    # Snow can't be above 0 C; in the tests snow was ~1-3 C colder than air when below 0.
    return min(0.0, air - 1.0)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--snow-temp", type=float, help="snow temperature, C")
    p.add_argument("--air-temp", type=float, help="air temperature, C (used if --snow-temp is missing)")
    p.add_argument("--humidity", type=float, required=True, help="snow humidity, percent (snøfukt)")
    p.add_argument("--top", type=int, default=10)
    a = p.parse_args()
    if a.snow_temp is None:
        if a.air_temp is None:
            p.error("give --snow-temp or --air-temp")
        a.snow_temp = estimate_snow_temp(a.air_temp)
        print(f"(snow temperature estimated from air: {a.snow_temp:+.1f} C)")
    rows, nearest = predict(a.snow_temp, a.humidity, a.top)
    print(f"\nConditions: snow {a.snow_temp:+.1f} C, snow humidity {a.humidity:.0f}%\n")
    print("Most similar past tests:")
    for t, w in nearest:
        print(f"  {t['date']}  snow {t['snow']:+5.1f} C  hum {hum_mid(t):4.0f}%  weight {w:4.2f}  "
              f"winner: {t['podium'][0][0]}")
    print(f"\n{'#':>2}  {'Product':<34} {'Score':>5}  {'Podium%':>7}  {'Evidence':>8}  Wins (any conditions)")
    for i, r in enumerate(rows, 1):
        print(f"{i:>2}  {r['product']:<34} {r['score']:5.2f}  {r['podium_rate']*100:6.0f}%  "
              f"{r['evidence']:8.2f}  {', '.join(r['wins'])}")
    print("\nScore = expected placing points (3/2/1) on a day like this; max 3.0.")
    print("Evidence = sum of similarity weights of the tests the product took part in (more = surer).")


if __name__ == "__main__":
    main()
