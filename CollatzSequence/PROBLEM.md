# Longest Collatz Sequence

The iterative sequence is defined as follows:

- n -> n / 2, if n is even;
- n -> 3 * n + 1, if in is odd

## Example:
 
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1


## Constraints

1 <= N <= 5 * 10**6


## Task

Which starting number, less than or equal to N produces the longest chain?

- N: input parameter
- Goal: return the number <= N that produces the longest Collatz sequence