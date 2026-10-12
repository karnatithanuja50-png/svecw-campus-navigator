"""
Main Application & Input Validation

Tie all modules together to run the campus navigator:
1. Get the list of locations and print them.
2. Ask the user for a source and destination.
3. Validate user input (e.g. check if locations exist, source is not destination).
4. Call find_shortest_route() from navigator.
5. Call display_route() to show the result.
"""

from locations import get_locations
from routes import ROUTES
from navigator import find_shortest_route
from display import display_route


def main():
    print("========================================")
    print("       SVECW CAMPUS NAVIGATOR")
    print("========================================")

    # TODO: 1. Get locations from get_locations()
    
    # TODO: 2. Print available locations
    
    # TODO: 3. Ask the user for 'source' and 'destination'
    
    # TODO: 4. Add Input Validation 
    # (e.g., handle invalid location, source == destination)

    # TODO: 5. Call find_shortest_route(ROUTES, source, destination)
    
    # TODO: 6. Call display_route(route, distance)
    # 1. Get locations
    locations = get_locations()

# 2. Print available locations
    print("\nAvailable Campus Locations:")
    for location in locations:
        print("-", location)

# 3. Ask the user for source and destination
    source = input("\nEnter starting location: ").strip()
    destination = input("Enter destination: ").strip()

# 4. Validate input
    if not source or not destination:
        print("Error: Location names cannot be empty.")
        return 

    if source not in locations:
        print(f"Error: '{source}' is not a valid location.")
        return

    if destination not in locations:
        print(f"Error: '{destination}' is not a valid location.")
        return

    if source == destination:
        display_route([source], 0)
        return

# 5. Find the shortest route
    route, distance = find_shortest_route(ROUTES, source, destination)

# 6. Display the result
    display_route(route, distance)

if __name__ == "__main__":
    main()


