"""

Consider our representation of permutations of students in a line from Exercise 1. (The teacher only swaps the positions of two students that are next to each other in line.) Let's consider a line of three students, Alice, Bob, and Carol (denoted A, B, and C). Using the Graph class created in the lecture, we can create a graph with the design chosen in Exercise 1: vertices represent permutations of the students in line; edges connect two permutations if one can be made into the other by swapping two adjacent students.

We construct our graph by first adding the following nodes:"""

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)
    
"""
Add the appropriate edges to the graph.
"""

edges = []
edges.append(Edge(nodes[0], nodes[1])) # edges[0]
edges.append(Edge(nodes[0], nodes[2])) # edges[1]
edges.append(Edge(nodes[1], nodes[4])) # edges[2]
edges.append(Edge(nodes[2], nodes[3])) # edges[3]
edges.append(Edge(nodes[3], nodes[5])) # edges[4]
edges.append(Edge(nodes[4], nodes[5])) # edges[5]

for e in edges:
    g.addEdge(e)
    
# CORRECT

