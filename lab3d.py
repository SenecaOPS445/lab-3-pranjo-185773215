#!/usr/bin/env python3
'''Description: Returns free disk space on a Linux system's root directory'''

# Author ID: pranjo

import subprocess

def free_space():
    free_space_return = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = free_space_return.communicate()
    stdout = output[0].decode('utf-8').strip()
    return stdout

if __name__ == '__main__':
    print(free_space())