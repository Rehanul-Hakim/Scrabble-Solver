def solve_board(game_board):
    find = find_empty(game_board)  # Finds an empty space on board
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if check_valid_board(game_board, i, (row, col)):  # Inserts a number 1-9 on empty space
            game_board[row][col] = i
            if solve_board(game_board):
                return True
            game_board[row][col] = 0
    return False


def check_valid_board(game_board, num, position):
    # Check row
    for i in range(len(game_board)):
        if game_board[position[0]][i] == num and position[1] != i:
            return False

    # Check column
    for i in range(len(game_board)):
        if game_board[i][position[1]] == num and position[0] != i:
            return False

    # Check box
    x_pos = position[1] // 3
    y_pos = position[0] // 3

    for i in range(y_pos * 3, y_pos * 3 + 3):
        for j in range(x_pos * 3, x_pos * 3 + 3):
            if game_board[i][j] == num and (i, j) != position:
                return False

    return True


def print_board(game_board):
    for i in range(len(game_board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")

        for j in range(len(game_board)):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(str(game_board[i][j]))
            else:
                print(str(game_board[i][j]) + " ", end="")


def find_empty(game_board):  # Find empty space on board
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == 0:
                return i, j  # row, column
    return None
