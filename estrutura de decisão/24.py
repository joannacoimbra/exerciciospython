# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele 
# deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#   par ou ímpar;
#   positivo ou negativo;
#   inteiro ou decimal.
x=float(input("informe um número: "))
y=float(input("informe outro número:"))
z=(input)(f"""  + soma
  - subtração
  * multiplicação
  / divisão
Qual operação você deseja fazer entre {x} e {y}?
""")
if z=="+" or z=="soma":
    soma=x+y
    print(f"{x} + {y} = {soma}")
    if soma%2==0:
        print(f"{soma} é par.")
    else:
        print(f"{soma} é ímpar.")
    if soma<0:
        print(f"{soma} é negativo.")
    else:
        print(f"{soma} é positivo.")
    if soma%1==0:
        print(f"{soma} é inteiro.")
    else:
        print(f"{soma} é decimal.")
if z=="-" or z=="subtração":
    subtração=x-y
    print(f"{x} - {y} = {subtração}")
    if subtração%2==0:
        print(f"{subtração} é par.")
    else:
        print(f"{subtração} é ímpar.")
    if subtração<0:
        print(f"{subtração} é negativo.")
    else:
        print(f"{subtração} é positivo.")
    if subtração%1==0:
        print(f"{subtração} é inteiro.")
    else:
        print(f"{subtração} é decimal.")
if z=="*" or z=="multiplicação":
    multiplicação=x*y
    print(f"{x} * {y} = {multiplicação}")
    if multiplicação%2==0:
        print(f"{multiplicação} é par.")
    else:
        print(f"{multiplicação} é ímpar.")
    if multiplicação<0:
        print(f"{multiplicação} é negativo.")
    else:
        print(f"{multiplicação} é positivo.")
    if multiplicação%1==0:
        print(f"{multiplicação} é inteiro.")
    else:
        print(f"{multiplicação} é decimal.")
if z=="/" or z=="divisão":
    divisão=x/y
    print(f"{x} / {y} = {divisão}")
    if divisão%2==0:
        print(f"{divisão} é par.")
    else:
        print(f"{divisão} é ímpar.")
    if divisão<0:
        print(f"{divisão} é negativo.")
    else:
        print(f"{divisão} é positivo.")
    if divisão%1==0:
        print(f"{divisão} é inteiro.")
    else:
        print(f"{divisão} é decimal.")