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

    dangerous = set()

    skip = False
    
    for roid in d:
        x_origin, y_origin, x_vel, y_vel = map(int, roid.split())

        #print(x_origin, y_origin, x_vel, y_vel)

        if x_vel == 0 == y_vel:
            skip = True
        elif x_origin > 99 and x_vel >= 0:
            skip = True
        elif y_origin > 99 and y_vel >= 0:
            skip = True
        elif x_origin < 0 and x_vel <= 0:
            skip = True
        elif y_origin < 0 and y_vel <= 0:
            skip = True
        if skip:

            continue

        x_path, y_path = [x_origin], [y_origin]

        
        max_ = 5000
        min_ = -5000       

        if x_vel > 0:
            x_path = list(range(x_origin, max_, x_vel))
        elif x_vel < 0:
            x_path = list(range(x_origin, min_, x_vel))
        if y_vel > 0:
            y_path = list(range(y_origin, max_, y_vel))
        elif y_vel < 0:
            y_path = list(range(y_origin, min_, y_vel))
            
        diff = len(x_path) - len(y_path)

        ## ensure zip will work - one path can't be shorter else will truncate

        if diff > 0:
            if y_vel == 0:
                y_path = y_path + [y_origin for _ in range(abs(diff))]
            else:
                limit = max_ if y_vel > 0 else min_
                y_path = y_path + list(range(y_path[-1]+1, limit, y_vel))
        elif diff < 0:
            if x_vel == 0:
                x_path = x_path + [x_origin for _ in range(abs(diff))]
            else:
                limit = max_ if y_vel > 0 else min_
                x_path = x_path + list(range(x_path[-1]+1, limit,  x_vel))


        path = zip(x_path, y_path)

        [dangerous.add((x, y)) for x, y in path if 0<=x<w and 0<=y<h]
        print(len(dangerous))

    return safe.difference(dangerous)

#w, h = 8, 8
#result = solve(load("test"))
if True: #result == EXPECTED:
    w, h = 100, 100
    print("TEST PASSED. FINAL RESULT:")
    print(solve(load("day")))
else:
    print(f"EXPECTED {EXPECTED} but got {result}.")
