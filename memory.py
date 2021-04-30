from time import sleep

# abstract memory class

class Memory():
  def __init__(self, name, data, process_time):
    self.process_time = process_time
    self.data = data
    self.name = name

  def read(self, loc, output_info=False):
    if output_info:
      print(f"->{self.name} read", end="")
    sleep(self.process_time)

    return self.data[loc]


  def write(self, byte, loc, output_info=False):
    if output_info:
      print(f"->{self.name} write", end="")
    sleep(self.process_time)

    self.data[loc] = byte
    

# defined memory types

class Register(Memory):
  def __init__(self):
    size = 2
    data = {"r0": 104, "r1": 0}
    Memory.__init__(self, "register", data, 0.05)

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
    Memory.__init__(self, "memory", data, 1)

# Cache class to be written by the learner

class Cache(Memory):
  def __init__(self):
    # class, __init__ and below two lines are implemented for the learner 
    self.upper_memory = MainMemory()
    self.read_cache = super().read
    self.size = 8

    self.data_index = []
    # data = [[]] * self.size
    data = []
    Memory.__init__(self, "cache", data, 0.1)

  def read(self, loc, output_info):
    if loc in self.data_index:
      print(f"->CACHE HIT", end="")
      index = self.data_index.index(loc)
      return self.read_cache(index)

    print(f"->CACHE MISS", end="")
    byte = self.upper_memory.read(loc)
    self.data_index.append(loc)
    self.data.append(byte)
    if len(self.data_index) > self.size:
      self.data_index = self.data_index[1:]
      self.data = self.data[1:]
    
    return byte