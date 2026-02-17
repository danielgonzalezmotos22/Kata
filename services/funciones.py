def calcular(cadena: str) -> int:
    if not cadena:
        return 0
    numeros = [int(n) for n in cadena.split(',')]
    return sum(numeros)