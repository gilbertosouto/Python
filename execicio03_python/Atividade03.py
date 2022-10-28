#  programa de calculadora que realiza as operações de
# soma, multiplicação, divisão e subtração!


print("+ para Adição")
print("- para Subtração")
print("* para Multiplicação")
print("/ para Divisão")

print("SELECIONE A OPERAÇÃO DESEJADA")

a = float(input("Primeiro número:"))
b = float(input("Segundo número:"))
operação = input("Digite a operação a realizar (+,-,* ou /):")
if operação == "+":
    resultado = a + b
elif operação == "-":
    resultado = a - b
elif operação == "*":
    resultado = a * b
elif operação == "/":
    resultado = a / b
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)






