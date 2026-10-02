"""Bounding-Box (LDU) eines LDraw-Teils, rekursiv ueber Untermodelle. Aufruf: ldraw_bbox.py <LDRAW_DIR> <teil> ..."""
import os, sys, functools

def make(root):
    def find(name):
        n = name.replace("\\", "/").lower()
        for d in ("parts", "p", "parts/s", "p/48", "models"):
            f = os.path.join(root, d, n)
            if os.path.exists(f): return f
    @functools.lru_cache(None)
    def bbox(name):
        f = find(name)
        if not f: return None
        lo = [1e9] * 3; hi = [-1e9] * 3
        def add(pt):
            for i in range(3): lo[i] = min(lo[i], pt[i]); hi[i] = max(hi[i], pt[i])
        for line in open(f, errors="ignore"):
            t = line.split()
            if not t: continue
            if t[0] in ("3", "4"):
                v = list(map(float, t[2:2 + (9 if t[0] == "3" else 12)]))
                for k in range(0, len(v), 3): add(v[k:k + 3])
            elif t[0] == "1":
                x, y, z, a, b, c, d, e, f2, g, h, i = map(float, t[2:14])
                sub = bbox(" ".join(t[14:]))
                if not sub: continue
                for cx in (sub[0][0], sub[1][0]):
                    for cy in (sub[0][1], sub[1][1]):
                        for cz in (sub[0][2], sub[1][2]):
                            add((a*cx+b*cy+c*cz+x, d*cx+e*cy+f2*cz+y, g*cx+h*cy+i*cz+z))
        return (tuple(lo), tuple(hi)) if lo[0] < 1e8 else None
    return bbox

if __name__ == "__main__":
    bb = make(sys.argv[1])
    for p in sys.argv[2:]:
        r = bb(p + ".dat")
        print(p, None if not r else [round(h - l) for l, h in zip(*r)], r)
