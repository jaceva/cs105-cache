from operator import is_
from memory import Memory, MainMemory
from random import randint

class Cache(Memory):
  def __init__(self):
    # class, __init__ and below two lines are implemented for the learner 
    self.main_memory = MainMemory()
    self.read_cache = super().read
    self.size = 4
    self.data = []
    for i in range(self.size):
      self.data.append({'tag': None, 'data': ''})

    # Mississippi
    # self.data = [
    #   {'tag': 0, 'data': 'M'},
    #   {'tag': 1, 'data': 'i'},
    #   {'tag': 2, 'data': 's'},
    #   {'tag': 3, 'data': 'p'},
    # ]
    

    latency = 0.1
    Memory.__init__(self, "Cache", self.data, latency)

  ## Given
  def is_hit(self, addr):
    for entry in self.data:
      if entry['tag'] == addr:
        return entry

    return None

  def add_entry(self, addr, data):
    for entry in self.data:
      if entry['tag'] == None:
        entry['tag'] = addr
        entry['data'] = data
        break

  def read(self, addr):
    entry = self.is_hit(addr)
    if entry is not None:

      print(f"->CACHE HIT", end="")
      data = entry['data']
      return self.read_cache(data)
    else:
      print(f"->CACHE MISS", end="")
      data = self.main_memory.read(addr)
      self.add_entry(addr, data)
      return self.read_cache(data)

    # cache_full = len(self.upper_index) == self.size
    
    # if loc in self.upper_index:
    #   print(f"->CACHE HIT", end="")
    #   index = self.upper_index.index(addr)
    #   if policy == "LRU":
    #     pass
    #     #TODO Move data and addr to front of line
    #     # make sure read adjusts to the data change
    #   return self.read_cache(index)

    # print(f"->CACHE MISS", end="")
    # byte = self.upper_memory.read(addr)

    # if len(self.upper_index) < self.size:
    #   self.upper_index.append(addr)
    #   self.data.append(byte)

    # def replace_fifo(byte):
    #   self.upper_index.append(addr)
    #   self.data.append(byte)
    #   if len(self.upper_index) > self.size:
    #     self.upper_index = self.upper_index[1:]
    #     self.data = self.data[1:]

    # def replace_random(byte):
    #   index = randint(0, self.size)
    #   self.upper_index[index] = addr
    #   self.data[index] = byte

    # def replace_lru(byte):
    #   pass
    # Replacement Policy: FIFO
    #TODO send loc with byte???
    # elif policy == "FIFO":
    #   replace_fifo(byte)
    # # Replacement Policy: Random
    # elif policy == "RANDOM":
    #   replace_random(byte)
    # # Replacement Policy: LRU
    # elif policy == "LRU":
    #   replace_lru(byte)