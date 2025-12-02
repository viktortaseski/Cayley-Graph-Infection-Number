import matplotlib.pyplot as plt
import networkx as nx

from solution import view_infected
from solution import m2

def generate_cayley(numberOfNodes, stepSize):
    edges = []
    steps = [1, -1, stepSize, -stepSize]

    for vertex in range(numberOfNodes):
        for s in steps:
            u = (vertex + s) % numberOfNodes
            edges.append((vertex, u))

    return nx.Graph(edges)

def debug(n, a, set):
    G = generate_cayley(n, a)
    view_infected(G, set)
    

def solution():
    for n in range(4,11):
        print(f"Graph with {n} nodes")
        for a in (2,3):
            G = generate_cayley(n, a)
            k, smallestInfectionSet = m2(G)
            view_infected(G, smallestInfectionSet)
            print(f"\tn={n}, a={a}: m2/subset size = {k}, example contagious set = {sorted(smallestInfectionSet)}")
        print(f"\n")


def main():

    #debug(6, 2, {0})
    solution()

    


if __name__ == "__main__":
    main()


plt.show()
