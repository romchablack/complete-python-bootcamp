board_default = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

available_moves = list(range(1, 10))

game_on = True

def print_current_board(board):
    for i in board:
        print(i)
    print("\n")

def new_game():
    available_moves = [1, 2]
    player = int(input("Who start? Player 1 or Player 2 (enter 1 or 2): "))
    return player

def who_is_next(player):
    if player == 1:
        player = 2
    else:
        player = 1
    print(f"The next move is Player_{player}.")
    return player

def select_position(moves):
    choice = input(f"Enter value from available range {moves}: ")
    if int(choice) in moves:
        moves.pop(moves.index(int(choice)))
    return int(choice)

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
    diagonal = tuple([board[y][y] for y in range(len(board))])
    if diagonal == tuple(["X"]*3):
        winner = 1
        return winner
    elif diagonal == tuple(["O"]*3):
        winner = 2
        return winner
    for i in range(len(board)):
        if board[i] == tuple(["X"]*3):
            winner = 1
            return winner
        elif board[i] == tuple(["O"]*3):
            winner = 2
            return winner
    board = list(zip(*board[::-1]))
    diagonal = tuple([board[y][y] for y in range(len(board))])
    if diagonal == tuple(["X"]*3):
        winner = 1
        return winner
    elif diagonal == tuple(["O"]*3):
        winner = 2
        return winner
    for i in range(len(board)):
        if board[i] == tuple(["X"]*3):
            winner = 1
            return winner
        elif board[i] == tuple(["O"]*3):
            winner = 2
            return winner
    return winner

while game_on:
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    moves = available_moves.copy()
    player = new_game()
    winner = 0
    while winner == 0:
        position = select_position(moves)
        add_selected_option(player, position, board, board_default)
        print_current_board(board)
        winner = check_winner(board)
        if winner == 0:
            player = who_is_next(player)
        else:
            print(f"Player_{winner} won the game.")
            replay = input(
                "AGAIN? (Y or N): "
                )
            if replay in ["Y"]:
                print("NEW")
                break
            else:
                game_on = False
                print("Bye!")
