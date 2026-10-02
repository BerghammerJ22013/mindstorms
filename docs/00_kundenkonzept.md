# Konzept für das Kundengespräch (bis 16.10.2026)

## Ziel
Autonomes Lego-Rennauto für den Schulgang (EG), Basis EV3 (Education Core Set 45544, bis zu 2 Sets von der Schule).

## Plan
1. Basisauto aus Schulmaterial: Gyro (Kurs), Ultraschall (Wände), Lego-Zentrallenkung, MicroPython.
2. Messen: Motorwerte, Akkuspannung, Rundenzeiten → `tools/speed_calc.py` mit echten Werten.
3. Optional: Fremdmotor und/oder Kamera, nur wenn Regeln und Budget passen.
4. 3D-Druck für Halterungen/Karosserie, nur wenn leichter oder steifer.

## Geld (Budget 200 €, inkl. Filament)
Priorität: (1) Differential/Zahnräder falls fehlend, (2) griffige Reifen, (3) ggf. Fremdmotor + Treiber + Akku, (4) Reserve ca. 20 €. Preise folgen über BrickLink-Wanted-List (keine API vorhanden).

## Fragen an den Kunden
- Maße des Gangs, Untergrund, Kurven/Ecken, Türen/Hindernisse?
- Fremdmotoren: Spannungs-/Leistungslimit? Eigene Stromversorgung erlaubt?
- Zählen gedruckte Felgen/Reifen als "Rad aus Lego"?
- Wird das zweite Set sicher gestellt? Ist es ein 45544?
- Welches Modell hat der Schul-Drucker, welche Filamente?
- Meilenstein-Termine für Live-Tests?

## Rollen (Vorschlag, im Team festlegen)
PO (Koordination, Kundenkontakt, Repo) · Mechanik/Bau · Software · 3D-Druck/CAD · Test/Doku.
