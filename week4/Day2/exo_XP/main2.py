print("EXERCICE 1 : Set")
# 1-
my_fav_numbers={5,10,15,20,30,40,50}
print("Ensemble initial: ",my_fav_numbers)
# 2-Ajout du dernier element
my_fav_numbers.add(9)
my_fav_numbers.add(25)
print("Ajout de 9 et 25 a ensemble initial: ",my_fav_numbers)
# 3-Supprisseion du dernier elelment
my_fav=my_fav_numbers.pop()
print("Le numero supprimer est: ",my_fav)
print("Suppression du dernier numero dans l'ensemble: ",my_fav)
# 4-
friend_fav_numbers={4,7,8,9,10,11,12,13,14,15}
print("Numeros favori d'amis: ",friend_fav_numbers)
# 5-concatenation de deux ensembles
our_fav_numbers=my_fav_numbers | friend_fav_numbers
print("Deux ensembles concatener: ",our_fav_numbers)

print("EXERCICE 2 : Tuple")

print("1. Non, on ne peut pas ajouter plus d'entiers au tuple car les tuples sont des listes immuables,les éléments ne peuvent pas être modifiés .")
print()

print("EXERCICE 3 : liste")

basket=["Banana","Apples","Oranges","Blueberries"]
print("basket=",basket,"\n")
print("1-Suppression de 'Banana' de la liste\n")
basket.remove("Banana")
print(basket,"\n")

print("2-Suppression de 'Myrtilles' de la liste\n")
try:
    basket.remove("Myrtilles")
except:
    pass
print(basket,"\n")
print("3-Ajout de 'Kiwi' à la fin de la liste\n")
basket.append("Kiwi")
print(basket,"\n")
print("4-Ajout de 'Pommes' au debut de la liste\n")
basket.insert(0, "Pommes")
print(basket,"\n")
print("5-Compter le nombre de 'Pommes dans le panier\n")
counter =0
for i in basket:
    if i=="Pommes":
        counter=counter+1
print("Le nombre de Pommes dans le panier est: ",counter,".\n")

print("6-Vider le panier\n")
basket.clear()
print("basket=", basket,"\n")

print("EXERCICE 4: Flotteurs")

print("1-Un float est un nombre decimal (un nombre à virgule flottante).\n Tandis qu'un entier ne comporte pas de virgule.\n")
print("2-\n")
print("3-")
liste_nombre=[1.5,2,2.5,3,3.5,4,4.5,5]
print("liste_nombre=",liste_nombre,"\n")

print("EXERCICE 5:Boucle For\n")

print("1-Imprission de tous les nombres de 1 à 20 inclus.\n")
for i in range(1,21):
    print(i)

print("2-Imprission de chaque élément qui a un index pair de 1 à 20 inclus.\n")
valeurs=list(range(1,21))
for i in valeurs:
    if valeurs.index(i)%2==0:
        print(i)
        

print("EXERCICE 6:Boucle While\n")
#Toujours demander le nom utilisateur,a moins que le nom soit egale a mon nom. 
nom=input("Entrer votre nom: ")
while nom.capitalize()!="Simeon".capitalize():
    nom=input("Entrer votre nom: ")
    


print("EXERCICE 7: Fruits Preferes\n")
# 1-
fruits=input("Saisissez ton (tes) fruit(s) prefere(s), laissez des espaces entre les fruits: ")
fruits.lower()
# 2-
liste_fruits=fruits.split(" ")
print("liste_fruits=",liste_fruits)

#3-
fruit=input("Entrer le nom d'un produit: ")
if fruit.lower() in liste_fruits:
    print("Vous avez choisi l'un de vos fruits préférés ! Prendre plaisir!\n")
else:
    print("Vous avez choisi un nouveau fruit. J'espère que tu apprécies !\n")
    
print("EXERCICE 8: Qui A Commander Une Pizza?\n")

garniture=""
sandwich_orders=[]
prix=10
# entrer "quitter" pour quitter le programme
while 1:
    garniture=input("Entrer une garniture de pizza: ")
    if garniture=="quitter":
        break
    else:
        sandwich_orders.append(garniture)
        print("Vous avez ajoute une garniture a notre pizza!")
        prix=prix+2.5
print("liste_garnitures=",sandwich_orders,"\nLe prix total: ",prix,"$\n")


print("EXERCICE 9: Cinema\n")
nombre=int(input("Entrer le nombre de personne de la famille qui veut un billet: "))
prix_billet=j=0

while j < nombre:
    print("Quelle est l'age de la",j+1,"e personne: ")
    age= int(input())
    if age<3: continue
    if 3<=age<12:
        prix_billet+=10
    else:
        prix_billet+=15
        
    j+=1
print("La somme totale a payer pour les billets est: ",prix_billet,"$\n")        
  
liste_adolescants=["Simeon","Richard","David","Victorien","Clement","Dif"]
j=0
while j < len(liste_adolescants):
    print(liste_adolescants[j],"Quel est ton age ?")
    age_adolescant=int(input())
    if age_adolescant not in list(range(16,22)):
        liste_adolescants.remove(liste_adolescants[j])
    j+=1
print("Liste d'adolescants retenue :",liste_adolescants)

 
print("EXERCICE 10: Commanders Sandwich\n")
finished_sandwiches=[]
while sandwich_orders!=[]:
    finished_sandwiche=input("La preparation de quel sandwich est fini: ")

    for sandwich in sandwich_orders:
        if sandwich.lower()==finished_sandwiche.lower():
            finished_sandwiches.append(sandwich)
            sandwich_orders.remove(sandwich)
    print("finished_sandwiches=",finished_sandwiches)
    print("sandwich_orders=",sandwich_orders)
for sandw in finished_sandwiches:
    print("J'ai prepare votre sandwiche ",sandw)
