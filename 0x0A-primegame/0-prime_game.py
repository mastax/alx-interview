#!/usr/bin/python3
"""Module defining isWinner function."""


def isWinner(x, nums):
    """Function to get who has won in prime game"""
    mariaWinsCount = 0
    benWinsCount = 0

    for n in nums:
        # Create set of numbers for the round
        roundSet = set(range(1, n + 1))
        
        # Get list of primes
        primes = [p for p in range(2, n + 1) if is_prime(p)]
        
        # Track whose turn it is
        playerTurn = 0  # 0 for Maria, 1 for Ben
        
        while primes:
            # Find the smallest prime in the current set
            valid_primes = [p for p in primes if p in roundSet]
            
            if not valid_primes:
                break
            
            # Choose the smallest prime
            prime = min(valid_primes)
            
            # Remove the prime and its multiples
            roundSet = {x for x in roundSet if x % prime != 0}
            
            # Remove the prime from available primes
            primes.remove(prime)
            
            # Switch turns
            playerTurn = 1 - playerTurn
        
        # If no primes left and it was Maria's turn, Ben wins
        if playerTurn == 0:
            benWinsCount += 1
        else:
            mariaWinsCount += 1

    # Determine overall winner
    if mariaWinsCount > benWinsCount:
        return "Maria"
    elif benWinsCount > mariaWinsCount:
        return "Ben"
    
    return None


def is_prime(n):
    """Returns True if n is prime, else False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
