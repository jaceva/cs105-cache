from time import sleep

# abstract memory class

class Memory():
  def __init__(self, name, access_time):
    self.name = name
    self.access_time = access_time

  def sim_read(self, output=True):
    if output:
      print(f" - {self.name} read: ", end="")
    sleep(self.access_time)


  def sim_write(self, output=True):
    if output:
      print(f" - {self.name} write: ", end="")
    sleep(self.access_time)

# defined memory types

class MainMemory(Memory):
  def __init__(self):
    self.size = 16
    # Mississippi
    self.data = ['M', 'i', 's', 'p',]

    # This is Mississippi.
    # self.data = [
    #   'T', 'h', 'i', 's', 
    #   ' ', 'M', 'p', '.']

    
    
    Memory.__init__(self, "Main Memory", 1)

  def read(self, address):
    data = self.data[address]
    super().sim_read()
    return data
