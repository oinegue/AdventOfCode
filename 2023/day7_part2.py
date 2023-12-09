from dataclasses import dataclass
from enum import Enum
from functools import cached_property
from pathlib import Path
from collections import Counter

import re


class Type(Enum):
    HIGH = 0
    ONE_P = 1
    TWO_P = 2
    THREE = 3
    FULL = 4
    FOUR = 5
    FIVE = 6


cards_order = "AKQT98765432J"


@dataclass
class Hand:
    hand: str
    bid: str | int

    def __post_init__(self):
        self.bid = int(self.bid)

    @cached_property
    def type(self) -> Type:
        c = Counter(self.hand)
        v = list(sorted(c.values()))
        j = c["J"]
        if v == [5]:
            return Type.FIVE
        elif v == [1, 4]:
            if j > 0:
                return Type.FIVE
            return Type.FOUR
        elif v == [2, 3]:
            if j > 0:
                return Type.FIVE
            return Type.FULL
        elif v == [1, 1, 3]:
            if j > 0:
                return Type.FOUR
            return Type.THREE
        elif v == [1, 2, 2]:
            if j == 1:
                return Type.FULL
            elif j == 2:
                return Type.FOUR
            return Type.TWO_P
        elif v == [1, 1, 1, 2]:
            if j > 0:
                return Type.THREE
            return Type.ONE_P
        elif v == [1, 1, 1, 1, 1]:
            if j == 1:
                return Type.ONE_P
            return Type.HIGH
        else:
            raise ValueError("?!?")

    def __eq__(self, v: "Hand") -> bool:
        return self.hand == v.hand

    def __gt__(self, v: "Hand") -> bool:
        if self.type.value > v.type.value:
            return True
        elif self.type.value == v.type.value:
            for a, b in zip(self.hand, v.hand):
                if a == b:
                    continue
                return cards_order.index(a) < cards_order.index(b)
            raise RuntimeError("?!?")
        else:
            return False


with Path("day7.txt").open("r") as f:
    hands = [Hand(*re.search(r"(.{5}) (\d+)", l.strip()).groups()) for l in f]

hands.sort()
s = 0
for i, h in enumerate(hands, 1):
    s += i * h.bid
print(s)
