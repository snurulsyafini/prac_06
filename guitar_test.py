"""CP1404/CP5632 Practical - Guitar test."""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2022


def test_run():
    """A test for Guitar class"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2010, 1512.90)

    print(f"{guitar.name} get_age() - Expected 98. Got {guitar.find_age()}")
    print(f"{other.name} get_age() - Expected 7. Got {other.find_age()}")

    print()
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected False. Got {other.is_vintage()}")


if __name__ == '__main__':
    test_run()
