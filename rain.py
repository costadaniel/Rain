# -*- coding: utf-8 -*-
from __future__ import print_function
from random import randint
from time import sleep
from sys import stdout
from os import system

rain = "Rain"
floor_charset = [',', '.', '_']
rain_charset = ['o', 'O', '(', ')']
output_string = ""

system("reset")

# Printing the floor
for y in range (24):
    stdout.write(" " * 80)
    stdout.flush()
    stdout.write("\b" * 80)

    for x in range (80):
        sleep(0.01)
        character = floor_charset[randint(0,2)]
        output_string += character
        stdout.write(character)
        stdout.flush()
    
    if(y != 23):
        output_string += '\n'
        stdout.write("\n")
    else: 
        output_string += '\0'

#Print the word: Rain
for i in range(4):
    stdout.write("\033[F" * 24) # Volta para o começo da linha superior
    sleep(1)
    output_string = output_string[:927+i] + rain[i] + output_string[928+i:]
    stdout.write(output_string)
    stdout.flush()

input()