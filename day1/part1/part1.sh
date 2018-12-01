#!/bin/bash

#Adds a space after each "+" and "-"
sed 's/\([+-]\)/\1 /g' input.txt > stuff.txt

#Runs math on it with the starting point of 0 like said by AoC then writes the answer to a file.
#Note this process itself is 0.03 seconds if you dont write and allready have the file, making it the fastest slove atm.
expr 0 $(stuff.txt) > output.txt

#Read the output
cat output.txt
