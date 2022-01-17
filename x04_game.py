#!python3

"""
Create a full rock paper scissors game
You can incorporate the other files in this project to help you
"""

from x01_player import playerChoice
from x02_computer import computerChoice
from x03_winner import playerWins

if __name__ == "__main__":
  b = playerChoice()
  a = computerChoice()
  print(playerWins(a,b))
  pass

