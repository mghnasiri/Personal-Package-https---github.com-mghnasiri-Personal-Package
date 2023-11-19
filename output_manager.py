
""" Dedicated to handling output-related tasks.
This could include functions for formatting output, saving results to a file, printing results in a certain way, etc. """
# output_manager.py
import matplotlib.pyplot as plt



# Function for visualizing the graph
def visualize_graph(G,depot,nx,x,my_pos):
    # Create a figure and axis object

    fig, ax = plt.subplots()

    tour_edges = [e for e in G.edges if x[e].x > 0.9]
    node_colors = ["red" if node == depot else "blue" for node in G.nodes()]
    node_sizes = [200 if node == depot else 100 for node in G.nodes()]
    
    # Counting nodes and edges
    num_nodes = len(G.nodes())
    num_edges = len(tour_edges)

    # Visualizing the graph
    #nx.draw(G, pos=my_pos, node_color=node_colors, node_size=node_sizes, with_labels=True)
    #nx.draw_networkx_edges(G, pos=my_pos, edgelist=tour_edges, edge_color="green", width=2)
    nx.draw(G, pos=my_pos, ax=ax,node_color=node_colors, node_size=node_sizes, edgelist=tour_edges, edge_color='green', width=2.0, with_labels=True)


    # Adding the count of nodes and edges as a title to the plot
    ax.set_title(f'Graph with {num_nodes} nodes and {num_edges} edges')
    plt.show()

