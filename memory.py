from time import sleep

# abstract memory class

class Memory():
  def __init__(self, name, access_time, data):
    self.access_time = access_time
    self.data = data
    self.name = name

  def read(self, data, output=True):
    if output:
      print(f"->{self.name} read: {data}", end="")

    sleep(self.access_time)
    return data


  def write(self, byte, loc):
    if self.name != "register":
      print(f"->{self.name} write", end="")
    sleep(self.access_time)

    self.data[loc] = byte

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
    
    Memory.__init__(self, "Main Memory", 1, self.data)

  def read(self, loc):
    data = self.data[loc]
    return super().read(data)

# Cache class to be written by the learner

