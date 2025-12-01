import matplotlib.pyplot as plt
import networkx as nx

from solution import check_infected

#                   N - #vertices   "a" - step size
# These are the only 2 parameters since the first parameter is always one and we do not need to pass it.
def generate_cayley(numberOfNodes, stepSize):
    edges = []
    steps = [1, -1, stepSize, -stepSize]

    for vertex in range(numberOfNodes):
        for s in steps:
            u = (vertex + s) % numberOfNodes
            edges.append((vertex, u))

    return nx.Graph(edges)

G1 = generate_cayley(5, 2)
G2 = generate_cayley(10, 2)
G3 = generate_cayley(10, 3)
check_infected(G1, {1, 3}, graph_name="G1")
check_infected(G2, {1, 6}, graph_name="G2")
check_infected(G3, {1, 6}, graph_name="G3")
plt.show()
