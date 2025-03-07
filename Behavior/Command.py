from abc import ABC,abstractmethod
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
class Button():
    command : Command
    def __init__(self,command : Command):
        self.command = command
    def click(self):
        return self.command.execute() 
class Editor():
    def save(self):
        print('Saved')
    def open(self):
        print('Opened')
    def close(self):
        print('Closed')

class SaveCommand(Command):
    def __init__(self,editor : Editor):
        self.editor = editor
    def execute(self):
        return self.editor.save()
class OpenCommand(Command):
    def __init__(self,editor : Editor):
        self.editor = editor
    def execute(self):
        return self.editor.open()
class CloseCommand(Command):
    def __init__(self,editor : Editor):
        self.editor = editor
    def execute(self):
        return self.editor.close()

editor = Editor()
save = SaveCommand(editor)
open = OpenCommand(editor)
close = CloseCommand(editor)
close_button = Button(close)
open_button = Button(open)
save_button = Button(save)
close_button.click()
open_button.click()
save_button.click()
    