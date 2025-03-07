from abc import ABC, abstractmethod
class State(ABC):
    @abstractmethod
    def handle(self):
        pass

class Receive(State):
    def handle(self,task):
        task.state = Process()
        return 'Task is received, next state is Process'

class Process(State):
    def handle(self,task):
        task.state = Finish()
        return 'Task is processing, next state is Finish'

class Finish(State):
    def handle(self,task):
        return 'Finished Task'

class Task():
    def __init__(self):
        self.state = Receive()
    def handle(self):
        return self.state.handle(self)

task = Task()
print(task.handle())
print(task.handle())
print(task.handle())
