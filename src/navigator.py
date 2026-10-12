"""
Route Finding & Shortest Route

Implement the logic to find the shortest path from a source to a destination.
You can use Dijkstra's Algorithm or Breadth-First Search (BFS) for this.

Example input:
    routes = ROUTES (from routes.py)
    source = "Main Gate"
    destination = "Library"

Example output:
    (["Main Gate", "CSE Block", "Library"], 200)  # (route_list, total_distance)
"""
import heapq

def find_shortest_route(routes, source, destination):
    """
    Find the shortest route from source to destination.

    Return:
        tuple: (route_list, total_distance)
        If no route exists, return ([], 0).
    """
    # TODO: Implement the navigation logic to find the shortest route
    

    import heapq


def find_shortest_route(routes, source, destination):
    if source not in routes or destination not in routes:
        return ([], 0)

    pq = [(0, source, [source])]
    distances = {source: 0}

    while pq:
        distance, current, path = heapq.heappop(pq)

        if current == destination:
            return (path, distance)

        if distance > distances.get(current, float('inf')):
            continue

        for neighbor, weight in routes[current].items():
            new_distance = distance + weight

            if new_distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_distance
                new_path = path + [neighbor]

                heapq.heappush(
                    pq,
                    (new_distance, neighbor, new_path)
                )

    return ([], 0)