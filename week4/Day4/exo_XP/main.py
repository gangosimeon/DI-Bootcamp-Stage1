#1-
def display_message():
    print("Bonjour tout le monde , j'apprends a ecrire une fonction en python .")
#Appel de la fonction 
display_message()

#EXERCICE2
def favorite_book(title):
    print(f"L'un de mes livres preferes est {title}")
    
#Appel de la fonction favorite_book
title="Alice au pays des merveilles"
favorite_book(title)

#EXERCICE 3

def describe_city(ville,pays):
    print(f"{ville} est au {pays}")

pays="Bukina Faso"
ville="Ouagadougou"
describe_city(ville,pays)

#EXERCICE 4

def nombre_aleatoire():
    print(random.randint(1,100))
import random
nombre_aleatoire()

#EXERCICE 5
#1;2;3
def make_shirt(taille,texte):
    print(f"la taille de la chemise est {taille} et le texte a imprimer est {texte}")
    
texte="J'aime la programmation !"
taille="M"
make_shirt(taille,texte)

def make_shirt():
    print("la taille de la chemise est XL et le texte a imprimer est J'aime Python")
make_shirt()

#5-
def make_shirt(taille):
    print(f"la taille de la chemise est {taille} et le texte a imprimer est J'aime Python")
make_shirt("XL")

#6-
def make_shirt(taille):
    print(f"la taille de la chemise est {taille} et le texte a imprimer est J'aime Python")
make_shirt("M")
#7-
def make_shirt(taille):
    print(f"la taille de la chemise est {taille} et le texte a imprimer est J'aime Python")
taille=input("entrer la taille du chemise: ")
make_shirt(taille)

#EXERCICE 6
#1;2
def show_magicians(magician_names):
    for magician_name in magician_names:
        print(magician_name)
 #3;4       
def make_great(magician_names):
    magician_names[0]=magician_names[0] +" the Great"
    magician_names[1]=magician_names[1] +" the Great"
    magician_names[2]=magician_names[2] +" the Great"
        
magician_names=['Harry Houdini', 'David Blaine', 'Criss Angel'] 
#appel fonction 1;2
show_magicians(magician_names)
#appel fonction 3;4
make_great(magician_names)       
show_magicians(magician_names)

#EXERCICE 7
#1-
def get_random_temp():
   return random.randint(-10,40)
import random
print(get_random_temp())
print("----------------------------------------------------------")
#2-
def main():
    temp=get_random_temp()
    print(f"La temperature actuelle est de {temp} degres Celsius.")
main()
print("----------------------------------------------------------")
#3-
def main():
    temp=get_random_temp()
    print(f"La temperature actuelle est de {temp} degres Celsius.")
    if temp<0:
        print("Brrr, c'est glacial ! Portez des couches supplémentaires aujourd'hui")
    elif 0<=temp<16:
        print("Assez froid ! N'oubliez pas votre manteau")
    elif 16<=temp<=23:
        print("Il fait froid")
    elif 24<=temp<=32:
        print("Le temps est bonne")
    else:
        print("Il fait legerement chaud")
main()
print("----------------------------------------------------------")
#4-
def get_random_temp(saison):
    if saison.lower()=="hiver":
        temp=random.randint(-10,16)
    elif saison.lower()=="printemps":
        temp=random.randint(16,23)
    elif saison.lower()=="ete":
        temp=random.randint(23,32)
    elif saison.lower()=="automne":
        temp=random.randint(32,40)
    else:
        print("Saison inexistant !")
    print(f"Nous sommes en {saison}, la temperature est {temp} degres celsius.")
saison=input("Quelle est la saison ? >> ")
get_random_temp(saison)
print("----------------------------------------------------------")

#3-
def get_random_temp(saison):
    if saison.lower()=="hiver":
        temp=random.randint(-10,16)
    elif saison.lower()=="printemps":
        temp=random.randint(16,23)
    elif saison.lower()=="ete":
        temp=random.randint(23,32)
    elif saison.lower()=="automne":
        temp=random.randint(32,40)
    return temp

def main():
    temp=get_random_temp(saison)
    print(f"La temperature actuelle est de {temp} degres Celsius.")
    if -10<=temp<16:
        print(f"Nous sommes en {saison},Brrr, c'est glacial ! Portez des couches supplémentaires aujourd'hui")
    elif 16<=temp<=23:
        print(f"Nous sommes en {saison},Il fait froid")
    elif 24<=temp<=32:
        print(f"Nous sommes en {saison},le temps est bonne")
    else:
        print(f"Nous sommes en {saison},Il fait legerement chaud")
saison=input("Quelle est la saison ? >> ")
import random
main()
print("----------------------------------------------------------")
#5-
def get_random_temp(saison):
    if saison.lower()=="hiver":
        temp=random.uniform(-10,16)
    elif saison.lower()=="printemps":
        temp=random.uniform(16,23)
    elif saison.lower()=="ete":
        temp=random.uniform(23,32)
    elif saison.lower()=="automne":
        temp=random.uniform(32,40)
    else:
        print("Saison inexistant !")
    print(f"Nous sommes en {saison}, la temperature est {temp} degres celsius.")
saison=input("Quelle est la saison ? >> ")
get_random_temp(saison)
print("----------------------------------------------------------")
#6-
print("1=janvier 2=fevrier 3=mars 4=avril 5=mai 6=juin 7=juillet 8=août 9=septembre 10=octobre 11=novembre 12=decembre")
numero=int(input("Entrer le numero du mois pour connaitre la saison: "))
if numero==3 or numero==4 or numero==5:
    print("Nous sommes au PRINTEMPS")
elif numero== 6 or numero==7 or numero==8:
    print("Nous sommes en ETE")
elif numero==9 or numero==10 or numero==11:
    print("Nous sommes en AUTOMNE")
elif numero==12 or numero==1 or numero==3:
    print("Nous sommes en HIVER")