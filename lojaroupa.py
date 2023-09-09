
totalcompra = float(input("Digite o Valor total de compra: "))
pagamento = input("Qual forma de pagamento? (A Vista / A Prazo): ")

if pagamento == 'A Vista':
    if totalcompra < 500:
        print("O Valor será de: ", totalcompra - (totalcompra * 10/100))
    elif totalcompra > 500:
        print("O Valor será de: ", totalcompra - (totalcompra * 15/100))
    elif totalcompra > 1000:
        print("O Valor será de: ", totalcompra - (totalcompra * 20/100))


if pagamento == 'A Prazo':
    parcelas = int(input("Informe a quantidade de parcelas: "))
    if totalcompra < 800:
        print("Valor total de compra = ", totalcompra) 


