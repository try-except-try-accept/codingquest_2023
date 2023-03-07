i = int

DAY = "02"
EXPECTED = 17837


def load(pre):
    with open(f"{pre}{DAY}.txt") as f:
        return map(i, f.read().splitlines())

def solve(d):
    MASK = (2**15)-1
    binaries = [bin(num)[2:].zfill(16) for num in d]
    wanted = filter(lambda n: n.count('1')%2==0, binaries)
    masked = [i(w, 2) & MASK for w in wanted]
    return round(sum(masked) / len(masked))

result = solve(load("test"))
if result == EXPECTED:
    print("TEST PASSED. FINAL RESULT:")
    print(solve(load("day")))
else:
    print(f"EXPECTED {EXPECTED} but got {result}.")
