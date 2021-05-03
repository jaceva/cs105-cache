from time import sleep
from random import randint

# abstract memory class

class Memory():
  def __init__(self, name, data, process_time):
    self.process_time = process_time
    self.data = data
    self.name = name

  def read(self, loc):
    data = self.data[loc]
    if self.name != "register":
      print(f"->{self.name} read: {chr(data)}", end="")
    sleep(self.process_time)

    return data


  def write(self, byte, loc):
    if self.name != "register":
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

    # This is Mississippi.
    data = [
      84, 104, 105, 115, 
      32, 77, 112, 46]
    
    # Hello World!
    # data = [
    #   72, 101, 108, 108, 
    #   111, 32, 87, 111, 
    #   114, 108, 100, 33, 
    #   0, 0, 0, 0
    # ]
    # self.data = [0] * self.size
    Memory.__init__(self, "memory", data, 1)

# Cache class to be written by the learner

class Cache(Memory):
  def __init__(self):
    # class, __init__ and below two lines are implemented for the learner 
    self.upper_memory = MainMemory()
    self.read_cache = super().read
    self.size = 4

    self.upper_index = []
    # data = [[]] * self.size
    data = []
    Memory.__init__(self, "cache", data, 0.1)

  def read(self, loc, policy="FIFO"):
    def replace_fifo(byte):
      self.upper_index.append(loc)
      self.data.append(byte)
      if len(self.upper_index) > self.size:
        self.upper_index = self.upper_index[1:]
        self.data = self.data[1:]

    def replace_random(byte):
      index = randint(0, self.size)
      self.upper_index[index] = loc
      self.data[index] = byte

    def replace_lru(byte):
      

    # cache_full = len(self.upper_index) == self.size

    if loc in self.upper_index:
      print(f"->CACHE HIT", end="")
      index = self.upper_index.index(loc)
      if policy == "LRU":
        pass
        #TODO Move data and loc to front of line
        # make sure read adjusts to the data change
      return self.read_cache(index)

    print(f"->CACHE MISS", end="")
    byte = self.upper_memory.read(loc)

    if len(self.upper_index) < self.size:
      self.upper_index.append(loc)
      self.data.append(byte)
    # Replacement Policy: FIFO
    #TODO send loc with byte???
    elif policy == "FIFO":
      replace_fifo(byte)
    # Replacement Policy: Random
    elif policy == "RANDOM":
      replace_random(byte)
    elif policy == "LRU":
      replace_lru(byte)


    # Replacement Policy: LRU

    
    
    return byte