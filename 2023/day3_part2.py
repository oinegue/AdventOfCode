from pathlib import Path
from string import digits

with Path("day3.txt").open("r") as f:
    lines = [l.strip() for l in f]

possible_gear_pos = []
for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c == '*':
            possible_gear_pos.append((x, y))

s = 0
for x, y in possible_gear_pos:
    adj_num = set()
    for xn, yn in [
        (x-1, y-1), (x+0, y-1), (x+1, y-1),
        (x-1, y+0), (x+0, y+0), (x+1, y+0),
        (x-1, y+1), (x+0, y+1), (x+1, y+1),
    ]:
        if (
            yn < 0 or yn >= len(lines) or
            xn < 0 or xn >= len(lines[0]) or
            lines[yn][xn] not in digits
        ):
            continue
        xa = xn
        xb = xn
        while xa >= 0 and lines[yn][xa-1] in digits:
            xa -= 1
        while xb < len(lines[0])-1 and lines[yn][xb+1] in digits:
            xb += 1
        pn = lines[yn][xa:xb+1]
        adj_num.add((int(pn), yn, xa))
    
    if len(adj_num) == 2:
        adj_num = list(adj_num)
        s += adj_num[0][0] * adj_num[1][0]

print(s)
