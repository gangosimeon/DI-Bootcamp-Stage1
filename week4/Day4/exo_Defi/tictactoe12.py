import random
    
board = []

def creer_table_jeu():
      board.append(["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"]),
      board.append(["*"," "," "," "," "," ","|"," "," "," ","|"," "," "," "," "," ","*"]),
      board.append(["*","-","-","-","-","-","|","-","-","-","|","-","-","-","-","-","*"]),
      board.append(["*"," "," "," "," "," ","|"," "," "," ","|"," "," "," "," "," ","*"]),
      board.append(["*","-","-","-","-","-","|","-","-","-","|","-","-","-","-","-","*"]),
      board.append(["*"," "," "," "," "," ","|"," "," "," ","|"," "," "," "," "," ","*"]),
      board.append(["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"])
                    
def random_premier_joueur():
      return random.randint(0, 1)

def placer_pillon(row, col, player):
      board[row][col] = player
      
 
def gagnant(player):
    win = None

    n = len(board)

    
    for i in range(1,n,2):
        win = True
        for j in range(1,n,2):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win
    
    
    
    for i in range(1,n,2):
        win = True
        for j in range(1,n,2):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win 
    
    
    
    
    # checking diagonals
    
    win = True
    for i in range(1,n,2):
        if board[i][i] != player:
            win = False
            break
    if win:
        return win
        
    
    
    win = True
    for i in range(1,n,2):
        if board[i][n - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False
    

    for row in board:
        for item in row:
            if item ==  ' ':
                return False
    return True
    


def is_board_filled():
      for row in board:
          for item in row:
              if item == ' ':
                  return False
      return True



def swap_player_turn(player):
     return 'X' if player == 'O' else 'O'

def affiche_table_jeu():
      for row in board:
          for item in row:
              print(item, end=" ")
          print()
def user_input():
            
            if row ==1 and col ==1:
                row = 1
                col=3
            elif row ==1 and col ==2:
                row = 1
                col=8
            elif row ==1 and col ==3:
                row = 1
                col=13
            elif row ==2 and col ==1:
                row = 3
                col=3
            elif row ==2 and col ==2:
                row = 3
                col=8
            elif row ==2 and col ==3:
                row = 3
                col=13
            elif row ==3 and col ==1:
                row = 5
                col=3
            elif row ==3 and col ==2:
                row = 5
                col=8
            elif row ==3 and col ==3:
                row = 5
                col=13
            print()

def start():

      player = 'X' if random_premier_joueur() == 1 else 'O'
     
      while True:
            print(f"Player {player} turn")
            creer_table_jeu()
            affiche_table_jeu()

            # taking user input
            row = int(input("Enter row : "))
            col = int(input("Enter column : "))
            user_input()
            # fixing the spot
            """
            while board[row][col] !=" ":
                row = int(input("Enter row : "))
                col = int(input("Enter column : "))
                user_input()
            """
            placer_pillon(row, col, player)
            
            # checking whether current player is won or not
            """
            if is_player_win(player):
                print(f"Player {player} wins the game!")
                break
            """
            # checking whether the game is draw or not
            if is_board_filled():
                print("Match Draw!")
                break
           
            # swapping the turn
            player =swap_player_turn(player)

            # showing the final view of board
            """print()
            affiche_table_jeu()
           """

# starting the game
start()