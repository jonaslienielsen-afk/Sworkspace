"""Write the glide test tables from glide_data.py:

  glide_tests.csv          one row per test: conditions + 1st/2nd/3rd + others + notes
  glide_results_long.csv   one row per product per test (placing, points) - for analysis
  glide_product_stats.csv  per product: tests, wins, 2nd, 3rd, points, podium rate, by condition
  glide_tests.xlsx         the three tables above as sheets
  RESULTS.md               the same as readable Markdown tables

Run: python3 build_tables.py
"""
import csv
from collections import defaultdict

from glide_data import TESTS, POINTS, components, condition_class, hum_mid

CLASSES = sorted({condition_class(t) for t in TESTS})


def fmt(x):
    return f"{x:+g}" if isinstance(x, (int, float)) else x


def test_rows():
    rows = []
    for t in sorted(TESTS, key=lambda t: t["id"]):
        r = {
            "Date": t["date"], "Season": t["season"], "Report": t["title"], "Test type": t["kind"],
            "Air temp C": t["air"], "Snow temp C": t["snow"],
            "Snow temp estimated": "yes" if t["snow_temp_est"] else "",
            "Snow humidity %": f"{t['hum_min']}" if t["hum_min"] == t["hum_max"] else f"{t['hum_min']}-{t['hum_max']}",
            "Humidity mid %": hum_mid(t), "Snow type": t["snow_type"], "Weather": t["weather"],
            "Condition class": condition_class(t),
        }
        for i, (name, typ, app, rem) in enumerate(t["podium"], 1):
            r[f"{i}. place"] = name
            r[f"{i}. type"] = typ
            r[f"{i}. application"] = app
            r[f"{i}. removal/brushing"] = rem
        r["Also tested (unranked)"] = "; ".join(t["others"])
        r["Best feel"] = t.get("best_feel", "")
        r["Distance retest"] = t.get("distance", "")
        r["Notes"] = t["notes"]
        rows.append(r)
    return rows


def long_rows():
    rows = []
    for t in sorted(TESTS, key=lambda t: t["id"]):
        items = [(n, i) for i, (n, *_ ) in enumerate(t["podium"], 1)] + [(n, None) for n in t["others"]]
        for name, place in items:
            rows.append({
                "Date": t["date"], "Test id": t["id"], "Condition class": condition_class(t),
                "Snow temp C": t["snow"], "Humidity mid %": hum_mid(t), "Air temp C": t["air"],
                "Snow type": t["snow_type"], "Entry": name,
                "Products in entry": " | ".join(components(name)),
                "Placing": place if place else "4+ (unranked)",
                "Points (3/2/1/0)": POINTS.get(place, 0),
                "Best feel": "yes" if name == t.get("best_feel") else "",
            })
    return rows


def product_stats():
    """Per product (combinations split into their products). A product's result
    in a test is its best entry in that test."""
    best = defaultdict(dict)  # product -> test id -> best placing (None = unranked)
    tests_by_id = {t["id"]: t for t in TESTS}
    for t in TESTS:
        items = [(n, i) for i, (n, *_ ) in enumerate(t["podium"], 1)] + [(n, None) for n in t["others"]]
        for name, place in items:
            for c in components(name):
                cur = best[c].get(t["id"], "unset")
                if cur == "unset" or (place is not None and (cur is None or place < cur)):
                    best[c][t["id"]] = place
    rows = []
    for prod, res in best.items():
        places = list(res.values())
        n = len(places)
        w = places.count(1); s = places.count(2); th = places.count(3)
        pts = sum(POINTS.get(p, 0) for p in places)
        r = {"Product": prod, "Tests": n, "Wins": w, "2nd": s, "3rd": th,
             "Podiums": w + s + th, "Points": pts,
             "Points per test": round(pts / n, 2), "Podium rate %": round(100 * (w + s + th) / n)}
        for c in CLASSES:
            ids = [i for i in res if condition_class(tests_by_id[i]) == c]
            cp = sum(POINTS.get(res[i], 0) for i in ids)
            r[f"{c[:1]} tests"] = len(ids)
            r[f"{c[:1]} points"] = cp
            r[f"{c[:1]} wins"] = sum(1 for i in ids if res[i] == 1)
        r["Won on"] = ", ".join(sorted(tests_by_id[i]["date"] for i, p in res.items() if p == 1))
        rows.append(r)
    rows.sort(key=lambda r: (-r["Points"], -r["Points per test"], r["Product"]))
    return rows


def write_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def write_xlsx(path, sheets):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter
    wb = Workbook()
    wb.remove(wb.active)
    gold, silver, bronze = (PatternFill("solid", fgColor=c) for c in ("FFE699", "E7E6E6", "F8CBAD"))
    for name, rows in sheets:
        ws = wb.create_sheet(name)
        cols = list(rows[0].keys())
        ws.append(cols)
        for r in rows:
            ws.append([r[c] for c in cols])
        for cell in ws[1]:
            cell.font = Font(bold=True)
            cell.fill = PatternFill("solid", fgColor="BDD7EE")
            cell.alignment = Alignment(wrap_text=True, vertical="top")
        for i, c in enumerate(cols, 1):
            width = min(60, max(10, max(len(str(r[c])) for r in rows[:50]) + 2, len(c) + 2))
            ws.column_dimensions[get_column_letter(i)].width = width
            if c in ("1. place", "2. place", "3. place"):
                fill = {"1": gold, "2": silver, "3": bronze}[c[0]]
                for row in ws.iter_rows(min_row=2, min_col=i, max_col=i):
                    row[0].fill = fill
        ws.freeze_panes = "B2"
        ws.auto_filter.ref = ws.dimensions
    wb.save(path)


def md_table(rows, cols):
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for r in rows:
        out.append("| " + " | ".join(str(r[c]).replace("|", "/") for c in cols) + " |")
    return "\n".join(out)


def write_md(path, tests, stats):
    lines = ["# Bull Superski glide project - all tests\n",
             "Source: https://bullsuperski.no/glidprosjektet/ (18 reports, Jan 2025 - Mar 2026, "
             "transcribed from the report images). Rebuild with `python3 build_tables.py`.\n",
             "## How placings are scored\n",
             "The reports rank only the top 3; the rest are listed as \"also tested\". So each result is "
             "scored **3 points for 1st, 2 for 2nd, 1 for 3rd, 0 for tested but off the podium**. "
             "Combinations (e.g. `Swix PS6 + Toko HP Blue`) give their points to every product in them. "
             "Per product this gives:\n",
             "- **Points per test** - average points when the product was in the test (0-3).",
             "- **Podium rate** - share of its tests where it finished top 3.",
             "- **Condition-class points** - points split into A cold/dry, B medium/transformed, C wet.\n",
             "Condition classes: " + "; ".join(CLASSES) + ".\n",
             "## All tests\n",
             md_table(tests, ["Date", "Air temp C", "Snow temp C", "Snow humidity %", "Snow type", "Weather",
                              "Condition class", "1. place", "2. place", "3. place", "Best feel"]),
             "\nSnow temperature for 2025-01-09 and 2025-01-16 is estimated (not in the report). "
             "The two 08.01 reports are labelled 2025 on the site but belong to January 2026.\n",
             "## Product ranking (all tests)\n",
             md_table([s for s in stats if s["Podiums"] > 0],
                      ["Product", "Tests", "Wins", "2nd", "3rd", "Points", "Points per test", "Podium rate %",
                       "A points", "B points", "C points", "Won on"]),
             "\nProducts that were tested but never reached the podium are in `glide_product_stats.csv`.\n"]
    for c in CLASSES:
        key = c[:1]
        top = sorted([s for s in stats if s[f"{key} points"] > 0],
                     key=lambda s: (-s[f"{key} points"], s[f"{key} tests"]))[:8]
        lines.append(f"### Best in class {c}\n")
        lines.append(md_table(top, ["Product", f"{key} tests", f"{key} wins", f"{key} points"]) + "\n")
    lines += ["## Predicting a race day in Holmenkollen\n",
              "`predict.py` weights every past test by how close its snow temperature and snow humidity "
              "are to the forecast and returns the products with the highest expected placing points:\n",
              "```\npython3 predict.py --snow-temp -2 --humidity 35\n"
              "python3 predict.py --air-temp 4 --humidity 70   # snow temp estimated from air\n```\n",
              "Snow humidity (snøfukt) is the strongest separator in this data, so measure or estimate it "
              "if you can. Treat the output as a short list to test, not a guarantee: there are only 18 "
              "tests, gaps between the top 3 are often described as small, and the product line-up "
              "changes from test to test.\n"]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    tests, longr, stats = test_rows(), long_rows(), product_stats()
    write_csv("glide_tests.csv", tests)
    write_csv("glide_results_long.csv", longr)
    write_csv("glide_product_stats.csv", stats)
    write_xlsx("glide_tests.xlsx", [("Tests", tests), ("Product stats", stats), ("Results long", longr)])
    write_md("RESULTS.md", tests, stats)
    print(f"{len(tests)} tests, {len(longr)} results, {len(stats)} products")


if __name__ == "__main__":
    main()
