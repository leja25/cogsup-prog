"""
Write a script that lists all the prime numbers between 1 and 10000.
(A prime number is an integer greater or equal to 2 which has no divisors except 1 and itself). 
Hint: Write an is_factor helper function.
"""

def is_factor(d, n):
    """True iff (if and only if) d is a divisor of n."""
    if n%d == 0:
        return True
    else:
        return False
    pass

def is_prime(n):

    if n < 2:
        return False

    for i in range(n):
        if is_factor(i+1, n) == True:
            if i+1 != 1 and i+1 != n:
                return False
            
    return True

list_of_primes = [x for x in range(10001) if is_prime(x) == True]

print(list_of_primes)

#Alternative:
#def is_prime(n):
#
#    if n < 2:
#        return False
#    divisors = []
#    for i in range(n):
#        if is_factor(i+1, n) == True:
#            divisors.append(i+1)
#    if divisors == [1, n]:
#        return True
#    else:
#        return False
