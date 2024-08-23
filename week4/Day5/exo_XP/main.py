import random
class tictactoe:
    def __init__(self):
        self.picture=[]
        
    def creation_table(self):    
                self.picture.append(["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"]),
                self.picture.append(["*"," "," ","+"," "," ","|"," ","+"," ","|"," "," ","+"," "," ","*"]),
                self.picture.append(["*","-","-","-","-","-","|","-","-","-","|","-","-","-","-","-","*"]),
                self.picture.append(["*"," "," ","+"," "," ","|"," ","+"," ","|"," "," ","+"," "," ","*"]),
                self.picture.append(["*","-","-","-","-","-","|","-","-","-","|","-","-","-","-","-","*"]),
                self.picture.append(["*"," "," ","+"," "," ","|"," ","+"," ","|"," "," ","+"," "," ","*"]),
                self.picture.append(["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"])
                    
   
    def display_board(self):
        for row in self.picture:
            for val in row:
                print(val, end="")
    """        print("")
    tictactoe=tictactoe()
    tictactoe.creation_table()
    tictactoe.display_board() 
    """
    #choisir le joueur qui debutera le jeu         
    def premier_joueur(self):
        return random.randint(0,1)



    def position_joueur(self,ro,col,joueur):
        picture[ro][col]=joueur
            
    def swap_player_turn(self,joueur):
        return 'X' if player == 'O' else 'O'
    #check_win():
        
        


    def play():
        self.creation_table()
        joueur = 'X' if self.premier_joueur() == 1 else 'O'
        while True:
            print(f"Player {joueur} turn")
            self.display_board()
            # taking user input
            ro = int(input("Enter row  numbers to fix spot: "))
            col =int(input("Enter column numbers to fix spot: "))
            print()
                
            # fixing the spot
            self.position_joueur(ro,col+2,joueur)
            joueur=self.swap_player_turn(joueur)
        print()
        self.display_board()
            
tictacto=tictactoe()
tictacto.play()


