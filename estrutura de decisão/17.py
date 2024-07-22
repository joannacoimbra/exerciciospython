# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe 
# se este ano é ou não bissexto.
x=int(input("informe um ano qualquer: "))
if (x%4==0 and x%100!=0) or (x%400==0):
    print(f"{x} é ano bissexto.")
else:
    print(f"{x} não é ano bissexto.")