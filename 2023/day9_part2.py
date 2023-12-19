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
        
        n = dd[-1][0]
        for i in range(len(dd)-1, -1, -1):
            n = dd[i][0] - n
        s += n
    
print(s)

