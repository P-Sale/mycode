#!/usr/bin/env python3

import crayons

def commandpush(devicemd):
    for ip in devicemd.keys():
        print(f"{crayons.red('handshaking')}. .. ... connecting with {ip}")
        for mycmds in devicemd[ip]:
            print(f"attempting to send command --> {mycmds}")
    return None

def main():

    devicemd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print("welcome to the network device command pusher")

    print("\nData set found\n")

    commandpush(devicemd)

if __name__ == "__main__":
    main()
