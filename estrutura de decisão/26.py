# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
#      até 20 litros, desconto de 3% por litro
#      acima de 20 litros, desconto de 5% por litro
# Gasolina:
#      até 20 litros, desconto de 4% por litro
#      acima de 20 litros, desconto de 6% por litro 
# - Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago 
# pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool
# é R$ 1,90.
print("""
===== TABELA DE PREÇOS =====
(A) Álcool............R$1,90
(G) Gasolina..........R$2,50
      """)
pedido=str(input("Qual combustível desejas: A ou G? "))
litros=float(input("Quantos litros? "))
if pedido=="A" or pedido=="a":
    if litros<=20:
        valor=litros*1.9
        desconto=valor*0.03
        total=valor-desconto
        print(f"Para {litros}L custará R${total}")
    elif litros>20:
        valor=litros*1.9
        desconto=valor*0.05
        total=valor-desconto
        print(f"Para {litros}L custará R${total}")
elif pedido=="G" or pedido=="g":
    if litros<=20:
        valor=litros*2.5
        desconto=valor*0.04
        total=valor-desconto
        print(f"Para {litros}L custará R${total}")
    elif litros>20:
        valor=litros*2.5
        desconto=valor*0.06
        total=valor-desconto
        print(f"Para {litros}L custará R${total}")