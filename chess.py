



      
'''PYTHON CHESS
Created by Parve Palial 23117027,
          Manujuswar kharikar 23117020,
          Sourav Patil 23117033,
          Raj 23117029
'''

print("lower case are black")
print("Upper case are white")
 

print("Enter the positions of start and ending ")

print("Captured pieces disappears")
 
print("Capture the king to win")

print(" ")



class ChessGame:
   def __init__(self):
       self.board = [
           ['8',' ','r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
           ['7',' ','p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
           ['6',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           ['5',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           ['4',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           ['3',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           ['2',' ','P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
           ['1',' ','R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
           [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ',' ','a', 'b', 'c','d', 'e', 'f', 'g', 'h']
       ]
       self.current_player = 'white'

   def print_board(self):
       for row in self.board:
           print(' '.join(row))

   def is_valid_move(self, start, end):
       start_row, start_col = start
       end_row, end_col = end

       # Check if end position is within the board
       if not (2 <= end_row < 10 and 2 <= end_col < 10):
           return False

       # Check if there is a piece at the start position
       if self.board[start_row][start_col] == ' ':
           return False

       # Check if the piece belongs to the current player
       if (self.current_player == 'white' and self.board[start_row][start_col].islower()) or \
          (self.current_player == 'black' and self.board[start_row][start_col].isupper()):
           return False

       # Check if the end position contains a friendly piece
       if (self.current_player == 'white' and self.board[end_row][end_col].isupper()) or \
          (self.current_player == 'black' and self.board[end_row][end_col].islower()):
           return False

       # Check specific piece rules
       piece = self.board[start_row][start_col].lower()

       # Pawn
       if piece == 'p':
           # Basic movement
           if start_col == end_col and self.board[end_row][end_col] == ' ':
               if (self.current_player == 'white' and end_row == start_row - 1 or (end_row == start_row - 2 and start_row==6)) or \
                  (self.current_player == 'black' and end_row == start_row + 1 or (end_row == start_row + 2 and start_row==1)):
                   return True
              
           # Capture
           elif abs(start_col - end_col) == 1 and end_row == start_row + (-1 if self.current_player == 'white' else 1):
               if self.board[end_row][end_col] != ' ' and \
                  ((self.current_player == 'white' and self.board[end_row][end_col].islower()) or \
                   (self.current_player == 'black' and self.board[end_row][end_col].isupper())):
                   return True
           return False

       # Rook
       elif piece == 'r':
           if start_row == end_row or start_col == end_col:
               flag = True
               if self.current_player == "white":
                   s = start_row
                   e = end_row
               else:
                   s = end_row
                   e = start_row
                  
               for i in range(s, e+1):
                   if self.board[i][end_col] != ' ' and start_col==end_col:
                       flag = False
               for i in range(s, e+1):
                   if self.board[end_row][i] != ' ' and start_row==end_row:
                       flag = False
              
               if flag == True:
                   return True
              
           #Capture
           if self.board[end_row][end_col] != ' ' and \
                  ((self.current_player == 'white' and self.board[end_row][end_col].islower()) or \
                   (self.current_player == 'black' and self.board[end_row][end_col].isupper())):
                   return True
              
           return False

       # Knight
       elif piece == 'n':
           if (abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1) or \
              (abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2):
               return True
              
      
           #Capture
           if self.board[end_row][end_col] != ' ' and \
                  ((self.current_player == 'white' and self.board[end_row][end_col].islower()) or \
                   (self.current_player == 'black' and self.board[end_row][end_col].isupper())):
                   return True
           return False


       # BISHOP
       if piece.lower() == "b":
           if abs(start_row - end_row) == abs(start_col - end_col):
               if start_row < end_row:
                   row_dir = 1
               else:
                   row_dir = -1
               if start_col < end_col:
                   col_dir = 1
               else:
                   col_dir = -1
               row = start_row + row_dir
               col = start_col + col_dir
               while row != end_row:
                   if self.board[row][col] != " ":
                       return False
                   row += row_dir
                   col += col_dir
               return True
            #Capture
           if self.board[end_row][end_col] != ' ' and \
                  ((self.current_player == 'white' and self.board[end_row][end_col].islower()) or \
                   (self.current_player == 'black' and self.board[end_row][end_col].isupper())):
                   return True


           return False
      
       if piece.lower() == "q":
           if start_row == end_row or start_col == end_col or abs(start_row - end_row) == abs(start_col - end_col):
               row_dir = (0 if start_row == end_row else (1 if start_row < end_row else -1))
               col_dir = (0 if start_col == end_col else (1 if start_col < end_col else -1))
               row = start_row + row_dir
               col = start_col + col_dir
               while row != end_row or col != end_col:
                   if self.board[row][col] != " " and (row != end_row or col != end_col):
                       return False
                   row += row_dir
                   col += col_dir
            #Capture
           if self.board[end_row][end_col] != ' ' and \
                  ((self.current_player == 'white' and self.board[end_row][end_col].islower()) or \
                   (self.current_player == 'black' and self.board[end_row][end_col].isupper())):
                   return True
           return True
          
       if piece.lower() == "k":
           if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
               return True
           #Capture
           if self.board[end_row][end_col] != ' ' and \
                  ((self.current_player == 'white' and self.board[end_row][end_col].islower()) or \
                   (self.current_player == 'black' and self.board[end_row][end_col].isupper())):
                   return True
      
       return False

   def move_piece(self, start, end):
       if self.is_valid_move(start, end):
           start_row, start_col = start
           end_row, end_col = end
           self.board[end_row][end_col] = self.board[start_row][start_col]
           self.board[start_row][start_col] = ' '

  
   def play(self):
       while True:
           self.print_board()
           print(f"{self.current_player}'s turn")

          
           starts = input("Enter start position (col row): ").split()
           t = starts[1]
           starts[1]= int(ord(starts[0]))-95
           starts[0]= 8-int(t)
          
           start = tuple(starts)
            
           ends = input("Enter end position (col row): ").split()
           t = ends[1]
           ends[1]= int(ord(ends[0]))-95
           ends[0]= 8-int(t)
          
           end = tuple(ends)
          
          
           if self.is_valid_move(start, end):
               self.move_piece(start, end)
               self.current_player = 'black' if self.current_player == 'white' else 'white'
           else:
               print("Invalid move. Try again.")
              
           total = [j for i in self.board for j in i]
          
           if 'K' not in total:
               print("BLACK WON THE GAME")
               break
           if 'k' not in total:
               print("WHITE WON THE GAME")
               break
         

if __name__ == "__main__":
   game = ChessGame()
   game.play()

'''
Gameplay

lower case are black
Upper case are white
 

Enter the positions of start and ending
 




Captured pieces disappears
 
Capture the king to win
'''