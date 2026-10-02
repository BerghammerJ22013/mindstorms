"""Erzeugt model/racecar.mpd (Platzhalter-Layout) und prueft: Teile-ID vorhanden, Menge <= Inventar, keine Box-Kollision.
LDraw: 1 LDU = 0.4 mm, y zeigt nach unten, Fahrtrichtung = -z.
Verbindungen (Pin-/Achsloecher) sind NICHT modelliert und NICHT geprueft."""
import csv, itertools, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from ldraw_bbox import make

LDRAW = os.environ.get("LDRAW_DIR", "/tmp/ldraw/ldraw")
bbox = make(LDRAW)
I = (1, 0, 0, 0, 1, 0, 0, 0, 1)
ROT_Y90 = (0, 0, 1, 0, 1, 0, -1, 0, 0)   # Raeder: Achse von z nach x

# (submodell, teil, farbe, x, y, z, rotation, label)
P = [
 ("chassis", "95646c01", 15, 0, 0, 0, I, "EV3 Brick"),
 ("antrieb", "95658", 71, -150, 70, 101, I, "Large Motor links"),
 ("antrieb", "95658", 71, 150, 70, 101, I, "Large Motor rechts"),
 ("antrieb", "56908", 71, -260, 50, 60, ROT_Y90, "Felge links"),
 ("antrieb", "41897", 0, -260, 50, 60, ROT_Y90, "Reifen links"),
 ("antrieb", "56908", 71, 260, 50, 60, ROT_Y90, "Felge rechts"),
 ("antrieb", "41897", 0, 260, 50, 60, ROT_Y90, "Reifen rechts"),
 ("lenkung", "99455", 71, 0, 40, -330, I, "Medium Motor Lenkung"),
 ("lenkung", "2815", 0, -70, 60, -240, ROT_Y90, "Vorderrad links"),
 ("lenkung", "2815", 0, 70, 60, -240, ROT_Y90, "Vorderrad rechts"),
 ("sensorik", "99380", 71, 0, -28, 0, I, "Gyro"),
 ("sensorik", "95652", 71, 0, 30, -359, I, "Ultraschall"),
]

def world(p):
    _, name, _, x, y, z, m, _ = p
    lo, hi = bbox(name + ".dat")
    pts = [(m[0]*a+m[1]*b+m[2]*c+x, m[3]*a+m[4]*b+m[5]*c+y, m[6]*a+m[7]*b+m[8]*c+z)
           for a in (lo[0], hi[0]) for b in (lo[1], hi[1]) for c in (lo[2], hi[2])]
    return [min(q[i] for q in pts) for i in range(3)], [max(q[i] for q in pts) for i in range(3)]

problems = []
inv = {}
for r in csv.DictReader(open("data/set_inventory.csv")):
    if r["ersatzteil"] == "False": inv[r["teil_id"]] = inv.get(r["teil_id"], 0) + int(r["menge"])
used = {}
for p in P:
    used[p[1]] = used.get(p[1], 0) + 1
    if not os.path.exists(f"{LDRAW}/parts/{p[1]}.dat"): problems.append(f"Teil fehlt in LDraw: {p[1]}")
for t, n in used.items():
    if inv.get(t, 0) < n: problems.append(f"Inventar zu klein: {t} braucht {n}, Set hat {inv.get(t, 0)}")
for a, b in itertools.combinations(P, 2):
    if {a[1], b[1]} == {"56908", "41897"}: continue   # Reifen sitzt gewollt auf der Felge
    (l1, h1), (l2, h2) = world(a), world(b)
    if all(l1[i] < h2[i] - 0.5 and l2[i] < h1[i] - 0.5 for i in range(3)):
        problems.append(f"Kollision: {a[7]} <-> {b[7]}")

subs = ["chassis", "antrieb", "lenkung", "sensorik"]
out = ["0 FILE racecar.ldr", "0 Mindstorms Racecar (Platzhalter-Layout)", "0 Author: team", "0 !LICENSE Redistributable under CCAL version 2.0 : see CAreadme.txt"]
for s in subs: out.append(f"1 16 0 0 0 1 0 0 0 1 0 0 0 1 {s}.ldr")
for s in subs:
    out += ["0 FILE " + s + ".ldr", "0 " + s]
    for p in P:
        if p[0] == s:
            _, name, col, x, y, z, m, lab = p
            out += [f"0 // {lab}", f"1 {col} {x} {y} {z} " + " ".join(map(str, m)) + f" {name}.dat", "0 STEP"]
os.makedirs("model", exist_ok=True)
open("model/racecar.mpd", "w").write("\n".join(out) + "\n")
print("Teile im Modell:", len(P), "| Probleme:", len(problems))
for pr in problems: print(" -", pr)
