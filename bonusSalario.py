# Bonus Salario

sal = float(input("Insira seu Salário: "))
temp = int(input("Quanto tempo de serviço(em anos): "))

if temp >= 5:
    print("Você contribuiu por mais de 5 anos \n seu salário bônus salarial é: ", sal * 1.05 )
else:
    print("Menos de 5 anos contribuindo. Sem bônus Salarial")