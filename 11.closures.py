# Closure is a function having access to the scope of its parent function
# after the parent function returned


def parent_function(person):
    coins = 3
    
    def play_game():
        nonlocal coins
        coins -= 1
        
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins ==1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins")
    
    return play_game

# parent function return function
tommy = parent_function("tommy")
tommy()
tommy()
maddy = parent_function("maddy")
maddy()
        
        