## Dictionaries
- Set of key-value pairs <br>
```{ key : value }```

### Multiple entries in a dictionary
```
{
    "Bug" : "An error in a program",
    "Function" : "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something again and again",
}
```
- Above is a dictionary with proper indentation

### Accessing items in a dictionary
- programming_dictionary["Bug"]
- If we put in a key that doesnt exist, we get key error
- Be vary of data types

### Adding new items to a dictionary
- dictionaryVariable[key]=value
- for ex:-
```
programming_dictionary["Conditionals"] = "If-else are called conditionals as we can use multiple conditions through them"
```

### Creating an empty dictionary
- ```empty_dictionary={}```

### Wiping an existing dictionary
- ```programming_dictionary={}```

### Editing an item in a dictionary
- ```programming_dictionary["Bug"]= "Some new value"```

### Loop through a dictionary
```
for thing in programming_dictionary:
    print(thing)
```
- Above code prints all the keys only from the dictionary
<br>
```
for thing in programming_dictionary:
    print(programming_dictionary[thing])
```
- Above prints all the values from the dictionary

## Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

### Nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Little", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

### Nesting a dictionary in a dictionary

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


### Nesting dictionaries inside a list
```
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
```

