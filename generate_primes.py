import numpy as np
import numba
import argparse

@numba.jit()
def check_prime(n, primes=[2,3]) -> bool:
    """Checks if a number n is prime"""
    if n in (2, 3):
        return True
    for p in primes:
        if p >= np.sqrt(n) + 1:
            break
        if n % p == 0:
            return False
        p += 2
        while p < np.sqrt(n) + 1:
            if n % p == 0:
                return False
            p += 2
    return True


def generate_primes(N, primes=[2,3]) -> np.array:
    """Generates primes below N"""
    if primes[-1] >= N:
        return primes
    i = len(primes)
    primes = np.array(list(primes) + [0] * (N - primes[-1]))
    for n in range(primes[i-1] + 2, N+1, 2):
        if check_prime(n, primes[:i]):
            primes[i] = n
            i += 1
    return primes[:i]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('N', type=int, help='The order of the group')
    args = parser.parse_args()

    try:
        with open('primes.npy', 'rb') as f:
            start_primes = np.load(f)
    except FileNotFoundError:
        start_primes = [2, 3]

    found_primes = generate_primes(args.N, start_primes)
    with open('primes.npy', 'wb') as f:
        np.save(f, found_primes)



