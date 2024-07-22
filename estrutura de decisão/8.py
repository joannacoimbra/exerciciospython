# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve 
# comprar, sabendo que a decisão é sempre pelo mais barato.
a=float(input("informe o preço de um produto a: "))
b=float(input("informe o preço de um produto b: "))
c=float(input("informe o preço de um produto c: "))
if a<b and a<c:
  print("você deve comprar o produto de R$", a,)
if b<a and b<c:
 print("você deve comprar o produto de R$", b,)
if c<a and c<b:
  print("você deve comprar o produto de R$", c)