import sys
import math
from collections import defaultdict

letters = """
A+ 90 
A  85
A- 80
B+ 77
B  73
B- 70
C+ 67
C  60
D  50
F  0
"""

elements = letters.strip().split()
# even entries are letters
letters = [x for (i,x) in enumerate(elements) if i % 2 == 0]
cutoffs = [float(x) for (i,x) in enumerate(elements) if (i % 2 == 1)]
def lookup(perc):
    perc = round(float(perc))
    for i, cutoff in enumerate(cutoffs):
        if perc >= cutoff:
            return letters[i]

groupby = defaultdict(int)

sum = 0
sumSq = 0
count = 0

for line in sys.stdin.readlines():
    perc = float(line.strip())
    letter = lookup(perc)
    print letter
    groupby[letter] += 1
    sum += perc
    sumSq += perc*perc
    count += 1

avg = sum / count
stdev = math.sqrt((sumSq / count) - avg*avg)

print "=" * 60
for letter in letters:
    print "%2s %d" % (letter, groupby[letter])
print "=" * 60
print "Average:      %.2f" % avg
print "Standard Dev: %.2f" % stdev

