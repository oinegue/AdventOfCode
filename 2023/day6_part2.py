from pathlib import Path
import re
import math

with Path("day6.txt").open("r") as f:
    times = [int(t.replace(" ", "")) for t in re.findall(r"([\d\s]+)", f.readline())]
    dists = [int(d.replace(" ", "")) for d in re.findall(r"([\d\s]+)", f.readline())]

s = 1
for T, D in zip(times, dists):
    # p²-p*T+D < 0
    p1 = math.ceil((T - math.sqrt(T**2 - 4 * D)) / 2)
    p2 = math.floor((T + math.sqrt(T**2 - 4 * D)) / 2)

    s *= p2-p1+1

print(s)
