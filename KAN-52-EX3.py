"""# Exercise 3: Polymorphic Zoo Simulator
Objective: Design a set of classes that simulate a zoo where different types of animals can
exhibit unique behaviors.
Requirements:
● Create an abstract base class Animal with a method speak().
● Derive classes like Dog, Cat, and Bird from Animal, each implementing speak()
in a way appropriate to the animal.
● Implement a function simulate_zoo() that takes a list of animals and makes each
animal speak."""
from abc import ABC, abstractmethod

class Animal:
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Bau Bau")


class Cat(Animal):
    def speak(self):
        print("Miao Miao")


class Bird(Animal):
    def speak(self):
        print("Cip Cip")


def simulate_zoo(l: list) -> None:
    for i in l:
        i.speak()

if __name__ == "__main__":
    list_animal = []
    cane = Dog()
    list_animal.append(cane)
    gatto = Cat()
    list_animal.append(gatto)
    uccello = Bird()
    list_animal.append(uccello)
    simulate_zoo(list_animal)
