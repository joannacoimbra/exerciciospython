# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo
# de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem 
# “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
x= float(input("digite uma nota: "))
y= float(input("digite outra nota: "))
media=(x+y)/2
conceito=""
resultado=""
if media>9 and media<=10:
    conceito= "A"
    resultado="Aprovado"
elif media>7.5 and media<=9:
    conceito="B"
    resultado="Aprovado"
elif media>6 and media<=7.5:
    conceito="C"
    resultado="Aprovado"
elif media>4 and media<=6:
    conceito="D"
    resultado="Reprovado"
elif media<=4 and media>=0:
    conceito="E"
    resultado="Reprovado"
print(f"""
Média de Aproveitamento  Conceito
Entre 9.0 e 10.0          A
Entre 7.5 e 9.0           B
Entre 6.0 e 7.5           C
Entre 4.0 e 6.0           D
Entre 4.0 e zero          E

Suas notas: {x} e {y}
Sua média: {media}
Conceito: {conceito}
Resultado: {resultado}
""")