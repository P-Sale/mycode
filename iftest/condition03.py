#!/usr/bin/env python3

#establish the hostname
hostname = input("what value should we set for hostname?")

#test any kind of capitolization with mtg in if statement
#also prints hostname match
if hostname.lower() == "mtg":
    print("the hostname was found to be mtg")
    print("hostname matches expected config")

#regardless of if statement outcome, prints exit
print("exiting the script")
