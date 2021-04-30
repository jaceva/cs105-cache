from isa import ISA
from time import time
from memory import MainMemory, Cache

if __name__ == "__main__":
  arch1 = ISA()
  # arch1.set_memory(MainMemory())
  arch1.set_memory(Cache())
  start = time()
  arch1.read_code("code.txt")
  print(f"CONSOLE OUTPUT: {arch1.output}")

  end = time()
  print(f"DURATION: {end - start:.2f} seconds")
