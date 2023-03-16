i = int

DAY = "08"
EXPECTED = 43

def pre_process(n):
    return n

def load(pre):
    with open(f"{pre}{DAY}.txt") as f:
        return map(pre_process, f.read().splitlines())

        

def solve(data):

    class Node:

        def __init__(self, i):
            self.label = i
            self.connections = []
            self.table = []

    graph = {}

    ORIGIN = 0

    
    graph {i+1:Node(i+1) for i in range(len(d))}

    for i, row in enumerate(d):
        node = i + 1

        for j, weight in enumerate(row.split()):
            neighbour = j

            if node == neighbour:
                continue

            graph[node].connections.append((graph[neighbour], int(weight)))


    ## find shortest path for all nodes

    
    for node in graph:

        node.table = {n:{"cost":INF if n.label!=ORIGIN else 0, "prev":None} for n in graph}

        unvisited = set(graph.values())

        for connection in node.connections:
            prev = node.table[connection]

            neighbour, weight = connection

            if neighbour in visited:
                continue

            cost = weight + node.table[node]["cost"]

            if cost < node.table[neighbour]["cost"]:

                node.table[neighbour]["cost"] = cost
                node.table[neighbour]["prev"] = node

            
        
        

result = solve(load("test"))
if result == EXPECTED:
    print("TEST PASSED. FINAL RESULT:")
    print(solve(load("day")))
else:
    print(f"EXPECTED {EXPECTED} but got {result}.")
