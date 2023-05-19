#Conjuntos
def conjunto(numeros):
    n = len(numeros)
    for i in range(1, 2**n):
        sumaSubconjuntos = sum(numeros[j] for j in range(n) if (i & (1 << j)) != 0)
        for j in range(i+1, 2**n):
            if (i & j) == 0 and sumaSubconjuntos == sum(numeros[k] for k in range(n) if (j & (1 << k)) != 0):
                return False
    return True #@

#Conjuntos suma espcial
def conjuntoSuma(filename):
    conjuntoSuma = []
    with open(filename, 'r') as file:
        for line in file:
            numeros = list(map(int, line.strip().split(',')))
            if conjunto(numeros):
                conjuntoSuma.append(numeros)
    return conjuntoSuma

#Suma de conjuntos
def SumaElementos(sets):
    return sum(sum(numeros) for numeros in sets)

filename = 'sets.txt'
conjuntos = conjuntoSuma(filename)
suma = SumaElementos(conjuntos)

print("Los conjuntos ""Suma especial"" son: ")
for i, numero in enumerate(conjuntos):
    print(f"A{i+1}: {numero}")
print("El resultado de la suma es:", suma)