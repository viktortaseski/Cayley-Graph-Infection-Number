import matplotlib.pyplot as plt
import networkx as nx

from solution import check_infected, m2
from utils import logTable, write_table


def generate_cayley(numberOfNodes, stepSize):
    edges = []
    steps = [1, -1, stepSize, -stepSize]

    for vertex in range(numberOfNodes):
        for s in steps:
            u = (vertex + s) % numberOfNodes
            edges.append((vertex, u))

    return nx.Graph(edges)


def solution():
    filename = "results.csv"
    results = []
    results.append(["n", "a", "Minimum Infection Set", "m2(Cn(1,a))"])

    for n in range(4, 11):
        for a in (2, 3):
            G = generate_cayley(n, a)
            k, smallestInfectionSet = m2(G)
            results.append([n, a, sorted(list(smallestInfectionSet)), k])
            check_infected(G, smallestInfectionSet)

    write_table(filename, results)

    print("\nSaved results to", filename)
    print("\n===== RESULT TABLE =====")
    logTable(results)


def main():
    solution()


if __name__ == "__main__":
    main()
    plt.show()
