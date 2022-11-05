# Faça um Programa que leia dois vetores com 10 posições cada e receba números inteiros.
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos
# pelos elementos intercalados dos dois outros vetores. Mostre ao final os três vetores



vetor =[ ]

vec1 = list()
vec2 = list()
vec3 = list()

print('Primeiro Vetor')

for i in range(10):

    vec1.append(int(input(f'Digite o valor do {i+1}° elemento: ')))

print('\nSegundo Vetor')

for i in range(10):

    vec2.append(int(input(f'Digite o valor do {i+1}° elemento: ')))

for i in range(10):

    vec3.append(vec1[i])

vec3.append(vec2[i])

print(f'\nO terceiro vetor fica: {vec3}')