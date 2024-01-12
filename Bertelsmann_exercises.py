# Write code to check if the numbers provided in the list check_prime are prime numbers.
# For each number, if the number is prime, the code should print that the number is a prime number.
# If the number is NOT a prime number, it should print that the number is not a prime number,
# and also print a factor of that number besides 1 and the number itself.

import time

start_time = time.perf_counter()

check_prime = [5966059, 7877029, 7619753, 7363543, 1218595, 2335943, 5415757,
               2923415, 5916413, 3658333, 5955901, 4138519, 9559667, 2622037,
               5495485, 4676833, 5475325, 7537859, 1265617, 3204703]


for num in check_prime:
    if num == 2:
        print('{} is prime'.format(num))
        continue
    for i in range(2, num):
        if num % i == 0:
            print("{} not prime, is a factor of {}".format(num, i))
            break
        if i == num - 1:
            print('{} is prime'.format(num))


end_time = time.perf_counter()
execution_time = end_time - start_time


print(f"Execution time: {execution_time:.10f} seconds")
