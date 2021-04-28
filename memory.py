# abstract memory class

class Memory():
  def __init__(self, blocks, process_time):
    self.blocks = blocks
    self.process_time = process_time

# defined memory types

class Register(Memory):
  def __init__(self):
    Memory.__init__(self, 4, 1)

class MainMemory(Memory):
  def __init__(self):
    Memory.__init__(self, 64, 100)

# cache to be written by the learner

class Cache(Memory):
  def __init__(self):
    Memory.__init__(self, 16, 10)

# read/write instructions

class ISA():
  def __init__(self, memory=MainMemory()):
    self.memory = memory

  def load(byte):
    return memory.read(byte)

  def store(value, byte):
    memory.write(value, byte)



if __name__ == "__main__":
  test_mem = Cache()
  print(test_mem.blocks)
  print(test_mem.process_time)
