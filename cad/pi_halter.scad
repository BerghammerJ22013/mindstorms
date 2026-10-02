// Raspberry-Pi-Halter (falls Kamera/Pi gekauft wird): Platte mit M2.5-Bohrungen 58 x 49 mm und Technic-Pinloechern.
// Pi-Lochabstand 58 x 49 mm ist eine Angabe aus dem Gedaechtnis, vor Druck am Board nachmessen.
$fn = 48;
pitch = 8; pin_d = 4.9; t = 3.2;
pw = 72; ph = 56;
difference() {
    cube([pw, ph, t]);
    for (x = [7, 7 + 58], y = [3.5 + 3, 3.5 + 3 + 49]) translate([x, y, -1]) cylinder(d = 2.7, h = t + 2);
    for (c = [0 : 8], r = [0 : 6]) translate([4 + pitch * c, 4 + pitch * r, -1])
        if (!(c > 0 && c < 8 && r > 0 && r < 6)) cylinder(d = pin_d, h = t + 2);
}
