#!/usr/bin/env python3

from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
from cheatdice import Cheat_Mulligan

def main():
    cheater1 = Cheat_Swapper()
    cheater2 = Cheat_Loaded_Dice()
    cheater3 = Cheat_Mulligan()

    cheater1.roll()
    cheater2.roll()
    cheater3.roll()

    cheater1.cheat()
    cheater2.cheat()
    cheater3.cheat()

    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")
    print(f"Cheater 3 rolled {cheater3.get_dice()}")

    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()) and sum(cheater1.get_dice()) == sum(cheater3.get_dice()):
        print("Draw!")

    elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()) and sum(cheater1.get_dice()) > sum(cheater3.get_dice()):
        print("Cheater 1 wins!")

    elif sum(cheater2.get_dice()) > sum(cheater1.get_dice()) and sum(cheater2.get_dice()) > sum(cheater3.get_dice()):
        print("cheater 2 wins!")

    elif sum(cheater1.get_dice()) == sum(cheater2.get_dice()) and sum(cheater1.get_dice()) > sum(cheater3.get_dice()):
        print("draw between cheater 1 and cheater 2!")
    
    elif sum(cheater1.get_dice()) == sum(cheater3.get_dice()) and sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
        print("draw between cheater 1 and cheater 3!")
    
    elif sum(cheater2.get_dice()) == sum(cheater3.get_dice()) and sum(cheater2.get_dice()) > sum(cheater1.get_dice()):
        print("draw between cheater 2 and cheater 3!")
    
    else:
        print("Cheater 3 wins!")

if __name__ == "__main__":
    main()
