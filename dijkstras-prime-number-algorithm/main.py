def find_primes(max_n):
    # Initialize the pool with the first prime (2) and its next composite (4)
    pool = [(2, 4)]
    # Initialize the list of primes with the first prime number (2)
    primes = [2]

    # Iterate over each number k from 3 to max_n
    for k in range(3, max_n):
        # If k is less than the smallest factor in the pool, it's prime
        if k < pool[0][1]:
            # Add k to the list of primes
            primes.append(k)
            # If k squared is less than max_n, add (k, k^2) to the pool
            if k * k <= max_n:
                pool.append((k, k * k))
        else:
            # Update the pool: for each (prime, factor) pair, if the factor is <= k, increment it
            for idx in range(len(pool)):
                prime, factor = pool[idx]
                # If the factor is greater than k, stop updating as the list is sorted
                if factor > k:
                    break
                # Update the factor to the next multiple of prime
                pool[idx] = (prime, factor + prime)
            # Sort the pool by the second element (factor) to maintain order
            pool.sort(key=lambda x: x[1])

    return primes


if __name__ == "__main__":
    all_primes = find_primes(20)
    print(all_primes)
