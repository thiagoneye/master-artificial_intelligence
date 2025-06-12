# Imports

import pandas as pd
import numpy as np

# Auxiliary Functions

def expand_routes(df: pd.DataFrame) -> dict:
    """
    Expands the routes in the dataframe por inverted routes.
    """
    inverted = df.rename(columns={"Origem": "Destino", "Destino": "Origem"})
    df = pd.concat([df, inverted], ignore_index=True).sort_values(by=["Origem", "Destino"], ignore_index=True)

    nested_dict = {}
    for _, row in df.iterrows():
        row = row.to_list()
        key1 = row[0]
        key2 = row[1]
        value = row[2]

        if key1 not in nested_dict.keys():
            nested_dict[key1] = {}
        nested_dict[key1][key2] = value
    return nested_dict

def is_isolated_station(lines: dict, station: str) -> bool:
    """
    Check if a station is isolated in the subway network.
    """
    return len(lines[station]) == 1

def objective_function(distances: dict, lines: dict, station1: str, station2: str, destination: str, atual_line: str,
                       switching_time: int, mean_velocity: int, print_the_execution=bool) -> float:
    """
    Objective function to be minimized, i.e., the travel time to between two stations.
    """
    distance_between_stations = distances[station1][station2]
    
    if station2 == destination:
        distance_to_destination = 0
    else:
        distance_to_destination = distances[station2][destination]

    distance = distance_between_stations + distance_to_destination
    theoretical_time = distance / mean_velocity * 60
    if atual_line != "" and atual_line != lines[station1][station2]:
        theoretical_time += switching_time
    
    if print_the_execution:
        print(f"Distance between {station1} and {station2}: {distance_between_stations}")
        print(f"Distance between {station2} and {destination}: {distance_to_destination}")
        print(f"Atual line: {atual_line}")
        print(f"Next line: {lines[station1][station2]}")
    
    return theoretical_time

def greedy_algorithm(distances: dict, lines: dict, origin: str, destination: str, switching_time: int,
                     mean_velocity: int, print_the_execution=False, stopping_criterion=10) -> list:
    """
    Greedy algorithm to find the best route between two stations.
    """
    route = [origin]
    total_time = 0

    loop_counter = 0
    station1 = origin
    atual_line = ""
    while station1 != destination and loop_counter < stopping_criterion:
        loop_counter += 1
        if print_the_execution:
            print(f"\nCurrent station: {station1}")
            print(f"Possible stations: {list(lines[station1].keys())}")
        best_time = float("inf")
        best_station = ""

        for station2 in lines[station1].keys():
            if print_the_execution:
                print("---------------------------")
                print(f"Verification of station {station2}")
            if not(is_isolated_station(lines, station2)) or station2 == destination:
                time = objective_function(distances, lines, station1, station2, destination, atual_line, switching_time, mean_velocity, print_the_execution)
                if time < best_time:
                    best_time = time
                    best_station = station2
                if print_the_execution:
                    print(f"Time: {time}")
            if print_the_execution:
                print(f"Best station: {best_station}")
                print(f"Best time: {best_time}")
            
        atual_line = lines[station1][best_station]
        total_time += best_time
        station1 = best_station
        route.append(best_station)
        if print_the_execution:
            print("------")
            print(f"Route: {route}")
            print(f"Total time: {total_time} minutes")
    if loop_counter == stopping_criterion:
        print("Stopping criterion reached.")
    return route, total_time

# Execution

if __name__ == "__main__":
    # Inputs
    switching_time = 4 # minutes
    mean_velocity = 30 # km/h
    origin = "E01"
    destination = "E12"

    # Data Reading
    distances = pd.read_excel("ShortestPathProblem/data/subway_distances.xlsx")
    lines = pd.read_excel("ShortestPathProblem/data/subway_lines.xlsx")

    # Data Processing
    distances = expand_routes(distances)
    lines = expand_routes(lines)

    # Heuristic Algorithm
    station1 = origin
    route, total_time = greedy_algorithm(distances, lines, origin, destination, switching_time, mean_velocity, print_the_execution=True)
