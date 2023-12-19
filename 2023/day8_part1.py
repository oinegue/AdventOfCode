from itertools import cycle
from pathlib import Path

import re

with Path("day8.txt").open("r") as f:
    instr = f.readline().strip()
    f.readline()
    m = {}
    for l in f:
        k, l, r = re.search(r"(\w{3}) = \((\w{3}), (\w{3})\)", l.strip()).groups()
        m[k] = {"L": l, "R": r}
    
    t = "AAA"
    i = 0
    instr_it = cycle(instr)
    while True:
        i += 1
        t = m[t][next(instr_it)]
        if t == "ZZZ":
            break        
print(i)
