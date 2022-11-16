#!/usr/bin/env python3
import shutil
import os

def main():
    #sets the working directory
    os.chdir("/home/student/mycode/labs/")

    #copy file A to file B
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #copy entire directory A to directory B
    shutil.copytree("5g_research/", "5g_research_backup/")

main()

