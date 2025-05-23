#!/usr/bin/python3
"""
Prime Game
"""

def sieve_primes(n):
    """Return a list where index i is True if i is prime."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve

def isWinner(x, nums):
    """
    Determines the winner of each round of Prime Game.
    Returns name of player with most wins or None if tie.
    """
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    prime_flags = sieve_primes(max_num)

    # Count primes up to each number using prefix sums
    prime_counts = [0] * (max_num + 1)
    count = 0
    for i in range(1, max_num + 1):
        if prime_flags[i]:
            count += 1
        prime_counts[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
