// Frontplatte: haelt Ultraschallsensor + Platz fuer Kamera, per Technic-Pins am LEGO-Rahmen.
// Lochmasse: Startwerte, nach Toleranztest (toleranz_test.scad) in pin_d eintragen.
$fn = 48;
pitch = 8;        // Technic-Raster [mm]
pin_d = 4.9;      // Pinloch-Durchmesser, KALIBRIEREN
t = 3.2;          // Plattendicke [mm]
cols = 12; rows = 3;   // 12 x 3 Raster = 96 x 24 mm
difference() {
    union() {
        cube([cols * pitch, rows * pitch, t]);
        // Steg nach vorn fuer Sensor
        translate([cols * pitch / 2 - 15, rows * pitch, 0]) cube([30, 10, t]);
    }
    for (c = [0 : cols - 1], r = [0 : rows - 1])
        translate([pitch * (c + 0.5), pitch * (r + 0.5), -1]) cylinder(d = pin_d, h = t + 2);
}
