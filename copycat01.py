#!/usr/bin/env python3

import shutil
import os

def main():
    #changes directory to home
    os.chdir("/home/student/mycode/")

    #copies a single file
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #copies and entire directory tree
    shutil.copytree("5g_research/", "5g_research_backup/")
if __name__ == __main__:
    main()

