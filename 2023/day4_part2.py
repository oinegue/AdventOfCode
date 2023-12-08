from pathlib import Path
import re

with Path("day4.txt").open("r") as f:
    lines = [l.strip() for l in f]

n_cards = [1 for _ in lines]
for i, l in enumerate(lines):
    g, = re.search(r"Card\s+\d+:(.*)", l).groups()
    wnn, mnn = g.split("|")
    wnn = set(map(int, re.findall(r"(\d+)\s+", wnn+ " ")))
    mnn = set(map(int, re.findall(r"(\d+)\s+", mnn+ " ")))
    assert(len(wnn) == 10)
    assert(len(mnn) == 25)
    c = sum(1 if mn in wnn else 0 for mn in mnn)
    for j in range(c):
        n_cards[i+j+1] += n_cards[i]

    dbg = 1

print(sum(n_cards))
