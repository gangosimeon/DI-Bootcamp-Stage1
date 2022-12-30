print("EXERCICE 1: Convertir des listes en dictionnaires\n")

keys=["Ten","Twenty","Thirty"]
values=[10,20,30]
dict={}
for key_value in zip(keys,values):
    a,b=key_value #recuperation des keys values include dans le tuple key_value
    dict[a]=b  #stockage des valeurs dans le dictionaire  
print(dict,"\n")

print("EXERCICE 2: Cinema\n")
# 1 , 2 et 3)
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
prix=0
for nom,age in family.items():
    if age <3:
        prix1=0
        prix+=prix1
        print(f"votre billet est gatuit!")
    elif 3<=age<12:
        prix2=10
        prix+=prix2
        print(f" {nom} votre billet est de {prix2}$.\n")
    else:
        prix3=15
        prix+=prix3
        print(f" {nom} votre billet est de {prix3}$.\n")
print("Le coût total de la famille pour les billets est: ",prix)        
# 4-Bonus

dic={}
nbre=int(input("Le nombre de personne dans la famille: "))
while nbre!=0:
    nom=input("Votre nom: ")
    print(f"{nom}, Quel est votre age: ")
    age=int(input())
    dic[nom]=age
    nbre-=1
print(dic)
print()

print("EXERCICE 3: Zara\n")
#2-
brand={"name":"Zara" ,"creation_date":1975,"creator_name":"Amancio Ortega Gaona","type_of_clothes":["men","women","childen","home"],"international_competitors":["Gap","H&M","Benetton"],"number_stores":7000,"major_color":{"France":"blue","Spain":"red","US":["pink","green"]}}
print (brand)
print()
#3-
brand["number_stores"]=2
print (brand)
print()
#4-
print("Vous avez besoin de vetements pour Homme , Femme, enfants, etc 'Vous etes le(la,les) bienvenu(e,s) cher(e)s client(e)s'.")
#5-
brand["country_creation"]="Spain"
print (brand)
print()
#6-
if "international_competitors" in brand.keys():
    liste=brand["international_competitors"]
    liste.append("Designal")
print (brand)
print()
#7-
del brand["creation_date"]
print (brand)
print()
#8-
print(brand["international_competitors"][-1])
print()
#9-
print(brand["major_color"]["US"])
print()
#10-
print("La longueur du dictionnaire est: ",len(brand))
print()
#11-
print("Les cles du dictionnaire sont: ",brand.keys())
print()
#12-
more_on_zara={"creation_date":1975,"number_stores":10000}
#13
brand.update(more_on_zara)
print(brand)
print()
#14-
print(brand["number_stores"])

print("On remarque que la valeur de number_stores a ete modifie a 10000, elle est passee de 2 a 10000 ")


print("EXERCICE 4: Personnages Disney\n")

users=["Mickey", "Minnie","Donald","Ariel","Pluto"]

#1
disney_users_A={}
i=0
for user in users:
    disney_users_A[user]=i
    i+=1
print(disney_users_A)
print()
#2-
disney_users_B={}
i=0
for user in users:
    disney_users_B[i]=user
    i+=1
print(disney_users_B)
print()
#3-
disney_users_C={}
i=0
for user in sorted(users):
    disney_users_C[user]=i
    i+=1
print(disney_users_C)
print()
#4-1
disney_users_A={}
j=0
for user in users:
    if "i" in user.lower():
        disney_users_A[user]=j
        j+=1
print(disney_users_A)
print()
#4-2
disney_users_A={}
j=0
for user in users:
    if "i" in user.lower() or "p" in user.lower():
        disney_users_A[user]=j
        j+=1
print(disney_users_A)
print()