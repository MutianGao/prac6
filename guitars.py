from prac6.guitar import Guitar


def main():
    print("My guitars!")
    guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]

    while True:
        name = input("Name: ")
        if name == "":
            break
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print("{} ({}) : ${} added".format(name, year, cost))

    print("These are my guitars:")
    i = 1
    for j in guitars:
        if j.is_vintage():
            vintage = "(vintage)"
        else:
            vintage = ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i, j.name, j.year, j.cost, vintage))
        i = i + 1


main()
