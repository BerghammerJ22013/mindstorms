# TODO & Plan – Mindstorms-Rennauto (Stand 2026-10-02)

Legende: `[ ]` offen · `[x]` erledigt. Wer = Rolle laut Team (PO, Mechanik, Software, Druck/CAD, Test).

## Meilenstein 0 – Kundengespräch bis **16.10.2026**
- [ ] `docs/00_kundenkonzept.md` im Team durchgehen und mit dem Kunden besprechen (PO)
- [ ] Fragen an den Kunden klären: Fremdmotor-Limit, gedruckte Räder = "Lego-Rad"?, bleibt die Bluetooth-Dongle-Regel (kein Wireless)?, Meilenstein-Termine (PO)
- [ ] Zweites Set bestätigen lassen (wir planen mit einem Set) (PO)
- [ ] Kamera ja/nein entscheiden (Preis, Aufwand) (Team)

## Bestellung
- [ ] `bom/bricklink_wanted.xml` bei BrickLink hochladen (2 große Räder + 2 Reifen), Händler **bricksbyaj**, Warenkorb ca. 4,98 € inkl. Versand (PO)
- [ ] Menge je Lot im Warenkorb prüfen (2 Stück), dann bestellen (PO)
- [ ] Optional: `bom/bricklink_wanted_ersatz.xml` in dieselbe Bestellung, Preise in `bom/ersatzteile.csv` eintragen (PO)
- [ ] Budget in `docs/05_budget.md` nachführen, Limit 200 € inkl. Filament (PO)

## Hardware messen (Mechanik/Test)
- [ ] Motordaten messen (Leerlauf-Speed in deg/s, `brick.battery.voltage()`), in `docs/07_tests.md` eintragen
- [ ] Werte in `tools/speed_calc.py` einsetzen (`MOTOR_RPM`, `STALL_NCM`, `MASS_KG`, `MU`), Übersetzung festlegen
- [ ] EV3 MicroPython auf microSD (4–32 GB) installieren, Sensoren am Brick testen (Software)

## 3D-Druck (Druck/CAD)
- [ ] `cad/toleranz_test.scad` drucken (PLA), passende Lochmaße ermitteln
- [ ] `pin_d` in `cad/sensor_halter.scad` und `cad/pi_halter.scad` anpassen, STL neu exportieren
- [ ] Sensor-Frontplatte drucken und anpassen
- [ ] Pi-Halter nur, wenn Pi/Kamera gekauft wird (Lochabstand am Board nachmessen)
- [ ] Drucker-Modell der Schule notieren

## Modell & Anleitung (Mechanik)
- [ ] `model/racecar.mpd` in Stud.io öffnen, Balkenrahmen, Achsen, Pin-Verbindungen ergänzen
- [ ] Hinweis: Rad = Felge 56908 + Reifen 41897; Set hat nur 2 Paare, daher 2. Paar bestellen
- [ ] Anleitung als PDF exportieren (Stud.io/LPub3D), `docs/04_bauanleitung.md` mit Bildern ergänzen
- [ ] Auto bauen (Antrieb hinten: 1 Large Motor je Hinterrad, Lenkung vorn mit Medium Motor)

## Software (Software)
- [ ] `src/main.py` auf dem Brick testen, Ports anpassen (A/D Antrieb, B Lenkung, S1 Gyro, S2 Ultraschall)
- [ ] Beschleunigungsrampe, Gyro-Geradeauslauf, Wandausweichen abstimmen
- [ ] Optional: Kamera am Pi per Kabel anbinden (Brick bleibt Pflicht-Steuerung)

## Test & Optimierung (Test)
- [ ] Mindestens 5 dokumentierte Läufe (`docs/07_tests.md`), nur eine Variable pro Lauf
- [ ] Immer Akkustand loggen, mit vollem Akku testen
- [ ] Teams kontrollieren sich gegenseitig: Regelkonformität vor Meilenstein prüfen

## Definition of Done
- [ ] Alle offenen Kundenfragen beantwortet
- [ ] Auto fährt autonom im Gang, liest Sensor und lenkt per Brick
- [ ] Anleitung als PDF, Fehlteile bestellt, Budget ≤ 200 €
- [ ] 5 Testläufe mit Zeiten dokumentiert

## Bekannte Lücken
- Motordaten und Gewicht sind Annahmen (siehe `docs/01_recherche.md`, `tools/speed_calc.py`)
- LDraw-Modell ist ein Platzhalter-Layout, Verbindungen ungeprüft (`docs/03_modell.md`)
- Felge/Reifen-Passung aus Maßen abgeleitet, nicht bestätigt
