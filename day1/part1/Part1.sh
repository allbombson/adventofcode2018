#!/bin/bash

#Adds a space after each "+" and "-"
sed 's/\([+-]\)/\1 /g' input.txt > stuff.txt
expr 0 $(stuff.txt) > output.txt
cat output.txt
