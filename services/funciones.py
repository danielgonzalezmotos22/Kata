def calcular(numeros: str) -> int:
    if not numeros:
        return 0
    numeros = [int(n) for n in numeros.split(',')]
    return sum(numeros)

if __name__ == '__main__':
    print(calcular('1,2,3,5,10,10')) 