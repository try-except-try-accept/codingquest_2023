from collections import Counter
from math import prod
i = int

DAY = "01"
EXPECTED = 187733700

def pre_process(n):
    return n

def load(pre):
    with open(f"{pre}{DAY}.txt") as f:
        return map(pre_process, f.read().splitlines())

def solve(d):
    rem = len("a056a0fd-0b61-4f38-a874-a464646447af ")

    tots = Counter()

    for line in d:
        amt, cat = line[rem:].split()
        tots[cat] += int(amt)
        
    return prod(t % 100 for t in tots.values())

result = solve(load("test"))
if result == EXPECTED:
    print("TEST PASSED. FINAL RESULT:")
    print(solve(load("day")))
else:
    print(f"EXPECTED {EXPECTED} but got {result}.")
