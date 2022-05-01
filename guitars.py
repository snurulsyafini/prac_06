"""CP1404/CP5632 Practical - Guitar program."""
from prac_06.guitar import Guitar


def main():
    """Start of program"""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = input("Cost: $")
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print(add_guitar, "added.")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        counter = 0
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            counter += 1
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print(f"Guitar {counter}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


if __name__ == '__main__':
    main()
