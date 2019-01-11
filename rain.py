# -*- coding: utf-8 -*-
from __future__ import print_function
from random import randint
from time import sleep
from sys import stdout
from os import system

floor_charset = [',', '.', '_']
rain_charset = ['o', 'O', '(', ')']
output_string = ""

system("clear")

# Printing the floor
for y in range (0, 24):
    stdout.write(" " * 80)
    stdout.flush()
    stdout.write("\b"*81)

    for x in range (0, 80):
        sleep(0.01)
        character = floor_charset[randint(0,2)]
        output_string += character
        stdout.write(character)
        stdout.flush()
    
    if(y != 23):
        stdout.write("\n")
    else:
        variable = input()

# Print the word: Rain