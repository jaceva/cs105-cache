from isa import ISA
from time import time
from memory import MainMemory
from cache import Cache

if __name__ == "__main__":
  cache_arch = ISA()
  # cache_arch.set_memory(MainMemory())
  cache_arch.set_memory(Cache())

  ### Run code
  duration = cache_arch.read_instructions("code_misp.txt")

  ### Output memory data and code execution duration
  if duration is not None:
    print(f"OUTPUT STRING: {cache_arch.output}")
    print(f"DURATION: {duration:.2f} seconds")
