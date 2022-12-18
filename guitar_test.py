from prac6.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another guitar", 2013, 12500)
    guitars = [gibson, another]

    for i in guitars:
        print("{} get_age() - Got {}".format(i.name, i.get_age()))
        print("{} is_vintage() - Got {}".format(i.name, i.is_vintage()))


main()
