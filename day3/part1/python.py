#import collections
import collections

#Main functiion runs once all the functions load
def main():
    with open('input.txt', 'r') as file:
        input = [line for line in file]
    print('Part 1:', part1(input))

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
    
    
main()
