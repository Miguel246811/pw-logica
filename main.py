idade = int(input("Digite sua idade: "))

if idade == 0:

    print("Idade invalida")

elif idade <= 12:

    print("Criança")

elif idade <= 17:

    print("Adolescente")

elif idade <= 18:

    print("Adulto")

elif idade >= 60:
    print("Idoso")
