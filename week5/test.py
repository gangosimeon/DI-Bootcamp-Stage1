def is_18(name):
    for member in members:
        if member["name"]==name and member["age"]>18:
            return True
        elif member["name"]==name and member["age"]<=18:
            return False   
members=[
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}]
print(is_18("Michael"))