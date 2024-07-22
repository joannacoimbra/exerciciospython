# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como 
# "Inocente".
print("""RESPONDA SIM OU NÃO:""")
a=input("Telefonou para a vítima? ")
b=input("Esteve no local do crime? ")
c=input("Mora perto da vítima? ")
d=input("Devia para a vítima? ")
e=input("Já trabalhou com a vítima? ")
if a=="sim" and b=="sim" and c=="sim" and d=="sim" and e=="sim":
    print("Classificação: Assassino")
if (a=="nao" and b=="sim" and c=="sim" and d=="sim" and e=="sim") or (a=="sim" and b=="nao" and c=="sim" and d=="sim" and e=="sim") or (a=="sim" and b=="sim" and c=="nao" and d=="sim" and e=="sim") or (a=="sim" and b=="sim" and c=="sim" and d=="nao" and e=="sim") or (a=="sim" and b=="sim" and c=="sim" and d=="sim" and e=="nao"):
    print("Classificação: Cúmplice")