''' 
Lab 2: Cities and Routes

In the final project, you will need a bunch of cities spread across a map. Here you 
will generate a bunch of cities and all possible routes between them.
'''
import random
import itertools
import math
import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))
from lab14.lab14 import global_journal

def get_randomly_spread_cities(size, n_cities):
    """
    > This function takes in the size of the map and the number of cities to be generated 
    and returns a list of cities with their x and y coordinates. The cities are randomly spread
    across the map.
    
    :param size: the size of the map as a tuple of 2 integers
    :param n_cities: The number of cities to generate
    :return: A list of tuples, each representing a city, with random x and y coordinates.
    """
    # Consider the condition where x size and y size are different
    global_journal.log("Starting to spread cities")
    global_journal.log("Finished spreading cities")
    #return [(random.randint(0, size[0]-1), random.randint(0, size[1]-1)) for _ in range(n_cities)]
    cities = []
    min_distance = 20
    while len(cities) < n_cities:
        new_city = (random.randint(0, size[0]-1), random.randint(0, size[1]-1))
        if all(math.hypot(new_city[0]-existing[0], new_city[1]-existing[1]) >= min_distance for existing in cities):
            cities.append(new_city)
    return cities
    

def get_routes(city_names):
    """
    It takes a list of cities and returns a list of all possible routes between those cities. 
    Equivalently, all possible routes is just all the possible pairs of the cities. 
    
    :param cities: a list of city names
    :return: A list of tuples representing all possible links between cities/ pairs of cities, 
            each item in the list (a link) represents a route between two cities.
    """
    global_journal.log("Calculating routes")
    global_journal.log("Routes calculated")
    return list(itertools.combinations(city_names, 2))



# TODO: Fix variable names
if __name__ == '__main__':
    city_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    '''print the cities and routes'''
    cities = get_randomly_spread_cities((100, 200), len(city_names))
    routes = get_routes(city_names)
    print('Cities:')
    for i, city in enumerate(cities):
        print(f'{city_names[i]}: {city}')
    print('Routes:')
    for i, route in enumerate(routes):
        print(f'{i}: {route[0]} to {route[1]}')
