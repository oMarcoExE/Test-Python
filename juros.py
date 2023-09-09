#Solicite o valor principal
#solicite taxa de juros anual e periodo de tempo em anos
#Mostrar montante (montante = principal + (principal * taxa * tempo))

valorPRIN = float (input("Informe o valor principal: ") )
jurosANUAL = float(input("Informe a taxa de juros anual: "))
tempo = int (input("Informe o período de tempo em anos: "))

montante = valorPRIN + (valorPRIN * jurosANUAL * tempo)

print(f"\nSeu montante é de {montante}")