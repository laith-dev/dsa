class Fibonacci:
    @classmethod
    def memoization(cls, n: int, memory: dict[int, int] = None) -> int:
        """
        Find the n-th Fibonacci number.

        Start from `n` down to the 0-th element, storing intermediate results down the way,
        and finally return the result (which should be calculated and stored in `memory`).

        This implementation uses `Memoization`, top-down approach.
        """

        # Initialize
        if memory is None:
            memory = {
                0: 0,
                1: 1
            }

        if n in memory:
            return memory[n]

        prev1 = cls.memoization(n - 1, memory)
        prev2 = cls.memoization(n - 2, memory)
        memory[n] = prev1 + prev2

        return memory[n]

    @staticmethod
    def tabulation(n: int) -> int:
        """
        Find the n-th Fibonacci number.

        Start from base cases, i.e. 0-th -> 0, 1-th -> 1. Then walk all the way up to `n`,
        storting intermediate results up to `n`.

        This implementation uses `Tabulation`, bottom-up approach.
        """

        if n < 2:
            return n

        # Initialize
        fibs = [0, 1]
        for i in range(2, n + 1):
            fibs.append(fibs[i - 1] + fibs[i - 2])

        return fibs[n]

    @staticmethod
    def optimized(n: int) -> int:
        """
        Space and time optimized solution where we don't store intermediate Fibonacci
        numbers, but rather, we calculate the nth Fib as we go.
        """
        if n <= 1:
            return n

        prev, curr = 0, 1
        for i in range(2, n + 1):
            prev, curr = curr, prev + curr

        return curr
