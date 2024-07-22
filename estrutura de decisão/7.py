# Faça um Programa que leia três números e mostre o maior e o menor deles.
a=float(input("informe um número: "))
b=float(input("informe outro número: "))
c=float(input("informe outro número: "))
if a>b and a>c:
  print(a, "é o maior numero.")
if b>a and b>c:
 print(b, "é o maior numero.")
if c>a and c>b:
  print(c, "é o maior numero.")
if a<b and a<c:
  print(a, "é o menor numero.")
if b<a and b<c:
 print(b, "é o menor numero.")
if c<a and c<b:
  print(c, "é o menor numero.")