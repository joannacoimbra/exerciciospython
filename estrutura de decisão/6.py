# Faça um Programa que leia três números e mostre o maior deles.
a=float(input("informe um número: "))
b=float(input("informe outro número: "))
c=float(input("informe outro número: "))
if a>b and a>c:
  print(a, "é o maior numero.")
elif b>a and b>c:
 print(b, "é o maior numero.")
elif c>a and c>b:
  print(c, "é o maior numero.")