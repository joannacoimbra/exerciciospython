# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.
x= int(input("informe um número inteiro:"))
y= int(input("informe outro número inteiro:"))
z= float(input("informe um número real:"))
print("a. o produto do dobro do primeiro com metade do segundo é: ", (x*2)+(y/2))
print("b. a soma do triplo do primeiro com o terceiro é:", (x*3)+z)
print("c. o terceiro elevado ao cubo é:", z**3)