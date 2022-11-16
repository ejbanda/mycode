#!/usr/bin/env python3
import shutil
import os

def main():
    #setting path to work from
    os.chdir('/home/student/mycode/labs/')
    
    #moving obj
    shutil.move('raynor.obj', 'ceph_storage/')

    #renaming file
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
