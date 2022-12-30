print("Defi1:")

mot=input("Entrer un mot: ")
dic={}
liste=[]
liste1=list(mot)

for j in range(len(liste1)):
      dic[liste1[j]]=[]
for j in range(len(liste1)):
      if liste1[j] in dic.keys():
         dic[liste1[j]].append(j)       
print(dic)

print("Defi2:")

items_purchase={"water":"$1","Bread":"$3","TV":"$1000 ","Fertilizer":"$20"}
wallet="$10"
liste=[]
for key in items_purchase.keys():
   if items_purchase[key]<=wallet:
      liste.append(key)

if liste!=[]:
   print(sorted(liste))
else:
   print("Nothing")