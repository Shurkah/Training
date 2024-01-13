cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
# write your for loop here

for i, actor in enumerate(cast):
    cast[i] = actor + ' ' + str(heights[i])
print(cast)