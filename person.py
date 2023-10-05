"""
Created by Fabian Gnatzig in 2023
Contact: fabiangnatzig@gmx.de
"""


class Person:
    """
    Class for a person.
    """

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_person(self):
        """
        Returns a string with name and age.
        :return: A person string.
        """
        return f"{self._name}, {self._age}"

    def get_age(self):
        """
        Returns the age.
        :return: The age.
        """
        return self._age
