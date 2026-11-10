"""Bull Superski "Glidprosjektet" fluor-free glide tests, transcribed by hand
from the report images at https://bullsuperski.no/glidprosjektet/ (seasons
2024/25 and 2025/26, 18 reports).

Each test lists:
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
    "Swix TSP10 + Swix TS10": ["Swix TSP10", "Swix TS10"],
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
}


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
    if t["snow"] <= -4.5 or h < 25:
        return "A: Cold / dry (snow <= -4.5C or <25% humidity)"
    return "B: Medium / transformed (25-55% humidity, snow -4 to 0C)"


# Placing points: winner 3, 2nd 2, 3rd 1, tested but off the podium 0.
POINTS = {1: 3, 2: 2, 3: 1}
