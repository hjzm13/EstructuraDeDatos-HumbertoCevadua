class FibonacciIterativo:
    @staticmethod
    def calcular(n: int) -> int:
        """Implementación iterativa O(n)"""
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
