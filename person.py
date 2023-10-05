"""
Created by Fabian Gnatzig in 2023
Contact: fabiangnatzig@gmx.de
"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_person(self):
        return f"{self.name}, {self.age}"