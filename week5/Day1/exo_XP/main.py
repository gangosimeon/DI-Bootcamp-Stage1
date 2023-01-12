#EXERCICE 1:
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

#1
Us_Cat=Cat("Bengal",5)
Turc_Cat=Cat("Anatoli",3)
Fr_Cat=Cat("Chartreux",8)
#Afr_Cat=Cat("Queeny",12)

#2
def ancien_Chat(dico_chats):
   for age in dico_chats.keys():
       if age==max(dico_chats.keys()):
           return dico_chats[age]
       
dico_chats ={Us_Cat.age:Us_Cat.name,Turc_Cat.age:Turc_Cat.name,Fr_Cat.age:Fr_Cat.name}
#dico_chats[Afr_Cat.age] =Afr_Cat.name
print(f"Le chat le plus âgé est {ancien_Chat(dico_chats)} et a {max(dico_chats.keys())} ans.")

#EXERCICE 2:

#1
class Dog:
#2
    def __init__(self, name,height):
        self.name = name
        self.height = height
#3
    def bark(self):
        print(f"{self.name} va woof!")
#4 
    def jump(self):
        print(f"{self.name} saute {self.height*2} cm de haut !")
#5 
davids_dog=Dog("Rex",50)
#6
davids_dog.bark()
davids_dog.jump()
#7
sarahs_dog=Dog("Teacup",20)
#8
sarahs_dog.bark()
sarahs_dog.jump()
#9
if sarahs_dog.height<davids_dog.height:
    big=davids_dog.name
else:
    big=sarahs_dog.name

print(f"Le plus gros est : {big}.")


#EXERCICE 3

#1
class Song:
#2
    def __init__(self,lyrics=[]):
        self.lyrics =lyrics
#3     
    def sing_me_a_song(self):
        for song in self.lyrics:
            print(song)
#4
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

