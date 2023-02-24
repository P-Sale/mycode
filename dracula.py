#!/usr/bin/env python3

vampireLine = 0

with open("dracula.txt", "r") as dracula:
    with open("vampytimes.txt", "w") as writeFile:
        for line in dracula:
            if "vampire" in line.lower():
                writeFile.write(line)
                vampireLine += 1
print(vampireLine)

