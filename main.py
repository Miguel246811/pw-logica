
nota = float(input("Sua nota: ").replace(",",","))

if nota >= 9:
    print("Conceito A - Excelente!")
elif nota >= nota >= 7:  
    print("Conceito B - Bom!")
elif nota >= 5:    
    print("Conceito C - Regular")
else:
    print("Conceito D - Reprovado")


