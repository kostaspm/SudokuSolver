board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_next(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return i, j
    return None


def check_rows(bo, row, num):
    for i in range(len(bo)):
        if bo[row][i] == num:
            return False
    return True


def check_columns(bo, col, num):
    for i in range(len(bo)):
        if bo[i][col] == num:
            return False
    return True


def check_boxes(bo, row, col, num):
    x_box = col // 3
    y_box = row // 3
    for i in range(y_box * 3, y_box * 3 + 3):
        for j in range(x_box * 3, x_box * 3 + 3):
            if bo[i][j] == num:
                return False
    return True


def check_position(bo, row, col, num):
    if check_rows(bo, row, num) and check_columns(bo, col, num) and check_boxes(bo, row, col, num):
        return True


def solve(bo):
    find = find_next(bo)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if check_position(bo, row, col, num):
            bo[row][col] = num
            if solve(bo):
                return True
            bo[row][col] = 0

    return False


if __name__ == "__main__":
    print_board(board)
    solve(board)
    print("-----------------------------")
    print_board(board)
