from memory import Memory, MainMemory
from random import randint

class Cache(Memory):
  def __init__(self):
    super().__init__(name="Cache", access_time=0.1)
    self.size = 4
    # Mississippi
    # self.data = [
    #  " {"tag": 0, 'data': "M"},
    #   {"tag": 1, 'data': "i"},
    #   {"tag": 2, 'data': "s"},
    #   {"tag": 3, 'data': "p"},
    # ]

    self.data = [
      {"tag": None, "data": ''},
      {"tag": None, "data": ''},
      {"tag": None, "data": ''},
      {"tag": None, "data": ''},
    ]

    self.main_memory = MainMemory()

    self.indices = [-1, 0, 1, 2]
    self.sets = 1 # 1,2 or 4

  def random_policy(self, set_number):
    if self.sets == 1:
      return randint(0, len(self.data)-1)
    elif self.sets == 2:
      return randint(set_number*2, set_number*2+1)
    
    return set_number
    

  def fifo_policy(self, set_number):
    self.indices[set_number] += 1
    if self.indices[set_number] == len(self.data)/self.sets + set_number:
      self.indices[set_number] = set_number - 1

    return self.indices[set_number]

  def replace_entry(self, address, data):
    index = 0
    set_number = address % self.sets
    index = self.fifo_policy(set_number)
    
    self.data[index] = {'tag': address, 'data': data}

  ## Given
  def get_entry(self, address):
    
    for entry in self.data:
      if entry['tag'] == address:
        ## This check added at write policy
        if entry['data'] is not None:
          print(f"HIT: ", end="")
          return entry

    print(f"MISS", end="")
    return None

  ## Given - removed after replacement policy
  def add_entry(self, address, data):
    for entry in self.data:
      if entry['tag'] == None:
        entry['tag'] = address
        entry['data'] = data
        return

  def read(self, address):
    super().sim_read()
    entry = self.get_entry(address)
    if entry is not None:
      data = entry['data']
    else:
      data = self.main_memory.read(address)
      self.replace_entry(address, data)

    return data

  # just the write-through policy
  def write(self, address, data):
    super().sim_write()
    entry = self.get_entry(address)
    if entry is not None:
      entry["data"] = data
    else:
      self.replace_entry(address, data)
    
    self.main_memory.write(address, data)

  def get_exec_time(self):
    return self.exec_time + self.main_memory.get_exec_time()
