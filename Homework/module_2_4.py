numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers :
    is_prime = True
    for i in range(2, number):
        if number % i ==0:
            is_prime = False
            break
    if is_prime and number != 1:
        primes.append (number)
    else :
        not_primes.append (number)
print('prime numbers:',primes)
print('not prime numbers:', not_primes)



