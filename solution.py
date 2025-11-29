import matplotlib.pyplot as plt
import networkx as nx

edges1 = [
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
edges2 = [
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 1),
    (5, 2),
]


G = nx.Graph(edges2)
pos = nx.spring_layout(G, seed=0)

infected = {3, 1}
print(f"Initial infected nodes: {infected}")

# 1. INITIAL COLORS: red for initially infected, blue for others
while True:
    newly_infected = set()

    for vertex in G:
        if vertex in infected:
            continue
        count = 0
        for neighbor in G.neighbors(vertex):
            if neighbor in infected:
                count += 1
        if count >= 2:
            newly_infected.add(vertex)
    if not newly_infected:
        break

    for node in newly_infected:
        G.nodes[node]["color"] = "red"
        infected.add(node)


print("Newly infected:", infected)

node_colors = ["red" if node in infected else "blue" for node in G.nodes()]

nx.draw_circular(G, node_color=node_colors, node_size=800, with_labels=True)
plt.show()
