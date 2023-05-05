import numpy as np
import numba
import argparse
with open('primes.npy', 'rb') as f:
    primes = np.load(f)


@numba.njit()
def factorise(n, primes=primes) -> tuple:
    """Returns the prime factorisation of n"""
    if n >= primes[-1]:
        print(f'Cannot factor {n} larger than {primes[-1]} please run '
              f'python generate_primes.py {n} and try again.')
        raise
    factors, powers = [], []
    for p in primes:
        if n % p == 0:
            factors.append(p)
            n = n // p
            k = 1
            while n % p == 0:
                k += 1
                n = n // p
            powers.append(k)
    return np.array(factors), np.array(powers)


@numba.njit()
def one_sylow(p, e) -> bool:
    """
    Returns true if there is can only be 1 sylow-p-subgroup
    based on a simple condition. Note this does not take
    into account special cases.
    """
    if e < p:
        return True
    k = 1
    while 1 + k*p <= e:
        if e % (1 + k * p) == 0:
            return False
        k += 1
    return True


@numba.njit()
def exclude_factorisation(factorisation) -> bool:
    """
    Returns True if given the prime factorisation of some number
    there is a prime where number of sylow-p-subgroups must be one
    based on the simple algorithm in 'one_sylow'
    """
    factors, powers = factorisation
    if len(factors) == 1:
        return True
    for i in range(len(factors)):
        p = factors[i]
        e = np.prod(np.delete(factors, i) ** np.delete(powers, i))
        if one_sylow(p, e):
            return True
    return False


def exclude_order(order: int) -> bool:
    factorisation = factorise(order)
    return exclude_factorisation(factorisation)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('order', type=int, help='The order of the group')
    args = parser.parse_args()
    print(exclude_order(args.order))