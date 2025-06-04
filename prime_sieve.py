"""Prime sieve implementation capable of generating primes up to 1 billion.

This module provides a segmented sieve algorithm which can be used to
iterate over prime numbers up to a specified limit. The segmented
approach avoids allocating a huge contiguous array, keeping memory
usage reasonable even for very large limits such as one billion.
"""

from math import isqrt


def simple_sieve(limit):
    """Return list of primes up to ``limit`` using a simple sieve."""
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"  # 0 and 1 are not prime
    for num in range(2, isqrt(limit) + 1):
        if sieve[num]:
            step = num
            start = num * num
            sieve[start: limit + 1: step] = b"\x00" * ((limit - start) // step + 1)
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def segmented_sieve(limit, segment_size=32768):
    """Yield primes up to ``limit`` using a segmented sieve."""
    if limit < 2:
        return
    base_primes = simple_sieve(isqrt(limit))
    yield from base_primes

    low = isqrt(limit) + 1
    high = low + segment_size - 1
    while low <= limit:
        if high > limit:
            high = limit
        size = high - low + 1
        sieve = bytearray(b"\x01") * size
        for p in base_primes:
            start = ((low + p - 1) // p) * p
            for multiple in range(start, high + 1, p):
                sieve[multiple - low] = 0
        for i in range(size):
            if sieve[i]:
                yield low + i
        low = high + 1
        high = low + segment_size - 1


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate primes up to a limit using a segmented sieve.")
    parser.add_argument("limit", type=int, nargs="?", default=10**9,
                        help="generate primes up to this limit (default: 1e9)")
    parser.add_argument("--count", action="store_true", help="only count primes instead of listing them")
    args = parser.parse_args()

    count = 0
    for prime in segmented_sieve(args.limit):
        if args.count:
            count += 1
        else:
            print(prime)
    if args.count:
        print(count)
