drinks = []
i = 1

print("Digite suas 5 bebidas favoritas: ")
while i <= 5:
    drink = str(input(f"Bebida {i}: "))
    drinks.append(drink)
    i+=1

drinks.sort()

print("\nBebidas favoritas: ")
for drink in drinks:
    print(drink)