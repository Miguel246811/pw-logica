import random

opcoes = ["pedra", "papel", "tesoura"]

print("=== PEDRA, PAPEL E TESOURA ===")

while True:
    jogador = input("\nEscolha pedra, papel ou tesoura: ").lower()

    if jogador not in opcoes:
        print("Opção inválida! Tente novamente.")
        continue

    computador = random.choice(opcoes)

    print("\nVocê escolheu:", jogador)
    print("O computador escolheu:", computador)

    if jogador == computador:
        print("🤝 EMPATE!")

    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("🏆 VOCÊ VENCEU!")

    else:
        print("😢 VOCÊ PERDEU!")

    continuar = input("\nDeseja jogar novamente? (sim/não): ").lower()

    if continuar != "sim":
        print("Obrigado por jogar!")
        break