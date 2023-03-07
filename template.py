i = int

DAY = "01"
EXPECTED = 17837


def load(pre):
    with open(f"{pre}{DAY}.txt") as f:
        return map(i, f.read().splitlines())

def solve(d):
    result = None
    return result

result = solve(load("test"))
if result == EXPECTED:
    print("TEST PASSED. FINAL RESULT:")
    print(solve(load("day")))
else:
    print(f"EXPECTED {EXPECTED} but got {result}.")
