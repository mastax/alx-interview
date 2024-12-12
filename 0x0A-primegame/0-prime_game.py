#!/usr/bin/python3
"""Module defining isWinner function for Prime Game."""

def is_prime(n):
    """
    Check if a number is prime
    Args:
        n (int): Number to check for primality.
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sieve_of_eratosthenes(n):
    """
    Generate prime numbers up to n using Sieve of Eratosthenes.
    Args:
        n (int): Upper limit for prime number generation.
    Returns:
        list: List of prime numbers up to n.
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.
    Args:
        x (int): Number of rounds to play.
        nums (list): List of integers representing n for each round.
    Returns:
        str or None: Name of the winner, or None if no clear winner.
    """
    if not nums or x <= 0:
        return None

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        # Skip rounds where no game can be played
        if n < 2:
            ben_wins += 1
            continue

        # Precompute primes up to n
        primes = sieve_of_eratosthenes(n)

        # Simulate the game
        current_set = set(range(1, n + 1))
        current_player = 0  # 0 for Maria, 1 for Ben

        # Continue while primes are available in the current set
        while True:
            # Find valid primes in the current set
            valid_primes = [p for p in primes if p in current_set]

            # If no primes available, current player loses
            if not valid_primes:
                break

            # Choose smallest valid prime
            prime = min(valid_primes)

            # Remove prime and its multiples
            current_set = {x for x in current_set if x % prime != 0}
            primes.remove(prime)

            # Switch players
            current_player = 1 - current_player

        # If no valid moves left and it was Maria's turn, Ben wins
        if current_player == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"

    return None
