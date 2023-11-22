""" Contains the core logic of your model.
This file  include functions or classes that define your model's behavior, calculations, data processing, etc. """
# model.py
import networkx as nx
import gurobipy as gp
from gurobipy import GRB
import math

# Function to create and initialize the graph


def create_graph(data_subset, num_data_points):
    n = len(data_subset) - 1
    # directed graph with a vertex for each city
    G = nx.complete_graph(num_data_points, nx.DiGraph())
    # Add any additional logic for graph initialization
    return G

# Function to parse coordinates (if this is a separate logic in your code)


def parse_coordinates(data_path):
    with open(data_path, 'r') as file:
        lines = file.readlines()
        coord_section = False
        cities = []
        for line in lines:
            if "EOF" in line:
                break
            if coord_section:
                city_info = line.split()
                cities.append((float(city_info[0]), float(
                    city_info[1]), float(city_info[2])))
            if "NODE_COORD_SECTION" in line:
                coord_section = True
    return cities


def eucl_dist(x1, y1, x2, y2):
    return round(math.sqrt((x1-x2)**2 + (y1-y2)**2))


def solve_TSP_MTZ_problem(G, dem_points, depot, k):
    """
    Solves an optimization problem given a graph, demand points, a depot, and the number of vehicles.

    Parameters:
    G (networkx.Graph): The graph representing the problem.
    dem_points (list): List of demand points.
    depot (int): The index of the depot node.
    k (int): Number of vehicles.
    Returns:
    Gurobi Model: The solved model.
    """

    m = gp.Model()
    x = m.addVars(G.edges, vtype=GRB.BINARY)

    # Set the objective function
    m.setObjective(gp.quicksum(
        G.edges[i, j]['length'] * x[i, j] for i, j in G.edges), GRB.MINIMIZE)

    # Enter each demand point once
    m.addConstrs(gp.quicksum(x[i, j]
                 for i in G.predecessors(j)) == 1 for j in dem_points)

    # Leave each demand point once
    m.addConstrs(gp.quicksum(x[i, j]
                 for j in G.successors(i)) == 1 for i in dem_points)

    # Leave the depot k times
    m.addConstr(gp.quicksum(x[depot, j] for j in G.successors(depot)) == k)

    # Add the MTZ variable
    u = m.addVars(G.nodes)
    c = m.addConstrs(u[i] - u[j] + len(G.nodes) * x[i, j] <=
                     len(G.nodes) - 1 for i, j in G.edges if j != depot)

    # Configure the model to find multiple solutions
    m.setParam(GRB.Param.PoolSolutions, 10)  # Store the 10 best solutions
    # Search for more than one optimal solution
    m.setParam(GRB.Param.PoolSearchMode, 2)
    # Set the time limit (in seconds)
    time_limit = 60  # for example, 60 seconds
    m.setParam(GRB.Param.TimeLimit, time_limit)
    m.optimize()
    return m


def get_optimization_results(model):
    """
    Extracts key information from a Gurobi optimization model.
    """
    results = {
        'Optimal Value': None,
        'Number of Iterations': None,
        'Runtime (seconds)': None,
        'Status': None
    }

    if model.status == GRB.OPTIMAL:
        results['Optimal Value'] = model.ObjVal
        results['Number of Iterations'] = model.IterCount
        results['Runtime (seconds)'] = model.Runtime
        results['MIP Gap'] = model.MIPGap if model.IsMIP else 'N/A'  # Set MIP Gap
        results['Status'] = 'Optimal'
    elif model.status == GRB.TIME_LIMIT:
        results['Optimal Value'] = model.ObjVal
        results['Number of Iterations'] = model.IterCount
        results['Runtime (seconds)'] = model.Runtime
        results['MIP Gap'] = model.MIPGap if model.IsMIP else 'N/A'  # Set MIP Gap

        results['Status'] = 'Passed the time limit.'
        # You can still extract and return the best found solution here, if needed
    else:
        results['Status'] = 'Not Optimal'

    return results


def get_dimension_from_tsp(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("DIMENSION"):
                # Extract the dimension value
                _, dimension = line.split(':')
                return int(dimension.strip())

    return None
