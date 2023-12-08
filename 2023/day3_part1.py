from pathlib import Path
from string import digits

with Path("day3.txt").open("r") as f:
    lines = [l.strip() for l in f]

sym_pos = []
for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c != '.' and c not in digits:
            sym_pos.append((x, y))

pns = set()
for x, y in sym_pos:
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
        pns.add((int(pn), yn, xa))

print(sum(p for p,_,_ in pns))
