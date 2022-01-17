#!python3
"""
Create a function that creates a random choice for the computer player:
input parameters: none required
output:

0 : rock
1 : paper
2 : scissors
"""


def computerChoice():
  import random
  a = random.choice("012")
  value = int(a)
  return value


if __name__ == "__main__":
  computer = computerChoice()
  print(computer)
