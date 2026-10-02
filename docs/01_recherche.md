# Phase 1 – Inventar & Recherche (Stand 2026-10-02)

## 1. Set
- Vermutlich **EV3 Education Core Set 45544-1** (547 Teile), von der Schule gestellt, evtl. 2 Stück (nicht bestätigt).
- Quelle: Rebrickable-API, abgerufen 2026-10-02 → `data/set_inventory.csv` (1 Set), `data/combined_inventory.csv` (2 Sets, Spalte `quelle`, 1094 Teile).
- Das ursprünglich geladene Home-Set 31313-1 hat **keinen** Gyro- und Ultraschallsensor und wurde verworfen.

## 2. Elektronik im Set (Quelle: Rebrickable 45544-1)
| Menge | Teil-ID | Name |
|---|---|---|
| 1 | 95646c01 | EV3 Brick |
| 1 | 95656 | Akku (wiederaufladbar) |
| 2 | 95658 | Large Motor |
| 1 | 99455 | Medium Motor |
| 1 | 99380 | Gyro-Sensor |
| 1 | 95652 | Ultraschall-Sensor |
| 1 | 95650 | Farbsensor |
| 2 | 95648 | Touch-Sensor |
| 4/2/1 | 11145/55805/55806 | Kabel 25 / 35 / 50 cm |

Mit 2 Sets: 4 Large + 2 Medium Motoren, 2 Gyro, 2 Ultraschall. Ein EV3-Brick hat 4 Motorports (A–D) und 4 Sensorports (1–4); ein zweiter Brick wird nicht verbaut.

## 3. Räder, Zahnräder, Lenkung (Quelle: Rebrickable 45544-1, pro Set)
- Reifen/Räder: 2× Tyre 56 x 28 ZR Street (41897), 2× Wheel 43.2 x 26 Racing Small (56908), 4× Wedge Belt Wheel Tire (2815). Welche Reifen auf welche Felge passen, ist **nicht verifiziert** (LDraw/Rebrickable-Teilebeziehungen prüfen).
- Zahnräder: 8Z (10928) ×4, 12Z Doppelkegel (32270) ×2, 12Z Kegel (6589) ×2, 16Z (94925) ×4, 20Z Doppelkegel (32269) ×2, 24Z (3648b) ×4, 36Z Doppelkegel (32498) ×2, 40Z (3649) ×2, Schnecke (4716) ×2.
- Lenkung: nur 1× Steering Ball Joint (92911) im Set. Zentrallenkung muss laut Regeln aus Lego sein.
- Ein Differential ist **nicht** im Inventar. Ein Lego-Differential (Teil-ID noch nicht geprüft) müsste ggf. zugekauft werden.

## 4. Firmware (vorläufig)
| | EV3 MicroPython v2.0 (pybricks.com/ev3-micropython) | ev3dev |
|---|---|---|
| Was | Offizielle LEGO-Education-MicroPython-Firmware auf Pybricks-Basis | Debian Linux von microSD, Firmware bleibt unberührt |
| Installation | microSD 4–32 GB (A1 empfohlen), Mini-USB-Kabel | microSD |
| Python | MicroPython, kleine API: `Motor`, `DriveBase`, `GyroSensor`, `UltrasonicSensor` | volles Python + Linux-Pakete |
| Zusatz | Doku zuletzt v2.0 vom 18.05.2020 (Quelle: Doku-Seite) | USB-/Bluetooth-Geräte, Kameras an USB möglich (Quelle: ev3dev.org) |

Vorläufige Empfehlung: **EV3 MicroPython** als Start. Es ist einfach, deckt die Pflicht (Sensor lesen, Lenkmotor ansteuern) ab, und ein Raspberry Pi mit Kamera würde per Kabel angebunden. ev3dev wäre erst nötig, wenn Kamera/USB direkt am Brick hängen soll. Funktioniert Gyro-Geradeauslauf in MicroPython sauber, ist das nicht verifiziert und wird in Phase 6/7 getestet.

## 5. Motordaten – NICHT verifiziert
Drehzahl, Drehmoment und Strom von Large/Medium Motor stehen hier bewusst nicht. Die übliche Quelle (philohome.com) liefert hier nur eine JS-Prüfseite, ev3dev nennt nur die Spannung 9 V und "no load" ohne Zahlen im abgerufenen Ausschnitt. Offen: Werte aus einer prüfbaren Quelle holen oder am Auto selbst messen (`motor.speed()` und `battery.voltage()`).

## 6. Offene Punkte
- Set-Typ bestätigen (45544 beider Sets?).
- Fremdmotoren erlaubt: Spannungs-/Leistungslimit unbekannt.
- Gang-Maße, Wände, Untergrund unbekannt.
- Drucker-Modell/Filament der Schule unbekannt.
- Preise: keine BrickLink-API, Preise kommen über Wanted-List-Upload (Phase 5).
