# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro 
# para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que 
# custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#   Informe ao usuário as quantidades de tinta a serem compradas e os respectivos 
#   preços em 3 situações:
#   a. comprar apenas latas de 18 litros;
#   b. comprar apenas galões de 3,6 litros;
#   c. misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#      Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
#      considere latas cheias.
import math
x= float(input("informe o tamanho da área em m2 a ser pintada: "))
litros= x/6
capacidade1= litros/18
capacidade2= litros/3.6
galao= 25
lata= 80
total= capacidade1*80
total2= capacidade2*25
print("comprar latas: ", math.ceil(capacidade1), "lata(s), vai custar ", math.ceil(total), "R$")
print("comprar galões: ", math.ceil(capacidade2), "galão(ões), vai custar ", math.ceil(total2),
"R$")
print("comprar latas e galões: ", math.ceil(capacidade1), "lata(s) e vai custar ", math.ceil(total),
"R$")