from itertools import cycle
from pathlib import Path
from math import lcm
import re

# NB: I don't think this is a general solution, but it works... don't know

with Path("day8.txt").open("r") as f:
    instr = f.readline().strip()
    f.readline()
    m = {}
    tt = {}
    for l in f:
        k, l, r = re.search(r"(\w{3}) = \((\w{3}), (\w{3})\)", l.strip()).groups()
        m[k] = {"L": l, "R": r}
        if k.endswith("A"):
            tt[len(tt)] = k
    
    cc = {}
    i = 0
    instr_it = cycle(instr)
    while True:
        i += 1
        ins = next(instr_it)
        for j, t in tt.items():
            tt[j] = m[t][ins]
        
        should_stop = True
        for j, t in list(tt.items()):
            if t.endswith("Z"):
                cc[j] = i
                del tt[j]
        
        if len(tt) == 0:
            break
print(lcm(*[int(i) for i in cc.values()]))
