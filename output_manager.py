
""" Dedicated to handling output-related tasks.
This could include functions for formatting output, saving results to a file, printing results in a certain way, etc. """
# output_manager.py
import matplotlib.pyplot as plt



# Function for visualizing the graph
def visualize_graph(G,depot,nx,x,my_pos):
    tour_edges = [ e for e in G.edges if x[e].x > 0.9 ]
    node_colors = ["red" if node == depot else "blue" for node in G.nodes()]
    node_sizes = [200 if node == depot else 100 for node in G.nodes()]

    nx.draw(G.edge_subgraph(tour_edges), pos=my_pos, with_labels=True, node_color=node_colors, node_size=node_sizes, edgelist=tour_edges, edge_color='green', width=2.0)
    plt.show()

