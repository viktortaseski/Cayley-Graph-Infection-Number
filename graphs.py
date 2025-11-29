import networkx as nx
import matplotlib.pyplot as plt
from solution import check_infected 

edges = [
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 1),
    (5, 2),
    (5, 3),
    (5, 4),
    (5, 6),
    (5, 7),
    (6, 7),
]

G = nx.Graph(edges)
G2 = nx.Graph([
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 1),
    (5, 2),
])

check_infected(G, {1, 7})
check_infected(G2, {2,3})