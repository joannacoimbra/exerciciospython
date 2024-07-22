# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe 
# contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte 
# critério, baseado no salário atual:
# - salários até R$ 280,00 (incluindo) : aumento de 20%
# - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# - salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na  tela:
#       o salário antes do reajuste;
#       o percentual de aumento aplicado;
#       o valor do aumento;
#       o novo salário, após o aumento.
aumento=0
percentual=0
reajuste=0
salario=float(input("qual seu salário? "))
if salario<280.0:
    percentual="20%"
    aumento=salario*0.2
    reajuste=aumento+salario
elif salario>=280.0 and salario<700:
    percentual="15%"
    aumento=salario*0.15
    reajuste=aumento+salario
elif salario>=700.0 and salario<1500.0:
    percentual="10%"
    aumento=salario*0.1
    reajuste=salario+aumento
elif salario >=1500.0:
    percentual="5%"
    aumento=salario*0.05
    reajuste=salario+aumento
print(f"""
- Contra Cheque -

Salário:                R$ {salario}
Aumento:                R$ {aumento}
Reajuste:               R$ {reajuste}
Percentual de Aumento:    {percentual}
""")