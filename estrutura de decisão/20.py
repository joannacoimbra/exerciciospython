# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a 
# média alcançada por aluno e presentar:
# - A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# - A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# - A mensagem "Aprovado com Distinção", se a média for igual a 10.
x=float(input("Informe uma nota: "))
y=float(input("Informe outra nota: "))
z=float(input("Informe outra nota: "))
media=(x+y+z)/3
if media>=7 and media<10:
    print("Aprovado.")
elif media<7:
    print("Reprovado.")
elif media==10:
    print("Aprovado com Distinção.")