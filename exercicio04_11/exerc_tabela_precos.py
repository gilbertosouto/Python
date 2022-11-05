# Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha,
# que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de
# pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
# Preço do pão será informado pelo usuário: se informar que custa R$ 0.18
# Mostrará a tabela abaixo:
# Tabela de preços

# 1 - R$ 0.18
# 2 - R$ 0.36
# 50 - R$ 9.00

# Programa Preços Panificadora Sr. Manoel!


# RS 1 - 0.18
# RS 2 - 0.36

# RS 50 - 9.00

preco = float(input("Preço do pão por unide: "))

print("Panificadora Sr. Manoel - Tabela de preços")

for i in range(1, 51):

    print(f"{i : 2d} - R$ {preco * i:5.2f}")

