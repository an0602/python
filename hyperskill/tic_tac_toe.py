###################################
# Ayaz Noor
# This is a tic-tac-toe-game
# THe game starts with a blank board.  This is a two-player game, where one player determines 'X,'
# and the other player determines'O.'  The game ends when a winning combination occurs, or else the game
# is a draw

# define variables
player_turn = True # 0 stands for "O", and 1 stands for "X" for turns. X goes first 
first_row = [" ", " ", " "]
second_row = [" ", " ", " "]
third_row = [" ", " ", " "]

game_grid = [first_row, second_row, third_row]

#function generates game grid with X and O values filled in
def print_grid():
    print("---------")
    print("| {} {} {} |".format(game_grid[0][0], game_grid[0][1], game_grid[0][2]))
    print("| {} {} {} |".format(game_grid[1][0], game_grid[1][1], game_grid[1][2]))
    print("| {} {} {} |".format(game_grid[2][0], game_grid[2][1], game_grid[2][2]))
    print("---------")

#checks for horizontal, vertical, and diagonal win states    
def determine_winner(game_grid):
    # check game states: X wins and O wins
    for x in range(3):
        if len(game_grid[x]) == 3 and "O" not in game_grid[x] and " " not in game_grid[x]:
            print(len(game_grid[x]))
            print("X wins")
            quit()
        elif len(game_grid[x]) == 3 and "X" not in game_grid[x] and " " not in game_grid[x]:
            print("O wins")
            quit()
        for y in range(3):
            vertical_column = [game_grid[y][x] for y in range(len(game_grid[y]))]
            if len(vertical_column) == 3 and "O" not in vertical_column and " " not in vertical_column:
                print("X wins")
                quit()
            elif len(vertical_column) == 3 and "X" not in vertical_column and " " not in vertical_column:
                print("O wins")
                quit()
                    
    diagonal_downward = game_grid[0][0] + game_grid[1][1] + game_grid[2][2]
    diagonal_upward = game_grid[2][0] + game_grid[1][1] + game_grid[0][2]
    if len(diagonal_downward) == 3 and "O" not in diagonal_downward and " " not in diagonal_downward:
        print("X wins")
        quit()
    elif len(diagonal_downward) == 3 and "X" not in diagonal_downward and " " not in diagonal_downward:
        print("O wins")
    elif len(diagonal_upward) == 3 and "O" not in diagonal_upward and " " not in diagonal_upward:
        print("X wins")
        quit()
    elif len(diagonal_upward) == 3 and "X" not in diagonal_upward and " " not in diagonal_upward:
        print("O wins")
        quit()

#checks for draw game state    
def draw_game(game_grid):
    first_row = game_grid[0]
    second_row = game_grid[1]
    third_row = game_grid[2]
    
    first_row = ["" if x == " " else x for x in first_row]
    second_row = ["" if x == " " else x for x in second_row]
    third_row = ["" if x == " " else x for x in third_row]

    
    if "" not in first_row and "" not in second_row and "" not in third_row:
        print("Draw")
        quit()
    

print_grid()

while True:
    x_coord, y_coord = input("Enter the coordinates: ").split()
    
    #check if user enters numbers or not
    try:
        x_coord = int(x_coord) - 1
        y_coord = int(y_coord) - 1
    except ValueError:
        print("You should enter numbers!")
        continue

    if not(0 <= x_coord <= 2 and 0 <= y_coord <= 2):
        print("Coordinates should be from 1 to 3!")
        continue        

    if game_grid[x_coord][y_coord] != " ":
        print("This cell is occupied! Choose another one!")
        continue
    else:
        if player_turn == True:
            game_grid[x_coord][y_coord] = "X"
            player_turn = not(player_turn)
            print_grid()
            determine_winner(game_grid)
            draw_game(game_grid)
        else:
            game_grid[x_coord][y_coord] = "O"
            player_turn = not(player_turn)
            print_grid()
            determine_winner(game_grid)
            draw_game(game_grid)