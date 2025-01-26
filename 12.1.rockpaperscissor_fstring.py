# Rock Paper and Scissor game implementation with user interactive
import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():  
        
        nonlocal player_wins
        nonlocal python_wins  

    # Below are the constant remain constant 
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSOR = 3

        
        print("Welcome Rock Paper and Scissor Game".center(50,"*"))
        playerChoice = input("Enter...\n1 for Rock\n2 for Paper\n3 for Scissor\n\n")
        
        if playerChoice not in ["1","2","3"]:
            print("You must enter 1,2 or 3.")
            play_rps()
            
        player = int(playerChoice)
    

        computerChoice = random.choice("123")
        machineChoice = int(computerChoice)

        print("-".center(25,"-"))
        # Below are accessing Enum constant and also removing RPS as prefix
        print(f"\nYou chose: {str(RPS(player)).replace("RPS.", "").title()} .")
        print(f"\nPython chose: {str(RPS(machineChoice)).replace("RPS.", "").title()}.")
        print("\n")
        print(f"Result of this game is{game_result}\n")

        def decide_winner(player,machine):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and machineChoice == 3:
                player_wins += 1
                return "🎉🎉🎉 You win!"
            elif player == 2 and machineChoice == 1:
                player_wins += 1
                return "🎉🎉🎉 You win!"
            elif player == 3 and machineChoice == 2:
                player_wins += 1
                return "🎉🎉🎉 You win!"
            elif player == machineChoice:
                return "😲😲😲 Game Tie"
            else:
                python_wins += 1
                return "🐍🐍🐍 Python wins!"
            
        game_result = decide_winner(player, machineChoice)
        print("Game result :" , game_result)
        
        nonlocal game_count 
        game_count = game_count + 1
        print(f"\n Game Count: {str(game_count)}")
        print(f"\n Player wins: {str(player_wins)}")
        print(f"\n Python wins:  {str(python_wins)}")
        
        playagain = input("\n would you like to play again?\nY for Yes\nQ for Quit\n\n")
        
        if playagain.lower() in ["y","Y"]:
            play_rps()        
        else:
            print("👋👋👋👋👋 Thanks")
            # we can use playagain = False or break
            #break
            playagain = False
    return play_rps
            
play = rps()
play()