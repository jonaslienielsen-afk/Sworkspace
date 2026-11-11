"""Bull Superski "Glidprosjektet" fluor-free glide tests, transcribed by hand
from the report images at https://bullsuperski.no/glidprosjektet/ (seasons
2024/25 and 2025/26, 18 reports) plus the 2023/24 "Produkttest" reports (11
tests). The 2024 heading on that page is empty, so the 2023/24 reports were
found in the site's public media library (wp-json/wp/v2/media).

Each test lists:
  - places (optional): the placing of each podium entry when there are ties,
    e.g. [1, 1, 3, 3]; default is 1, 2, 3.
  - conditions (air temp, snow temp, snow humidity %, snow type, weather)
  - the podium (1st, 2nd, 3rd). The reports only rank the top 3; every other
    product is listed as "also in the test" without a placing.
  - products tested but not on the podium ("others")
  - notes (best feel, distance retests, base layer used etc.)

Product names are normalised so the same product has one spelling across
reports (e.g. "Toko High Performance Blue" -> "Toko HP Blue", "Skigo FFR LDQ"
/ "Skigo LDQ" -> "Skigo LDQ", "Star Next Mid" -> "Star Next Med",
"HWK Rød" -> "HWK UHX Red"). A combination is written "A + B" (base/under
layer first). The original wording is kept in `notes` where it matters.
"""

# snow_temp_est=True means the report gave no snow temperature and the value is
# an estimate (snow cannot be warmer than 0 C; on a cold day it is close to air).
TESTS = [
    # ------------------------------------------------------------- 2023/24
    # These reports also give air humidity (air_hum). Base layer under the
    # tested products was Swix Base Protection Liquid (BPL), Swix PS6 or PS5.
    dict(id="2023-12-14", date="2023-12-14", season="2023/24", title="Fluorfritest 14. desember",
         kind="Topcoat (Swix BPL base on all)", air=-5, air_hum=96, snow=-5, snow_temp_est=False,
         hum_min=18, hum_max=22, snow_type="Mix of man-made and new snow", weather="Overcast",
         places=[1, 2, 3, 3],
         podium=[
             ("Skigo FFR Blue liquid", "Liquid", "Sponge on bottle, dry 30 min, rotor fleece",
              "Fine steel by hand (2-3 light strokes), rotor nylon"),
             ("Holmenkol Syntec FF1 Red", "Powder", "Iron 200C", "Rotor horsehair and steel"),
             ("Star Next Med", "Powder", "Iron 200C", "Rotor horsehair and steel"),
             ("Swix TSP6", "Powder", "Iron 180C", "Rotor horsehair and steel"),
         ],
         others=["Toko HP Red", "Skigo FFR Red", "Maplus GM Boost Med", "Vauhti LDR New Snow liquid"],
         best_feel="Skigo FFR Blue liquid",
         distance="Same gap between 1st and 2nd after 7 km",
         notes="Even between the top four. Surprising that a liquid won; it was also best on feel. "
               "The other liquid in the test did not reach the top."),
    dict(id="2024-01-11", date="2024-01-11", season="2023/24", title="Fluorfritest 11. januar",
         kind="Topcoat (Swix BPL base on all)", air=4.8, air_hum=57, snow=-1, snow_temp_est=False,
         hum_min=22, hum_max=22, snow_type="Natural snow on man-made base", weather="Partly cloudy",
         podium=[
             ("Skigo LDQ", "Powder", "Iron 200C", "Rotor horsehair and steel"),
             ("Rode RXL Warm liquid", "Liquid", "Felt block + rotor fleece", "Fine steel + rotor nylon"),
             ("Holmenkol Syntec FF1 Red", "Powder", "Iron 200C", "Rotor horsehair and steel"),
         ],
         others=["Toko HP Yellow glider", "Vauhti Old Snow Warm liquid", "Maplus Base Gel + Maplus Boost liquid",
                 "Red Creek FF Lilla", "Star Next Med"],
         best_feel="",
         distance="Finalists retested after 5 km: the winner only increased its margin",
         notes="Clear winner. Tendency that powder/glider applied with high heat beat those applied "
               "with low heat."),
    dict(id="2024-01-18", date="2024-01-18", season="2023/24", title="Fluorfritest 18. januar",
         kind="Topcoat (Swix PS6 base on all)", air=-7.2, air_hum=68, snow=-7, snow_temp_est=False,
         hum_min=15, hum_max=15, snow_type="New snow (snowed 17 Jan)", weather="Sun",
         podium=[
             ("Skigo FFR Blue", "Powder", "Iron 200C", "Rotor horsehair and steel"),
             ("Toko HP Blue", "Powder", "Iron 200C", "Rotor horsehair and steel"),
             ("Swix TSP5", "Powder", "Iron 200C", "Rotor horsehair and steel"),
         ],
         others=["Swix TSP5 (ironed 160C)", "Vauhti Race Cold New Snow glider", "Red Creek FF Lilla",
                 "Rode R20", "Rex NF21G liquid"],
         best_feel="",
         notes="Even between the top two, bigger gaps below. Rode R20 a good cheaper alternative. "
               "Skis zeroed before the test."),
    # Two images exist for 25 Jan: identical results, one mislabelled "18. januar".
    dict(id="2024-01-25", date="2024-01-25", season="2023/24", title="Fluorfritest 25. januar",
         kind="Topcoat (Swix PS6 base on all)", air=1, air_hum=74, snow=-2, snow_temp_est=False,
         hum_min=30, hum_max=30, snow_type="Transformed with some new snow", weather="Sun",
         places=[1, 1, 3, 3],
         podium=[
             ("Toko HP Yellow", "Powder", "Iron 200C", "Rotor horsehair and steel"),
             ("Vauhti LDR New Snow liquid", "Liquid", "Sponge on bottle, rotor felt", "Fine steel, blue nylon"),
             ("Skigo FFR Red liquid", "Liquid", "Sponge on bottle, rotor felt", "Fine steel, blue nylon"),
             ("Swix TS10 liquid", "Liquid", "Felt pad, rotor felt", "Fine steel, blue nylon"),
         ],
         others=["Maplus GM Hot", "Maplus GM Hot + Maplus Boost Hot liquid", "Rex NF11 liquid", "Maplus BP1 Hot"],
         best_feel="",
         notes="Very even, very little between the top four. Maplus BP1 Hot not far behind as a "
               "cheaper alternative. Skis zeroed before the test."),
    # Two versions exist for 26 Jan with different placings. The later upload
    # (12:04 vs 11:28) is used: 1. Skigo FFR Red, 2= Swix TSP7, 2= Rode.
    # The earlier version had 1= Swix TSP7, 1= Rode Endurance + RXL Warm, 3. Skigo FFR Red.
    dict(id="2024-01-26", date="2024-01-26", season="2023/24", title="Fluorfritest 26. januar",
         kind="Topcoat (Swix PS6 base on all)", air=-1, air_hum=99, snow=-1, snow_temp_est=False,
         hum_min=25, hum_max=35, snow_type="New snow over transformed", weather="Snowing",
         places=[1, 2, 2],
         podium=[
             ("Skigo FFR Red", "Powder", "Iron 200C", "Rotor horsehair and steel"),
             ("Swix TSP7", "Powder", "Iron 200C", "Rotor horsehair and steel"),
             ("Rode Endurance + Rode RXL Warm liquid", "Glider + liquid", "Iron 155C, felt pad + felt rotor",
              "Rotor horsehair and steel + fine steel, blue nylon"),
         ],
         others=["Vauhti LDR New Snow liquid", "Swix White Marathon", "Swix TS10 liquid", "Toko HP Yellow",
                 "Toko HP glider"],
         best_feel="",
         notes="Three products stood out, bigger gaps below. NB: the site has two versions of this "
               "report; an earlier one had Swix TSP7 and Rode Endurance + RXL Warm tied 1st and "
               "Skigo FFR Red 3rd. The later upload is used here."),
    dict(id="2024-02-01", date="2024-02-01", season="2023/24", title="Fluorfritest 1. februar",
         kind="Topcoat (Swix BPL base on all)", air=1, air_hum=99, snow=-0.5, snow_temp_est=False,
         hum_min=32, hum_max=40, snow_type="Powdery layer of new snow over transformed", weather="Clear",
         podium=[
             ("Rex NF11 liquid", "Liquid", "Felt block, cure 20 min, rotor felt", "Fine steel by hand + blue nylon rotor"),
             ("Maplus BP1 Hot", "Liquid", "Felt block + rotor felt after drying", "Fine steel by hand + nylon rotor"),
             ("Skigo FFR Yellow", "Powder", "Iron 200C", "Rotor horsehair + fine steel + nylon"),
         ],
         others=["Vauhti LDR Old Snow", "Swix TS10 liquid", "Toko HP Yellow", "Star Next Warm liquid",
                 "Swix White Marathon + Swix TST8 block"],
         best_feel="",
         notes="Two good options at the top. Skigo FFR Yellow (3rd) is more durable, a good choice "
               "for long races. Skis zeroed before the test."),
    dict(id="2024-02-02", date="2024-02-02", season="2023/24", title="Fluorfritest 2. februar",
         kind="Topcoat (Swix BPL base on all)", air=0, air_hum=99, snow=-3, snow_temp_est=False,
         hum_min=20, hum_max=36, snow_type="Fresh new snow over transformed", weather="Snowing",
         places=[1, 2, 2],
         podium=[
             ("Toko HP Yellow liquid", "Liquid", "Felt block, cure 20 min, rotor felt",
              "Fine steel by hand + blue nylon rotor"),
             ("Swix TS10 liquid", "Liquid", "Felt block + rotor felt after drying", "Nylon rotor"),
             ("Rex G41 liquid", "Liquid", "Felt block + rotor felt after drying", "Fine steel by hand + nylon rotor"),
         ],
         others=["Maplus BP1 Hot", "Swix White Marathon", "Skigo FFR Yellow", "Rex NF11 liquid",
                 "Maplus BP1 Hot (with wool)"],
         best_feel="",
         notes="Very even top 3. The two yellow products could gain in warmer/wetter snow; the Rex "
               "option tolerates icier/sharper snow. Swix White Marathon was 4th and works well as a "
               "base for the liquids."),
    dict(id="2024-02-08", date="2024-02-08", season="2023/24", title="Fluorfritest 8. februar",
         kind="Topcoat (Swix PS5 base on all)", air=-11, air_hum=92, snow=-10, snow_temp_est=False,
         hum_min=27, hum_max=27, snow_type="Fresh snow over transformed", weather="Partly cloudy",
         places=[1, 2, 3, 3],
         podium=[
             ("Toko HP Blue", "Powder", "Iron 200C", "Rotor horsehair / steel / horsehair, blue nylon"),
             ("Skigo LDQ", "Powder", "Iron 200C", "Rotor horsehair and steel"),
             ("Skigo FFR Green", "Powder", "Iron 200C", "Rotor horsehair and steel"),
             ("Swix TSP5", "Powder", "Iron 200C", "Rotor horsehair and steel"),
         ],
         others=["Swix White Marathon", "Skigo FFR Blue", "Star Next Cold", "Vauhti Polar"],
         best_feel="",
         notes="Even test."),
    dict(id="2024-02-15", date="2024-02-15", season="2023/24", title="Fluorfritest 15. februar",
         kind="Base layer (topcoat Swix TSP7 on all, over Swix BPL)", air=-1, air_hum=99, snow=-1,
         snow_temp_est=False, hum_min=21, hum_max=32, snow_type="Fresh snow", weather="Overcast",
         podium=[
             ("Swix White Marathon", "Base powder", "Iron 200C", "Rotor horsehair and steel"),
             ("Vauhti GW Polar liquid", "Base liquid", "From bottle + rotor felt", "Fine steel and blue nylon"),
             ("(no base layer)", "-", "-", "-"),
         ],
         others=["Swix HS5", "Swix PS6", "Rode Endurance", "Vauhti GW Polar", "Swix White Marathon block"],
         best_feel="",
         distance="1st and 2nd retested after 8 km: Swix White Marathon an even clearer winner",
         notes="Base-glider test for speed and wear, relevant for long races. Fairly large gaps "
               "further down. Placings are for the base layer; Swix TSP7 was the topcoat on every ski."),
    dict(id="2024-02-22", date="2024-02-22", season="2023/24", title="Fluorfritest 22. februar",
         kind="Topcoat, powder vs liquid (Swix BPL base on all)", air=2, air_hum=99, snow=0,
         snow_temp_est=False, hum_min=50, hum_max=65, snow_type="Coarse, wet", weather="Rain",
         places=[1, 2, 2],
         podium=[
             ("Swix TSP10 + Swix HS10 liquid", "Powder + liquid",
              "Iron 200C; liquid with felt block, cure 20 min, rotor fleece",
              "Rotor horsehair/steel on powder; fine steel and rotor nylon on liquid"),
             ("Toko HP Yellow liquid", "Liquid", "Felt pad, rotor fleece", "Fine steel and rotor nylon"),
             ("Rex NFX11", "Powder", "Iron 200C", "Rotor horsehair and steel"),
         ],
         others=["Toko HP Yellow", "Rex Sisu White", "Skigo FFR Yellow", "Skigo N3", "Vauhti Race Warm Old Snow liquid"],
         best_feel="",
         distance="Rex NFX11 vs Toko HP Yellow liquid after 6 and 12 km: the powder held up somewhat better",
         notes="Powder and liquid test in rain. Surprisingly close at the top, bigger gaps below. "
               "Best pure liquid and best pure powder were equal, just behind the powder + liquid winner. "
               "Rex NFX11 the better choice for a long race in these conditions."),
    dict(id="2024-03-07", date="2024-03-07", season="2023/24", title="Fluorfritest 7. mars",
         kind="Topcoat (Swix BPL base on all)", air=2, air_hum=69, snow=0, snow_temp_est=False,
         hum_min=34, hum_max=34, snow_type="Coarse, transformed", weather="Clear, sun",
         podium=[
             ("Rex G41 liquid", "Liquid", "Sponge on bottle, cure 6 h, rotor felt",
              "Fine steel + rotor horsehair + rotor blue nylon"),
             ("Rex NF41 liquid", "Liquid", "Felt block + rotor felt", "Fine steel + rotor horsehair + rotor blue nylon"),
             ("Toko Jet Yellow + Toko Jet Yellow liquid", "Powder + liquid", "Iron 180C + 2 layers of spray",
              "Rotor horsehair, steel, nylon; liquid: nylon"),
         ],
         others=["Toko HP Yellow", "Toko Jet Yellow", "Star Dark Warm", "Toko Jet Yellow liquid + Toko Jet Yellow",
                 "Toko Jet Red"],
         best_feel="Rex G41 liquid",
         distance="1st and 3rd retested after 10 km: the powder version gained a little, not enough; "
                  "it was slightly better on drier, sun-dried parts of the track",
         notes="New Toko products with different methods, plus new Rex and Star products; Rex G41 "
               "as reference. Rex G41 a clear winner, also best on feel (good release). Curing 6 h "
               "improved durability."),
    # ------------------------------------------------------------- 2024/25
    dict(id="2025-01-09", date="2025-01-09", season="2024/25", title="Fluorfritest 9. januar",
         kind="Topcoat", air=-3, snow=-4, snow_temp_est=True, hum_min=24, hum_max=24,
         snow_type="New snow (nysnø)", weather="Clear, sun",
         podium=[
             ("HWK UHX Red", "Powder", "Iron 200C", "Steel + rotor horsehair + rotor blue nylon"),
             ("Toko HP Red", "Powder", "Iron 200C", "Steel + rotor horsehair + rotor blue nylon"),
             ("Star Next Med", "Powder", "Iron 200C", "Fine steel + rotor horsehair + rotor blue nylon"),
         ],
         others=["Toko Jet Red", "Skigo LDQ", "Rex Sisu Black", "Swix PS6", "Swix TSP6"],
         best_feel="HWK UHX Red",
         notes="All skis had Swix TSP6 as base for the topcoat test. Close at the top, HWK Red slightly "
               "better on speed and feel. Base-layer test (8 options): Swix PS6 (200C) or Swix White "
               "Marathon block stood out."),
    dict(id="2025-01-16", date="2025-01-16", season="2024/25", title="Fluorfritest 16. januar",
         kind="Topcoat", air=4, snow=0, snow_temp_est=True, hum_min=38, hum_max=50,
         snow_type="Coarse, transformed (grovkornet omdannet)", weather="Clear",
         podium=[
             ("HWK UHX Warm powder + HWK UHX Warm liquid", "Powder + liquid",
              "Iron 200C / spray, spread with felt, cure 60 min", "Rotor horsehair / fine steel / nylon + rotor nylon"),
             ("Skigo LDQ", "Powder", "Iron 200C", "Rotor horsehair / fine steel / rotor nylon"),
             ("Swix TSP10 + Toko Jet Warm liquid", "Powder + liquid",
              "Iron 200C / spray directly on ski, cure 60 min", "Horsehair / steel / nylon + no brushing"),
         ],
         others=["Swix TSP10 + Swix TS10", "Skigo GRP + Skigo LDQ", "Rex NFX41", "Swix PS6 + Rex G41 liquid", "Swix PS6"],
         best_feel="HWK UHX Warm powder + HWK UHX Warm liquid",
         notes="Snow humidity 38% before, 50% after the test. Even between top 3, clear advantage on "
               "slip/feel with liquid topping. LDQ without GRP base best at first, but after 6 km the "
               "GRP-base pair recovered half the gap."),
    dict(id="2025-01-30", date="2025-01-30", season="2024/25", title="Fluorfritest 30. januar",
         kind="Topcoat", air=-1.5, snow=-1, snow_temp_est=False, hum_min=24, hum_max=32,
         snow_type="Coarse, transformed (refrozen)", weather="Fog",
         podium=[
             ("Skigo LDQ", "Powder", "Iron 200C", "Rotor horsehair / rotor steel / rotor nylon"),
             ("Swix White Marathon + Swix TS6 liquid", "Powder + spray",
              "Iron 200C + spray with felt", "Rotor horsehair / steel / nylon + fleece/blue nylon"),
             ("Swix PS6", "Glider", "Swix Wax Machine + iron 200C", "Rotor horsehair / steel / nylon"),
         ],
         others=["Swix PS6 (other method)", "Vauhti LDR Old Snow", "Skigo LDQ + Toko Jet Med liquid",
                 "Swix TSB8", "HWK UHX Red"],
         best_feel="",
         notes="Frozen overnight after rain/mild days. Top 2 even, bigger gaps further down. "
               "5 km distance test LDQ vs Marathon+TS6: result held. Considered relevant for "
               "Ungdommens Holmenkollrenn."),
    dict(id="2025-02-06", date="2025-02-06", season="2024/25", title="Fluorfritest 6. februar",
         kind="Topcoat", air=2, snow=-2, snow_temp_est=False, hum_min=38, hum_max=38,
         snow_type="Coarse (grovkornet)", weather="Sun",
         podium=[
             ("HWK UHX Red", "Powder", "Iron 200C", "Steel hand / rotor horsehair / rotor steel / rotor nylon"),
             ("Rex Sisu White", "Powder", "Iron 200C", "Steel hand / rotor horsehair / rotor steel / rotor nylon"),
             ("Toko HP Red", "Powder", "Iron 200C", "Steel hand / rotor horsehair / rotor steel / rotor nylon"),
         ],
         others=["Swix PS6", "Swix PM-25", "Star Next Med", "Star Next Warm powder + spray"],
         best_feel="",
         notes="Cold night, rising temperature during the day. Powder with spray on top was somewhat "
               "behind today."),
    dict(id="2025-02-13", date="2025-02-13", season="2024/25", title="Fluorfritest 13. februar",
         kind="Topcoat", air=0, snow=-4, snow_temp_est=False, hum_min=34, hum_max=34,
         snow_type="Coarse (grovkornet)", weather="Sun",
         podium=[
             ("Skigo LDQ", "Powder", "Iron 200C", "Steel hand / rotor horsehair / rotor steel / rotor nylon"),
             ("Star Next Med", "Powder", "Iron 200C", "Steel hand / rotor horsehair / rotor steel / rotor nylon"),
             ("HWK UHX Red", "Powder", "Iron 200C", "Steel hand / rotor horsehair / rotor steel / rotor nylon"),
         ],
         others=["Star Dark Next Med", "Rode RX22", "Red Creek Blue glider", "Rode RX22 + Rode RXL Cold liquid"],
         best_feel="",
         notes="A few minus degrees overnight, near 0 in the morning. Very little separated LDQ and "
               "Star Next Med. 'LDQ as usual at the top on this snow.'"),
    dict(id="2025-02-20", date="2025-02-20", season="2024/25", title="Fluorfritest 20. februar",
         kind="Topcoat (liquids, LDQ as reference)", air=-4, snow=-3.5, snow_temp_est=False, hum_min=35, hum_max=40,
         snow_type="Coarse (grovkornet)", weather="Overcast",
         podium=[
             ("Star Next Med liquid", "Liquid", "Felt applicator x2", "Fine steel hand / rotor blue nylon"),
             ("Skigo LDQ", "Powder", "Iron 200C", "Steel hand / rotor horsehair / rotor steel / rotor nylon"),
             ("Star Next Med liquid (ironed 120C)", "Liquid", "Felt + iron 120C", "Fine steel / rotor nylon"),
         ],
         others=["Red Creek -3/-20 liquid", "Vauhti Cold Old Snow", "Rode RX32 + Rode RXL Med liquid",
                 "Toko HP Blue", "Toko Jet Blue"],
         best_feel="",
         notes="Down to -7 overnight, high air humidity. Tested how cold-snow products tolerate "
               "moister/milder snow (relevant for long races with changing conditions)."),
    dict(id="2025-02-25", date="2025-02-25", season="2024/25", title="Underlagstest 25.2.2025",
         kind="Base layer (topcoat Swix White Marathon powder on all)", air=2, snow=0, snow_temp_est=False,
         hum_min=56, hum_max=70, snow_type="Coarse, wet (grov våt)", weather="Overcast",
         podium=[
             ("Skigo GRP + Skigo FFC Yellow", "Liquid + glider", "Felt + iron 200C",
              "Rotor horsehair/steel + steel hand, rotor horsehair/steel"),
             ("Rex Sisu White", "Glider", "Iron 200C", "Steel hand / rotor horsehair / rotor steel / rotor nylon"),
             ("Rode Endurance", "Glider", "Iron 200C", "Steel hand / rotor horsehair / rotor steel"),
         ],
         others=["Skigo FFC Yellow", "Swix White Marathon", "Washed ski (Toko racing wax remover)",
                 "Star Durable Long Distance Dark", "Swix PS6"],
         best_feel="",
         distance="5 km retest: 1. Swix PS6, 2. Skigo GRP + Skigo FFC Yellow (GRP lost a lot after 5 km)",
         notes="Base-layer test ahead of Holmenkollmarsjen and Vasaloppet. GRP gave a big lift but "
               "faded badly after 5 km, so not recommended for distance. Theory: GRP was the key, a "
               "different glider on top would hold up better."),
    dict(id="2025-02-27", date="2025-02-27", season="2024/25", title="Topprodukt 27. februar",
         kind="Topcoat", air=2, snow=-1, snow_temp_est=False, hum_min=68, hum_max=68,
         snow_type="Coarse, wet, loose", weather="",
         podium=[
             ("Skigo LDQ", "Powder", "Iron 200C", "Steel hand / rotor horsehair / rotor steel / rotor nylon"),
             ("Rex NFX11", "Powder", "Iron 200C", "Steel hand / rotor horsehair / rotor steel / rotor nylon"),
             ("Toko HP Yellow", "Powder", "Iron 200C", "Steel hand / rotor horsehair / rotor steel / rotor nylon"),
         ],
         others=["Star Dark Warm", "Swix White Marathon", "HWK UHX Warm", "HWK UHX Middle", "Swix PS6"],
         best_feel="",
         notes="Topcoat test ahead of Holmenkollmarsjen. LDQ named the safe choice; expected to be "
               "at least as good on firmer/drier tracks."),
    dict(id="2025-03-27", date="2025-03-27", season="2024/25", title="Glidtest 27.3.2025 (Holmenkollen)",
         kind="Topcoat (liquid vs powder)", air=8, snow=0, snow_temp_est=False, hum_min=90, hum_max=100,
         snow_type="Coarse, wet, dirty", weather="Sun",
         podium=[
             ("Skigo GRP", "Liquid", "Sponge applicator, dry 15 min",
              "Fine steel hand + rotor horsehair + rotor nylon"),
             ("Swix PC100", "Powder", "Iron 200C", "Rotor steel/horsehair, fine steel hand + rotor nylon"),
             ("Skigo LDQ", "Liquid", "Iron 200C", "Rotor steel/horsehair, fine steel hand + rotor nylon"),
         ],
         others=["Skigo FFR Yellow", "Skigo LDQ/FFR Yellow 50/50", "Block Y + HWK FFL34",
                 "Rode RW50 + HWK FFL34", "Skigo LDQ + Skigo FFR Yellow liquid"],
         best_feel="",
         distance="Top 2 retested after 10 km: same result (equal durability)",
         notes="Wet, dirty snow in Holmenkollen. Fairly clear winner, closer further down. "
               "All skis had Swix Pro Cleaner as base."),
    # ------------------------------------------------------------- 2025/26
    # The two 8 Jan reports are named "08.01.2025" on the site, but they were
    # uploaded in Jan 2026 and listed under 2026, so they are dated 2026-01-08.
    dict(id="2026-01-08a", date="2026-01-08", season="2025/26", title="Fluorfritest 08. januar (powder)",
         kind="Topcoat (powders, same method)", air=-11, snow=-6, snow_temp_est=False, hum_min=19, hum_max=21,
         snow_type="Fine-grained, cold (finkornet)", weather="Clear",
         podium=[
             ("Toko HP Blue", "Powder", "Iron 200C", "Rotor horsehair / rotor steel / rotor nylon"),
             ("Rex NFX21G", "Powder", "Iron 200C", "Rotor horsehair / rotor steel / rotor nylon"),
             ("Toko Jet Cold", "Powder", "Iron 200C", "Rotor horsehair / rotor steel / rotor nylon"),
         ],
         others=["Swix PF25", "Optiwax test powder", "HWK test powder", "Star Next Cold", "Toko Jet White"],
         best_feel="Toko HP Blue",
         notes="HP Blue and Rex 21G almost equal on glide; HP Blue best feel and best overall. "
               "Toko Jet Cold slightly behind but competitive. In hindsight Star Next Cold should have "
               "been ironed at 180C."),
    dict(id="2026-01-08b", date="2026-01-08", season="2025/26", title="Fluorfritest 08. januar del 2 (method)",
         kind="Method / combinations on Toko HP Blue", air=-8, snow=-4.5, snow_temp_est=False, hum_min=22, hum_max=25,
         snow_type="Fine-grained (finkornet)", weather="Clear",
         podium=[
             ("Toko HP Blue + Rode RW20", "Powder + block", "Iron 200C + wool",
              "Rotor horsehair / steel / nylon + wool"),
             ("Swix PS6 + Toko HP Blue", "Glider + powder", "Iron 200C", "Rotor horsehair / steel / nylon"),
             ("Toko HP Blue", "Powder", "Iron 200C", "Rotor horsehair / steel / nylon"),
         ],
         others=["Toko SJX + Toko HP Blue", "Toko HP Blue + Swix test product",
                 "Toko HP Blue + Toko Jet White", "Toko HP Blue + Toko Jet Mid"],
         best_feel="",
         notes="PS6 base at 200C lifts plain HP Blue by 20 cm; Rode RW20 wool on top lifts HP Blue by "
               "40 cm. Recommendation: Swix PS6 + Toko HP Blue + Rode RW20."),
    dict(id="2026-01-15", date="2026-01-15", season="2025/26", title="Fluorfritest 15. januar",
         kind="Topcoat (Swix PS6 base on all)", air=-2, snow=-2, snow_temp_est=False, hum_min=25, hum_max=29,
         snow_type="New snow, medium grains", weather="Fog, snowing",
         podium=[
             ("Swix PF35", "Powder", "Iron 200C", "Rotor horsehair / rotor steel / rotor nylon"),
             ("Vola NSD2325", "Powder", "Iron 200C", "Rotor horsehair / rotor steel / rotor nylon"),
             ("Toko Jet Mid liquid", "Liquid", "Spray, dry 20 min", "No brushing"),
         ],
         others=["Swix PS6", "Toko Jet White", "Optiwax KM50", "Swix PC35", "Toko HP Red"],
         best_feel="Toko Jet Mid liquid",
         notes="Toko Jet Mid liquid best on feel; it lifted plain Swix PS6 by 40 cm, could likely lift "
               "PF35 too."),
    dict(id="2026-01-29", date="2026-01-29", season="2025/26", title="Fluorfritest 29. januar",
         kind="Topcoat", air=-11, snow=-10, snow_temp_est=False, hum_min=25, hum_max=34,
         snow_type="Mixed (coarse below, fine on top)", weather="Clear, sun",
         podium=[
             ("Toko HP Blue", "Powder", "Iron 200C", "Rotor horsehair / rotor steel / rotor nylon"),
             ("Red Creek Old Fashion Green", "Glider", "Iron 200C", "Rotor horsehair / rotor steel / rotor nylon"),
             ("Star Next Cold", "Powder", "Iron 200C", "Rotor horsehair / rotor steel / rotor nylon"),
         ],
         others=["Rode RX22", "Swix White Marathon", "Skigo FFR Blue", "Swix PF35", "Toko HP Red"],
         best_feel="Star Next Cold",
         notes="Star Next Cold just behind on pure glide but clearly best on feel. Relevant for "
               "Kvalfosssprinten (skate) where feel matters a lot."),
    dict(id="2026-02-05", date="2026-02-05", season="2025/26", title="Fluorfritest 5. februar",
         kind="Topcoat", air=-10, snow=-8, snow_temp_est=False, hum_min=23, hum_max=39,
         snow_type="Mixed (coarse below, finer on top)", weather="Clear, a little snow in the air",
         podium=[
             ("Swix PM Molybdenum", "Powder", "Iron 200C", "Rotor horsehair / rotor steel / rotor nylon"),
             ("Vauhti Race Pink", "Powder", "Iron 200C", "Rotor horsehair / rotor steel / rotor nylon"),
             ("Toko Jet Mid", "Powder", "Iron 200C", "Rotor horsehair / rotor steel / rotor nylon"),
         ],
         others=["Skigo Booster Cold + Toko HP Blue", "Toko HP Blue", "Skigo LDQ", "Rex Sisu White", "Star Next Med"],
         best_feel="Toko Jet Mid",
         notes="39% humidity in the track, 23% on the new snow on top. Toko Jet Mid slightly behind on "
               "glide, best on feel. Skigo Booster under powder gave a lift. Liquid on top did not lift."),
    dict(id="2026-02-19", date="2026-02-19", season="2025/26", title="Fluorfritest 19. februar",
         kind="Base + topcoat combinations", air=-8, snow=-11, snow_temp_est=False, hum_min=23, hum_max=42,
         snow_type="Fine-grained", weather="Clear",
         podium=[
             ("Skigo Booster Cold + Vola NSD2319", "Liquid + powder", "Sponge + iron 200C",
              "Rotor horsehair / rotor steel / rotor nylon"),
             ("Swix PS6", "Glider", "Iron 200C", "Rotor horsehair / rotor steel / rotor nylon"),
             ("Swix PS6 + Rode RW20", "Glider + block", "Iron 200C + wool block",
              "Rotor horsehair / steel / nylon + wool"),
         ],
         others=["Toko HP Blue", "Toko HP Blue/Skigo LDQ 50/50", "Swix HS6", "Vola NSD2319", "Vola HM Race Purple"],
         best_feel="Skigo Booster Cold + Vola NSD2319",
         distance="5 km: Skigo Booster Cold + Vola NSD2319 gained 20 cm vs Swix PS6",
         notes="Surprisingly moist snow (39% track, 23% top) after a long cold period. Booster Cold gave "
               "a big lift vs plain NSD2319. Toko Jet Cold liquid sprayed on top after the final lifted 20 cm."),
    dict(id="2026-02-26", date="2026-02-26", season="2025/26", title="Fluorfritest 26. februar",
         kind="Topcoat", air=1, snow=-2, snow_temp_est=False, hum_min=71, hum_max=96,
         snow_type="Wet", weather="Rain and fog",
         podium=[
             ("Skigo FFR Yellow", "Powder", "Iron 200C", "Rotor horsehair / rotor steel / rotor nylon"),
             ("Skigo FFR Yellow + Skigo CM26", "Powder + block", "Iron 200C + iron 120C",
              "Rotor horsehair / rotor steel / rotor nylon"),
             ("Star Next Dark Wet", "Powder", "Iron 200C", "Rotor horsehair / rotor steel / rotor nylon"),
         ],
         others=["Skigo CM26", "Star Next KC001", "Vola NSD2415", "Skigo CM26 + Skigo FFR Yellow",
                 "Toko Jet Warm liquid"],
         best_feel="Skigo FFR Yellow",
         notes="96% humidity in the track, 71% on top. FFR Yellow the clear winner on glide and feel. "
               "CM26 over or under FFR Yellow gave no lift. Separate 4-pair liquid series: Toko Jet Warm "
               "and HWK UHX Warm stood out on speed and feel."),
    dict(id="2026-03-19", date="2026-03-19", season="2025/26", title="Glidtest World Cup Skiskyting 19. mars",
         kind="Topcoat (liquids)", air=6, snow=0, snow_temp_est=False, hum_min=70, hum_max=70,
         snow_type="Coarse, moist, salted tracks", weather="Sun",
         podium=[
             ("Toko Prototype liquid", "Liquid", "Spray", "None"),
             ("Rode RW50", "Block", "Rubbed on", "Rotor felt + rotor wool"),
             ("Toko Jet Warm liquid", "Liquid", "Spray", "None"),
         ],
         others=["Skigo FFR Yellow", "Rode Superwet liquid", "Toko Jet Black liquid", "Star Next Warm liquid",
                 "HWK FFL34 liquid"],
         best_feel="Toko Prototype liquid",
         distance="Toko Prototype gained considerably after distance; Rode RW50 lost to liquid on retest",
         notes="Before the biathlon World Cup in Holmenkollen. Salted tracks. Toko Prototype best on glide "
               "and feel. Toko Jet Warm a very good, competitive alternative."),
    dict(id="2026-03-26", date="2026-03-26", season="2025/26", title="Fluorfritest 26. mars",
         kind="Method / brushes / combinations", air=8, snow=0, snow_temp_est=False, hum_min=90, hum_max=90,
         snow_type="Coarse, moist", weather="Sun",
         podium=[
             ("Toko Prototype liquid + Skigo FFR Yellow + Toko Prototype liquid", "Liquid + powder + liquid",
              "Spray + iron 200C + spray", "Red Creek rotor horsehair / rotor steel / rotor nylon on powder"),
             ("Skigo FFC Yellow + Skigo FFR Yellow", "Glider + powder", "Iron 125C + iron 200C",
              "Rotor horsehair / rotor steel / rotor nylon"),
             ("Toko Prototype liquid (x2)", "Liquid", "Spray the day before + spray right before", "None"),
         ],
         others=["Skigo FFR Yellow", "Toko Prototype liquid", "Skigo FFR Yellow (Skigo horsehair+steel+nylon brushes)",
                 "Skigo FFR Yellow (Toko horsehair+copper+nylon brushes)"],
         best_feel="Toko Prototype liquid + Skigo FFR Yellow + Toko Prototype liquid",
         notes="Focus on method and brushes. Winner best on pure glide and feel. FFC Yellow + FFR Yellow "
               "just behind on glide, heavier feel. Toko Prototype also good alone (sprayed twice or once)."),
]


# Components a combination is made of, for per-product statistics. Anything
# not listed here is its own single component. Variants that are the same
# product with a different method collapse to the product.
COMPONENTS = {
    "HWK UHX Warm powder + HWK UHX Warm liquid": ["HWK UHX Warm"],
    "Swix TSP10 + Toko Jet Warm liquid": ["Swix TSP10", "Toko Jet Warm liquid"],
    "Skigo GRP + Skigo LDQ": ["Skigo GRP", "Skigo LDQ"],
    "Swix PS6 + Rex G41 liquid": ["Swix PS6", "Rex G41 liquid"],
    "Swix White Marathon + Swix TS6 liquid": ["Swix White Marathon", "Swix TS6 liquid"],
    "Swix PS6 (other method)": ["Swix PS6"],
    "Skigo LDQ + Toko Jet Med liquid": ["Skigo LDQ", "Toko Jet Med liquid"],
    "Star Next Warm powder + spray": ["Star Next Warm"],
    "Rode RX22 + Rode RXL Cold liquid": ["Rode RX22", "Rode RXL Cold liquid"],
    "Star Next Med liquid (ironed 120C)": ["Star Next Med liquid"],
    "Rode RX32 + Rode RXL Med liquid": ["Rode RX32", "Rode RXL Med liquid"],
    "Skigo GRP + Skigo FFC Yellow": ["Skigo GRP", "Skigo FFC Yellow"],
    "Skigo LDQ/FFR Yellow 50/50": ["Skigo LDQ", "Skigo FFR Yellow"],
    "Block Y + HWK FFL34": ["Block Y", "HWK FFL34 liquid"],
    "Rode RW50 + HWK FFL34": ["Rode RW50", "HWK FFL34 liquid"],
    "Skigo LDQ + Skigo FFR Yellow liquid": ["Skigo LDQ", "Skigo FFR Yellow liquid"],
    "Toko HP Blue + Rode RW20": ["Toko HP Blue", "Rode RW20"],
    "Swix PS6 + Toko HP Blue": ["Swix PS6", "Toko HP Blue"],
    "Toko SJX + Toko HP Blue": ["Toko SJX", "Toko HP Blue"],
    "Toko HP Blue + Swix test product": ["Toko HP Blue"],
    "Toko HP Blue + Toko Jet White": ["Toko HP Blue", "Toko Jet White"],
    "Toko HP Blue + Toko Jet Mid": ["Toko HP Blue", "Toko Jet Mid"],
    "Skigo Booster Cold + Toko HP Blue": ["Skigo Booster Cold", "Toko HP Blue"],
    "Skigo Booster Cold + Vola NSD2319": ["Skigo Booster Cold", "Vola NSD2319"],
    "Swix PS6 + Rode RW20": ["Swix PS6", "Rode RW20"],
    "Toko HP Blue/Skigo LDQ 50/50": ["Toko HP Blue", "Skigo LDQ"],
    "Skigo FFR Yellow + Skigo CM26": ["Skigo FFR Yellow", "Skigo CM26"],
    "Skigo CM26 + Skigo FFR Yellow": ["Skigo CM26", "Skigo FFR Yellow"],
    "Toko Prototype liquid + Skigo FFR Yellow + Toko Prototype liquid": ["Toko Prototype liquid", "Skigo FFR Yellow"],
    "Skigo FFC Yellow + Skigo FFR Yellow": ["Skigo FFC Yellow", "Skigo FFR Yellow"],
    "Toko Prototype liquid (x2)": ["Toko Prototype liquid"],
    "Skigo FFR Yellow (Skigo horsehair+steel+nylon brushes)": ["Skigo FFR Yellow"],
    "Skigo FFR Yellow (Toko horsehair+copper+nylon brushes)": ["Skigo FFR Yellow"],
    "Washed ski (Toko racing wax remover)": ["(washed ski, no wax)"],
    "Swix TSP10 + Swix TS10": ["Swix TSP10", "Swix TS10 liquid"],
    "Swix TSP5 (ironed 160C)": ["Swix TSP5"],
    "Maplus Base Gel + Maplus Boost liquid": ["Maplus Base Gel", "Maplus Boost liquid"],
    "Maplus GM Hot + Maplus Boost Hot liquid": ["Maplus GM Hot", "Maplus Boost Hot liquid"],
    "Rode Endurance + Rode RXL Warm liquid": ["Rode Endurance", "Rode RXL Warm liquid"],
    "Swix White Marathon + Swix TST8 block": ["Swix White Marathon", "Swix TST8 block"],
    "Maplus BP1 Hot (with wool)": ["Maplus BP1 Hot"],
    "Swix TSP10 + Swix HS10 liquid": ["Swix TSP10", "Swix HS10 liquid"],
    "Toko Jet Yellow + Toko Jet Yellow liquid": ["Toko Jet Yellow", "Toko Jet Yellow liquid"],
    "Toko Jet Yellow liquid + Toko Jet Yellow": ["Toko Jet Yellow liquid", "Toko Jet Yellow"],
}


def podium_places(t):
    """[(place, name, type, application, removal)] - handles tied places."""
    places = t.get("places") or list(range(1, len(t["podium"]) + 1))
    return [(p, *row) for p, row in zip(places, t["podium"])]


def components(name):
    return COMPONENTS.get(name, [name])


def hum_mid(t):
    return (t["hum_min"] + t["hum_max"]) / 2


def condition_class(t):
    """Three condition groups, mainly driven by snow humidity (the metric the
    reports themselves lead with) and snow temperature."""
    h = hum_mid(t)
    if h >= 55:
        return "C: Wet (>=55% humidity, snow ~0C)"
    if t["snow"] <= -4.5 or (h < 25 and t["snow"] <= -3):
        return "A: Cold / dry (snow <= -4.5C, or <25% humidity and snow <= -3C)"
    return "B: Medium / transformed (<55% humidity, snow -4.5 to 0C)"


# Placing points: winner 3, 2nd 2, 3rd 1, tested but off the podium 0.
# Tied products get the points of the shared place (1=, 1= -> 3 each).
POINTS = {1: 3, 2: 2, 3: 1}


# Snow type (grain) per test, grouped from each report's "Snø:" line:
#   new           new / fresh / falling snow
#   new_over_old  new snow on top of older transformed snow ("mixed")
#   fine          fine-grained, cold old snow (finkornet)
#   transformed   coarse / transformed, not wet (grovkornet, omdannet)
#   wet           wet coarse snow, slush
# 2024-01-11 ("natural snow on man-made base", +4.8 C air) is counted as transformed.
SNOW_TYPE = {
    "2023-12-14": "new",
    "2024-01-18": "new",
    "2024-02-15": "new",
    "2025-01-09": "new",
    "2026-01-15": "new",
    "2024-01-25": "new_over_old",
    "2024-01-26": "new_over_old",
    "2024-02-01": "new_over_old",
    "2024-02-02": "new_over_old",
    "2024-02-08": "new_over_old",
    "2026-01-29": "new_over_old",
    "2026-02-05": "new_over_old",
    "2026-01-08a": "fine",
    "2026-01-08b": "fine",
    "2026-02-19": "fine",
    "2024-01-11": "transformed",
    "2024-03-07": "transformed",
    "2025-01-16": "transformed",
    "2025-01-30": "transformed",
    "2025-02-06": "transformed",
    "2025-02-13": "transformed",
    "2025-02-20": "transformed",
    "2024-02-22": "wet",
    "2025-02-25": "wet",
    "2025-02-27": "wet",
    "2025-03-27": "wet",
    "2026-02-26": "wet",
    "2026-03-19": "wet",
    "2026-03-26": "wet",
}

SNOW_TYPES = ["new", "fine", "new_over_old", "transformed", "wet"]
SNOW_TYPE_LABELS = {
    "new": "New / falling snow",
    "fine": "Fine-grained, cold",
    "new_over_old": "New snow on old",
    "transformed": "Transformed / coarse",
    "wet": "Wet / slush",
}

# How much a test with snow type b counts when you are waxing for snow type a.
SNOW_TYPE_SIM = {
    "new":          {"new": 1.0, "fine": 0.6, "new_over_old": 0.6, "transformed": 0.2, "wet": 0.1},
    "fine":         {"new": 0.6, "fine": 1.0, "new_over_old": 0.5, "transformed": 0.3, "wet": 0.1},
    "new_over_old": {"new": 0.6, "fine": 0.5, "new_over_old": 1.0, "transformed": 0.5, "wet": 0.2},
    "transformed":  {"new": 0.2, "fine": 0.3, "new_over_old": 0.5, "transformed": 1.0, "wet": 0.4},
    "wet":          {"new": 0.1, "fine": 0.1, "new_over_old": 0.2, "transformed": 0.4, "wet": 1.0},
}


def snow_type(t):
    return SNOW_TYPE[t["id"]]
