# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário
# nas seguintes situações:
# a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
import math
x1=0
x2=0
a=float(input("informe o valor de a: "))
if a==0:
    print("ERROR")
else:
    b=float(input("informe o valor de b: "))
    c=float(input("informe o valor de c: "))
    delta=(b**2)-4*a*c
    raizdelta= math.pow(delta,1/2)
    if delta<0:
        print("a equação não possui raízes reais.")
    else:
        x1=(-b-(raizdelta))/2*a
        x2=(-b+(raizdelta))/2*a
print(f"as raizes sao x¹: {x1} e x²: {x2}")