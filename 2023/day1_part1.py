from pathlib import Path
from string import digits

with Path("day1.txt").open("r") as f:
    lines = [l.strip() for l in f]

s = 0
for l in lines:
    d = [int(c) for c in l if c in digits]
    s += d[0] * 10 + d[-1]
print(s)
