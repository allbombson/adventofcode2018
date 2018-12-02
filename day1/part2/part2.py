#Import needed tools
import itertools

def part1():
    #Open the file with the input
    with open('input.txt', 'r') as fp:
        #Read the file
        text = fp.read()
        #Setup for eval
        text = text.replace('\n', ' ')
        #Run eval for answer
        return eval(text)

def part2(ncycles=300):
    #Define the var for the current freq
    currentfreq = 0
    #Define freq var
    freq = {currentfreq}
    #Open the file with our input
    with open('input.txt', 'r') as fp:
        #Define info
        info = [int(l) for l in fp]
    #Define info_cycled
    info_cycled = itertools.cycle(info)
    #for every num cycled
    for num in info_cycled:
        #add the num to our freq
        currentfreq = currentfreq + num
        #If our current freq is in freq
        if currentfreq in freq:
            #return
            return currentfreq
        freq.add(currentfreq)


if __name__ == "__main__":
    
    #Part1 rewritten in python printed
    print("Part1:")
    print(part1())
    
    #Part2
    print("Part2:")
    print(part2())
