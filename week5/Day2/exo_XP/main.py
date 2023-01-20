#EXERCICE 1:

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
#1
class Siamese(Cat):
    def sing(self,sounds):
        return f'{sounds}'
    
#2
bengal=Bengal('Rex',5)
chartreux=Chartreux('Rio',10)
siamese=Siamese('Rufus',15)

all_cats=[bengal, siamese,chartreux]

#3
sara_pets=Pets(all_cats)
#4
sara_pets.walk()


#EXERCICE 2:

#1
class Dog:
    def __init__(self,dog_name,age,weight):
        self.dog_name = dog_name
        self.age = age
        self.weight = weight
#2    
    def bark(self):
        print(f"{self.dog_name} is barking")
        
    def run_speed(self):
        return (self.weight/self.age*10)

    #other_dog=Dog() 
    def fight(self,other_dog):
        if self.run_speed()<other_dog.run_speed():
            print(f"The winner is {other_dog.dog_name}")
        elif self.run_speed()>other_dog.run_speed():
            print(f"The winner is {self.dog_name}")
        else:
            print(f"Draw fight between {other_dog.dog_name} and {self.dog_name}")

#3

other_dog=Dog("Rio",15,15)
print()
bengal=Dog("Rufous",15,15)
chartreux=Dog("Rex",9,20)

bengal.fight(other_dog)
chartreux.fight(other_dog)

#EXERCICE 3:
#1
#import EXERCICE2 si l'exercice2 etait un fichier python hors d'ici
class Dog:
    def __init__(self,dog_name,age,weight):
        self.dog_name = dog_name
        self.age = age
        self.weight = weight
    def bark(self):
        print(f"{self.dog_name} is barking")
#2
class petDog(Dog):
#3
    def __init__(self,dog_name,age,weight,trained):
        Dog.__init__(self,dog_name,age,weight)
        self.trained = False
#4
    def train(self):
        self.bark()
        self.trained = True
           
#bengal=petDog("Rufous",15,15,True)
#bengal.train()

    def play(self,*args):
        for arg in args:
            print(arg,end=" ")
        print("all play together")
            
#dog=petDog("","","","")
#dog.play("Rio ","Rex","Zo","Rufous")  

    def do_a_trick(self):
        import random
        phrases=["fait un tonneau","se dresse sur ses pattes","te serre la main","fait la mort"]
        random.shuffle(phrases)
        print(f"{self.dog_name} {phrases[0]}")

bengal=petDog("Rufous",15,15,True)
bengal.do_a_trick()
        