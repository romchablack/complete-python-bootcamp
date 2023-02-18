availale_range = list(range(1, 10))


board = [
    (7, 8, 9), 
    (4, 5, 6), 
    (1, 2, 3)
    ]


def check_winner(board):
    get_winner = False
    continue_check = True
    winner = 0

    while winner == 0 or continue_check == True:
        
        # CHECK ROWS 
        for i in range(len(board)):
            if board[i] == ["X"]*3:
                winner = 1
                get_winner = True
                break
            elif board[i] == ["O"]*3:
                winner = 2
                get_winner = True
                break
            else:
                continue

        # CHECK DIAGONAL
        new_list = [board[y][y] for y in range(len(board))]
        if new_list == ["X"]*3:
            winner = 1
            get_winner = True
            break
        elif new_list == ["O"]*3:
            winner = 2
            get_winner = True
            break

        # ROTATE THE BOARD
        board = list(zip(*board[::-1]))
    
        for i in range(len(board)):
            if board[i] == ["X"]*3:
                winner = 1
                get_winner = True
                break
            elif board[i] == ["O"]*3:
                winner = 2
                get_winner = True
                break
        # CHECK DIAGONAL
        new_list = [board[y][y] for y in range(len(board))]
        if new_list == ["X"]*3:
            winner = 1
            get_winner = True
            break
        elif new_list == ["O"]*3:
            winner = 2
            get_winner = True
            break
        
        continue_check = False
        
    return winner
    

board_current = [
    [" ", " ", " "], 
    [" ", " ", " "], 
    [" ", " ", " "]
    ]
    
board = [
    ["X", "0", "X"], 
    ["X", " ", "X"], 
    [" ", "X", "X"]
    ]

check_winner(board)


    


board = [
    [7, 8, 9], 
    [4, 5, 6], 
    [1, 2, 3]
    ]

board_current = [
    [" ", " ", " "], 
    [" ", " ", " "], 
    [" ", " ", " "]
    ]


availale_range = list(range(1, 10))


win = False


def check_win():
    for i in range(len(board)):
        if board[i][i] == board[i][i+1] and board[i][i] == board[i][i+2]

