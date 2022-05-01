"""CP1404/CP5632 Practical - Guitar class."""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Store details of guitars"""

    def __init__(self, name="", year=0, cost=0):
        """Add a Guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string format of guitar"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def find_age(self):
        """Find out if guitar is vintage or not"""
        return self.find_age() >= VINTAGE_AGE

    def is_vintage(self):
        """Get age of guitar based on current year"""
        return self.find_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Sort guitars by year released (less than)"""
        return self.year < other.year
