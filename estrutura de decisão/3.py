# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.
x=str(input("informe a letra inicial do seu gênero: "))
if x== "f" or x== "F":
  print("Feminino")
elif x== "m" or x== "M":
  print("M - Masculino")
else:
  print("Gênero Inválido.")