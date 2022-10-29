# programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota da 1ª, 2ª, 3ª e 4ª prova e a nota do 1º, 2º, 3º e 4º trabalho. Após deverá
# mostrar na tela a média obtida no 1º, 2º, 3º e 4º bimestre.
# E depois o total informado se o aluno foi aprovado, esta em
# recuperação ou foi reprovado sem recuperação.


prova01=float(input("Digite a nota da PRIMEIRA prova: "))
trab01=float(input("Digite a nota 1º trabalho: "))
prova02=float(input("Digite a nota da SEGUNDA prova: "))
trab02=float(input("Digite a nota 2º trabalho: "))
prova03=float(input("Digite a nota da TERCEIRA prova: "))
trab03=float(input("Digite a nota 3º trabalho: "))
prova04=float(input("Digite a nota da QUARTA prova: "))
trab04=float(input("Digite a nota 4º trabalho: "))

resultado = (prova01 + prova02 + prova03 + prova04)

resultado = (trab01 + trab02 + trab03 + trab04)

print("A nota da 1ª prova é: ",prova01)
print("A nota do 2ª prova é: ",prova02)
print("A nota do 3ª prova é: ",prova03)
print("A nota do 4ª prova é: ",prova04)

print("A nota obtida pelo aluno foi: " , resultado)
