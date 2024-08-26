from random import randint

board = [] #board is an empty list

for x in range(5):
  board.append(["O"] * 5)   #board contains 5 empty rows and columns

def print_board(board):
  for row in board:
    print(" ".join(row)) #remove unnecessary " " and []

print_board(board) #prints empty board and shows start of game

#computer chooses a random number between 0 and 4 to determine the row and column \
#signifying where the ship is located
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#loop to start the game
for turn in range(4):
  print("Turn", turn + 1)
  guess_row = (input("Guess Row 1-4: "))    #coordinates between 1 and 4
  guess_col = (input("Guess Col 1-4: "))

  if not guess_row.isdigit() and not guess_col.isdigit():   #this prints if theres an invalid input
    print("Please enter coordinates 1-4")
  else:
    guess_row = int(guess_row)
    guess_col = int(guess_col)

    if guess_row == ship_row and guess_col == ship_col:     #if the guess is correct
      print("Congratulations! You sunk my battleship!")
      break
    else:
      if guess_row not in list(range(5)) or guess_col not in list(range(5)):    #if the guess is 5 or greater
        print("Oops, that's not even in the ocean.")
      elif(board[guess_row][guess_col] == "X"):     #if the guess is similar to the previous guess
        print("You guessed that one already.")
      else:
        print("You missed my battleship!")  #if the guess misses the battleship
        board[guess_row][guess_col] = "X"
  if turn == 3:         #you get 4 turns to sink the ship
    print("Game Over")
  else:
      print_board(board)



