# Write code to check if the numbers provided in the list check_prime are prime numbers.
# For each number, if the number is prime, the code should print that the number is a prime number.
# If the number is NOT a prime number, it should print that the number is not a prime number,
# and also print a factor of that number besides 1 and the number itself.

# The program in our course checked all factors up to the number itself.
# I see no use in checking over half of the number if 2 is not its factor, etc.
# So I decided to make a faster version with shrinking range.

# Execution time: 1.6751163000 seconds for the course code
# Execution time: 0.7943204000 seconds for my code!

import time

start_time = time.perf_counter()

check_prime = [5966059, 7877029, 7619753, 7363543, 1218595, 2335943, 5415757,
               2923415, 5916413, 3658333, 5955901, 4138519, 9559667, 2622037,
               5495485, 4676833, 5475325, 7537859, 1265617, 3204703]


for num in check_prime:
    if num == 2:
        print('{} IS a prime number'.format(num))
        continue

    checked_num = 2
    max_reasonable_check = int(num / checked_num)
    for i in range(checked_num, max_reasonable_check + 1):
        if num % i == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, num, i))
            break
        if i == max_reasonable_check - 1:
            print('{} IS a prime number'.format(num))
    else:
        checked_num = i


end_time = time.perf_counter()
execution_time = end_time - start_time


print(f"Execution time: {execution_time:.10f} seconds")