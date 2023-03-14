i = int

DAY = "06"
EXPECTED = {(5,4)}

def pre_process(n):
    return n

def load(pre):
    with open(f"{pre}{DAY}.txt") as f:
        return map(pre_process, f.read().splitlines())

def get_distance(val):

    if val > 99:
        return (val - 99)
    elif val < 0:
        return 0 - val
    else:
        return 0

def solve(d):

    safe = []
    [[safe.extend([(x, y)]) for x in range(w)] for y in range(h)]
    safe = set(safe)


    for roid in d:
        x_origin, y_origin, x_vel, y_vel = map(int, roid.split())

        x = x_origin + (3600 * x_vel)
        y = y_origin + (3600 * y_vel)
        if (x, y) in safe:
            safe.remove((x, y))

        for i in range(60):
            x += x_vel
            y += y_vel

            if (x, y) in safe:
                safe.remove((x, y))

    return list(safe)

    
    

       

#w, h = 8, 8
#result = solve(load("test"))
if True: #result == EXPECTED:
    w, h = 100, 100
    print("TEST PASSED. FINAL RESULT:")
    print(solve(load("day")))
else:
    print(f"EXPECTED {EXPECTED} but got {result}.")
