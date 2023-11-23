""" This file use functions or classes from both model.py and output_manager.py.
It acts as the orchestrator, calling the necessary functions from each module and passing data between them. """
# main.py
import networkx as nx
import os
import pandas as pd
from model import create_graph, parse_coordinates, eucl_dist, solve_TSP_MTZ_problem, get_optimization_results, get_dimension_from_tsp
from output_manager import visualize_graph


def main():

    # Load the list of dataset
    dataset_paths = [#TSPLIB DataSet
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/eil51.tsp',
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/eil76.tsp',
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/eil101.tsp',
                     
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/ch130.tsp',                     
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/ch150.tsp',
                     
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/a280.tsp'

                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/d198.tsp',
                     
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/kroA100.tsp',
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/kroA150.tsp',
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/kroB100.tsp',
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/kroC100.tsp',
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/kroE100.tsp',    
                                      
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/fl417.tsp',
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/dsj1000.tsp',
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/brd14051.tsp',
                     
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/d198.tsp',
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/d493.tsp',
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/d657.tsp',
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/d1291.tsp',
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/d1655.tsp',
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/d2103.tsp',
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/d15112.tsp',
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/TSPLIB/ALL_tsp/d18512.tsp',
                     
                     #Solomon DataSet
                      '/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/R1/R101.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/R1/R102.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/R1/R103.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/R1/R104.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/R1/R105.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/R1/R106.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/R1/R107.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/R1/R108.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/R1/R109.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/R1/R110.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/R1/R111.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/R1/R112.CSV'
                     
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/C1/C101.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/C1/C102.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/C1/C103.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/C1/C104.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/C1/C105.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/C1/C106.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/C1/C107.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/C1/C108.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/C1/C109.CSV'
                     
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/RC1/RC101.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/RC1/RC102.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/RC1/RC103.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/RC1/RC104.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/RC1/RC105.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/RC1/RC106.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/RC1/RC107.CSV'
                     #'/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/Datasets/Solomon/solomon_dataset/RC1/RC108.CSV'
                     ]
    for data_path in dataset_paths:
        
        dataset_name_with_extension = os.path.basename(data_path)
        data = pd.read_csv(data_path)
        
        # Number of data points you want to use (including depot)
        num_data_points = get_dimension_from_tsp(data_path)  # Adjust this value as needed
        
        # Extract a subset based on the desired number of data points
        data_subset = data.head(num_data_points)
        n = len(data_subset)-1
        Q = 200
        k = 1                       # number of vehicles
        depot = 0
        dem_points = list(range(1, n+1))  # nodes 1, 2, ..., 20
        G = create_graph(data_subset, num_data_points)
        cities = parse_coordinates(data_path)
        my_pos = {point[0]-1: (point[1], point[2])
                  for point in cities}  # pos[i] = (x_i, y_i)«
        for i, j in G.edges:
            (x1, y1) = my_pos[i]
            (x2, y2) = my_pos[j]
            G.edges[i, j]['length'] = eucl_dist(x1, y1, x2, y2)
        cities = parse_coordinates(data_path)
        # Assuming you want to print this based on your original script
        print(cities)
        model = solve_TSP_MTZ_problem(G, dem_points, depot, k)
        
        # Assuming model is the returned Gurobi model from solve_TSP_MTZ_problem
        x_vars = model.getVars()
        x = {e: x_var for e, x_var in zip(G.edges, x_vars)}
        results = get_optimization_results(model)
        output_file_path = f"/home/centor.ulaval.ca/ghafomoh/Downloads/ADM-7900/{dataset_name_with_extension}.png"
        # If graph visualization is needed
        visualize_graph(G, depot, nx, x, my_pos, results,
                        dataset_name_with_extension, output_file_path)


if __name__ == "__main__":
    main()
