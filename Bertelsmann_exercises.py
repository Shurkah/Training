# Write code to check if the numbers provided in the list check_prime are prime numbers.
# For each number, if the number is prime, the code should print that the number is a prime number.
# If the number is NOT a prime number, it should print that the number is not a prime number,
# and also print a factor of that number besides 1 and the number itself.

check_prime = [26, 39, 51, 53, 57, 79, 85]

for num in check_prime:
    if num == 2:
        print('{} IS a prime number'.format(num))
        continue
    for i in range(2, num):
        if num % i == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, num, i))
            break
        if i == num - 1:
            print('{} IS a prime number'.format(num))

