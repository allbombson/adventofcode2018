#Used sort -v on input.txt and saved as input2.txt

#Import re
import re
#Import counter
from collections import Counter

#Open sorted file
with open("input2.txt", "r") as f:
    #Define guards
    guards = {}
    #Define times
    start, stop, current_guard = 0, 0, 0
    #Define lines
    lines = [x.strip() for x in f.readlines()]

    #Make loop
    for line in lines:
        values = re.findall("\d+", line)
        #Set current guard
        if "Guard" in line:
            current_guard = int(values[-1])
        #Set when they start sleeping
        elif "falls asleep" in line:
            start = int(values[-1])
        #Set when they wake up
        elif "wakes up" in line:
            stop = int(values[-1])
            for i in range(start, stop):
                guards.setdefault(current_guard, []).append(i)
    #Part 1
    #Define part 1
    part1 = max(guards, key=lambda x: len(guards[x]))
    #Define counter
    counter = Counter(guards[part1])
    #Define minute
    minute = counter.most_common()[0][0]
    #Define anwser
    part1ANS = part1 * minute
    #Print anwser
    print('Part 1:',part1ANS)




    #Part 2
    #Define part2
    part2 = max(guards, key=lambda x: Counter(guards[x]).most_common()[0][1])
    #Define anwser
    part2ANS = part2 * Counter(guards[part2]).most_common()[0][0]
    #Print anwser
    print('Part 2:',part2ANS)
