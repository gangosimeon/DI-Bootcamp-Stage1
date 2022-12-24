print("Defi 1:\n")
longueur=int(input("Entrer une longueur: "))
liste=[]
j=0
while j<longueur:
    nombre=int(input("Entrer un nombre: "))
    liste.append(nombre)
    j+=1
print("listes_Des_Nombre=",liste,"\n")

print("Defi 2\n")
chaine=input("Entrer une chaine de caractere: ")
ch=""
for j in chaine:
    if j not in ch:
        ch=ch+j
print(ch,"\n")