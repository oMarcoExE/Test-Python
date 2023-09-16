#Programa desenvolvido para uma atividade de Loja de roupas 
totalcompra = float(input("Digite o Valor total de compra: "))
pagamento = input("Qual forma de pagamento? (A Vista / A Prazo): ")

if pagamento == 'A Vista':
    if totalcompra < 500: totalcompra = totalcompra - (totalcompra * 10/100)
    elif totalcompra > 500 and totalcompra < 1000: totalcompra = totalcompra - (totalcompra * 15/100)
    elif totalcompra > 1000: totalcompra = totalcompra - (totalcompra * 20/100)

if pagamento == 'A Prazo':
    parcelas = int(input("Informe a quantidade de parcelas: "))
    if totalcompra < 800 and parcelas >= 6:
        print("Compras abaixo de 800 reais só podem ser parceladas até 5x!")
    elif parcelas <= 10:
        totalcompra = totalcompra
    elif parcelas == 11: totalcompra = totalcompra + (totalcompra * 5/100)
    elif parcelas == 12: totalcompra = totalcompra + (totalcompra * 6.5/100)
    elif parcelas == 13: totalcompra = totalcompra + (totalcompra * 7/100)
    elif parcelas == 14: totalcompra = totalcompra + (totalcompra * 9/100)
    elif parcelas == 15: totalcompra = totalcompra + (totalcompra * 9.5/100)
    elif parcelas == 16: totalcompra = totalcompra + (totalcompra * 10/100)
    elif parcelas == 17: totalcompra = totalcompra + (totalcompra * 11.3/100)
    elif parcelas == 18: totalcompra = totalcompra + (totalcompra * 12/100)
    else: print("Quantidade não valida")
print(f"Sua compra Deu um total R$ {totalcompra}")