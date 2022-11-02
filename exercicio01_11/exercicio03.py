# Numa fazenda em um local reservado para criação coloca-se um casal de coelhos. Supondo que em cada mês,
# a partir do segundo mês de vida, cada casal dá origem a um novo casal de coelhos, ao fim de um ano,
# quantos casais de coelhos estão no pátio? Escreva um programa para calcular a quantidade de coelhos em um ano.

# sequencia fibonacci

ntermos = 12

n1, n2 = 0, 1
contador = 0
print("quantidade coelhos anual")
while contador  < ntermos:
    print(n1)
    n = n1 + n2
    n1 = n2
    n2 = n
    contador += 1
