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
    Memory.__init__(self, "REGISTER", self.data, 0.05)

class MainMemory(Memory):
  def __init__(self):
    self.size = 16
    self.data = [
      72, 101, 108, 108, 
      111, 32, 87, 111, 
      114, 108, 100, 33, 
      0, 0, 0, 0
    ]
    # self.data = [0] * self.size
    Memory.__init__(self, "MEMORY", self.data, 1)

# Cache class to be written by the learner

# class Cache(Memory):
#   def __init__(self):
#     Memory.__init__(self, "CACHE", 8, 0.5)