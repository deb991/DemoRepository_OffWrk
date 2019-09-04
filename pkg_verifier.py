#!/usr/bin/env python
import os
import sys
import pathlib
from threading import *

"""This package is for verifying any package, into the entire system
& confirm whether it is existing or, not. """

def find_file(root, file, first=False):
    for d, subD, f in os.walk(root):
        if file in f:
            print("{0} : {1}".format(file, d))
            if first == True:
                break

find_file("C:\\", 'python.exe', first=False)

t = Thread(target=find_file, daemon=False)

t.start()
t
