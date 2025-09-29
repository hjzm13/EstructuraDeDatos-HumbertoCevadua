class FibonacciRecursivo:
    @staticmethod
    def calcular(n: int) -> int:
        """
        Implementación recursiva O(2^n)
        CUIDADO: Muy lenta para n > 35
        """
        if n <= 1:
            return n
        return FibonacciRecursivo.calcular(n - 1) + FibonacciRecursivo.calcular(n - 2)
