# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Little", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a dictionary in a dictionary

travel_dict = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10,
    }
}


# Nesting dictionaries inside a list
travel_list = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {"country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10,
    },
]
