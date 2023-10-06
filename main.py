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
    person_a = Person("Fabian", 22)
    person_b = Person("Lea", 27)

    print(person_a.get_person())
    print(person_b.get_person())


if __name__ == '__main__':
    main()
