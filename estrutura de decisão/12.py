# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do 
# Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
# e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que 
# deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa 
# deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
#   - Salário Bruto até 900 (inclusive) - isento
#   - Salário Bruto até 1500 (inclusive) - desconto de 5%
#   - Salário Bruto até 2500 (inclusive) - desconto de 10%
#   - Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas 
#     conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
x=float(input("Quanto você ganha por hora? "))
y= float(input("Quantas horas no mês você trabalha? "))
salariobruto=x*y
IR=0
IRpercentual=""
INSS= salariobruto*0.1
sindicato=salariobruto*0.03
FGTS=salariobruto*0.11
if salariobruto<=900.0:
    IRpercentual=" 0%"
    IR=salariobruto*0
elif salariobruto<=1500.0:
    IRpercentual=" 5%"
    IR=salariobruto*0.05
elif salariobruto<=2500.0:
    IRpercentual="10%"
    IR=salariobruto*0.1
elif salariobruto>2500:
    IRpercentual="20%"
    IR=salariobruto*0.2
descontos= IR+sindicato+INSS
salarioliquido= salariobruto-descontos
print(f"""
------------- Folha de Pagamento -------------
    Salário Bruto:      R$ {salariobruto}
(-) IR({IRpercentual}):            R$ {IR}
(-) INSS(10%):          R$ {INSS}
    FGTS(11%):          R$ {FGTS}
    Descontos:          R$ {descontos}
    Salário Liquido:    R$ {salarioliquido}
""")