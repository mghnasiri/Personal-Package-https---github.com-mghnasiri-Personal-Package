# output_manager.py
import matplotlib.pyplot as plt
import pandas as pd

# Function for visualizing the graph and displaying results in a table


def visualize_graph(G, depot, nx, x, my_pos, results, dataset_name_with_extension):
    # Create a figure with two subplots (one for the graph and one for the table)
    fig = plt.figure(figsize=(10, 8))
    fig.canvas.manager.set_window_title(dataset_name_with_extension)

    # Create a subplot for the graph
    ax1 = fig.add_subplot(211)  # 2 rows, 1 column, 1st subplot
    tour_edges = [e for e in G.edges if x[e].x > 0.9]
    node_colors = ["red" if node == depot else "blue" for node in G.nodes()]
    node_sizes = [200 if node == depot else 100 for node in G.nodes()]

    # Counting nodes and edges
    num_nodes = len(G.nodes())
    num_edges = len(tour_edges)

    # Visualizing the graph
    nx.draw(G, pos=my_pos, ax=ax1, node_color=node_colors, node_size=node_sizes,
            edgelist=tour_edges, edge_color='green', width=2.0, with_labels=True)

    # Adding the count of nodes and edges as a title to the graph
    ax1.set_title(f'Graph with {num_nodes} nodes and {num_edges} edges')

    # Create a subplot for the table
    ax2 = fig.add_subplot(212)  # 2 rows, 1 column, 2nd subplot
    ax2.axis('tight')
    ax2.axis('off')

    ax2.table(cellText=[list(results.values())], colLabels=list(
        results.keys()), cellLoc='center', loc='center')

    plt.tight_layout()
    plt.show ()
