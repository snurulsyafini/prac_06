"""CP1404/CP5632 Practical - Car class example."""


class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre

        name: __str__ method: Car, fuel, odometer -> Limo, fuel, odometer
        """
        self.fuel = fuel
        self.odometer = 0

        # 6/7. Add __str__ method and add name field
        self.name = Car

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance

    def display(self):
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel, self.odometer)
