from pathlib import Path
import re

with Path("day4.txt").open("r") as f:
    lines = [l.strip() for l in f]

s = 0
for l in lines:
    g, = re.search(r"Card\s+\d+:(.*)", l).groups()
    wnn, mnn = g.split("|")
    wnn = set(map(int, re.findall(r"(\d+)\s+", wnn+ " ")))
    mnn = set(map(int, re.findall(r"(\d+)\s+", mnn+ " ")))
    assert(len(wnn) == 10)
    assert(len(mnn) == 25)
    c = sum(1 if mn in wnn else 0 for mn in mnn)
    if c > 0:
        s += 2**(c-1)

print(s)
