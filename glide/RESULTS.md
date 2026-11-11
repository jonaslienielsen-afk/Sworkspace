# Bull Superski glide project - all tests

Source: https://bullsuperski.no/glidprosjektet/ (29 tests, Dec 2023 - Mar 2026, transcribed from the report images). The 2024 section of that page is empty; the 2023/24 reports were taken from the site's public media library. Rebuild with `python3 build_tables.py`.

## How placings are scored

The reports rank only the top 3; the rest are listed as "also tested". So each result is scored **3 points for 1st, 2 for 2nd, 1 for 3rd, 0 for tested but off the podium**. Tied products share the place and its points (two 1= both get 3). Combinations (e.g. `Swix PS6 + Toko HP Blue`) give their points to every product in them. Per product this gives:

- **Points per test** - average points when the product was in the test (0-3).
- **Podium rate** - share of its tests where it finished top 3.
- **Condition-class points** - points split into A cold/dry, B medium/transformed, C wet.

Condition classes: A: Cold / dry (snow <= -4.5C, or <25% humidity and snow <= -3C); B: Medium / transformed (<55% humidity, snow -4.5 to 0C); C: Wet (>=55% humidity, snow ~0C).

## All tests

| Date | Air temp C | Air humidity % | Snow temp C | Snow humidity % | Snow type group | Weather | Condition class | 1. place | 2. place | 3. place | Best feel |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2023-12-14 | -5 | 96 | -5 | 18-22 | New / falling snow | Overcast | A: Cold / dry (snow <= -4.5C, or <25% humidity and snow <= -3C) | Skigo FFR Blue liquid | Holmenkol Syntec FF1 Red | Star Next Med = Swix TSP6 (tie) | Skigo FFR Blue liquid |
| 2024-01-11 | 4.8 | 57 | -1 | 22 | Transformed / coarse | Partly cloudy | B: Medium / transformed (<55% humidity, snow -4.5 to 0C) | Skigo LDQ | Rode RXL Warm liquid | Holmenkol Syntec FF1 Red |  |
| 2024-01-18 | -7.2 | 68 | -7 | 15 | New / falling snow | Sun | A: Cold / dry (snow <= -4.5C, or <25% humidity and snow <= -3C) | Skigo FFR Blue | Toko HP Blue | Swix TSP5 |  |
| 2024-01-25 | 1 | 74 | -2 | 30 | New snow on old | Sun | B: Medium / transformed (<55% humidity, snow -4.5 to 0C) | Toko HP Yellow = Vauhti LDR New Snow liquid (tie) |  | Skigo FFR Red liquid = Swix TS10 liquid (tie) |  |
| 2024-01-26 | -1 | 99 | -1 | 25-35 | New snow on old | Snowing | B: Medium / transformed (<55% humidity, snow -4.5 to 0C) | Skigo FFR Red | Swix TSP7 = Rode Endurance + Rode RXL Warm liquid (tie) |  |  |
| 2024-02-01 | 1 | 99 | -0.5 | 32-40 | New snow on old | Clear | B: Medium / transformed (<55% humidity, snow -4.5 to 0C) | Rex NF11 liquid | Maplus BP1 Hot | Skigo FFR Yellow |  |
| 2024-02-02 | 0 | 99 | -3 | 20-36 | New snow on old | Snowing | B: Medium / transformed (<55% humidity, snow -4.5 to 0C) | Toko HP Yellow liquid | Swix TS10 liquid = Rex G41 liquid (tie) |  |  |
| 2024-02-08 | -11 | 92 | -10 | 27 | New snow on old | Partly cloudy | A: Cold / dry (snow <= -4.5C, or <25% humidity and snow <= -3C) | Toko HP Blue | Skigo LDQ | Skigo FFR Green = Swix TSP5 (tie) |  |
| 2024-02-15 | -1 | 99 | -1 | 21-32 | New / falling snow | Overcast | B: Medium / transformed (<55% humidity, snow -4.5 to 0C) | Swix White Marathon | Vauhti GW Polar liquid | (no base layer) |  |
| 2024-02-22 | 2 | 99 | 0 | 50-65 | Wet / slush | Rain | C: Wet (>=55% humidity, snow ~0C) | Swix TSP10 + Swix HS10 liquid | Toko HP Yellow liquid = Rex NFX11 (tie) |  |  |
| 2024-03-07 | 2 | 69 | 0 | 34 | Transformed / coarse | Clear, sun | B: Medium / transformed (<55% humidity, snow -4.5 to 0C) | Rex G41 liquid | Rex NF41 liquid | Toko Jet Yellow + Toko Jet Yellow liquid | Rex G41 liquid |
| 2025-01-09 | -3 |  | -4 | 24 | New / falling snow | Clear, sun | A: Cold / dry (snow <= -4.5C, or <25% humidity and snow <= -3C) | HWK UHX Red | Toko HP Red | Star Next Med | HWK UHX Red |
| 2025-01-16 | 4 |  | 0 | 38-50 | Transformed / coarse | Clear | B: Medium / transformed (<55% humidity, snow -4.5 to 0C) | HWK UHX Warm powder + HWK UHX Warm liquid | Skigo LDQ | Swix TSP10 + Toko Jet Warm liquid | HWK UHX Warm powder + HWK UHX Warm liquid |
| 2025-01-30 | -1.5 |  | -1 | 24-32 | Transformed / coarse | Fog | B: Medium / transformed (<55% humidity, snow -4.5 to 0C) | Skigo LDQ | Swix White Marathon + Swix TS6 liquid | Swix PS6 |  |
| 2025-02-06 | 2 |  | -2 | 38 | Transformed / coarse | Sun | B: Medium / transformed (<55% humidity, snow -4.5 to 0C) | HWK UHX Red | Rex Sisu White | Toko HP Red |  |
| 2025-02-13 | 0 |  | -4 | 34 | Transformed / coarse | Sun | B: Medium / transformed (<55% humidity, snow -4.5 to 0C) | Skigo LDQ | Star Next Med | HWK UHX Red |  |
| 2025-02-20 | -4 |  | -3.5 | 35-40 | Transformed / coarse | Overcast | B: Medium / transformed (<55% humidity, snow -4.5 to 0C) | Star Next Med liquid | Skigo LDQ | Star Next Med liquid (ironed 120C) |  |
| 2025-02-25 | 2 |  | 0 | 56-70 | Wet / slush | Overcast | C: Wet (>=55% humidity, snow ~0C) | Skigo GRP + Skigo FFC Yellow | Rex Sisu White | Rode Endurance |  |
| 2025-02-27 | 2 |  | -1 | 68 | Wet / slush |  | C: Wet (>=55% humidity, snow ~0C) | Skigo LDQ | Rex NFX11 | Toko HP Yellow |  |
| 2025-03-27 | 8 |  | 0 | 90-100 | Wet / slush | Sun | C: Wet (>=55% humidity, snow ~0C) | Skigo GRP | Swix PC100 | Skigo LDQ |  |
| 2026-01-08 | -11 |  | -6 | 19-21 | Fine-grained, cold | Clear | A: Cold / dry (snow <= -4.5C, or <25% humidity and snow <= -3C) | Toko HP Blue | Rex NFX21G | Toko Jet Cold | Toko HP Blue |
| 2026-01-08 | -8 |  | -4.5 | 22-25 | Fine-grained, cold | Clear | A: Cold / dry (snow <= -4.5C, or <25% humidity and snow <= -3C) | Toko HP Blue + Rode RW20 | Swix PS6 + Toko HP Blue | Toko HP Blue |  |
| 2026-01-15 | -2 |  | -2 | 25-29 | New / falling snow | Fog, snowing | B: Medium / transformed (<55% humidity, snow -4.5 to 0C) | Swix PF35 | Vola NSD2325 | Toko Jet Mid liquid | Toko Jet Mid liquid |
| 2026-01-29 | -11 |  | -10 | 25-34 | New snow on old | Clear, sun | A: Cold / dry (snow <= -4.5C, or <25% humidity and snow <= -3C) | Toko HP Blue | Red Creek Old Fashion Green | Star Next Cold | Star Next Cold |
| 2026-02-05 | -10 |  | -8 | 23-39 | New snow on old | Clear, a little snow in the air | A: Cold / dry (snow <= -4.5C, or <25% humidity and snow <= -3C) | Swix PM Molybdenum | Vauhti Race Pink | Toko Jet Mid | Toko Jet Mid |
| 2026-02-19 | -8 |  | -11 | 23-42 | Fine-grained, cold | Clear | A: Cold / dry (snow <= -4.5C, or <25% humidity and snow <= -3C) | Skigo Booster Cold + Vola NSD2319 | Swix PS6 | Swix PS6 + Rode RW20 | Skigo Booster Cold + Vola NSD2319 |
| 2026-02-26 | 1 |  | -2 | 71-96 | Wet / slush | Rain and fog | C: Wet (>=55% humidity, snow ~0C) | Skigo FFR Yellow | Skigo FFR Yellow + Skigo CM26 | Star Next Dark Wet | Skigo FFR Yellow |
| 2026-03-19 | 6 |  | 0 | 70 | Wet / slush | Sun | C: Wet (>=55% humidity, snow ~0C) | Toko Prototype liquid | Rode RW50 | Toko Jet Warm liquid | Toko Prototype liquid |
| 2026-03-26 | 8 |  | 0 | 90 | Wet / slush | Sun | C: Wet (>=55% humidity, snow ~0C) | Toko Prototype liquid + Skigo FFR Yellow + Toko Prototype liquid | Skigo FFC Yellow + Skigo FFR Yellow | Toko Prototype liquid (x2) | Toko Prototype liquid + Skigo FFR Yellow + Toko Prototype liquid |

Snow temperature for 2025-01-09 and 2025-01-16 is estimated (not in the report). The two 08.01 reports are labelled 2025 on the site but belong to January 2026. Air humidity is only reported for 2023/24. 2024-01-26 exists in two versions with different placings; the later upload is used (see notes).

## Product ranking (all tests)

| Product | Tests | Wins | 2nd | 3rd | Points | Points per test | Podium rate % | A points | B points | C points | Won on |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Skigo LDQ | 11 | 4 | 3 | 1 | 19 | 1.73 | 73 | 2 | 13 | 4 | 2024-01-11, 2025-01-30, 2025-02-13, 2025-02-27 |
| Toko HP Blue | 8 | 4 | 1 | 0 | 14 | 1.75 | 62 | 14 | 0 | 0 | 2024-02-08, 2026-01-08, 2026-01-08, 2026-01-29 |
| HWK UHX Red | 4 | 2 | 0 | 1 | 7 | 1.75 | 75 | 3 | 4 | 0 | 2025-01-09, 2025-02-06 |
| Skigo FFR Yellow | 7 | 2 | 0 | 1 | 7 | 1.0 | 43 | 0 | 1 | 6 | 2026-02-26, 2026-03-26 |
| Toko Prototype liquid | 2 | 2 | 0 | 0 | 6 | 3.0 | 100 | 0 | 0 | 6 | 2026-03-19, 2026-03-26 |
| Skigo GRP | 3 | 2 | 0 | 0 | 6 | 2.0 | 67 | 0 | 0 | 6 | 2025-02-25, 2025-03-27 |
| Skigo FFC Yellow | 2 | 1 | 1 | 0 | 5 | 2.5 | 100 | 0 | 0 | 5 | 2025-02-25 |
| Toko HP Yellow liquid | 2 | 1 | 1 | 0 | 5 | 2.5 | 100 | 0 | 3 | 2 | 2024-02-02 |
| Rex G41 liquid | 3 | 1 | 1 | 0 | 5 | 1.67 | 67 | 0 | 5 | 0 | 2024-03-07 |
| Swix White Marathon | 9 | 1 | 1 | 0 | 5 | 0.56 | 22 | 0 | 5 | 0 | 2024-02-15 |
| Swix PS6 | 10 | 0 | 2 | 1 | 5 | 0.5 | 30 | 4 | 1 | 0 |  |
| Rex NFX11 | 2 | 0 | 2 | 0 | 4 | 2.0 | 100 | 0 | 0 | 4 |  |
| Rode RW20 | 2 | 1 | 0 | 1 | 4 | 2.0 | 100 | 4 | 0 | 0 | 2026-01-08 |
| Rode RXL Warm liquid | 2 | 0 | 2 | 0 | 4 | 2.0 | 100 | 0 | 4 | 0 |  |
| Swix TSP10 | 2 | 1 | 0 | 1 | 4 | 2.0 | 100 | 0 | 1 | 3 | 2024-02-22 |
| Rex Sisu White | 4 | 0 | 2 | 0 | 4 | 1.0 | 50 | 0 | 2 | 2 |  |
| Star Next Med | 6 | 0 | 1 | 2 | 4 | 0.67 | 50 | 2 | 2 | 0 |  |
| Toko HP Yellow | 6 | 1 | 0 | 1 | 4 | 0.67 | 33 | 0 | 3 | 1 | 2024-01-25 |
| Skigo FFR Blue liquid | 1 | 1 | 0 | 0 | 3 | 3.0 | 100 | 3 | 0 | 0 | 2023-12-14 |
| Star Next Med liquid | 1 | 1 | 0 | 0 | 3 | 3.0 | 100 | 0 | 3 | 0 | 2025-02-20 |
| Swix HS10 liquid | 1 | 1 | 0 | 0 | 3 | 3.0 | 100 | 0 | 0 | 3 | 2024-02-22 |
| Swix PM Molybdenum | 1 | 1 | 0 | 0 | 3 | 3.0 | 100 | 3 | 0 | 0 | 2026-02-05 |
| Vola NSD2319 | 1 | 1 | 0 | 0 | 3 | 3.0 | 100 | 3 | 0 | 0 | 2026-02-19 |
| HWK UHX Warm | 2 | 1 | 0 | 0 | 3 | 1.5 | 50 | 0 | 3 | 0 | 2025-01-16 |
| Holmenkol Syntec FF1 Red | 2 | 0 | 1 | 1 | 3 | 1.5 | 100 | 2 | 1 | 0 |  |
| Skigo Booster Cold | 2 | 1 | 0 | 0 | 3 | 1.5 | 50 | 3 | 0 | 0 | 2026-02-19 |
| Skigo FFR Red | 2 | 1 | 0 | 0 | 3 | 1.5 | 50 | 0 | 3 | 0 | 2024-01-26 |
| Swix PF35 | 2 | 1 | 0 | 0 | 3 | 1.5 | 50 | 0 | 3 | 0 | 2026-01-15 |
| Rex NF11 liquid | 3 | 1 | 0 | 0 | 3 | 1.0 | 33 | 0 | 3 | 0 | 2024-02-01 |
| Rode Endurance | 3 | 0 | 1 | 1 | 3 | 1.0 | 67 | 0 | 2 | 1 |  |
| Skigo FFR Blue | 3 | 1 | 0 | 0 | 3 | 1.0 | 33 | 3 | 0 | 0 | 2024-01-18 |
| Vauhti LDR New Snow liquid | 3 | 1 | 0 | 0 | 3 | 1.0 | 33 | 0 | 3 | 0 | 2024-01-25 |
| Swix TS10 liquid | 5 | 0 | 1 | 1 | 3 | 0.6 | 40 | 0 | 3 | 0 |  |
| Toko HP Red | 5 | 0 | 1 | 1 | 3 | 0.6 | 40 | 2 | 1 | 0 |  |
| Red Creek Old Fashion Green | 1 | 0 | 1 | 0 | 2 | 2.0 | 100 | 2 | 0 | 0 |  |
| Rex NF41 liquid | 1 | 0 | 1 | 0 | 2 | 2.0 | 100 | 0 | 2 | 0 |  |
| Rex NFX21G | 1 | 0 | 1 | 0 | 2 | 2.0 | 100 | 2 | 0 | 0 |  |
| Skigo CM26 | 1 | 0 | 1 | 0 | 2 | 2.0 | 100 | 0 | 0 | 2 |  |
| Swix PC100 | 1 | 0 | 1 | 0 | 2 | 2.0 | 100 | 0 | 0 | 2 |  |
| Swix TS6 liquid | 1 | 0 | 1 | 0 | 2 | 2.0 | 100 | 0 | 2 | 0 |  |
| Swix TSP7 | 1 | 0 | 1 | 0 | 2 | 2.0 | 100 | 0 | 2 | 0 |  |
| Vauhti GW Polar liquid | 1 | 0 | 1 | 0 | 2 | 2.0 | 100 | 0 | 2 | 0 |  |
| Vauhti Race Pink | 1 | 0 | 1 | 0 | 2 | 2.0 | 100 | 2 | 0 | 0 |  |
| Vola NSD2325 | 1 | 0 | 1 | 0 | 2 | 2.0 | 100 | 0 | 2 | 0 |  |
| Rode RW50 | 2 | 0 | 1 | 0 | 2 | 1.0 | 50 | 0 | 0 | 2 |  |
| Swix TSP5 | 2 | 0 | 0 | 2 | 2 | 1.0 | 100 | 2 | 0 | 0 |  |
| Maplus BP1 Hot | 3 | 0 | 1 | 0 | 2 | 0.67 | 33 | 0 | 2 | 0 |  |
| Toko Jet Warm liquid | 3 | 0 | 0 | 2 | 2 | 0.67 | 67 | 0 | 1 | 1 |  |
| (no base layer) | 1 | 0 | 0 | 1 | 1 | 1.0 | 100 | 0 | 1 | 0 |  |
| Skigo FFR Green | 1 | 0 | 0 | 1 | 1 | 1.0 | 100 | 1 | 0 | 0 |  |
| Skigo FFR Red liquid | 1 | 0 | 0 | 1 | 1 | 1.0 | 100 | 0 | 1 | 0 |  |
| Star Next Dark Wet | 1 | 0 | 0 | 1 | 1 | 1.0 | 100 | 0 | 0 | 1 |  |
| Toko Jet Cold | 1 | 0 | 0 | 1 | 1 | 1.0 | 100 | 1 | 0 | 0 |  |
| Toko Jet Mid liquid | 1 | 0 | 0 | 1 | 1 | 1.0 | 100 | 0 | 1 | 0 |  |
| Toko Jet Yellow | 1 | 0 | 0 | 1 | 1 | 1.0 | 100 | 0 | 1 | 0 |  |
| Toko Jet Yellow liquid | 1 | 0 | 0 | 1 | 1 | 1.0 | 100 | 0 | 1 | 0 |  |
| Swix TSP6 | 2 | 0 | 0 | 1 | 1 | 0.5 | 50 | 1 | 0 | 0 |  |
| Toko Jet Mid | 2 | 0 | 0 | 1 | 1 | 0.5 | 50 | 1 | 0 | 0 |  |
| Star Next Cold | 3 | 0 | 0 | 1 | 1 | 0.33 | 33 | 1 | 0 | 0 |  |

Products that were tested but never reached the podium are in `glide_product_stats.csv`.

### Best in class A: Cold / dry (snow <= -4.5C, or <25% humidity and snow <= -3C)

| Product | A tests | A wins | A points |
|---|---|---|---|
| Toko HP Blue | 7 | 4 | 14 |
| Rode RW20 | 2 | 1 | 4 |
| Swix PS6 | 3 | 0 | 4 |
| HWK UHX Red | 1 | 1 | 3 |
| Skigo FFR Blue liquid | 1 | 1 | 3 |
| Swix PM Molybdenum | 1 | 1 | 3 |
| Vola NSD2319 | 1 | 1 | 3 |
| Skigo Booster Cold | 2 | 1 | 3 |

### Best in class B: Medium / transformed (<55% humidity, snow -4.5 to 0C)

| Product | B tests | B wins | B points |
|---|---|---|---|
| Skigo LDQ | 5 | 3 | 13 |
| Rex G41 liquid | 3 | 1 | 5 |
| Swix White Marathon | 5 | 1 | 5 |
| Rode RXL Warm liquid | 2 | 0 | 4 |
| HWK UHX Red | 3 | 1 | 4 |
| Toko HP Yellow liquid | 1 | 1 | 3 |
| Star Next Med liquid | 1 | 1 | 3 |
| HWK UHX Warm | 1 | 1 | 3 |

### Best in class C: Wet (>=55% humidity, snow ~0C)

| Product | C tests | C wins | C points |
|---|---|---|---|
| Toko Prototype liquid | 2 | 2 | 6 |
| Skigo GRP | 2 | 2 | 6 |
| Skigo FFR Yellow | 5 | 2 | 6 |
| Skigo FFC Yellow | 2 | 1 | 5 |
| Skigo LDQ | 2 | 1 | 4 |
| Rex NFX11 | 2 | 0 | 4 |
| Swix TSP10 | 1 | 1 | 3 |
| Swix HS10 liquid | 1 | 1 | 3 |

## Predicting a race day in Holmenkollen

`predict.py` (and the Glide Picker app in `src/glide/`) weights every past test by how close its snow temperature and snow humidity are to the forecast and returns the products with the highest expected placing points:

```
python3 predict.py --snow-temp -2 --humidity 35
python3 predict.py --air-temp 4 --humidity 70   # snow temp estimated from air
```

Snow humidity (snøfukt) is the strongest separator in this data, so measure or estimate it if you can. Treat the output as a short list to test, not a guarantee: there are only 18 tests, gaps between the top 3 are often described as small, and the product line-up changes from test to test.
