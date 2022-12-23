print("EXERCICE 1 : Hello world-J'aime python\n")

i=0
while i<4:
    print("Hello world")
    i+=1
    
i=0
while i<4:
    print("I love python")
    i+=1
print()

print("EXERCICE 2 : Quelle est la saison ?\n")

printemps=["mars","avril","mai"]
ete=["juin","juillet","août"]
automne=["septembre","octobre","novembre"]
hiver=["decembre","janvier","fevrier"]
mois=input("Entrer le mois pour connaitre la saison: ").lower()
if mois in printemps:
    print("Nous sommes au PRINTEMPS")
elif mois in ete:
    print("Nous sommes en ETE")
elif mois in automne:
    print("Nous sommes en AUTOMNE")
elif mois in hiver:
    print("Nous sommes en HIVER")

