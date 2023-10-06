"""
Created by Fabian Gnatzig in 2023
Contact: fabiangnatzig@gmx.de
"""
from person import Person


class student(Person):

    def __init__(self, name, age, matrNr):
        super().__init__(name, age)

        self._matrNr = matrNr


    def get_person(self) -> str:
        return f"Der Student mit dem Namen {self._name} ist {self._age} Jahre alt und besitzt die Matrikelnummer: {self._matrNr}"
    @property
    def matrNr(self):
        return self._matrNr