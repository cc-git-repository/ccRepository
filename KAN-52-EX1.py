"""# Exercise 1: Custom Container with Access Control
Objective: Implement a custom container class that mimics a list but with access control.
Users should be able to add elements to the list only if they have the correct permissions.
Requirements:
● Create a class ControlledList that allows only users with a specific role to add
items.
● Use the @property decorator and __getitem__ method for encapsulating the
access to list items.
● Implement methods to check user permissions when adding or removing items."""

class ControlledList:
    def __init__(self, controlledlist) -> None:
        self._controlledlist = controlledlist
        self._role = "Guest"

    def __getitem__(self, items): 
        if self._role != "Admin":
            print("Operation not permitted")
        else:
            return self._controlledlist[items]

    def __setitem__(self, items, newvalue):
        if self._role != "Admin":
            print("Operation not permitted")
        else:
            self._controlledlist[items] = newvalue

    def __str__(self) -> str:
        if self._role != "Admin":
            return "Operation not permitted"
        else:
            return str(self._controlledlist)

    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, new_role):
        if new_role not in ["Admin", "Guest"]:
            print("Role not admitted!")
        else:
            self._role = new_role


if __name__ == "__main__":
    l = ControlledList([1, 2, 3, 4])
    print(l.__getitem__(1))
    l.__setitem__(2, 5)
    print(l)
    l.role = "Admin"
    print(l.__getitem__(1))
    l.__setitem__(2, 5)
    print(l)



