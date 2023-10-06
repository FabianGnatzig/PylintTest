"""
Created by Fabian Gnatzig in 2023
Contact: fabiangnatzig@gmx.de
"""
from person import Person


def main():
    """
    Main function
    :return: None
    """
    personA = Person("Fabian", 22)
    personB = Person("Lea", 27)

    print(personA.get_person())
    print(personB.get_person())


if __name__ == '__main__':
    main()
