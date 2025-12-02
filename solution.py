import matplotlib.pyplot as plt
import networkx as nx
from itertools import combinations

def infect(Graph, initial):
    infected = set(initial)
    while True: 
        newly_infected = set()
        for vertex in Graph:
            if vertex in infected:
                    continue
            count = sum(1 for nb in Graph.neighbors(vertex) if nb in infected)
            if count >= 2:
                newly_infected.add(vertex)
        if not newly_infected:
            break
        infected |= newly_infected
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


def view_infected(Graph, infected):
    # 1. INITIAL COLORS: red for initially infected, blue for others
    infected_after = infect(Graph, infected)
    node_colors = ["red" if node in infected_after else "blue" for node in Graph.nodes()]
    
    plt.figure()
    nx.draw_circular(Graph, node_color=node_colors, node_size=800, with_labels=True)
    plt.title(f"initial infected {sorted(infected_after)}")
