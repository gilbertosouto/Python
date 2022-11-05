# Faça um programa que calcule o fatorial de um número,
# é obrigatório o uso de função recursiva para o calculo fatorial.

# Programa Calculo Fatorial com Função Recursiva


numero = int(input("Fatorial de: ") )

resultado=1

count=1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)