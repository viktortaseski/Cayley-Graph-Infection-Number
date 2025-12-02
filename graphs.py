import matplotlib.pyplot as plt
import networkx as nx

from solution import view_infected
from solution import m2

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

def debug():
    G1 = generate_cayley(5, 2)
    G2 = generate_cayley(10, 2)
    G3 = generate_cayley(10, 3)
    view_infected(G1, {1, 3})
    view_infected(G2, {1, 6})
    view_infected(G3, {1, 6})

def main():

    #debug()

    for n in range(4,11):
        for a in (2,3):
            G = generate_cayley(n, a)
            k, smallestInfectionSet = m2(G)
            view_infected(G, smallestInfectionSet)
            print(f"n={n}, a={a}: m2 = {k}, example contagious set = {sorted(smallestInfectionSet)}")


if __name__ == "__main__":
    main()


plt.show()
