import random
class TicTacToe:
    
    def __init__(self):
        self.board = []

    def creer_table_jeu(self):
        self.board.append(["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"]),
        self.board.append(["*"," "," "," "," "," ","|"," "," "," ","|"," "," "," "," "," ","*"]),
        self.board.append(["*","-","-","-","-","-","|","-","-","-","|","-","-","-","-","-","*"]),
        self.board.append(["*"," "," "," "," "," ","|"," "," "," ","|"," "," "," "," "," ","*"]),
        self.board.append(["*","-","-","-","-","-","|","-","-","-","|","-","-","-","-","-","*"]),
        self.board.append(["*"," "," "," "," "," ","|"," "," "," ","|"," "," "," "," "," ","*"]),
        self.board.append(["*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*","*"])
                    

    def random_premier_joueur(self):
        return random.randint(0, 1)

    def placer_pillon(self, row, col, player):
        self.board[row][col] = player

    def check_win(self,player):
        win = None
 
        n = len(self.board)

        # checking rows
        for i in range(1,n,2):
            win = True
            for j in range(3,18,5):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win
        
        # checking columns
        for i in range(3,18,5):
            win = True
            for j in range(1,n,2):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
        
        # checking diagonals
        win = True
        i=1
        j=3
        while i<n and j <18:
            if self.board[i][j] != player:
                win = False
                break
            i+=2
            j+=5
        if win:
            return win

        win = True
        i=1
        j=13
        while i<n and j>0:
            if self.board[i][j] != player:
                win = False
                break
            i+=2
            j-=5
        if win:
            return win
        return False
        
        
        for row in self.board:
            for item in row:
                if item == ' ':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == ' ':
                    return False
        return True
    
    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def affiche_table_jeu(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.creer_table_jeu()

        player = 'X' if self.random_premier_joueur() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.affiche_table_jeu()

            # taking user input
            row = int(input("Enter row : "))
            col = int(input("Enter column : "))
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

            # fixing the spot
            self.placer_pillon(row, col, player)
            
            # checking whether current player is won or not
            if self.check_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break
            
            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.affiche_table_jeu()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()