#EXERCICE1

#1/
class Family:
    members=[{'last_name':'Michael','first_name':'Zongo','age':35,'gender':'Male','is_child':False},
    {'last_name':'Sarah','first_name':'Kabore','age':32,'gender':'Female','is_child':False}]

    def __init__(self,fisrt_name:str,last_name:str,age:int,gender:str,is_child:bool):
        self.first_name=fisrt_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.is_child=is_child

#2/   
       
    def born(self,**kargs):
        self.members.append(kargs)
        print(self.members)
        print("Felicitations à la famille!!!")
        
#family=Family("","","","","")
#family.born(last_name="Simeon",first_name="Zongo",age=10,gender="Male",is_child=True)
#family.born(last_name="Germaine",first_name="Zongo",age=15,gender="Female",is_child=True)

    def is_18(self,last_name):
        for member in self.members:
            if member["last_name"]==last_name and member["age"]>18:
                return True
            elif member["last_name"]==last_name and member["age"]<=18:
                return False   

#family=Family("","","","","")
#print(family.is_18("Sarah"))
#print(family.is_18("Simeon"))


    def family_presentation(self):
        for member in self.members:
            print(member["first_name"], member["last_name"])
#family=Family("","","","","") 
#family.family_presentation()
  
  
  
#TEST GENERAL
family=Family("","","","","")
family.born(last_name="Simeon",first_name="Zongo",age=10,gender="Male",is_child=True)
print()
family.born(last_name="Germaine",first_name="Zongo",age=15,gender="Female",is_child=True)
print()
family=Family("","","","","")
print(family.is_18("Sarah"))
print(family.is_18("Simeon"))

print()
    
#family=Family("","","","","")
#family.family_presentation()


#EXERCICE 2
#importattion de la classe parent
class Family:
    def __init__(self,fisrt_name:str,last_name:str,age:int,gender:str,is_child:bool):
        self.first_name=fisrt_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.is_child=is_child  
       
    def born(self,**kargs):
        self.members.append(kargs)
        print(self.members)
        print("Felicitations à la famille!!!")
        
    def is_18(self,last_name):
        for member in self.members:
            if member["last_name"]==last_name and member["age"]>18:
                return True
            elif member["last_name"]==last_name and member["age"]<=18:
                return False

    def family_presentation(self):
        for member in self.members:
            print(member["first_name"], member["last_name"])
#1/
class TheIncredibles(Family):
    members=[{'last_name':'Michael','first_name':'Zongo','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'last_name':'Sarah','first_name':'Kabore','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}]

    def __init__init__(self,fisrt_name:str,last_name:str,age:int,gender:str,is_child:bool,power:str,incredible_name:str):
        Family.__init__(self,fisrt_name,last_name,age,gender,is_child)
        self.power=power
        self.incredible_name=incredible_name
        
#2/
    def use_power(self,last_name):
        for member in self.members:
            if member["last_name"]==last_name and member["age"]>18:
                print(f"{member['first_name']} {member['last_name']} power is {member['power']}.")
            elif member["last_name"]==last_name and member["age"]<=18:
                print(f"{member['first_name']} {member['last_name']} is not over 18 years old")
                
#member=TheIncredibles("","","","","")
#member.use_power("Sarah")
         
         
    def incredible_presentation(self):
        super().family_presentation()
        print("These are all the members' power and incredible name: ")
        for member in self.members:
            print("power: ",member['power'],",","Incredible name: ",member['incredible_name'])

#4/       
member=TheIncredibles("","","","","")
member.incredible_presentation()

#5/
family=TheIncredibles("","","","","")
family.born(last_name="Jack",first_name="Zongo",age=10,gender="Male",is_child=True,power="UnknownPower",incredible_name="")
#6
family.incredible_presentation()