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
    # print("Data not written in Memory() class")
    # self.data[loc] = byte

# defined memory types

class MainMemory(Memory):
  def __init__(self):
    size = 16

    # This is Mississippi.
    self.data = [
      'T', 'h', 'i', 's', 
      ' ', 'M', 'p', '.']

    # Mississippi
    # self.data = ['M', 'i', 's', 'p',]
    
    Memory.__init__(self, "Main Memory", 1)

  def read(self, loc):
    data = self.data[loc]
    super().sim_read()
    return data

# Cache class to be written by the learner

