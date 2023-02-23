#!/usr/bin/env python3

import shutil
import os

def main():
    #move into user home directory
    os.chdir('/home/student/mycode/')

    #moves object to ceph_storage
    shutil.move('raynor.obj', 'ceph_storage/')

    #asks user to rename the object
    xname = input("what is the new name for kerrigan.obj?")
    
    #uses that input to rename the object
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if __name__ == "__main__":
    main()
