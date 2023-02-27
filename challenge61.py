#!/usr/bin/env python3

sing = True

while sing:
    y= int(input("How many bottles of beer do you want to start on the wall?"))

    if y < 101:
        sing = False
        bottle = range(y, 0, -1)
        for x in bottle:
            print(f"{x} bottles of beer on the wall!")
            print(f"{x} bottles of beer on the wall! {x} bottles of beer! You take on down pass it around!")
    else:
        print("too many bottles, must be less than 101!")

