"""# 1. Item Class: Create a base class called Item with properties (title, is_checked_out) and methods
(check_out(), return_item()). Use print statements for error handling in check_out() and return_item()
for already checked out or not checked out scenarios.
2. Book and Journal Classes: Inherits from Item. These classes can be used to demonstrate
polymorphism further if desired.
3. Library System: Implement main program functionality to create a mix of books and journals,
attempting to check out and return items, showcasing basic exception handling.
This exercise focuses on the fundamentals of polymorphism and basic exception handling without
custom exceptions or complex features."""

class Item():
    def __init__(self, title: str, is_checked_out: bool) -> None:
        self.title = title
        self.is_checked_out = is_checked_out

    def check_out(self):
        pass

    def return_item():
        pass

class Book(Item):
    def __init__(self, title: str, is_checked_out: bool) -> None:
        super().__init__(title, is_checked_out)

    def check_out(self):
        if self.is_checked_out:
            print(f"Book ({self.title}) is already checked out")
        else:
            self.is_checked_out = True
            print(f"Book ({self.title}) is now checked out")

    def return_item(self):
        if not self.is_checked_out:
            print(f"Book ({self.title}) is already returned")
        else:
            self.is_checked_out = False
            print(f"Book ({self.title}) is now returned")

class Journal(Item):
    def __init__(self, title: str, is_checked_out: bool) -> None:
        super().__init__(title, is_checked_out)
    
    def check_out(self):
        if self.is_checked_out:
            print(f"Journal ({self.title}) is already checked out")
        else:
            self.is_checked_out = True
            print(f"Journal ({self.title}) is now checked out")
    
    def return_item(self):
        if not self.is_checked_out:
            print(f"Journal ({self.title}) is already returned")
        else:
            self.is_checked_out = False
            print(f"Journal ({self.title}) is now returned")

if __name__ == "__main__":
    b1 =  Book(title="The Da Vinci Code", is_checked_out=True)
    b1.check_out()
    b1.return_item()
    b1.check_out()

    b2 = Book(title="The Diary of a Young Girl", is_checked_out=False)
    b2.check_out()

    j1 = Journal(title="sales journal", is_checked_out=False)
    j1.check_out()
    j1.return_item()

    j2 = Journal(title="purchases journal", is_checked_out=False)
    j2.return_item()
    j2.check_out()

