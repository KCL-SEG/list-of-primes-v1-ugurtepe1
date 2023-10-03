"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    number = 1
    while len(list) < number_of_primes:
        if(isPrime(number)):
            list.append(number)
        number += 1
    return list

def isPrime(number):
    if (number == 1 or number == 0):
        return False
    if (number == 2):
        return True
    for i in range(2,number):
        if(number % i == 0):
            return False
    return True


print(primes(12))