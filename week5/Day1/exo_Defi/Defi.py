class Farm:
    def __init__(self,owner_name):
        self.owner_name=owner_name
        self.farm_animals=[]
    def add_animal(self,animal,*args):
        self.farm_animals.append(animal)
        nb=int(*args)-1
        while nb>0 :
            self.farm_animals.append(animal)
            nb-=1
    def get_info(self):
        dic={}
        print(f"{self.owner_name}'s Farm")
        print()
        for animal in self.farm_animals:
            if animal not in dic:
                dic[animal]=self.farm_animals.count(animal)
        for key , value in dic.items():
            print(f"{key}:  {value}")
        print()
        return "\tE-I-E-I-0!"
            
       
 
 

"""
mc=Farm("Cd")
mc.add_animal("mouton")
mc.add_animal("cabri",5)
mc.add_animal("mouton",6)
mc.add_animal("cabri")
"""

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())