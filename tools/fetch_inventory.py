"""Laedt das Teile-Inventar eines Sets von der Rebrickable-API (Key aus REBRICKABLE_API_KEY)."""
import csv, os, sys, time, requests

SET = sys.argv[1] if len(sys.argv) > 1 else "31313-1"
OUT = sys.argv[2] if len(sys.argv) > 2 else "data/set_inventory.csv"
H = {"Authorization": f"key {os.environ['REBRICKABLE_API_KEY']}"}
url = f"https://rebrickable.com/api/v3/lego/sets/{SET}/parts/?page_size=1000&inc_minifig_parts=0"
rows = []
while url:
    r = requests.get(url, headers=H, timeout=30)
    if r.status_code == 429:
        time.sleep(2); continue
    r.raise_for_status()
    d = r.json()
    for p in d["results"]:
        rows.append({
            "quelle": "set1", "teil_id": p["part"]["part_num"], "name": p["part"]["name"],
            "farbe": p["color"]["name"], "farbe_id": p["color"]["id"], "menge": p["quantity"],
            "ersatzteil": p["is_spare"], "bild": p["part"]["part_img_url"],
        })
    url = d["next"]
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
print(f"{SET}: {len(rows)} Zeilen, {sum(r['menge'] for r in rows if not r['ersatzteil'])} Teile -> {OUT}")
