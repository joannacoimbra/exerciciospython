# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em 
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 
# 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem 
# compradas e o preço total.
import math
x= float(input("informe o tamanho da área em m² a ser pintada: "))
litros= x/3
latas= litros/18
total= latas*80
print("para pintar", x, "m², você precisa de:" , (x/3), "litros de tinta. Para isso vc precisa de ", math.ceil(latas), "lata(s) e vai custar ", math.ceil(total), "reais.")