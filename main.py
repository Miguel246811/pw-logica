nome = input("Qual seu nome? ")

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em KG: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("IMC abaixo do peso 18.5")

elif imc < 25:
    print("IMC entre 18.5 e 24.9 na media")

else:
    print("IMC igual ou acima de 25 gordo")