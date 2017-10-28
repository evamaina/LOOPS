"""Define a function called is_prime that takes a number x as input.

For each number n from 2 to x - 1, test if x is evenly divisible by n.

If it is, return False.

If none of them are, then return True.Remember: all numbers less than 2 are not prime numbers!"""

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True