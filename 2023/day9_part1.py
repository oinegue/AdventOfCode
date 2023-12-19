from itertools import cycle
from pathlib import Path

import re

def diff(a):
    return [a[i+1] - a[i] for i in range(len(a) - 1)]

s = 0
with Path("day9.txt").open("r") as f:
    for l in f:
        nn = [int(i) for i in l.split()]

        dd = [nn]
        while len(dd[-1]) > 1:
            dd.append(diff(dd[-1]))
        
        next_n = sum(d[-1] for d in dd)

        s += next_n
    
print(s)

