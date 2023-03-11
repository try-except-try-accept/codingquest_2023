from math import prod
i = int

DAY = "05"
EXPECTED = '''........
.######.
.#......
.#......
.######.
.#......
.#......
.######.'''

dims = (8, 8)

def get_mask(x, y, dims):
    pixel = (x * dims[0] + y + 1)
    mask = 2 ** (prod(dims) - pixel) 
    return mask


def get_mask_v2(x, y, w, dims):
    # couldn't get this method to work
    shift = prod(dims) - (((x+1) * dims[0]-1))
    bits = (2 ** w)-1
    mask = bits << shift 
    print(bin(mask).rjust(67))
    return mask

def convert_image(img, w, h):
    s = ""
    for i, bit in enumerate(bin(img)[2:]):
        s += "#" if int(bit) else "."
        if i%w == 0:
            s += "\n"
    return s

def pre_process(n):
    return n

def load(pre):
    with open(f"{pre}{DAY}.txt") as f:
        return map(pre_process, f.read().splitlines())

def solve(d, dims):
    img = 2**prod(dims)
    for row in d:
        x, y, w, h = map(int, row.split())
        for y2 in range(y, y+h):
            for x2 in range(x, x+w):
                img = img ^ get_mask(y2, x2, dims)  

    return convert_image(img, *dims)[1:-1].strip()

result = solve(load("test"), dims)
if result == EXPECTED:
    dims = (50, 10)
    print("TEST PASSED. FINAL RESULT:")
    print(solve(load("day"), dims))
else:
    print(f"EXPECTED\n{EXPECTED}\nbut got\n{result}.")

    for i, j in zip(EXPECTED, result):
        if i != j:
            print("!",end="")
        print(i, end="")
            
