# Programa perguntar em que turno estuda!
# M-matutino ou V-Vespertino ou N-Noturno!
# Mostre a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!

turno = input("Digite M para Matutino ou V para Vespertino ou N para Noturno: ").upper()

match turno:
    case "M":
        print("Bom Dia")
    case "V":
        print("Boa tarde")
    case "N":
        print ("Boa Noite")

    case _: print("Turno Inválido")

