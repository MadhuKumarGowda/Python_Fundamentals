# Rock Paper and Scissor game implementation with user interactive
import sys
import random
from enum import Enum

# Below are the constant remain constant 
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

print("Welcome Rock Paper and Scissor Game".center(50,"*"))
playerChoice = input("Enter...\n1 for Rock\n2 for Paper\n3 for Scissor\n\n")
player = int(playerChoice)
if player < 1 or player > 3:
    sys.exit("You must enter 1,2 or 3.")

computerChoice = random.choice("123")
machineChoice = int(computerChoice)

print("-".center(25,"-"))
# Below are accessing Enum constant and also removing RPS as prefix
print("You chose:" + str(RPS(player)).replace("RPS.", "") + ".")
print("Python chose:" + str(RPS(machineChoice)).replace("RPS.", "") + ".")
print("\n")
print("Result of this game is\n")

if player == 1 and machineChoice == 3:
    print("🎉🎉🎉 You win!")
elif player == 2 and machineChoice == 1:
    print("🎉🎉🎉 You win!")
elif player == 3 and machineChoice == 2:
    print("🎉🎉🎉 You win!")
elif player == machineChoice:
    print("😲😲😲 Game Tie")
else:
    print("🐍🐍🐍 Python wins!")
