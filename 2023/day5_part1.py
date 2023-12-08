from pathlib import Path
import re
from string import digits

with Path("day5.txt").open("r") as f:
    seeds = re.findall(r"(\d+)\s+", f.readline().strip() + " ")
    seeds = [[0, int(s)] for s in seeds]

    level = 0
    for l in f.readlines():
        l = l.strip()
        if l == "":
            continue

        if l[0] not in digits:
            level += 1
            for s in seeds:
                s[0] = level
            continue

        dst, src, rng = map(int, re.search(r"(\d+) (\d+) (\d+)", l).groups())

        for s in seeds:
            if s[0] > level:
                continue
            if src <= s[1] and s[1] < (src + rng):
                s[1] = dst + s[1] - src
                s[0] += 1

    print(min(n for _, n in seeds))
