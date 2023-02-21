#!/usr/bin/env python3
#makes the list
my_list = ["192.168.0.5", 5060, "UP"]
#prints the first item in the list
print("the first item in the list (IP): " + my_list[0])
#prints the second item in the list
print("the second item in the list (port): " + str(my_list[1]))
#prints the last item in the list
print("the last item in the list (state): " + my_list[2])
new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print("IP addresses: " + new_list[3] + ", and " + new_list[4])
