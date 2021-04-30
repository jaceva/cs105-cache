from isa import ISA
from time import time

if __name__ == "__main__":
  arch1 = ISA()
  start = time()
  arch1.read_code("code.txt")
  print(f"CONSOLE OUTPUT: {arch1.output}")

  end = time()
  print(f"DURATION: {end - start:.2f} seconds")

    # arch1.parse_line("li r1 0")
  # arch1.parse_line("lb r0 r1")
  # arch1.parse_line("j 100")

  # arch1.parse_line("li r1 1")
  # arch1.parse_line("lb r0 r1")
  # arch1.parse_line("j 100")

  # arch1.parse_line("li r1 2")
  # arch1.parse_line("lb r0 r1")
  # arch1.parse_line("j 100")

  # arch1.parse_line("li r1 3")
  # arch1.parse_line("lb r0 r1")
  # arch1.parse_line("j 100")

  # arch1.parse_line("li r1 4")
  # arch1.parse_line("lb r0 r1")
  # arch1.parse_line("j 100")

  # store 'hello' in memory
  # arch1.parse_line("li r0 104")
  # arch1.parse_line("li r1 0")
  # arch1.parse_line("sb r0 r1")

  # arch1.parse_line("li r0 101")
  # arch1.parse_line("li r1 1")
  # arch1.parse_line("sb r0 r1")

  # arch1.parse_line("li r0 108")
  # arch1.parse_line("li r1 2")
  # arch1.parse_line("sb r0 r1")

  # arch1.parse_line("li r0 108")
  # arch1.parse_line("li r1 3")
  # arch1.parse_line("sb r0 r1")

  # arch1.parse_line("li r0 111")
  # arch1.parse_line("li r1 4")
  # arch1.parse_line("sb r0 r1")