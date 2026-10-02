# Phase 2 – Konzept & Berechnung (Entwurf, Stand 2026-10-02)

Berechnung: `tools/speed_calc.py`. **Alle Motorwerte sind Annahmen** (170 rpm, 40 Ncm, 1,2 kg, µ 0,7), nicht verifiziert. Die Zahlen zeigen nur Verhältnisse; echte Werte kommen aus Messungen (Phase 7).

## Rahmen (aus den Schulregeln)
Schulgang im EG, ohne Linie, autonom, alle Autos starten gleichzeitig, Stören erlaubt, keine kabellose Verbindung. Pflicht: EV3-Brick liest mind. 1 fahrrelevanten Sensor und steuert den Lenkmotor. Räder, Zentrallenkung und Brick aus Lego. Fremdmotoren, Raspberry Pi und Kamera erlaubt. Budget 200 € inkl. Filament; Teile von zuhause zählen mit Gebrauchtpreis.

## Varianten
| | A – Sensor-Flitzer (nur Set) | B – Hybrid Fremdmotor | C – Kamera-Auto |
|---|---|---|---|
| Antrieb | 2–3 Large Motors gekoppelt, 1 Stufe ins Schnelle | 1 Fremd-DC-Motor an eigener Stromversorgung, vom Brick per Motortreiber geschaltet | wie A oder B |
| Lenkung | Lego-Zentrallenkung, Medium Motor | wie A | wie A |
| Sensorik | Gyro (Geradeaus), Ultraschall (Wände) | wie A | Pi + Kamera für Gang-Orientierung, Brick liest Gyro/Ultraschall (Pflicht) |
| Speed (qualitativ) | ca. 1–1,2 m/s bei 36/12 und 43 mm Rad (Annahme) | höher möglich, hängt von Motor ab | wie A/B |
| Kosten | ca. 0–30 € | + Motor, Treiber, Akku: Schätzung 30–70 € | + Pi/Kamera: nur wenn Schule keinen stellt |
| Risiko | niedrig | mittel: Regelkonformität, Verkabelung | hoch: Software-Aufwand |

## Empfehlung
**A als Basis, B als Ausbaustufe, C nur wenn Preis und Zeit passen.** Grund: A erfüllt alle Pflichten mit Schulmaterial, ist ohne Zukäufe testbar und liefert zuerst Messwerte. Danach entscheiden Messdaten, ob ein Fremdmotor den Aufwand lohnt. Bei Kurven im Gang zählt Stabilität mehr als Spitzengeschwindigkeit.

## Berechnungsergebnis (Annahmen!)
- 3 Large Motors tragen mehr Drehmoment, die Traktion (Reifenhaftung) begrenzt aber die Beschleunigung bei fast allen Übersetzungen. Mehr Motoren bringen dann nur Gewicht.
- Ins Schnelle übersetzen bringt Speed (36/12 ≈ 1,15 m/s bei 43 mm Rad), mit 1 Motor sinkt a_max leicht.
- Größeres Rad (56 mm) ersetzt eine Übersetzungsstufe.

## Nächste Schritte
1. Motorwerte messen und `speed_calc.py` aktualisieren.
2. Gangmaße vom Kunden erfragen, danach Lenkungsart festlegen.
3. Regel klären: Fremdmotor-Limit, gedruckte Felgen als "Lego-Rad".
