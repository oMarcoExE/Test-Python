# Calculos com condições

nmr1 = int (input("Digite o primeiro Número: "))
nmr2 = int (input ("Digite o segundo Número: "))
operador = input("Digite um operador lógico: ")

if operador == '+':
    print("Resultado = ", nmr1 + nmr2)
elif operador == '-':
    print("Resultado = ", nmr1 - nmr2)
elif operador == '*':
    print("Resultado = ", nmr1 * nmr2)
elif operador == '/':
    print("Resultado = ", nmr1 / nmr2)
else:
    print("Operador Lógico não reconhecido! Utilize +, -, *, ou / ")
