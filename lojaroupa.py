
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
    if totalcompra < 800 and parcelas >= 6:
        print("Compras abaixo de 800 reais só podem ser parceladas até 5x!")
    elif parcelas <= 10:
        print("O valor total será de: ", totalcompra)
    elif parcelas == 11:
        print("O valor total será de: ", totalcompra + (totalcompra * 5/100))
    elif parcelas == 12:
        print("O valor total será de: ", totalcompra + (totalcompra * 6.5/100))
    elif parcelas == 13:
        print("O valor total será de: ", totalcompra + (totalcompra * 7/100))
    elif parcelas == 14:
        print("O valor total será de: ", totalcompra + (totalcompra * 9/100))
    elif parcelas == 15:
        print("O valor total será de: ", totalcompra + (totalcompra * 9.5/100))
    elif parcelas == 16:
        print("O valor totalserá de: ", totalcompra + (totalcompra * 10/100))
    elif parcelas == 17:
        print("O valor total será de: ", totalcompra + (totalcompra * 11.3/100))
    elif parcelas == 18:
        print("O valor total será de: ", totalcompra + (totalcompra * 12/100))
    else:
        print("Quantidade não valida")