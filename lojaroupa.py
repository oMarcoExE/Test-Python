#Programa desenvolvido para uma atividade de Loja de roupas 
totalcompra = float(input("Digite o Valor total de compra: "))
pagamento = input("Qual forma de pagamento? (A Vista / A Prazo): ")

if pagamento == 'A Vista':
    if totalcompra < 500: 
        totalcompra = totalcompra - (totalcompra * 10/100)
    elif totalcompra > 500 and totalcompra < 1000: 
        totalcompra = totalcompra - (totalcompra * 15/100)
    elif totalcompra > 1000: 
        totalcompra = totalcompra - (totalcompra * 20/100)

if pagamento == 'A Prazo':
    parcelas = float(input("Informe a quantidade de parcelas: "))
    if totalcompra < 800 and parcelas >= 6:
        print("Compras abaixo de 800 reais só podem ser parceladas até 5x!")
    elif parcelas <= 10: totalcompra = totalcompra
    elif parcelas == 11: totalcompra = totalcompra + totalcompra * (0.05 * parcelas)
    elif parcelas == 12: totalcompra = totalcompra + totalcompra * (0.065 * parcelas)
    elif parcelas == 13: totalcompra = totalcompra + totalcompra * (0.07 * parcelas)
    elif parcelas == 14: totalcompra = totalcompra + totalcompra * (0.09 * parcelas)
    elif parcelas == 15: totalcompra = totalcompra + totalcompra * (0.095 * parcelas)
    elif parcelas == 16: totalcompra = totalcompra + totalcompra * (0.1 * parcelas)
    elif parcelas == 17: totalcompra = totalcompra + totalcompra * (0.0113 * parcelas)
    elif parcelas == 18: totalcompra = totalcompra + totalcompra * (0.012 * parcelas)
    else: print("Quantidade não valida")

print(f"Sua compra Deu um total R$ {totalcompra}") 