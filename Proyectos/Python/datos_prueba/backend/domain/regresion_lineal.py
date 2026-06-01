import numpy as np

class RegresionLineal:

    @staticmethod
    def fit(x: list[float], y: list[float]) -> dict:

        if len(x) != len(y):
            raise ValueError(
                "x e y deben tener la misma longitud"
            )

        if len(x) < 2:
            raise ValueError(
                "Se requieren al menos dos observaciones"
            )

        x = np.array(x, dtype=float)
        y = np.array(y, dtype=float)

        n = len(x)

        # Esta regresión lineal esta hecha solo para datos bidimensioanales
        A = np.column_stack([
            np.ones(n),
            x
        ])

        # Hacemos la regresión lineal estandar
        beta = np.linalg.inv(
            A.T @ A
        ) @ A.T @ y
        # beta es nuestro vector de parametros de la recta

        predictions = (
            intercept + slope * x
        ).tolist()

        intercept = float(beta[0])
        slope = float(beta[1])

        return {
            "samples": n,
            "intercept": intercept,
            "slope": slope,
            "predictions": predictions
        }