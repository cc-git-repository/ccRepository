"""# Exercise 4: Singleton Metaclass
Objective: Implement a Singleton metaclass that ensures a class has only one instance.
Requirements:
● Create a metaclass Singleton that controls instance creation.
● Use this metaclass to make another class ApplicationSettings a singleton.
● Ensure that any instantiation of ApplicationSettings returns the same object."""

class Singleton:
    _istanza = None

    def __new__(cls):
        if cls._istanza == None:
            cls._istanza = super().__new__(cls)
        return cls._istanza
    
class ApplicationSettings(Singleton):
    pass

if __name__ == "__main__":
    istanza1 = ApplicationSettings()
    print(id(istanza1))
    istanza2 = ApplicationSettings()
    print(id(istanza2))
    print(istanza1 == istanza2)
