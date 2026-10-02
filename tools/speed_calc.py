"""Theoretische Endgeschwindigkeit: v [m/s] = (rpm / 60) * Uebersetzung * pi * d

Uebersetzung = Zaehne_Motor / Zaehne_Rad (>1 = ins Schnelle).
ACHTUNG: MOTOR_RPM und STALL_NCM sind ANNAHMEN (nicht verifiziert, siehe docs/01_recherche.md).
Zuerst am echten Motor messen (motor.speed(), battery.voltage()) und hier eintragen.
Raddurchmesser stammen aus den Rebrickable-Teilenamen (Tyre 56 x 28, Wheel 43.2 x 26).
"""
import itertools, math

MOTOR_RPM = 170.0    # ANNAHME Leerlauf Large Motor bei voller Spannung
STALL_NCM = 40.0     # ANNAHME Haltemoment Large Motor [Ncm] (grob, unverifiziert)
LOSS_PER_STAGE = 0.95  # grober Wirkungsgrad je Zahnradstufe
MASS_KG = 1.2        # ANNAHME Gesamtgewicht
MU = 0.7             # ANNAHME Haftreibung Reifen/Boden (Gang, Fliesen/Linoleum)
G = 9.81

wheels = {"43.2mm": 0.0432, "56mm": 0.056}
# (Zaehne_Motor, Zaehne_Rad) -> i = Motor/Rad
stages = {"direkt 1:1": (1, 1), "20/12 ins Langsame": (12, 20), "12/36 ins Langsame": (12, 36),
          "24/16 ins Schnelle": (24, 16), "36/12 ins Schnelle": (36, 12), "40/16 ins Schnelle": (40, 16)}

print(f"{'Motoren':>7} {'Rad':>7} {'Uebersetzung':<20} {'v [m/s]':>8} {'F_Rad [N]':>9} {'a_max [m/s2]':>12} {'faehrt an':>9}")
for n, (wn, d), (sn, (z_m, z_r)) in itertools.product((1, 2, 3), wheels.items(), stages.items()):
    i_rad = z_m / z_r                      # Radumdrehungen pro Motorumdrehung = z_m/z_r
    v = (MOTOR_RPM / 60) * i_rad * math.pi * d
    t_motor = n * STALL_NCM / 100 * LOSS_PER_STAGE       # Nm
    t_wheel = t_motor / i_rad                            # Nm am Rad
    f = t_wheel / (d / 2)                                # N
    f_max = MU * MASS_KG * G                             # Traktionsgrenze
    a = min(f, f_max) / MASS_KG
    print(f"{n:>7} {wn:>7} {sn:<20} {v:8.2f} {f:9.2f} {a:12.2f} {'ja' if f>0.3*f_max else 'kaum':>9}")
