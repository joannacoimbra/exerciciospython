# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a 
# velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado 
# de download do arquivo usando este link (em minutos).
import math
x=float(input("informe o tamanho do arquivo em MB: "))
y=float(input("informe a velocidade da internet em Mbps: "))
print("o tempo de download aproximadamente é de: ", math.ceil(((x*8)/y)/60), "minutos.")