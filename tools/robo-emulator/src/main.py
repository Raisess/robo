#! /usr/bin/env python3

# e.g.: ./src/main.py ../../main/main.ino

import sys
from builder import Builder

if __name__ == "__main__":
  cpp = Builder("clang++ -std=c++14", "/usr/local/include/robo", sys.argv[1])

  cpp.compile()
  print("\t\tRunning with ROBO Emulator\n")
  cpp.run()
