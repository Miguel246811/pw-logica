nome1 = input("Seu nome: ")
nome2 = input("Nome do parceiro: ")
nome3 = input("Nome do outro resenha: ")
ano_nascimento1 = int(input(f"Ano de nascimento do {nome1}:"))
ano_nascimento2 = int(input(f"Ano de nascimento do {nome2}:"))
ano_nascimento3 = int(input(f"Ano de nascimento do {nome3}:"))

ano_atual = 2026

idade1 = ano_atual - ano_nascimento1
idade2 = ano_atual - ano_nascimento2
idade3 = ano_atual - ano_nascimento3

ano_1001 = ano_nascimento1 + 100
ano_1002 = ano_nascimento2 + 100
ano_1003 = ano_nascimento3 + 100

print(f"{nome1}, você tem (ou vai fazer) {idade1} anos em {ano_atual}")
print(f"Você vai completar 100 anos em {ano_1001}")
print(f"{nome2}, você tem (ou vai fazer) {idade2} anos em {ano_atual}")
print(f"Você vai completar 100 anos em {ano_1002}")
print(f"{nome3}, você tem (ou vai fazer) {idade3} anos em {ano_atual}")
print(f"Você vai completar 100 anos em {ano_1003}")