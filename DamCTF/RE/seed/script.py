#!/usr/bin/env python3
import sys
import time
import datetime
import random
import hashlib

def hash(text):
    return hashlib.sha256(str(text).encode()).hexdigest()

def crackRandom():

    dt = datetime.datetime(2021,11,6, 1, 1)
    s = round(dt.timestamp())

    while s > 0:
        s = s - 1

        random.seed(s, version=2)

        x = random.random()
        flag = hash(x)

        if 'b9ff3ebf' in flag:
            print(f"The flag -> dam{{{flag}}}")
            #Interesting to know.
            print("The flag file was created at:", datetime.datetime.fromtimestamp(s).strftime("%A, %B %d, %Y %I:%M:%S"))
            break

crackRandom()
