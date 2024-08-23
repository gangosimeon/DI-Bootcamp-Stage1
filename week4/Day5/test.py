        
picture=[
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*"," "," ","+"," "," ","|"," ","+"," ","|"," "," ","+"," "," ","*"],
        ["*","-","-","-","-","-","|","-","-","-","|","-","-","-","-","-","*"],
        ["*"," "," ","+"," "," ","|"," ","+"," ","|"," "," ","+"," "," ","*"],
        ["*","-","-","-","-","-","|","-","-","-","|","-","-","-","-","-","*"],
        ["*"," "," ","+"," "," ","|"," ","+"," ","|"," "," ","+"," "," ","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"]
        ]
print(len(picture))
"""
picture=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,"11",0,0,2,0,"12",0,2,0,0,"13",0,0,1],
        [1,3,3,3,3,3,2,3,3,3,2,3,3,3,3,3,1],
        [1,0,0,"21",0,0,2,0,"22",0,2,0,0,"23",0,0,1],
        [1,3,3,3,3,3,2,3,3,3,2,3,3,3,3,3,1],
        [1,0,0,"31",0,0,2,0,"32",0,2,0,0,"33",0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]

i=0
while i<9:
    ro=input("Enter row: ")
    col=input("Enter column: ")
    joueur=input("Enter joueur: ") 

    vali=ro+col
    for row in picture:
        for val in row:
            if val==1:
                print("*",end='')
            elif val==0:
                print(" ",end='')
            elif val==2:
                print("|",end='')
            elif val==3:
                print("-",end='')
            elif int(val)==int(vali):
                print(joueur,end='')
            elif int(val)==int(vali):
                print(joueur,end='')
            elif int(val)==int(vali):
                print(joueur,end='')
            elif int(val)==int(vali):
                print(joueur,end='')
            elif int(val)==int(vali):
                print(joueur,end='')
            elif int(val)==int(vali):
                print(joueur,end='')
            elif int(val)==int(vali):
                print(joueur,end='')
            elif int(val)==int(vali):
                print(joueur,end='')
            elif int(val)==int(vali):
                print(joueur,end='')    
            else:
                print(" ",end='')
        print()
    i+=1 
"""       