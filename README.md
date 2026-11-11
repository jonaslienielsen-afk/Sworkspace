# Ski Serial Check

A mobile web app for scanning the serial number on cross-country skis and
checking whether it is in a list (e.g. club rental skis, a stolen-ski
register, or an inventory).

It runs in the phone's browser and can be installed on the home screen
("Add to Home Screen"). Everything runs on the phone: the list and the scan
history never leave the device, and after the first visit the app works
offline.

## Features

- **Barcode / QR scanning**: point the camera at the ski, and any barcode or QR
  code is read automatically.
- **Printed serial numbers (OCR)**: fit the printed number inside the box and
  tap *Read serial number*. Works with dark text on light backgrounds and light
  text on dark backgrounds. If several values are recognised, tap the right one.
- **Photo fallback**: take or pick a photo if the live camera isn't available.
- **Manual entry**: type the number and tap *Check*.
- **Forgiving matching**: case, spaces and dashes are ignored (`20-123 456` =
  `20123456`). Values that only differ by OCR look-alikes (O/0, I/1, S/5, B/8 …)
  or by a single character are shown as **Possible match**. You compare them
  with the ski and confirm.
- **Your own list**: import a CSV/TSV/TXT file or paste the list. It can be one
  serial per line, or a table with a header row (`Serial;Brand;Model;Owner`).
  The serial column is detected automatically and can be changed. Other columns
  (model, owner, status …) are shown when a ski matches.
- **History**: every check is logged with time and result. Export it as CSV.
  The list view marks serials that have been scanned (✓), which is handy for
  stock-taking.

Excel files: use *File → Save as → CSV* first.

## Running it

```bash
npm install
npm test          # unit tests for the matching logic
npm start         # builds into dist/ and serves on http://localhost:8080
```

Phones only allow the camera on **https** pages (or `localhost`), so to use it
on a phone, host `dist/` on any static HTTPS host.

### GitHub Pages (included)

`.github/workflows/pages.yml` runs the tests, builds the app and publishes it
to GitHub Pages on every push to `main`. Enable it once under
**Settings → Pages → Build and deployment → Source: GitHub Actions**. The app
is then at `https://<user>.github.io/<repo>/`. Open that on the phone and
choose *Add to Home Screen*.

## Project layout

```
src/
  index.html, styles.css   UI
  app.js                   camera, barcode, OCR, list/history handling
  matcher.js               list parsing + matching logic (unit-tested)
  sw.js                    offline cache (file list filled in at build)
  sample-list.csv          example list
scripts/build.mjs          copies src/ and OCR/barcode libraries into dist/
scripts/serve.mjs          tiny local web server
test/matcher.test.mjs      unit tests
```

Libraries (bundled at build time, no CDN): [Tesseract.js](https://github.com/naptha/tesseract.js)
for text recognition and [ZXing](https://github.com/zxing-js/browser) for
barcodes (the browser's built-in `BarcodeDetector` is used when available).

## Tips for scanning

- Use the **Light** button (shown on phones with a torch) for glossy topsheets.
- Hold the phone so the serial number runs horizontally inside the box.
- Wipe off snow and wax. Engraved or very small numbers may need a closer shot
  or manual entry.

## Glide Picker (`/glide/`)

A second app in the same site: pick a fluor-free glide wax for a day in
Holmenkollen from Bull Superski's glide tests (29 tests, Dec 2023 – Mar 2026).
Enter snow temperature (or air temperature) and snow humidity, and it ranks
the gliders that did best in the most similar test conditions, with how Bull
applied them. It also lists every test and per-product statistics, and works
offline.

- App: `src/glide/` (model in `src/glide/model.js`, tests in `test/glide.test.mjs`)
- Data: `glide/glide_data.py` is the source; run `python3 glide/build_tables.py`
  to regenerate the tables and `src/glide/data.json` after adding a test.
- Method and back-testing: `glide/predict.py`, `glide/validate.py`, `glide/RESULTS.md`
