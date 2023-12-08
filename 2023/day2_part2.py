from pathlib import Path
from string import digits
import re

with Path("day2.txt").open("r") as f:
    lines = [l.strip() for l in f]

s = 0
for l in lines:
    i, g = re.search(r"Game (\d+):(.*)", l).groups()
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for _, n, c in re.findall(r"( (\d+) (red|green|blue)),", g.replace(";", ",") + ","):
        min_cubes[c] = max(int(n), min_cubes[c])
    s += min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
print(s)
