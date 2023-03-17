i = int
from math import inf as INF
DAY = "10"
EXPECTED = 115

def pre_process(n):
    return n

def load(pre):
    with open(f"{pre}{DAY}.txt") as f:
        return list(map(pre_process, f.read().splitlines()))

class Node:
    def __init__(self, label):
        self.label = label
        self.connections = {}

    def __repr__(self):
        return self.label

def bug_print(*n):
    pass

class Graph:

    def __init__(self, data):
        
        self.nodes = {}
        self.origin = HOME
        self.destination = END
        self.parse(data)

    

    def get_node(self, label):

        node = self.nodes.get(label)

        if node is None:
            node = Node(label)
            self.nodes[label] = node

        if label == self.origin:
            self.origin = node
        elif label == self.destination:
            self.destination = node

        return node

    def parse(self, data):

        for row in data:

            start, stops = row.split(" => ")

            start = self.get_node(start)

            for stop in stops.split():

                dest, weight = stop.split(":")

                dest = self.get_node(dest)
                weight = int(weight)
                
                start.connections[dest] = weight
        

    def shortest_path(self):
        destination = self.destination
        node = destination

        
        path = [str(destination)]

        tot = 0

        while node is not self.origin:
                prev = self.table[node]["prev"]
                tot += prev.connections[node] + WAIT
                node = prev
                
                path.append(str(node))
                
                


        print(f"The shortest path from {self.origin} to {destination} is..." + " → ".join(reversed(path)))

        return tot - WAIT

    def dijk_table(self):

        table = {n:{"node":str(n), "cost":INF if n is not self.origin else 0, "prev":"", "calc":""} for n in self.nodes.values()}                        


        unvisited = list(self.nodes.values())

        visited = []


        while len(unvisited):

                smallest = INF
                current_node = None

                ## find the unvisited vertex with smallest known distance from the origin
                for node, data in table.items():
                        if node not in unvisited:        continue
                        if data["cost"] < smallest:
                                smallest = data["cost"]
                                current_node = node
                bug_print("The current vertex is", current_node)

                ## find each unvisited neighbour of the current vertex

                for neighbour, cost in current_node.connections.items():
                        
                        bug_print(f"{current_node} is connected to {neighbour}")
                        if neighbour not in unvisited:
                            pass
                            bug_print("Already visited")
                        else:
                            ## calculate total distance from origin node
                            tot = cost

                            calc = str(tot)
                            # until we've got back to the start

                            
                            bug_print(f"We need to make it back from {current_node} to {self.origin}")
                            pitstop = table[current_node]["cost"]
                            bug_print(f"Came via {current_node} and that cost {pitstop}")
                            tot += pitstop
                            calc += " + " + str(pitstop)
                            bug_print(f"so the total is now {tot}")


                            if tot < table[neighbour]["cost"]:
                                    table[neighbour]["prev"] = current_node                                                        
                                    table[neighbour]["cost"] = tot                                                                                                              
                                    table[neighbour]["calc"] = calc
                                 
                                    for node, data in table.items():
                                        pass
                                        bug_print(f'{str(node)} \t\t {data["cost"]} \t\t {data["prev"]} \t\t {data["calc"]}')

                                    bug_print()
                            else:
                                    bug_print(f"{tot} was not shorter. table not updated")
                unvisited.remove(current_node)
        self.table = table


def solve(d):
    g = Graph(d)
    g.dijk_table()
    return g.shortest_path()

WAIT = 10
HOME, END = "AAA", "ZZZ"
result = solve(load("test"))

if result == EXPECTED:
    HOME, END = "TYC", "EAR"
    WAIT = 600
    print("TEST PASSED. FINAL RESULT:")
    print(solve(load("day")))
else:
    print(f"EXPECTED {EXPECTED} but got {result}.")
