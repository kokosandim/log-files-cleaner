#!/bin/python3

import shutil      # For CopyFile
import os          # For GetFileSize and check if file exist
import sys         # For CLI arguments

if(len(sys.argv) < 4):
    print("Missing arguments! Usage is is script.py 10 5")
    exit(1)

file_name = sys.argv[1]
limitsize = int(sys.argv[2])
logsnumber = int(sys.argv[3])

if(os.path.isfile(file_name) == True):                   # Check if main logfile exist
    logfile_size = os.stat(file_name).st_size            # Get file size in bytes
    logfile_size = logfile_size / 1024                   # Convert from bytes to kilobites

    if(logfile_size >= limitsize):
        if(logsnumber > 0):
            for currentFileNum in range(logsnumber, 1, -1):
                src = file_name + "_" + str(currentFileNum-1)
                dst = file_name + "_" + str(currentFileNum)
                if(os.path.isfile(src) == True):
                    shutil.copyfile(src, dst)
                    print("Copied: " + src + " to " + dst)

            shutil.copyfile(file_name, file_name + "_1")
            print("Copied: " + file_name + " to " + file_name + "_1")
        myfile = open(file_name, 'w')
        myfile.close()