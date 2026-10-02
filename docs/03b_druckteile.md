# Phase 3b – 3D-Druckteile (Stand 2026-10-02)

Regel: nur drucken, wenn leichter, steifer oder günstiger als die LEGO-Lösung. Drucker der Schule: Modell unbekannt, PLA verfügbar. STLs wurden mit OpenSCAD 2021.01 erzeugt (`cad/stl/`), Gewichte aus dem STL-Volumen berechnet (PLA 1,24 g/cm³, 100 % Infill).

| Teil | Zweck | Gewicht 100 % | Status |
|---|---|---|---|
| `toleranz_test` | Loch-/Achsmaße kalibrieren (4,7–5,1 mm) | 4,9 g | **zuerst drucken** |
| `sensor_halter` | Frontplatte für Ultraschall/Kamera, 12×3 Pinraster | 7,6 g | Maße unkalibriert |
| `pi_halter` | Pi-Platte, nur falls Pi gekauft wird | 13,8 g | Pi-Lochabstand aus Gedächtnis, nachmessen |

Druckhinweise: Pinlöcher senkrecht zum Druckbett, 0,2 mm Layer, PLA 40 % Infill reicht für Halter. Nach dem Toleranztest `pin_d` in beiden Dateien anpassen. Gedruckte Räder/Karosserie: noch nicht entworfen, weil unklar ist, ob "Räder aus Lego" gedruckte Felgen erlaubt. Keine Teile sind gedruckt oder passend geprüft.
