import random

def create_board():
    return [["~"] * 5 for _ in range(5)]

def print_board(board):
    for row in board:
        print(" ".join(row))

def place_battleship():
    return random.randint(0, 4), random.randint(0, 4)

def play_game():
    print("Welcome to Battleship!")
    board = create_board()
    ship_row, ship_col = place_battleship()
    attempts = 5 
    
    while attempts > 0:
        print("\nYour Board:")
        print_board(board)
        print(f"Remaining attempts: {attempts}")
        
        try:
            guess_row = int(input("Guess Row (0-4): "))
            guess_col = int(input("Guess Column (0-4): "))
        except ValueError:
            print("Invalid input! Enter numbers between 0 and 4.")
            continue

     
        if 0 <= guess_row < 5 and 0 <= guess_col < 5:
            if guess_row == ship_row and guess_col == ship_col:
                print("Congratulations! You sunk the battleship!")
                break
            elif board[guess_row][guess_col] == "X":
                print("You already guessed that spot.")
            else:
                print("Miss!")
                board[guess_row][guess_col] = "X"
                attempts -= 1
        else:
            print("Out of bounds! Try again.")
    
    if attempts == 0:
        print("Game over! You ran out of attempts.")
        print(f"The battleship was at ({ship_row}, {ship_col}).")


if _name_ == "_main_":
    play_game()