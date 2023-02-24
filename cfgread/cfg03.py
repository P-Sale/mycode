#!/usr/bin/env python3
line = 0
file = input("What file would you like to load? ")

with open(file, "r") as configfile:
    configlist = configfile.readlines()
for x in configlist:
    line +=1
print(configlist)
print("total lines: ", line)
