# Calculo de IMC

### nome, idade, peso, altura // e calcular imc

nome = input("Olá! Qual seu nome?: ")
idade = input("Qual sua idade? ")
altura = float(input("Sua altura: "))
peso = float(input ("Seu peso: "))

IMC = peso / (altura ** 2)

print(f"Olá {nome}!")
print(f"Sua idade é de {idade} anos")
print(f"Seu IMC é de {IMC}")
