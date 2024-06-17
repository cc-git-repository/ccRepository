"""# 1. Animal Class: Create a base class Animal with properties (name, diet) and a method eat() that
prints the animal's diet.
2. Flying and Swimming Behaviors: Create two mixin classes, Flying and Swimming, with methods
fly() and swim() that print actions specific to flying or swimming.
3. Specific Animal Classes: Create classes like Eagle and Penguin that inherit from Animal and one
or both of the behavior mixins, utilizing these behaviors.
4. Zoo System: Demonstrate eating behavior and specific actions (flying, swimming) of various
animals in a simple main program."""

class Animal():
    def __init__(self, name: str, diet: str) -> None:
        self.name = name
        self.diet = diet

    def eat(self):
        print(f"My name is {self.name} and I eat {self.diet}!")

class Flying(Animal):
    def fly(self):
        print(f"My name is {self.name} and I can fly!")


class Swimming(Animal):
    def Swim(self):
        print(f"My name is {self.name} and I can swim!")


class Eagle(Flying, Animal):
    def __init__(self, name: str, diet: str) -> None:
        super().__init__(name, diet)


class Penguin(Swimming, Animal):
    def __init__(self, name: str, diet: str) -> None:
        super().__init__(name, diet)


if __name__ == "__main__":
    eagle = Eagle(name="Marahute", diet="small wild animals")
    eagle.eat()
    eagle.fly()

    penguin = Penguin(name="Pingu", diet="fish")
    penguin.eat()
    penguin.Swim()


