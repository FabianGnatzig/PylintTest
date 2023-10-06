"""
Created by Fabian Gnatzig in 2023
Contact: fabiangnatzig@gmx.de
"""


class Person:
    """
    Class for a person.
    """

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def get_person(self) -> str:
        """
        Returns a string with name and age.
        :return: A person string.
        """
        return f"{self._name}, {self._age}"

    @property
    def name(self) -> str:
        """
        Returns the name property.
        :return: The name property.
        """
        return self._name

    @property
    def age(self) -> int:
        """
        Returns the age property.
        :return: The age property.
        """
        return self._age
