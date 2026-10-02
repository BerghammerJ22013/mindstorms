#!/usr/bin/env pybricks-micropython
"""Fahrprogramm Entwurf (EV3 MicroPython v2.0, API laut pybricks.com/ev3-micropython).

Ports sind ANNAHMEN, beim Bau anpassen. Ungetestet.
Gyro haelt Kurs, Ultraschall weicht Waenden aus (Lenkmotor am Medium Motor).
"""
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, GyroSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait, StopWatch

DRIVE_SPEED = 600       # deg/s, nach Messung anpassen
STEER_LIMIT = 35        # Grad Lenkausschlag
KP = 1.2                # P-Regler Gyro -> Lenkwinkel
WALL_MM = 400           # darunter ausweichen

brick = EV3Brick()
drive_l = Motor(Port.A, Direction.CLOCKWISE)
drive_r = Motor(Port.D, Direction.CLOCKWISE)
steer = Motor(Port.B)
gyro = GyroSensor(Port.S1)
sonic = UltrasonicSensor(Port.S2)


def clamp(x, lim):
    return max(-lim, min(lim, x))


def run():
    brick.light.on()
    print("Akku mV:", brick.battery.voltage())
    gyro.reset_angle(0)
    steer.reset_angle(0)
    target = 0
    watch = StopWatch()
    while True:
        if sonic.distance() < WALL_MM:
            target += 30                       # Kurs anpassen
            gyro_err = target - gyro.angle()
        else:
            gyro_err = target - gyro.angle()
        steer.run_target(500, clamp(KP * gyro_err, STEER_LIMIT), then=Stop.HOLD, wait=False)
        drive_l.run(DRIVE_SPEED)
        drive_r.run(DRIVE_SPEED)
        wait(10)


run()
