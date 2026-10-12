"""
Output & Display Formatting

Neatly display the chosen route and the total distance to the user in the terminal.

Example output:
    Shortest route:
    Main Gate -> CSE Block -> Library

    Total distance: 200 m
"""


def display_route(route, distance):
    """
    Display the route and distance in a user-friendly format.

    Args:
        route (list): List of location names in order.
        distance (int/float): The total distance of the route.
    """
    # TODO: Implement the logic to format and print the route and distance
    
    if not route:
        print("No route found.")
        return

    print("Shortest route:")
    print(" -> ".join(route))
    print()
    print(f"Total distance: {distance} m")


