# programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota do 1º, 2º, 3º e 4º bimestre.
# Após deverá mostrar na tela se o aluno foi aprovado, Se está em recuperação ou foi reprovado sem chance de recuperação.
# Lembrando que cada bimestre vale 25 pontos num total anual de 100 pontos

# Programa para calcular as notas!


nota01=float(input("Digite a nota do PRIMEIRO bimestre: "))
nota02=float(input("Digite a nota do SEGUNDO bimestre: "))
nota03=float(input("Digite a nota do TERCEIRO bimestre: "))
nota04=float(input("Digite a nota do QUARTO bimestre: "))
resultado = (nota01 + nota02 + nota03 + nota04)

print("A nota do 1º Bimestre é: ",nota01)
print("A nota do 2º Bimestre é: ",nota02)
print("A nota do 3º Bimestre é: ",nota03)
print("A nota do 4º Bimestre é: ",nota04)

print("A nota obtida pelo aluno foi: " , resultado)

if (resultado >= 60):
   print("Aprovado")
elif (resultado < 60 or resultado >= 40):
    print("recuperação")
elif (resultado < 40):
    print("Não Aprovado")





