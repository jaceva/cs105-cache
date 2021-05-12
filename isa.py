from memory import Memory
from time import time

class Register(Memory):
  def __init__(self):
    Memory.__init__(self, name="Register", access_time=0.05)
    self.data = {"r0": None, "r1": None}

  def read(self, loc):
    super().sim_read(output=False)
    return self.data[loc]

  def write(self, data, address):
    super().sim_write(output=False)
    self.data[address] = data

class ISA():
  def __init__(self):
    self.memory = None
    self.registers = Register()
    self.instructions = { 
      "lb": self.load_b, 
      "sb": self.store,
      "li": self.load_i,
      "j": self.jump,
    }
    self.output = ""

  def set_memory(self, memory):
    self.memory = memory

  def read_instructions(self, file):
    if self.memory is not None:
      print(f"ISA memory: {self.memory.name}")
      start = time()
      with open(file) as codefile:
        code = codefile.readlines()
        lines = [line.strip() for line in code if line.strip() != '']
        for line in lines:
          self.parse_line(line)
      return time() - start
    else:
      print("Architecture has found no memory")
      return None

  def parse_line(self, line):
    tokens = line.split(' ')
    inst = tokens[0]
    if inst == "lb" or inst == "sb":
      print(f"{line}", end="")
    arg1 = tokens[1]
    if len(tokens) > 2:
      arg2 = tokens[2]
      self.instructions[inst](arg1, arg2)
    else:
      self.instructions[inst](arg1)

  def load_b(self, arg1, arg2):
    loc = self.registers.read(arg2)
    byte = self.memory.read(loc)
    self.registers.write(byte, arg1)

  def store(self, arg1, arg2):
    byte = self.registers.read(arg1)
    loc = self.registers.read(arg2)
    self.memory.write(byte, loc)

  def load_i(self, arg1, arg2):
    self.registers.write(int(arg2), arg1)

  def jump(self, arg1):
    if arg1 == "100":
      byte = self.registers.read('r0')
      if byte is not None:
        self.output += byte
      else:
        print(" - NO DATA")
    else:
      print("Jump address not recognized.")