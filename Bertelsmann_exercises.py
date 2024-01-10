# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1

while current <= number:
    product *= current
    current += 1

print(product)


# number to find the factorial of
number = 6
# start with our product equal to one
product = 1

for i in range(1, number + 1):
    product *= i

print(product)