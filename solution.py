import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations

def infect(Graph, initial):
    infected = set(initial)
    while True:
        newly = set()
        for v in Graph:
            if v in infected:
                continue
            count = sum(1 for nb in Graph.neighbors(v) if nb in infected)
            if count >= 2:
                newly.add(v)
        if not newly:
            break
        infected |= newly
    return infected

def m2(Graph):
    nodes = list(Graph.nodes)
    n = len(nodes)

    for k in range(1, n+1):
        for subset in combinations(nodes, k):
            final = infect(Graph, subset)
            if len(final) == n:
                return k, set(subset)
    return None, None
def check_infected(Graph, infected):
# 1. INITIAL COLORS: red for initially infected, blue for others

    print(f"{Graph}\tBEFORE infection: {infected}")
    while True:
        newly_infected = set()

        for vertex in Graph:
            if vertex in infected:
             continue
            count = 0
            for neighbor in Graph.neighbors(vertex):
                if neighbor in infected:
                    count += 1
            if count >= 2:
                newly_infected.add(vertex)
        if not newly_infected:
            break

        for node in newly_infected:
            Graph.nodes[node]["color"] = "red"
            infected.add(node)
    

    print(f"{Graph}\tAFTER infected:", infected)
    node_colors = ["red" if node in infected else "blue" for node in Graph.nodes()]

    #labels = {node: node + 1 for node in Graph.nodes()}
    nx.draw_circular(Graph, node_color=node_colors, node_size=800, with_labels=True)
    plt.show()
