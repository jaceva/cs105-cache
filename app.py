from isa import ISA
from time import time
from memory import MainMemory
from cache import Cache

if __name__ == "__main__":
  cache_arch = ISA()
  # cache_arch.set_memory(MainMemory())
  cache_arch.set_memory(Cache())

  ### Run code
  cache_arch.read_instructions("code_write.txt")
  exec_time = cache_arch.get_exec_time()

  ### Output memory data and code execution duration
  if exec_time > 0:
    print(f"OUTPUT STRING: {cache_arch.output}")
    print(f"EXECUTION TIME: {exec_time:.2f} seconds")
