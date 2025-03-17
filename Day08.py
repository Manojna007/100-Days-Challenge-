"""
Problem Statement:
Given an integer `n`, return the Nth Fibonacci number.
The Fibonacci sequence is defined as:
F(1) = 0, F(2) = 1
F(n) = F(n-1) + F(n-2) for n > 2

Approach 1: Recursion (Exponential Time Complexity - O(2^n))
Approach 2: Memoization (Optimized Recursion - O(n) Time, O(n) Space)
Approach 3: Iterative (O(n) Time, O(1) Space)
"""

# -------------------- APPROACH 1: RECURSION --------------------
# Time Complexity: O(2^n) | Space Complexity: O(n)
def getNthFibRecursive(n):
    """Computes the Nth Fibonacci number using recursion (slow)."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return getNthFibRecursive(n - 1) + getNthFibRecursive(n - 2)


# -------------------- APPROACH 2: MEMOIZATION --------------------
# Time Complexity: O(n) | Space Complexity: O(n)
def getNthFibMemoization(n, memo={1: 0, 2: 1}):
    """Computes the Nth Fibonacci number using memoization (Top-Down DP)."""
    if n in memo:
        return memo[n]
    memo[n] = getNthFibMemoization(n - 1, memo) + getNthFibMemoization(n - 2, memo)
    return memo[n]


# -------------------- APPROACH 3: ITERATIVE --------------------
# Time Complexity: O(n) | Space Complexity: O(1)
def getNthFibIterative(n):
    """Computes the Nth Fibonacci number using an iterative approach."""
    if n == 1:
        return 0
    elif n == 2:
        return 1

    lastTwo = [0, 1]
    for _ in range(3, n + 1):
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
    return lastTwo[1] if n>1 else lastTwo[0]


# -------------------- TEST CASES --------------------
if __name__ == "__main__":
    n = 1  # Example: Find the 8th Fibonacci number
    print(f"Recursive Approach: Fib({n}) =", getNthFibRecursive(n))
    print(f"Memoization Approach: Fib({n}) =", getNthFibMemoization(n))
    print(f"Iterative Approach: Fib({n}) =", getNthFibIterative(n))