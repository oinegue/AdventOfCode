from pathlib import Path
from string import digits
import re

with Path("day2.txt").open("r") as f:
    lines = [l.strip() for l in f]

cubes = {"red": 12, "green": 13, "blue": 14}
s = 0
for l in lines:
    i, g = re.search(r"Game (\d+):(.*)", l).groups()
    for _, n, c in re.findall(r"( (\d+) (red|green|blue)),", g.replace(";", ",") + ","):
        if int(n) > cubes.get(c):
            break
    else:
        s += int(i)
print(s)
