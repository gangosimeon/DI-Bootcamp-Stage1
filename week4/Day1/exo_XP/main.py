print("---------------------------------------------------------")
print("EXERCICE 1 : Hello world\n")

print(4*"Hello world \n")

print("---------------------------------------------------------")

print("EXERCICE 2: Quelques Maths\n")
# 1.
print("\nLe resultat de (99^3)*8 = ",(99**3)*8)

print("--------------------------------------------------------")

print("EXERCICE 3: Quelle est la sortie\n")

# 1. Resultat attendu (' ' correspond a " ")
print(" >>>5<3 False\n >>>3==3 True \n >>>3=='3' False\n >>>'3'>3 error \n >>>'Hello'=='hello' False \n")

print("--------------------------------------------------------")

print("EXERCICE 4: Votre marque d'ordinateur\n")

computer_brand="HP celeron"
print("I have a {} as a computer ! \n".format(computer_brand))


print("--------------------------------------------------------")

print(" EXERCICE 5: Vos informations\n")

name="GANGO"
age=24
shoe_size=42
info="Salut a tous ! je m'appelle {}, j'ai {} ans, ma pointure est {} . Je suis passionne par la programmation !\n".format(name , age, shoe_size)
print(info)

print("-------------------------------------------------------")

print("EXERCICE 6: A & B\n")

a=float(input("a = "))
b=float(input("b = "))
if a>b:
    print("Hello world!\n")

print("-------------------------------------------------------")
 
print("EXERCICE 7: Pair ou Impair\n")

a=int(input("Entrer un nombre : "))
if a%2==0:
    print(f"Le nombre {a} est pair .\n")
else:
    print(f"Le nombre {a} est impair .\n")
    
    
print("--------------------------------------------------------")

print("EXERCICE 8: Comment t'appelles-tu ?\n")

nom=input("Comment t'appelles-tu ?\n")
if nom.capitalize()=="simeon".capitalize():
    print("Bravo ! Tres interessant , vous avez le meme nom !\n")
else:
    print("OR , ce serait plus cool si vous avez le meme nom !\n")


print("--------------------------------------------------------")

print("EXERCICE 9: Assez grand pour faire des montages russes\n")

taille=int(input("Quelle est votre taille : "))
if taille>145 :
    print("Vous etes assez grand pour rouler !\n")
else:
    print("Vous devez grandir un peu plus pour rouler !\n")

print("---------------------------------------------------------")