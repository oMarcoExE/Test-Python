# Classificação De Nota

nota = int(input("Insira uma Nota (0-100)"))

if nota < 60:
    print("Nota = F")
elif nota >= 60 and nota <= 69:
    print("Nota = D")
elif nota >= 70 and nota <= 79:
    print("Nota = C")
elif nota >= 80 and nota <= 89:
    print("Nota = B")
elif nota >= 90 and nota <= 100:
    print("Nota = A")
else: 
    print("Número não válido!")