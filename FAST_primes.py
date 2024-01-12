# Write code to check if the numbers provided in the list check_prime are prime numbers.
# For each number, if the number is prime, the code should print that the number is a prime number.
# If the number is NOT a prime number, it should print that the number is not a prime number,
# and also print a factor of that number besides 1 and the number itself.

# The program in our course checked all factors up to the number itself.
# I see no use in checking over half of the number if 2 is not its factor, etc.
# So I decided to make a faster version with shrinking range.

# For the course program:
# Execution time: 0.0150424000 seconds

# check_prime = [21897013937080798977, 1857927482005638293, 53184369225338942887, 95396205509102818005, 72499347817809840533, 47475329596724670037, 37125508206880601923, 18688789375325057457, 52993902931591669613, 29390415841456367117, 59393690896147384183, 7115161165028304969, 74155373360896243963, 14113748079895258565, 58749498340182396299, 93667547285960574321, 30619825076230330717, 55878702370200137451, 89626910283089621291, 7112645674883940841, 88383077277026938101, 53997202001645952773, 20946528156140156749, 42204975834661733435, 72751209676550349243, 887469239118740869, 40234965508240375099, 92284751600745753779, 94710307072713334929, 30711114475284340421]
check_prime = [46009, 19933, 95465, 26297, 50957, 25571, 71815, 4157, 37193, 35123,
               35599, 89183, 20143, 57253, 2257, 15047, 96395, 95129, 27245, 7721]


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


