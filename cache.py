from operator import is_
from memory import Memory, MainMemory
from random import randint

class Cache(Memory):
  def __init__(self):
    self.size = 4
    # Mississippi
    self.data = [
      {'tag': 0, 'data': 'M'},
      {'tag': 1, 'data': 'i'},
      {'tag': 2, 'data': 's'},
      {'tag': 3, 'data': 'p'},
    ]
    # self.data = []
    # for i in range(self.size):
    #   self.data.append({'tag': None, 'data': ''})

    self.sim_read = super().sim_read

    self.main_memory = MainMemory()

    self.index = -1
    
    
    self.policy = self.replace_fifo

    Memory.__init__(self, "Cache", 0.1)

  def replace_random(self, addr, data):
    return randint(0, self.size-1)
    

  def replace_fifo(self, addr, data):
    self.index += 1
    if self.index == self.size:
      self.index = 0

    return self.index

  def replace(self, addr, data):
    index = self.policy(addr, data)
    entry = self.data[index]
    print(f"\nOld entry {index} - tag: {entry['tag']}, data: \"{entry['data']}\"")
    entry = {'tag': addr, 'data': data}
    self.data[index] = entry
    print(f"New entry {index} - tag: {entry['tag']}, data: \"{entry['data']}\"")

  ## Given
  def is_hit(self, addr):
    
    for entry in self.data:
      if entry['tag'] == addr:
        print(f" - CACHE HIT", end="")
        return entry

    print(f" - CACHE MISS", end="")
    return None

  ## Given
  def add_entry(self, addr, data):
    for entry in self.data:
      if entry['tag'] == None:
        entry['tag'] = addr
        entry['data'] = data
        return
    
    # ex 5
    # self.replace(addr, data)

  def read(self, addr):
    entry = self.is_hit(addr)
    if entry is not None:
      self.sim_read()
      # data = entry['data']
      # print(data)
      # return data
    # else:
    #   print(f" - CACHE MISS", end="")
    #   data = self.main_memory.read(addr)
    #   self.add_entry(addr, data)
    #   return self.read_cache(data)