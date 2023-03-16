i = int

DAY = "08"
EXPECTED = 43
from itertools import permutations
from math import inf as INF

def pre_process(n):
    return list(map(int, n.split()))

def load(pre):
    with open(f"{pre}{DAY}.txt") as f:
        return list(map(pre_process, f.read().splitlines()))

        

def solve(data):

    best = INF

    for p in permutations(range(len(data))):

        tot = 0
        log = ""
        for node, neighbour in zip(p, p[1:]+(p[0],)):
            weight = data[node][neighbour]
            log += (f"travel from {node} to {neighbour} costs {weight}\n")
            tot += weight

        if tot < best:
            best = tot
            info = log

    print(info)
    return tot

result = solve(load("test"))
if result == EXPECTED:
    print("TEST PASSED. FINAL RESULT:")
    print(solve(load("day")))
else:
    print(f"EXPECTED {EXPECTED} but got {result}.")
