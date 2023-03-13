i = int

DAY = "06"
EXPECTED = "5:4"

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

    [[safe.extend([(y, x)]) for x in range(w)] for y in range(h)]

    safe = set(safe)

    
    
    for roid in d:
        xo, yo, xvel, yvel = map(float, roid.split())
        print(xo, yo, xvel, yvel)
        skip = False

        if xvel == 0 == yvel:
            skip = True

        elif xo > 99 and xvel >= 0:
            skip = True
        elif yo > 99 and yvel >= 0:
            skip = True
        elif xo < 0 and xvel <= 0:
            skip = True
        elif yo < 0 and yvel <= 0:
            skip = True

        if skip:
            print("Will never cross the region")
            continue
            
        
        x_distance = get_distance(xo)

        y_distance = get_distance(yo)


        if x_distance == y_distance:
            if yvel == 0:
                x = 0
            else:
                x = 0 if xvel > 0 else 99

            if xvel == 0:
                y = 0

            else:            
                y = 0 if yvel > 0 else 99

        else:

            best = min(x_distance, y_distance)
                
                
            yo = yo + best * yvel
            xo = xo + best * xvel
                


            x = xo
            y = yo

        print("Will cross at", x, y)

        while True:
            x += xvel
            y += yvel

                       

            x_limit = (x < 0) if xvel < 0 else x > 99
            y_limit = (y < 0) if yvel < 0 else y > 99


            if x_limit or y_limit:
                break

            if 0<=x<=99 and 0<=y<=99:
                coord = (x, y)
                if coord in safe:
                    safe.remove(coord)


        
    print(safe)
w, h = 8, 8
result = solve(load("test"))
if result == EXPECTED:
    w, y = 100, 100
    print("TEST PASSED. FINAL RESULT:")
    print(solve(load("day")))
else:
    print(f"EXPECTED {EXPECTED} but got {result}.")
