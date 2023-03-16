i = int

DAY = "09"
EXPECTED = 16
from collections import Counter
from math import prod

def pre_process(n):
    return n

def load(pre):
    with open(f"{pre}{DAY}.txt") as f:
        return f.read().splitlines()


class Node:

    def __init__(self, num):
        self.value = num
        self.left = None
        self.right = None

def add(num, node):        
    if num < node.value:
        if node.left is None:
            node.left = Node(num)
        else:
            add(num, node.left)
    else:
        if node.right is None:
            node.right = Node(num)
        else:
            add(num, node.right)
    
def traverse(node, deepest=0, d=1, widths=None):
    left, right = node.left, node.right
    
    if widths is None:
        widths = Counter()
    else:
        widths[d] += 1
        
    if left is not None:
        deepest, _ = traverse(left, deepest, d+1, widths)

    if right is not None:
        deepest, _ = traverse(right, deepest, d+1, widths)

    if d > deepest:
        deepest = d

    return deepest, max(widths.values())
        




def solve(d):
    root = Node(int(d[0], 16))

    for num in d[1:]:
        add(int(num, 16), root)
    
    result = traverse(root)

    return prod(result)

result = solve(load("test"))
if result == EXPECTED:
    print("TEST PASSED. FINAL RESULT:")
    print(solve(load("day")))
else:
    print(f"EXPECTED {EXPECTED} but got {result}.")
