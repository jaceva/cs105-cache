from time import sleep

# abstract memory class

class Memory():
  def __init__(self, name, data, process_time):
    # self.blocks = blocks
    self.process_time = process_time
    self.data = data
    self.name = name

  def read(self, loc):
    print(f"\t{self.name} ACCESS TIME: {self.process_time}")
    sleep(self.process_time)

    return self.data[loc]

  
  def write(self, byte, loc):
    print(f"\t{self.name} ACCESS TIME: {self.process_time}")
    sleep(self.process_time)

    self.data[loc] = byte
    

# defined memory types

class Register(Memory):
  def __init__(self):
    self.size = 4
    self.data = {"r0": 104, "r1": 0}
    Memory.__init__(self, "REGISTER", self.data, 0.25)

class MainMemory(Memory):
  def __init__(self):
    self.size = 16
    self.data = [
      104, 101, 108, 108, 
      111, 0, 0, 0, 
      0, 0, 0, 0, 
      0, 0, 0, 0
    ]
    # self.data = [0] * self.size
    Memory.__init__(self, "MEMORY", self.data, 2)

# cache to be written by the learner

# class Cache(Memory):
#   def __init__(self):
#     Memory.__init__(self, "CACHE", 8, 0.5)

# read/write instructions

class ISA():
  def __init__(self, memory=MainMemory()):
    self.memory = memory
    self.registers = Register()
    self.instructions = { 
      "lb": self.load_b, 
      "sb": self.store,
      "li": self.load_i,
      "j": self.jump,
    }
    self.console = ""

  def parse_line(self, line):
    tokens = line.split(' ')
    inst = tokens[0]
    arg1 = tokens[1]
    if len(tokens) > 2:
      arg2 = tokens[2]
      self.instructions[inst](arg1, arg2)
    else:
      self.instructions[inst](arg1)

  def load_b(self, arg1, arg2):
    print(f"Load Byte:")
    loc = self.registers.read(arg2)
    byte = self.memory.read(loc)
    self.registers.write(byte, arg1)
    print()

  def store(self, arg1, arg2):
    print(f"Store Byte:")
    byte = self.registers.read(arg1)
    loc = self.registers.read(arg2)
    self.memory.write(byte, loc)
    print()

  def load_i(self, arg1, arg2):
    print(f"Load Immediate:")
    self.registers.write(int(arg2), arg1)
    print()

  def jump(self, arg1):
    print(f"Jump Immediate:")

    if arg1 == "100":
      byte = self.registers.read('r0')
      self.console += chr(byte)
    else:
      print("Jump address not recognized.")

    print()



if __name__ == "__main__":
  arch1 = ISA()

  arch1.parse_line("li r1 0")
  arch1.parse_line("lb r0 r1")
  arch1.parse_line("j 100")

  arch1.parse_line("li r1 1")
  arch1.parse_line("lb r0 r1")
  arch1.parse_line("j 100")

  arch1.parse_line("li r1 2")
  arch1.parse_line("lb r0 r1")
  arch1.parse_line("j 100")

  arch1.parse_line("li r1 3")
  arch1.parse_line("lb r0 r1")
  arch1.parse_line("j 100")

  arch1.parse_line("li r1 4")
  arch1.parse_line("lb r0 r1")
  arch1.parse_line("j 100")

  print(f"CONSOLE OUTPUT: {arch1.console}")

  # store 'hello' in memory
  # arch1.parse_line("li r0 104")
  # arch1.parse_line("li r1 0")
  # arch1.parse_line("sb r0 r1")

  # arch1.parse_line("li r0 101")
  # arch1.parse_line("li r1 1")
  # arch1.parse_line("sb r0 r1")

  # arch1.parse_line("li r0 108")
  # arch1.parse_line("li r1 2")
  # arch1.parse_line("sb r0 r1")

  # arch1.parse_line("li r0 108")
  # arch1.parse_line("li r1 3")
  # arch1.parse_line("sb r0 r1")

  # arch1.parse_line("li r0 111")
  # arch1.parse_line("li r1 4")
  # arch1.parse_line("sb r0 r1")

  print(arch1.memory.data)
  print(arch1.registers.data)