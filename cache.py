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
    self.index = -1
    for i in range(self.size):
      self.data.append({'tag': None, 'data': '', 'age': None})

    # Mississippi
    # self.data = [
    #   {'tag': 0, 'data': 'M'},
    #   {'tag': 1, 'data': 'i'},
    #   {'tag': 2, 'data': 's'},
    #   {'tag': 3, 'data': 'p'},
    # ]
    
    self.policy = self.replace_fifo

    latency = 0.1
    Memory.__init__(self, "Cache", self.data, latency)

  def replace_random(self, addr, data):
    return randint(0, self.size-1)
    

  def replace_fifo(self, addr, data):
    self.index += 1
    if self.index == self.size:
      self.index = 0

    return self.index

  def replace_lru(self, addr, data):
    for i, entry in enumerate(self.data):
      if entry['tag'] == addr:
        index = i
      else:
        entry['age'] += 1

  def replace(self, addr, data):
    index = self.policy(addr, data)
    entry = self.data[index]
    print(f"\nOld entry {index} - tag: {entry['tag']}, data: \"{entry['data']}, age: {entry['age']}\"")
    entry = {'tag': addr, 'data': data}
    self.data[index] = entry
    print(f"New entry {index} - tag: {entry['tag']}, data: \"{entry['data']}, age: {entry['age']}\"")

  ## Given
  def is_hit(self, addr):
    selected_entry = None

    for entry in self.data:
      if entry['tag'] == addr:
        ## added for lru
        entry['age'] = 0
      ## added for lru
      elif entry['age'] != self.size:
        entry['age'] += 1

    return selected_entry

  ## Given
  def add_entry(self, addr, data):
    for i, entry in enumerate(self.data):
      if entry['tag'] == None:
        entry['tag'] = addr
        entry['data'] = data
        emtry['age'] = i
        return

    self.replace(addr, data)

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