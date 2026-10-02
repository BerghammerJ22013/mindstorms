# Phase 4 – Bauanleitung (Gerüst, Stand 2026-10-02)

Die Schritte folgen den Submodellen in `model/racecar.mpd` (`0 STEP` je Teil). **Noch nicht verwendbar:** Der Balkenrahmen und alle Pin-/Achsverbindungen fehlen im Modell, daher gibt es noch keine Schrittbilder und kein PDF. Aufgabe fürs Team: Modell in Stud.io öffnen, Rahmen ergänzen, dann PDF über Stud.io oder LPub3D exportieren.

1. **Chassis:** EV3-Brick (95646c01) mittig, Akku eingelegt.
2. **Antrieb:** je 1 Large Motor (95658) links/rechts hinten, direkt auf Rad (Felge 56908 + Reifen 41897) oder über eine Übersetzungsstufe. Prüfen: Räder laufen frei und lange nach, Zahnradspiel gering.
3. **Lenkung:** Medium Motor (99455) vorn, Lego-Zentrallenkung, Vorderräder (Reifen 2815) lenkbar. Prüfen: Lenkausschlag beidseitig gleich.
4. **Sensorik:** Gyro (99380) mittig über der Achse, Ultraschall (95652) vorn auf dem Sensorhalter (`cad/sensor_halter.scad`).
5. **Kabel:** kurz verlegen und fixieren, Ports wie in `src/main.py` (A/D Antrieb, B Lenkung, S1 Gyro, S2 Ultraschall).
6. **Funktionstest:** Motoren einzeln drehen, Gyro/Ultraschall am Display lesen (`brick.battery.voltage()` loggen), dann Lauf nach `docs/07_tests.md`.
