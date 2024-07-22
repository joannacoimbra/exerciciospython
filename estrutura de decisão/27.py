# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                 Até 5 Kg                Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) 
# de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
pedido= input("Qual fruta desejas? (1)Morango ou (2)Maçã: ")
kilos= float(input("Quantos kilos desejas: "))
total= 0
desconto= 0
if pedido=="morango" and kilos<=5:
    total=kilos*2.5
    if total > 25:
        desconto= total*(10/100)
        total= total-desconto
        print(f"O valor a ser pago é de: R$ {total}")
elif pedido=="morango" and pedido>5:
    total=kilos*2.2
    if kilos>=8:
        desconto= 0.1/total
        total= total-desconto
        desconto= 0.1/total
        print(f"O valor a ser pago é de: R$ {total}")
    elif total>25:
        desconto= 0.1/total
        total= total-desconto
        print(f"O valor a ser pago é de: R$ {total}")
else:
    print(f"O valor a ser pago é de: R$ {total}")
if pedido=="maçã" and kilos<=5:
    total=kilos*1.8
    if total > 25:
        desconto= 0.1/total
        total= total-desconto
        print(f"O valor a ser pago é de: R$ {total}")
elif pedido=="maçã" and pedido>5:
    total=kilos*1.5
    if kilos>=8:
        desconto= 0.1/total
        total= total-desconto
        print(f"O valor a ser pago é de: R$ {total}")
    elif total>25:
        desconto= 0.1/total
        total= total-desconto
        print(f"O valor a ser pago é de: R$ {total}")
else:
    print(f"O valor a ser pago é de: R$ {total}")