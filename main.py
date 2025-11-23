from motor import Motor
from automovil import Automovil
from motocicleta import Motocicleta

motor1 = Motor("Híbrido", 180)
motor2 = Motor("Diesel", 250)
motor3 = Motor("Gasolina 4 cil.", 200)
motor4 = Motor("Eléctrico", 15)

auto1 = Automovil("Lexus", "RX 450h", 2022, 5, motor1)
auto2 = Automovil("RAM", "2500", 2020, 2, motor2)

moto1 = Motocicleta("Ducati", "Panigale V4", 2023, 1103, motor3)
moto2 = Motocicleta("Segway", "E110S", 2023, 50, motor4)

print(auto1.encender())
print(auto1.abrir_maletero())
print(auto1.motor.encender_motor())

print()

print(moto1.encender())
print(moto1.hacer_caballito())
print(moto1.motor.encender_motor())

print()

print(auto1)
print(auto2)
print(moto1)
print(moto2)
