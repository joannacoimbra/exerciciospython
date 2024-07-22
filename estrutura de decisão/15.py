# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores
# podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero,
# isósceles ou escaleno.
# Dicas:
# - Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# - Triângulo Equilátero: três lados iguais;
# - Triângulo Isósceles: quaisquer dois lados iguais;
# - Triângulo Escaleno: três lados diferentes;
x=float(input("Informe o 1º lado de um triângulo: "))
y=float(input("O 2º lado: "))
z=float(input("O 3º lado: "))
if (x+y)>z and (x+z)>y and (y+z)>x:
    if x==y and x==z and y==z:
        print(f"os valores {x}, {y} e {z} formam um triângulo equilatero.")
    elif (x==y,z) or (y==x,z) or (z==x,y):
        print(f"os valores {x}, {y} e {z} formam um triângulo isóceles.")
    elif x!=y and x!=z and z!=y:
        print(f"os valores {x}, {y} e {z} formam um triângulo escaleno.")
else:
    print(f"os valores {x}, {y} e {z} são inválidos.")