class CPU:
    def freeze(self):
        print("CPU is frozen (halted)")

    def jump(self, position):
        print(f"CPU jumps to address {position}")

    def execute(self):
        print("CPU starts executing instructions...")

class Memory:
    def load(self, position, data):
        print(f"Memory load data '{data}' to address {position}")

class HardDrive:
    def read_sector(self, sector, size):

        print(f"HardDrive reading {size} bytes at sector {sector}")
        return "boot_loader_code"

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hdd = HardDrive()

    def startComputer(self):
        self.cpu.freeze()
        boot_data = self.hdd.read_sector(sector=0, size=512)
        self.memory.load(position=0x00, data=boot_data)
        self.cpu.jump(position=0x00)
        self.cpu.execute()


if __name__ == "__main__":
 

    computer = ComputerFacade()
    computer.startComputer()
