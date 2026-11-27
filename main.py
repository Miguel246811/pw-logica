numeros = []

for contador in range (10):
    numero = int(input(f"Digite o {contador + 1}ª número: "))
    numeros.append(numero)
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    print("\nLista original", numeros)
    print("\nNúmeros pares", pares)
    print("\nNúmeros ímpares", impares)
    print("\nQuantidade de pares", len(pares))
    print("\nQuantidade de ímpares", len(impares))