# Faça um Programa que pergunte quanto você ganha por hora
# Número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato
# mostre todos os descontos, mostre o salário bruto e o líquido

# Quanto pagou ao INSS.
# Quanto pagou ao sindicato.
# O salário líquido.
# Calcule os descontos e o salário líquido, conforme a tabela abaixo:
# Salário Bruto : R$ - IR (11%) : R$ - INSS (8%) : R$ - Sindicato ( 5%)
# Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

# Programa Salário

print("complete as seguintes informações")

salario = int(input("salario mensal"))
inss = 5/100 * salario
salarioinss = salario - inss
sindicato = 11/100 * salario
salariosindicato = salario - sindicato
salaliquido = salario -inss - sindicato
dia = int(input("dias trabalhados por mes: "))
salariodia = salario / dia
hora = int(input("carga horaria por dia: "))
salariohora = salariodia /hora

print("salario bruto: " , salario)
print("salario recebido por dia: " , salariodia)
print("salario recebido por hora , trabalhada: ")
print("desconto do inss: , inss")
print("desconto do sindicato: , sindicato")
print(" o salario liquido é de: ", salaliquido)