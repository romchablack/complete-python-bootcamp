board_default = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

board_current = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

availale_range = list(range(1, 10))

game_on = True


# PRINT CLEAR BOARD AS EXAMPLE
def print_default_board():
    print("The default board is: ")
    for i in board_default:
        print(i)
    print("\n")


# PRINT CURRENT BOARD
def print_current_board():
    print("The current board is: ")
    for i in board_current:
        print(i)
    print("\n")


# SELECT FIRST PLAYER
def start_game():
    is_digit = False
    is_in_range = False
    availale_range = [1, 2]
    while is_digit == False or is_in_range == False:
        player = input(
            "Who start? Player 1 or Player 2 (enter 1 or 2): "
            )
        if player.isdigit():
            is_digit = True
            if int(player) in availale_range:
                is_in_range = True
                player = int(player)
                return player
            else:
                print("Please enter value from range (1 or 2)")
        else:
            print("Please enter valid INT value")


# SELECT NEXT PLAYER
def who_is_next(player):
    if player == 1:
        player = 2
    else:
        player = 1
    print(f"The next move is Player_{player}.")
    return player


# SELECT MOVE
def select_move(availale_range):
    is_digit = False
    is_in_range = False
    while is_digit == False or is_in_range == False:
        # print_current_board()
        choice = input(f"Enter value from available range {availale_range}: ")
        # print(choice)
        if choice.isdigit():
            is_digit = True
            if int(choice) in availale_range:
                is_in_range = True
                availale_range.pop(availale_range.index(int(choice)))
                return int(choice)
            else:
                print(f"Please enter value from range: {availale_range}")
        else:
            print(f"Please enter INT value from {availale_range}")


# PUT ON BOARD
def add_selected_option(player_move, player):
    for i in range(len(board_default)):
        for y in range(len(board_default[i])):
            if board_default[i][y] == player_move:
                if player == 1:
                    board_current[i][y] = "X"
                else:
                    board_current[i][y] = "O"
                return board_current


player = start_game()
print_default_board()
print(f"Player_{player} starts the game.")

while game_on:
    if len(availale_range) > 0:
        move = select_move(availale_range)
        add_selected_option(move, player)
        print_current_board()
        player = who_is_next(player)
    else:
        replay = input("The game is over. \nDo you want to play another game? (Y or N): ")
        if replay in ["y", "Y", "yes", "Yes", "YES"]:
            print("NEW GAME!!!")

        else:
            game_on = False
            print("Game over.")
