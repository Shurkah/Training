primes = []
for i in range(1, 251):
    isPrime = True
    for div in range(2, int(i//2)):
        if i % div == 0:
            isPrime = False
            break
    if isPrime:
            primes.append(i)

print(primes)

with open('primes_results.txt', 'w') as results:
    results.write(str(primes))