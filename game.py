board_default = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

board_clear = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

available_moves = list(range(1, 10))

game_on = True


# PRINT CLEAR BOARD AS EXAMPLE
def print_default_board(board):
    print("The default board is: ")
    for i in board:
        print(i)
    print("\n")


# PRINT CURRENT BOARD
def print_current_board(board):
    print("The current board is: ")
    for i in board:
        print(i)
    print("\n")


# SELECT FIRST PLAYER
def new_game():
    is_digit = False
    is_in_range = False
    available_moves = [1, 2]
    while is_digit == False or is_in_range == False:
        player = input(
            "Who start? Player 1 or Player 2 (enter 1 or 2): "
            )
        if player.isdigit():
            is_digit = True
            if int(player) in available_moves:
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
def select_position(moves):
    is_digit = False
    is_in_range = False
    while is_digit == False or is_in_range == False:
        # print_current_board()
        choice = input(f"Enter value from available range {moves}: ")
        # print(choice)
        if choice.isdigit():
            is_digit = True
            if int(choice) in moves:
                is_in_range = True
                moves.pop(moves.index(int(choice)))
                return int(choice)
            else:
                print(f"Please enter value from range: {moves}")
        else:
            print(f"Please enter INT value from {moves}")


# PUT ON BOARD
def add_selected_option(player, move, board, board_default):
    for i in range(len(board_default)):
        for y in range(len(board_default[i])):
            if board_default[i][y] == move:
                if player == 1:
                    board[i][y] = "X"
                else:
                    board[i][y] = "O"
                return board


def check_winner(board):
    winner = 0
    # CHECK DIAGONAL
    diagonal = tuple([board[y][y] for y in range(len(board))])
    if diagonal == tuple(["X"]*3):
        winner = 1
        return winner
    elif diagonal == tuple(["O"]*3):
        winner = 2
        return winner
    # CHECK ROWS 
    for i in range(len(board)):
        if board[i] == tuple(["X"]*3):
            winner = 1
            return winner
        elif board[i] == tuple(["O"]*3):
            winner = 2
            return winner
    # ROTATE THE BOARD
    board = list(zip(*board[::-1]))
    # CHECK DIAGONAL
    diagonal = tuple([board[y][y] for y in range(len(board))])
    if diagonal == tuple(["X"]*3):
        winner = 1
        return winner
    elif diagonal == tuple(["O"]*3):
        winner = 2
        return winner
    # CHECK ROWS ROTATED
    for i in range(len(board)):
        if board[i] == tuple(["X"]*3):
            winner = 1
            return winner
        elif board[i] == tuple(["O"]*3):
            winner = 2
            return winner
    return winner


while game_on:
    # newboard
    board = board_clear.copy()
    # define full set of available moves
    moves = available_moves.copy()
    # define first Player
    player = new_game()
    
    winner == 0
    while winner == 0:
        # select move
        position = select_position(moves)
        # add move to the board
        add_selected_option(player, position, board, board_default)
        print_current_board(board)
        winner = check_winner(board)
        if winner == 0:
            player = who_is_next(player)
        else:
            print(f"Player_{winner} won the game.")
            replay = input(
                "The game is over. \nDo you want to play another game? (Y or N): "
                )
            if replay in ["y", "Y", "yes", "Yes", "YES"]:
                print("NEW GAME!!!")
            else:
                print("Thank you for the game. Bye!")
                game_on = False
