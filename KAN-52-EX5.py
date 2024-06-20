"""# Exercise 5: Command Pattern for Undoable Operations
Objective: Implement the command pattern to support undoable operations in a software
application.
Requirements:
● Define a Command interface with methods execute() and undo().
● Create concrete command classes implementing operations like AddCommand,
RemoveCommand, and ModifyCommand for a collection.
● Implement a CommandManager class that keeps a history stack and supports
undoing and redoing commands."""

from abc import ABC, abstractmethod

class CommandInterface(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass


class CommandClass(CommandInterface):
    def __init__(self, cmd):
        self.cmd = cmd
        
    def execute(self):
        self.cmd.execute_command()
    
    def undo(self):
        self.cmd.undo_command()

    
class Command:
    id = 0
    def __init__(self) -> None:
        self._id = Command.id
        Command.id += 1
    
    def __str__(self):
        return f"Command id: {self._id}"
    
    def execute_command(self):
        print(f"{str(self)} is being executing")

    def undo_command(self):
        print(f"{str(self)} is being undoing")


class CommandManager:
    def __init__(self, dimension=100) -> None:
        self.operations = []
        self.position = 0
        self.dimension = dimension

    def size(self):
        return len(self.operations)
    
    def undoing(self):
        if self.size() == 0:
            print("Command list empty!")
            return
        if self.position > 0:
            print(f"Undoing ...")
            self.operations[self.position].undo()
            self.position -= 1

    def redoing(self):
        if self.size() == 0:
            print("Command list empty!")
            return
        if self.position < self.size():
            print(f"Redoing ...")
            self.operations[self.position].execute()
            if self.position != self.size() - 1:
                self.position += 1

    def addcommand(self, cmd):
        self.operations.append(cmd)

    def removecommand(self):
        if self.size() == 0:
            print("Command list empty!")
            return
        if self.position == self.size() - 1:
            self.position -= 1
        self.operations.pop()

    def modifycommand(self, cmd):
        if self.size() == 0:
            print("Command list empty!")
            return
        self.operations[self.position] = cmd


if __name__ == "__main__":
    cm = CommandManager()
    com1 = Command()
    com2 = Command()
    concrete_com1 = CommandClass(com1)
    cm.addcommand(concrete_com1)
    concrete_com2 = CommandClass(com2)
    cm.addcommand(concrete_com2)
    cm.redoing()
    cm.undoing()
    cm.redoing()
    cm.redoing()
    com3 = Command()
    concrete_com3 = CommandClass(com3)
    cm.modifycommand(concrete_com3)
    cm.redoing()
    cm.removecommand()
    cm.addcommand(concrete_com2)
    cm.addcommand(concrete_com3)
    cm.redoing()
    cm.redoing()
    cm.redoing()
    cm.removecommand()
    cm.removecommand()
    cm.removecommand()
    cm.removecommand()
    cm.redoing()
