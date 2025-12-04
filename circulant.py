import networkx as nx

def circulant_graph(n, a):
    G = nx.Graph()
    for x in range(n):
        G.add_edge(x, (x+1) % n)
        G.add_edge(x, (x-1) % n)
        G.add_edge(x, (x+a) % n)
        G.add_edge(x, (x-a) % n)
    return G
