#!/usr/bin/python3

from cheatdice import *

def main():

    swapper = Cheat_Swapper()

    loaded_dice = Cheat_Loaded_Dice()

    mulligan_dice = Cheat_Mulligan()
    
    swapper_score = 0
    loaded_dice_score = 0
    mulligan_score = 0

    # how many games we want to run
    number_of_games = 100000
    game_number = 0

    # begin!
    print("Simulation running")
    print("==================")
    while game_number < number_of_games:
        swapper.roll()
        loaded_dice.roll()
        mulligan_dice.roll()

        swapper.cheat()
        loaded_dice.cheat()
        mulligan_dice.roll()
        
        if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()) and sum(swapper.get_dice()) == sum(mulligan_dice.get_dice()):
            pass

        elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()) and sum(swapper.get_dice()) > sum(mulligan_dice.get_dice()):
            swapper_score += 1

        elif sum(loaded_dice.get_dice()) > sum(swapper.get_dice()) and sum(loaded_dice.get_dice()) > sum(mulligan_dice.get_dice()):
            loaded_dice_score += 1

        elif sum(swapper.get_dice()) == sum(loaded_dice.get_dice()) and sum(swapper.get_dice()) > sum(mulligan_dice.get_dice()):
            pass

        elif sum(swapper.get_dice()) == sum(mulligan_dice.get_dice()) and sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
            pass

        elif sum(loaded_dice.get_dice()) == sum(mulligan_dice.get_dice()) and sum(loaded_dice.get_dice()) > sum(swapper.get_dice()):
            pass

        else:
            mulligan_score += 1

        game_number += 1

    # the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(f"Swapper won: {swapper_score}")
    print(f"Loaded dice won: {loaded_dice_score}")
    print(f"Mulligan dice won: {mulligan_score}")

    # determine the winner

    if swapper_score == loaded_dice_score and swapper_score == mulligan_score:
        print("Draw between all 3.")

    elif swapper_score > loaded_dice_score and swapper_score > mulligan_score:
        print("swapper won the most games")

    elif loaded_dice_score > swapper_score and loaded_dice_score > mulligan_score:
        print("Loaded dice won the most games")

    elif swapper_score == loaded_dice_score and swapper_score > mulligan_score:
        print("Swapper and Loaded dice tied")    

    elif swapper_score == mulligan_score and swapper_score > loaded_dice_score:
        print("Swapper and Mulligan tied")

    elif loaded_dice_score == mulligan_score and loaded_dice_score > swapper_score:
        print("Loaded dice and Mulligan tied")

    else:
        print("Mulligan won the most games")
if __name__ == "__main__":
    main()
