"""Export glide_data.py to src/glide/data.json for the Glide Picker web app.

Run: python3 export_json.py   (build_tables.py also runs it)
"""
import json
import os

from glide_data import TESTS, POINTS, components, condition_class, hum_mid, podium_places

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "glide", "data.json")


def export(path=OUT):
    tests = []
    for t in sorted(TESTS, key=lambda t: (t["date"], t["id"])):
        tests.append({
            "id": t["id"], "date": t["date"], "season": t["season"], "title": t["title"], "kind": t["kind"],
            "air": t["air"], "airHum": t.get("air_hum"), "snow": t["snow"], "snowEst": t["snow_temp_est"],
            "humMin": t["hum_min"], "humMax": t["hum_max"], "hum": hum_mid(t),
            "snowType": t["snow_type"], "weather": t["weather"], "cls": condition_class(t),
            "podium": [{"place": p, "name": n, "type": ty, "apply": a, "remove": r,
                        "points": POINTS[p], "products": components(n)}
                       for p, n, ty, a, r in podium_places(t)],
            "others": [{"name": n, "products": components(n)} for n in t["others"]],
            "bestFeel": t.get("best_feel", ""), "distance": t.get("distance", ""), "notes": t["notes"],
        })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"source": "https://bullsuperski.no/glidprosjektet/", "tests": tests}, f,
                  ensure_ascii=False, indent=1)
    return path, len(tests)


if __name__ == "__main__":
    print("wrote %s (%d tests)" % export())
