#!/usr/bin/env python3

while True:
    try:
        print("Divide X by Y.")
        x = int(input("What is the integer value of x? "))
        y = int(input("What is the integer value of y? "))

        print("The value of x/y: ", x/y)
    except ZeroDivisionError as zerr:
        print("Handling run-time error:", zerr)

    except Exception as err:
        print("we did not anticipate that:", err)

