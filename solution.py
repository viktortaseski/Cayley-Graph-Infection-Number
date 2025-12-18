from itertools import combinations

import matplotlib.pyplot as plt
import networkx as nx


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

    for k in range(1, n + 1):
        for subset in combinations(nodes, k):
            final = infect(Graph, subset)
            if len(final) == n:
                return k, set(subset)
    return None, None


def check_infected(Graph, infected):
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

        nx.draw_circular(
            Graph,
            node_color=[
                "red" if node in infected else "blue" for node in Graph.nodes()
            ],
            node_size=800,
            with_labels=True,
        )
        plt.show()

        for node in newly_infected:
            Graph.nodes[node]["color"] = "red"
            infected.add(node)
            node_colors = [
                "red" if node in infected else "blue" for node in Graph.nodes()
            ]
            nx.draw_circular(
                Graph, node_color=node_colors, node_size=800, with_labels=True
            )
            plt.show()

    # labels = {node: node + 1 for node in Graph.nodes()}
    # plt.show()
    #


def check_infected_step(Graph, infected):
    fig, ax = plt.subplots()

    pos = nx.circular_layout(Graph)

    def draw():
        ax.clear()
        colors = ["red" if n in infected else "blue" for n in Graph.nodes()]
        nx.draw(Graph, pos, node_color=colors, node_size=800, with_labels=True, ax=ax)
        fig.canvas.draw_idle()

    def on_key(event):
        nonlocal infected

        if event.key == "n":  # press N for next step
            newly_infected = set()

            for v in Graph:
                if v in infected:
                    continue
                count = sum(1 for u in Graph.neighbors(v) if u in infected)
                if count >= 2:
                    newly_infected.add(v)

            if newly_infected:
                infected |= newly_infected
                draw()
            else:
                print("No more infections.")

    fig.canvas.mpl_connect("key_press_event", on_key)
    draw()
    plt.show()
