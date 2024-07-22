# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve 
# calcular a média alcançada por aluno e apresentar:
# - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# - A mensagem "Reprovado", se a média for menor do que sete;
# - A mensagem "Aprovado com Distinção", se a média for igual a dez.
a=input("Digite uma nota: ")
b=input("Digite outra nota: ")
m= (float(a)+float(b)/2)
if(m>=7 and m<10):
  print("Aprovado")
elif (m<7):
  print("Reprovado")
elif(m==10):
  print("Aprovado *")