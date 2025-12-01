import matplotlib.pyplot as plt
import networkx as nx


def check_infected(Graph, infected, graph_name="Graph"):
    # 1. INITIAL COLORS: red for initially infected, blue for others
    initial_infected = set(infected)
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

    plt.figure(graph_name)
    plt.title(f"{graph_name}: initial infected {sorted(initial_infected)}")
    nx.draw_circular(Graph, node_color=node_colors, node_size=800, with_labels=True)
