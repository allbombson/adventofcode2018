#import collections
import collections

#Main functiion runs once all the functions load
def main():
    with open('input.txt', 'r') as file:
        input = [line for line in file]
    print('Part 1:',part1(input))
    print('Part 2:',part2(input))

#Make Claim Class
class Claim:
    def __init__(self, string):
        str_split = string.split()
        self.id = str_split[0].strip('#')
        self.left = int(str_split[2].split(',')[0])
        self.top = int(str_split[2].split(',')[1].strip(':'))
        self.right = self.left + int(str_split[3].split('x')[0])
        self.bottom = self.top + int(str_split[3].split('x')[1])
        self.coords = set()
        for x in range(self.left, self.right):
            for y in range(self.top, self.bottom):
                self.coords.add(f'{x},{y}')

#Define func get_claim_counts
def get_claim_counts(claims):
    #Define fabric_claim_counts
    fabric_claim_counts = collections.defaultdict(int)
    for claim in claims:
        for coord in claim.coords:
            fabric_claim_counts[coord] += 1
    return fabric_claim_counts

#Part 1 slove
def part1(input):
    #Load the claims
    claims = [Claim(string) for string in input]
    fabric_claim_counts = get_claim_counts(claims)
    #Make counter var
    counter = 0
    for coord in fabric_claim_counts:
        if fabric_claim_counts[coord] > 1:
            counter += 1
    return counter

#Part 2 Slove
def part2(input):
    #Load the claims
    claims = [Claim(string) for string in input]
    fabric = get_claim_counts(claims)
    #Make claim boolean
    unique_claim_found = False
    #Define i
    i = 0
    #Make loop
    while not unique_claim_found and i < len(claims):
        claim = claims[i]
        is_unique = True
        #Define the cords
        coords = claim.coords
        while is_unique and coords:
            #Check to see if it does colide if it does set to fasle
            if fabric[coords.pop()] != 1:
                is_unique = False
        #if it doesnt colide set to True
        if not coords and is_unique:
            unique_claim_found = True
        i += 1
    #Give the unique claim id if found
    return claim.id if unique_claim_found else None



main()
