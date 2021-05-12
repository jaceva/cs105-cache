from time import sleep

# abstract memory class

class Memory():
  def __init__(self, name, data, process_time):
    self.process_time = process_time
    self.data = data
    self.name = name

  def read(self, data, output=True):
    if output:
      print(f"->{self.name} read: {data}", end="")

    sleep(self.process_time)
    return data


  def write(self, byte, loc):
    if self.name != "register":
      print(f"->{self.name} write", end="")
    sleep(self.process_time)

    self.data[loc] = byte

# defined memory types

class MainMemory(Memory):
  def __init__(self):
    size = 16
    latency = 1

    # This is Mississippi.
    self.data = [
      'T', 'h', 'i', 's', 
      ' ', 'M', 'p', '.']

    # Mississippi
    # self.data = ['M', 'i', 's', 'p',]
    
    Memory.__init__(self, "Main Memory", self.data, latency)

  def read(self, loc):
    data = self.data[loc]
    return super().read(data)

# Cache class to be written by the learner

