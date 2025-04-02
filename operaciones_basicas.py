"""
Integrante:
- Ricaldi Solis Maylon
"""

class OperacionesBasicas:
    """Clase que realiza operaciones matemáticas básicas como suma y resta."""

    def __init__(self):
        self.resultado = 0

    def sumar(self, a, b):
        """Suma dos números y almacena el resultado."""
        self.resultado = a + b

    def restar(self, a, b):
        """Resta dos números y almacena el resultado."""
        self.resultado = a - b

    def obtener_resultado(self):
        """Retorna el resultado de la última operación realizada."""
        return self.resultado


# pylint: disable=too-few-public-methods
class CalculadoraPromedio:
    """Clase para calcular el promedio de una lista de valores."""

    def __init__(self, valores):
        self.valores = valores

    def calcular_promedio(self):
        """Calcula y retorna el promedio de la lista de valores."""
        return sum(self.valores) / len(self.valores) if self.valores else 0


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedio = calculadora_promedio.calcular_promedio()
    print(f"El promedio de los números es: {promedio}")
