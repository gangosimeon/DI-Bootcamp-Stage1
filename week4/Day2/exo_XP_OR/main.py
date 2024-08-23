print("EXERCICE 1: Concatener Des Liste sans utiliser +\n")

liste1 = [10, 20, 7, 6, 18]
liste2 = [10, 15, 25,35,44]
liste1.extend(liste2)
print("Liste concaténée:\n",liste1,"\n")

print("EXERCICE 2: Plage De nombres\n")

print("Les nombres multiples de 5 et 7\n")
for nombre in range(1500,2501):
    if nombre%5==0 and nombre%7==0:
        print(nombre)