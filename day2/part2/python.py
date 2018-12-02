#Import OS
import os
#import sys
import sys
#Import Counter
from collections import Counter

#Open the file with our input
with open('input.txt') as f:
    #Splilt the input into an array to be used later
    hashes = f.readlines()


#Make 2 vars one for counting the double letters and one for counting the tripple letters
doubles = 0
tripples = 0
#Make the loop for the ammount of lines in the array
for i in hashes:
    #Var to count the common letters
    letters = [j for i,j in Counter(i).most_common()]
    #If the same letter shows 3 times add one to doubles
    if 2 in letters:
        doubles += 1
    if 3 in letters:
        tripples += 1

    #Make loop for the ammount in the array again to find part2
    for j in hashes:
        #Define diffrence var named diff
        diff = 0
        #For the index every diffrence
        for idx, ch in enumerate(i):
            #For everydiffrent letter add one
            if ch != j[idx]:
                diff += 1
        #If diff = 1
        if diff == 1:
            #Stores the answer as a string in ans and hash
            ans = [ch for idx, ch in enumerate(i) if j[idx] == ch]
            hash = "".join(ans)









print('\nPart1:')
print('Doubles:',doubles)
print('Tripples:',tripples)
print('Total:',doubles * tripples,'\n')

print('Part Two:')
print('Hash:',hash)
