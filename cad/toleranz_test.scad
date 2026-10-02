// Toleranz-Testteil: Technic-Loecher und Achsloecher in Abstufungen.
// Nominalmasse sind Startwerte (Loch ca. 4.8 mm, Achse ca. 4.8 mm Kreuz) und MUESSEN per Testdruck kalibriert werden.
$fn = 64;
hole_d = [4.7, 4.8, 4.9, 5.0, 5.1];
pitch = 8;
difference() {
    cube([pitch * (len(hole_d) * 2 + 1), 2 * pitch, 3.2]);
    for (i = [0 : len(hole_d) - 1]) {
        // runde Pinloecher
        translate([pitch * (i + 1), pitch, -1]) cylinder(d = hole_d[i], h = 6);
        // Kreuzachsloecher
        translate([pitch * (i + len(hole_d) + 1), pitch, 1.6]) {
            cube([hole_d[i], 1.8, 6], center = true);
            cube([1.8, hole_d[i], 6], center = true);
        }
    }
}
