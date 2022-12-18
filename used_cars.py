"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from parc6.car import Car


def main():
    """Demo test code to show how to use car class."""

    my_car = Car("Car_01", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    print("——————————————————————————————————————————————")

    Limo = Car("Limo",100)
    Limo.add_fuel(30)
    print("fuel =", Limo.fuel)
    Limo.drive(115)
    print("odo =", Limo.odometer)
    print(Limo)

main()