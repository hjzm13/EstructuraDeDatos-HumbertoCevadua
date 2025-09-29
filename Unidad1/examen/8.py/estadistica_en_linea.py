



import math

class EstadisticaEnLinea:
    def __init__(self):
        self.n = 0
        self._media = 0.0
        self._M2 = 0.0
        self._min = math.inf
        self._max = -math.inf

    def actualizar(self, x: float) -> None:
        # min/max
        if x < self._min: self._min = x
        if x > self._max: self._max = x

        # Welford
        self.n += 1
        delta = x - self._media
        self._media += delta / self.n
        delta2 = x - self._media
        self._M2 += delta * delta2

    def media(self) -> float:
        return self._media

    def varianza(self) -> float:
        return self._M2 / (self.n - 1) if self.n > 1 else 0.0

    def desviacion_estandar(self) -> float:
        return math.sqrt(self.varianza())

    def minimo(self) -> float:
        return self._min if self.n > 0 else math.nan

    def maximo(self) -> float:
        return self._max if self.n > 0 else math.nan

    def resumen(self) -> dict:

        return {
            "conteo": self.n,
            "media": round(self.media(), 2),
            "varianza": round(self.varianza(), 2),
            "desv_estandar": round(self.desviacion_estandar(), 2),
            "min": round(self.minimo(), 2),
            "max": round(self.maximo(), 2),
        }
