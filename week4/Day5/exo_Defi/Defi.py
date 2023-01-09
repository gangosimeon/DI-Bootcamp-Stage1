mots=input("Entrer l'ensemble des mots: ")
liste=sorted(mots.split(","))
j=0
while j < len(liste)-1:
    print(liste[j],end=",")
    j+=1
print(liste[-1])