# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: 
# utilize uma função de arredondamento.
x=float(input("informe um número: "))
if x%1==0:
    print(f"{x} é inteiro.")
else:
    print(f"{x} é decimal.")