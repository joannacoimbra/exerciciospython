# Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize 
# o operador módulo (resto da divisão).
x=int(input("informe um número inteiro: "))
if x%2==0:
    print(f"{x} é par.")
else:
    print(f"{x} é ímpar.")