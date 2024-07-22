# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
dia=int(input("informe uma data no formato dd/mm/aaaa. \ndia: "))
if dia>31 or dia<1:
    print("data inválida")
else:
    mes=int(input("mês: "))
    if mes>12 or mes<1:
        print("data inválida")   
    else:
        ano=int(input("ano: "))
        if ano<1 or ano>30000:
            print("data inválida")   
        else:
            print(f"{dia}/{mes}/{ano} é uma data válida")