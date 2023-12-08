from pathlib import Path
import re
from string import digits
from dataclasses import dataclass
from tqdm import tqdm


@dataclass(unsafe_hash=True)
class SeedRange:
    level: int
    A: int
    range: int

    @property
    def B(self):
        return self.A + self.range


with Path("day5.txt").open("r") as f:
    seeds = re.findall(r"(\d+)\s+", f.readline().strip() + " ")
    seed_ranges = [
        SeedRange(0, int(s), int(r)) for s, r in zip(seeds[::2], seeds[1::2])
    ]

    level = 0
    for l in tqdm(f.readlines()):
        l = l.strip()
        if l == "":
            continue

        if l[0] not in digits:
            level += 1
            for s in seed_ranges:
                s.level = level

            # remove empty seed ranges
            seed_ranges = [sr for sr in seed_ranges if sr.range > 0]

            # join ranges on new level
            seed_ranges.sort(key=lambda sr: sr.A)
            i = 0
            while i < len(seed_ranges) - 1:
                assert seed_ranges[i].B <= seed_ranges[i + 1].A
                if seed_ranges[i].B == seed_ranges[i + 1].A:
                    seed_ranges[i].range += seed_ranges[i + 1].range
                    del seed_ranges[i + 1]
                else:
                    i += 1

            continue

        X, C, rng = map(int, re.search(r"(\d+) (\d+) (\d+)", l).groups())
        D = C + rng
        Y = X + rng

        new_seed_ranges = []
        for sr in seed_ranges:
            if sr.level > level:
                new_seed_ranges.append(sr)
            elif C <= sr.A:
                if D > sr.B:
                    sr.A += X - C
                    sr.level += 1
                    new_seed_ranges.append(sr)
                elif D > sr.A:
                    # Remaining part
                    new_seed_ranges.append(SeedRange(sr.level, D, sr.B - D))

                    # Converted part
                    sr.range = D - sr.A
                    sr.A += X - C
                    sr.level += 1
                    new_seed_ranges.append(sr)
                else:
                    new_seed_ranges.append(sr)
            elif C < sr.B:
                if D > sr.B:
                    # Remaining part
                    new_seed_ranges.append(SeedRange(sr.level, sr.A, C - sr.A))

                    # Converted part
                    sr.range = sr.B - C
                    sr.A = X
                    sr.level += 1
                    new_seed_ranges.append(sr)
                else:
                    # Remaining part
                    new_seed_ranges.append(SeedRange(sr.level, sr.A, C - sr.A))
                    new_seed_ranges.append(SeedRange(sr.level, D, sr.B - D))

                    # Converted part
                    sr.range = rng
                    sr.A = X
                    sr.level += 1
                    new_seed_ranges.append(sr)
            else:
                new_seed_ranges.append(sr)

        seed_ranges = list(set(new_seed_ranges))
        dbg = 1

    print(min(sr.A for sr in seed_ranges))
