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
    size = 2
    data = {"r0": 104, "r1": 0}
    Memory.__init__(self, "REGISTER", data, 0.05)

class MainMemory(Memory):
  def __init__(self):
    size = 16
    data = [
      72, 101, 108, 108, 
      111, 32, 87, 111, 
      114, 108, 100, 33, 
      0, 0, 0, 0
    ]
    # self.data = [0] * self.size
    Memory.__init__(self, "MEMORY", data, 1)

# Cache class to be written by the learner

class Cache(Memory):
  def __init__(self):

    self.memory = MainMemory()
    self.data_index = []
    self.size = 8
    # data = [[]] * self.size
    data = []
    Memory.__init__(self, "CACHE", data, 0.1)

  def read(self, loc):
    if loc in self.data_index:
      print(f"\t-- CACHE HIT --")
      index = self.data_index.index(loc)
      return super().read(index)

    
    print(f"\t-- CACHE MISS --")
    byte = self.memory.read(loc)
    self.data_index.append(loc)
    self.data.append(byte)
    if len(self.data_index) > self.size:
      self.data_index = self.data_index[1:]
      self.data = self.data[1:]
    
    return byte