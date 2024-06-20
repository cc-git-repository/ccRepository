"""# Exercise 2: Logger Decorator for Class Methods
Objective: Create a decorator that logs the entry and exit of every method call in a class.
Requirements:
● Develop a decorator log_methods that can be applied to any class.
● The decorator should automatically log whenever any method of the class is called,
recording the method name and the arguments.
● Use could use the logging module for generating logs."""

import logging


def log_methods(cls):
    for name, value in vars(cls).items():
        if callable(value):
            setattr(cls, name, log_method(value))
    return cls

def log_method(func):
    def wrapper(*args, **kwargs):
        logging.basicConfig(level=logging.DEBUG)
        logging.info(f"Method: {func.__name__} Arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@log_methods
class Animal:
    def __init__(self, name: str, diet: str) -> None:
        self.name = name
        self.diet = diet

    def eat(self):
        print(f"My name is {self.name} and I eat {self.diet}!")


@log_methods
class Flying(Animal):
    def fly(self):
        print(f"My name is {self.name} and I can fly!")


@log_methods
class Swimming(Animal):
    def swim(self):
        print(f"My name is {self.name} and I can swim!")


@log_methods
class Eagle(Flying, Animal):
    def __init__(self, name: str, diet: str) -> None:
        super().__init__(name, diet)


@log_methods
class Penguin(Swimming, Animal):
    def __init__(self, name: str, diet: str) -> None:
        super().__init__(name, diet)


if __name__ == "__main__":
    eagle = Eagle(name="Marahute", diet="small wild animals")
    eagle.eat()
    eagle.fly()

    penguin = Penguin(name="Pingu", diet="fish")
    penguin.eat()
    penguin.swim()