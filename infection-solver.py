from itertools import combinations
from solution import check_infected

def infection_number(G):
    n = len(G.nodes())
    nodes = list(G.nodes())

    for k in range(1, n+1):
        for S in combinations(nodes, k):
            infected = set(S)
            if check_infected(G.copy(), infected, display=False):
                return k, S
    return None
