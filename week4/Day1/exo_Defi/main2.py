print("-----------------------------------------------------")

chaine =input("Entrer une chaine de caractere de 10 caracteres : ")
if len(chaine)<10:
    print("Chaine pas assez longue")
elif len(chaine)>10:
    print("Chaine trop longue")
else:
    print("Bravo ! Chaine correcte !")
    
print("2-\n")

print(chaine[0],"*********", chaine[-1])

print("3-\n")

chain=""
for j in range(len(chaine)):
    chain= chain + chaine[j]
    print(chain)
    
print("4-\n")

print()
import random
liste=[]
for j in range(len(chaine)):
    liste.append(chaine[j])

random.shuffle(liste)
ch=""
for j in liste:
    ch=ch+j
print(ch)

print("-----------------------------------------------------")