# Rewrite this code to be more concise by replacing the is_short function with a lambda expression
# defined within the call to filter().

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

#def is_short(name):
#    return len(name) < 10
#short_cities = list(filter(is_short, cities))

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)