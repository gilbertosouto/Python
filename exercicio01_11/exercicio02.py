# • Faça um programa para imprimir igual abaixo:
# 1
# 2 2
# 3 3 3 ...
# n n n n ...

# Programa impressão números e Letras!

def enes(n):
    for c in range(1, n + 1):
        cont = 1
        while True:
            print(c, end=' ')
            if cont == c:
                break
            cont += 1
        print()

n = int(input('Digite um número:  '))

for i in range(n):
        i += 1
        print(str(i) * i)
n = int(input('Digite um número: '))

