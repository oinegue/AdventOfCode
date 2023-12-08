from pathlib import Path
from string import digits
import re

with Path("day1.txt").open("r") as f:
    lines = [l.strip() for l in f]

words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

s = 0
p = "|".join(words.keys()) + "|" + "|".join(digits)
for l in lines:
    d0 = re.search(p, l).group()
    d1 = re.search(p[::-1], l[::-1]).group()[::-1]
    d0 = words.get(d0, d0)
    d1 = words.get(d1, d1)
    s += int(d0) * 10 + int(d1)
print(s)
