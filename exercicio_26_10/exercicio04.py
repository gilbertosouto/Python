

# Programa para receber 5 produtos em variaveis iPhone, Samsung, Tablet, PS5, notebook,
# com valores respectivos de 2980, 2540,  1950, 2100, 2350

iphone = 2980
samsung = 2540
tablet = 1950
pS5 = 2100
notebook = 2350

int(input ("Quantos iPhones você deseja comprar?", qtiphone))
int(input ("Quantos Samsung você deseja comprar?", qtsamsung))
int(input ("Quantos Tablets você deseja comprar?", qttablet))
int(input ("Quantos Tablets você deseja comprar?", qtPS5) )
int(input ("Quantos Tablets você deseja comprar?", qtnotebook))

Total = (qtiphone * iphone) + (qtsamsung * samsung) + (qttablet *
tablet) + (qtps5 * ps5) + (qtnotebook * Notebook)

print("Valor parcelado de 3 vezes é:", total/3 )
print("Valor parcelado de 6 vezes é:", (total*1.05)/6 )
print("Valor com desconto a vista é:", total-(total*0.10) )
