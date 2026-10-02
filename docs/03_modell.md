# Phase 3 – 3D-Modell (Platzhalter-Layout, Stand 2026-10-02)

`tools/build_model.py` erzeugt `model/racecar.mpd` (Submodelle `chassis`, `antrieb`, `lenkung`, `sensorik`, je mit `0 STEP`). LDraw-Bibliothek: `library.ldraw.org/library/updates/complete.zip` (lokal nach `/tmp/ldraw`, `LDRAW_DIR` setzbar).

**Geprüft (automatisch):** alle 12 Teile-IDs existieren in der LDraw-Bibliothek, Mengen liegen im Inventar von 45544-1, keine Bounding-Box-Kollision (Reifen auf Felge ausgenommen).

**NICHT geprüft:** Pin-/Achsverbindungen (Rahmen aus Balken fehlt noch), Öffnen in Stud.io/LeoCAD, Renders (LDView/LeoCAD nicht installiert).

Erkenntnis: 56908 (Felge 43,2 mm) + 41897 (Reifen 56 × 28) ergibt das 56-mm-EV3-Rad, davon gibt es nur **2 pro Set**. Vorne bleiben nur die kleinen 2815-Reifen (ca. 31 mm). Die Passung Felge/Reifen ist aus den Maßen abgeleitet, nicht aus einer Quelle bestätigt.

Nächste Schritte: Rahmen aus Balken (`32316`, `32525`, …) und Achsen ergänzen, Verbindungen am Raster (20 LDU) ausrichten, in Stud.io öffnen und prüfen.
