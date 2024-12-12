#!/usr/bin/python3
"""Module defining isWinner function."""


def is_prime(n):
    """Returns True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    """
    Efficiently generate primes up to n using Sieve of Eratosthenes
    """
    # Create a boolean array "is_prime[0..n]" and initialize 
    # all entries it as true. A value in is_prime[i] will 
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i starting from i*i
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    
    # Collect all prime numbers
    return [i for i in range(2, n+1) if is_prime[i]]


def isWinner(x, nums):
    """Function to get who has won in prime game"""
    if not nums or x <= 0:
        return None

    mariaWinsCount = 0
    benWinsCount = 0

    for n in nums:
        # Skip rounds where no game can be played
        if n < 2:
            benWinsCount += 1
            continue

        # Precompute primes up to n
        primes = sieve_of_eratosthenes(n)
        
        # Simulate the game
        currentSet = set(range(1, n + 1))
        currentPlayer = 0  # 0 for Maria, 1 for Ben

        # Continue while primes are available in the current set
        while True:
            # Find valid primes in the current set
            validPrimes = [p for p in primes if p in currentSet]
            
            # If no primes available, current player loses
            if not validPrimes:
                break
            
            # Choose smallest valid prime
            prime = min(validPrimes)
            
            # Remove prime and its multiples
            currentSet = {x for x in currentSet if x % prime != 0}
            primes.remove(prime)
            
            # Switch players
            currentPlayer = 1 - currentPlayer

        # If no valid moves left and it was Maria's turn, Ben wins
        if currentPlayer == 0:
            benWinsCount += 1
        else:
            mariaWinsCount += 1

    # Determine overall winner
    if mariaWinsCount > benWinsCount:
        return "Maria"
    elif benWinsCount > mariaWinsCount:
        return "Ben"
    
    return None
