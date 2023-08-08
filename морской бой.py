import random

# Создаем игровое поле
board = []
for _ in range(6):
    board.append(["O"] * 6)

# Функция для вывода игрового поля
def print_board(board):
    print("# | 1 | 2 | 3 | 4 | 5 | 6 |")
    i=0
    for row in board:
        print(f"{i} | "+" | ".join(row))
        i+=1

# Функция для случайного выбора координат
def random_row(board):
    return random.randint(0, len(board) - 1)

def random_col(board):
    return random.randint(0, len(board[0]) - 1)

# Начало игры
print("Давайте сыграем в Морской бой!")
print_board(board)


ship_row = random_row(board)
ship_col = random_col(board)


for turn in range(4):
    print(f"Ход {turn + 1}")
    guess_row = int(input("Укажите строку (0-6): "))
    guess_col = int(input("Укажите столбец (0-6): "))

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

# Конец игры
print("Игра окончена.")