# In this exercise you need to list all the possible routes that start from Panama
# and visit each of the other ports exactly once.

# The template code below contains an incomplete permutations function
# which takes as input a specified route and a list of port names absent from that route.
# Modify the function so that it prints out all the possible orderings of the ports that always begin with Panama (PAN).

# The mathematical term for such orderings is a permutation.
# Note that your program should work for an input portnames list of any length.
# The order in which the permutations are printed doesn't matter.

# As the output the function should print each permutation on its own row,
# as one string, with the port names separated by spaces.


portnames = ["PAN", "AMS", "CAS", "NYC", "HEL", "RIO"]


def permutations(route, ports):
    # If there are no more ports to visit, print the route
    if not ports:
        print(' '.join([portnames[i] for i in route]))
    else:
        # For each unvisited port, add it to the route and recurse
        for i in ports:
            permutations(route + [i], [j for j in ports if j != i])


# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))