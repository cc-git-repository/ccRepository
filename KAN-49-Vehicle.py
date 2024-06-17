"""# 1. Vehicle Class (Base Class):
- Attributes: Include attributes like make (the manufacturer), model, and year of manufacture
directly without private naming conventions.
- Methods: Implement a method display_info() that prints the vehicle's information.
2. Car Class (Inherits from Vehicle):
- Attributes: Add an attribute is_electric (boolean) to indicate whether the car is electric.
- Polymorphism: Override the display_info() method to include is_electric status.
3. Motorcycle Class (Inherits from Vehicle):
- Attributes: Add an attribute has_sidecar (boolean) to indicate whether the motorcycle comes with
a sidecar.
- Polymorphism: Override the display_info() method to include has_sidecar status.
4. Vehicle Management:
- Demonstrate creating instances of both Car and Motorcycle, and storing them in a list. Iterate
over this list and call display_info() on each vehicle to show polymorphism in action."""

class Vehicle():
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"Manufacturer: {self.make}\nModel: {self.model}\nyear of manufacture: {self.year}"


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, is_electric: bool) -> None:
        super().__init__(make, model, year)
        self.is_electric = is_electric

    def display_info(self):
        info = super().display_info()
        return info + f"\nis electric: {self.is_electric}"

class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, has_sidecar: bool) -> None:
        super().__init__(make, model, year) 
        self.has_sidecar = has_sidecar   

    def display_info(self):
        info = super().display_info()
        return info + f"\nhas sidecar: {self.has_sidecar}"

if __name__ == "__main__":
    vehicle_list = []
    c = Car(make="Fiat", model="Panda", year=2023, is_electric=True)
    vehicle_list.append(c)
    
    m = Motorcycle(make="Honda", model="X-ADV", year=2022, has_sidecar=False)
    vehicle_list.append(m)
    
    for i in vehicle_list:
        print(i.display_info())
        print()
