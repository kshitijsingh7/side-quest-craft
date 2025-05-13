# Prime Number Finder using Dijkstra's Algorithm
This code implements an efficient prime number finding algorithm inspired by Edsger Dijkstra's approach. Instead of using a traditional Sieve of Eratosthenes, this algorithm employs a dynamic programming method that maintains a list of (prime, next composite) pairs to determine the primality of numbers up to a given maximum value.

# Description
The algorithm dynamically updates a list of tuples, called pool, where each tuple contains a prime number and its next multiple. As each number is evaluated:

* If the number is smaller than all next multiples in the pool, it is considered prime.
* If it is not, the pool is updated to reflect the next multiples.

This method is memory efficient as it avoids the need for a large array to mark multiples.