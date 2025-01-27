import sys
import random

def guess_number(name="PlayerOne"):
    game_count = 0
    player_win = 0
    
    def play_guess_number():
        nonlocal name
        nonlocal player_win
        
        playerChoice = input(f"\n{name}, guess which number I'm thinking of ... 1, 2 or 3.\n\n" )
        
        if playerChoice not in ["1","2","3"]:
            print(f"{name}, please enter 1, 2 or 3.")
            return play_guess_number()
        
        computerChoice = random.choice("123")
        
        print(f"\n{name}, you chose {playerChoice}")
        print(f"I was thinking about the number {computerChoice}.\n")
        
        player = int(playerChoice)
        computer = int(computerChoice)
        
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_win
            
            if player == computer:
                player_win += 1
                return f"🎉🎉🎉 {name}, you win!"
            else:
                return f"Sorry, {name}. Better luck next time. 😟"
        
        game_result = decide_winner(player, computer)
        print(game_result)
        
        nonlocal game_count
        game_count += 1
        
        print(f"\n Game count: {game_count}")
        print(f"\n{name}'s wins: {player_win}")
        print(f"\nYour winning percentage: {player_win / game_count:.2%}")
        
        print("\nPlay again. {name}?")
        
        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() in ["y", "Y"]:
                continue
            else:
                break
        
        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print("\n 🎉🎉🎉🎉🎉")
            print("Thank you for playing\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋")
            else:
                return
    
    return play_guess_number

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Provides a personalized game experience")
    
    parser.add_argument(
        '-n','--name', metavar="name",
        required=True, help="The name of the person playing the game."
    )
    
    args = parser.parse_args()
    
    guess_my_number = guess_number(args.name)
    guess_my_number()
            
        
        
        