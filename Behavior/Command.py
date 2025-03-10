from abc import ABC, abstractmethod

class Canvas:
    def __init__(self):
        self.color = None

    def set_color(self, new_color):
        self.color = new_color

    def show(self):
        print(f"[Canvas] color = {self.color}")

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class ColorCommand(Command):
    def __init__(self, canvas: Canvas, new_color: str):
        self.canvas = canvas
        self.new_color = new_color
        self.old_color = None

    def execute(self):
        self.old_color = self.canvas.color
        self.canvas.set_color(self.new_color)

    def undo(self):
        self.canvas.set_color(self.old_color)

class EraseCommand(Command):
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self.old_color = None

    def execute(self):
        self.old_color = self.canvas.color
        self.canvas.set_color(None)

    def undo(self):
        self.canvas.set_color(self.old_color)

class CommandManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def do_command(self, cmd: Command):
        cmd.execute()
        self.undo_stack.append(cmd)
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            print("Không còn gì để undo.")
            return
        cmd = self.undo_stack.pop()
        cmd.undo()
        self.redo_stack.append(cmd)

    def redo(self):
        if not self.redo_stack:
            print("Không còn gì để redo.")
            return
        cmd = self.redo_stack.pop()
        cmd.execute()
        self.undo_stack.append(cmd)

if __name__ == "__main__":
    canvas = Canvas()
    manager = CommandManager()

    cmd_red = ColorCommand(canvas, "Đỏ")
    cmd_blue = ColorCommand(canvas, "Xanh")
    cmd_erase = EraseCommand(canvas)

    manager.do_command(cmd_blue)
    manager.do_command(cmd_red)
    
    manager.do_command(cmd_erase)
    canvas.show()
    manager.undo()
    manager.undo()
    manager.redo()
    canvas.show()
    