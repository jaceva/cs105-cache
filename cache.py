from operator import is_
from memory import Memory, MainMemory
from random import randint

class Cache(Memory):
  def __init__(self):
    Memory.__init__(self, name="Cache", access_time=0.1)
    self.size = 4
    # Mississippi
    # self.data = [
    #   {'tag': 0, 'data': 'M'},
    #   {'tag': 1, 'data': 'i'},
    #   {'tag': 2, 'data': 's'},
    #   {'tag': 3, 'data': 'p'},
    # ]

    self.data = []
    for i in range(self.size):
      self.data.append({'tag': None, 'data': ''})

    self.sim_read = super().sim_read

    self.main_memory = MainMemory()

    self.index = -1
    
    
    self.policy = self.replace_fifo


  def replace_random(self):
    return randint(0, self.size-1)
    

  def replace_fifo(self):
    self.index += 1
    if self.index == self.size:
      self.index = 0

    return self.index

  def replace(self, new_address, new_data):
    index = self.policy()
    entry = self.data[index]
    print(f"\nOld entry {index} - tag: {entry['tag']}, data: \"{entry['data']}\"")
    entry = {'tag': new_address, 'data': new_data}
    self.data[index] = entry
    print(f"New entry {index} - tag: {entry['tag']}, data: \"{entry['data']}\"")

  ## Given
  def is_hit(self, address):
    
    for entry in self.data:
      if entry['tag'] == address:
        print(f" - CACHE HIT", end="")
        return entry

    print(f" - CACHE MISS", end="")
    return None

  ## Given
  def add_entry(self, address, data):
    for entry in self.data:
      if entry['tag'] == None:
        entry['tag'] = address
        entry['data'] = data
        return
    
    # ex 5
    # self.replace(address, data)

  def read(self, address):
    entry = self.is_hit(address)
    if entry is not None:
      self.sim_read()
      data = entry['data']
      print(data)
      return data
    else:
      data = self.main_memory.read(address)
      self.add_entry(address, data)
      self.sim_read()
      print(data)
      return data