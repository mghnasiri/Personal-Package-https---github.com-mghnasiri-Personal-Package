""" This file use functions or classes from both model.py and output_manager.py.
It acts as the orchestrator, calling the necessary functions from each module and passing data between them. """
import networkx as nx
# main.py
import pandas as pd
from model import create_graph, parse_coordinates, eucl_dist, solve_TSP_MTZ_problem
from output_manager import visualize_graph

def main():
    
    # Load the dataset
    data_path = '/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/eil51.tsp'
    data = pd.read_csv(data_path)

    # Number of data points you want to use (including depot)
    num_data_points = 51  # Adjust this value as needed

    # Extract a subset based on the desired number of data points
    data_subset = data.head(num_data_points)
    n=len(data_subset)-1
    Q=200
    k = 1                       # number of vehicles
    depot = 0                       
    dem_points = list(range(1,n+1)) # nodes 1, 2, ..., 20
    
    G = create_graph(data_subset,num_data_points)
    cities = parse_coordinates(data_path)

    my_pos ={point[0]-1: (point[1], point[2]) for point in cities} # pos[i] = (x_i, y_i)«

    for i,j in G.edges:
     (x1,y1) = my_pos[i]
     (x2,y2) = my_pos[j]
     G.edges[i,j]['length'] = eucl_dist(x1,y1,x2,y2)





    cities = parse_coordinates(data_path)
    cities = parse_coordinates(data_path)

    print(cities)  # Assuming you want to print this based on your original script
    model = solve_TSP_MTZ_problem(G, dem_points, depot, k)
    # Assuming model is the returned Gurobi model from solve_TSP_MTZ_problem
    x_vars = model.getVars()
    x = {e: x_var for e, x_var in zip(G.edges, x_vars)}

    visualize_graph(G,depot,nx,x,my_pos)  # If graph visualization is needed


if __name__ == "__main__":
    main()
