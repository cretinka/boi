import random


board = []
for _ in range(5):
    board.append(["O"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))


def random_row(board):
    return random.randint(0, len(board) - 1)

def random_col(board):
    return random.randint(0, len(board[0]) - 1)


print("Давайте сыграем в Морской бой!")
print_board(board)


ship_row = random_row(board)
ship_col = random_col(board)


for turn in range(4):
    print(f"Ход {turn + 1}")
    guess_row = int(input("Укажите строку (0-4): "))
    guess_col = int(input("Укажите столбец (0-4): "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Поздравляю! Вы потопили корабль ИИ!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Упс, вышли за пределы поля!")
        elif board[guess_row][guess_col] == "X":
            print("Вы уже угадали эту клетку.")
        else:
            print("Мимо!")
            board[guess_row][guess_col] = "X"
    print_board(board)


print("Игра окончена.")