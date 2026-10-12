"""
Campus Connections (Routes)

Represent the connections between different locations and the distance between them.
Use a dictionary where the keys are locations, and the values are also dictionaries 
representing connected locations and the distance in meters.

Make sure the graph is bidirectional:
if Main Gate connects to CSE Block, CSE Block must also connect to Main Gate with the same distance.

Example format:
ROUTES = {
    "Main Gate": {
        "CSE Block": 120,
        "Canteen": 180,
    },
    "CSE Block": {
        "Main Gate": 120,
        "Library": 80,
        # Add more connections...
    },
    # Add more locations...
}
"""

# TODO: Define the full ROUTES dictionary following the example above
ROUTES = {
    
    "Main Gate": {
        "Administrative Block": 150,
        "Canteen": 180,
        "Parking Area": 100
    },

    "Library": {
        "Computer Science Department": 80,
        "Administrative Block": 120
    },

    "Administrative Block": {
        "Main Gate": 150,
        "Library": 120,
        "Computer Science Department": 100
    },

    "Canteen": {
        "Main Gate": 180,
        "Hostel": 200
    },

    "Computer Science Department": {
        "Library": 80,
        "Administrative Block": 100,
        "Auditorium": 140
    },

    "Hostel": {
        "Canteen": 200,
        "Auditorium": 160
    },

    "Auditorium": {
        "Computer Science Department": 140,
        "Hostel": 160
    },

    "Parking Area": {
        "Main Gate": 100
    }
}


