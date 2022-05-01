"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    # 1. Create new Car objects with 100 units of fuel
    limo = Car("Limo", 100)

    # 2. Add more units of fuel using add method
    limo.add_fuel(20)

    # 3. Print amount of fuel in car
    print(f"Fuel={limo.fuel}")

    # 4. Attempt to drive car 115km with drive method
    distance_driven = limo.drive(115)

    # 5. Print odometer reading
    print(f"Odometer after moving {distance_driven}km = {limo.odometer}")

    # 8. Add __str__ method to Car class
    print(limo)


main()
