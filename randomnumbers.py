import random

least = []
while len(least) < 20:
    a = random.randint(10 ** 2, 10 ** 7)
    if a % 2 != 0 and a % 3 != 0:
        least.append(a)

print(least)