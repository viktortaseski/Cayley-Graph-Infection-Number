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
    
def logTable(table):
    for row in table:
        print(f"{row[0]:10} {row[1]:15} \t{row[2]:20}")

def solution():

    table = [["n", "a", "size" ],]

    for n in range(4,11):
        for a in (2,3):
            G = generate_cayley(n, a)
            k, smallestInfectionSet = m2(G)
            view_infected(G, smallestInfectionSet)

            new_row = [f"{n}", f"{smallestInfectionSet}", f'{k}']
            table.append(new_row)
    logTable(table)

def main():

    #debug(4, 2, {0, 1})
    solution()  


if __name__ == "__main__":
    main()


plt.show()
