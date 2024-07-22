# Faça um Programa que leia três números e mostre-os em ordem decrescente.
a = float(input("informe um numero a: "))
b = float(input("informe um numero b: "))
c = float(input("informe um numero c: "))
if a > b > c:
  print("os números em ordem descrescente é", a, b, c)
if a > c > b:
  print("os números em ordem descrescente é", a, c, b)
if b > a > c:
  print("os números em ordem descrescente é", b, a, c)
if b > c > a:
  print("os números em ordem descrescente é", b, c, a)
if c > a > b:
  print("os números em ordem descrescente é", c, a, b)
if c > b > a:
  print("os números em ordem descrescente é", c, b, a)