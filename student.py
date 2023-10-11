"""
Created by Fabian Gnatzig in 2023
Contact: fabiangnatzig@gmx.de
"""
from person import Person


class student(Person):

    def __init__(self, name, age, matr_nr):
        super().__init__(name, age)

        self._matr_nr = matr_nr


    def get_person(self) -> str:
        return f"Name: {self._name}; Alter: {self._age}; Matrikelnummer: {self._matr_nr};"

    @property
    def matr_Nr(self):
        return self._matr_nr
