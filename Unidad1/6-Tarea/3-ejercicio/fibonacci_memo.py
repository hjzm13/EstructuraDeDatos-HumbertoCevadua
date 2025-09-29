class FibonacciMemo:
    @staticmethod
    def calcular(n: int, memo: dict = {}) -> int:
        """
        BONUS: Implementación con memoization O(n)
        """
        if n in memo:
            return memo[n]
        if n <= 1:
            memo[n] = n
        else:
            memo[n] = FibonacciMemo.calcular(n - 1, memo) + FibonacciMemo.calcular(n - 2, memo)
        return memo[n]
