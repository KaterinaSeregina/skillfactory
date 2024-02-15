def greet():
    print('_________________')
    print('Привет')
    print('давай поиграем')
    print('в крестики-нолики')
    print('_________________')
    print('формат ввода х, у')
    print('х номер строки')
    print('у номер столбца')
greet()

field = [[' '] * 3 for i in range(3)]
def show():
    print()
    print('  | 0 | 1 | 2 |')
    print('_______________')
    for i, row in enumerate(field):
        row_str = str(i) + ' | ' + ' | '.join(map(str, row))
        print(row_str)
        print('_______________')

def ask():
    while True:
        cords = input('   Твой ход: ').split()

        if len(cords) != 2:
            print('введи 2 числа')
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print('нужны только числа')
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print('упс, вне поля')
            continue

        if field[x][y] != ' ':
            print('упс, занято')
            continue

        return x, y

def check_win():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ['X', 'X', 'X']:
            print('Выйграл Х')
            return True
        if symbols == ['0', '0', '0']:
            print('Выйграл 0')
            return True
    return False

num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print('Ходит Х')
    else:
        print('Ходит 0')
    x, y = ask()
    if num % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = '0'
    if check_win():
        break
    if num == 9:
        print('ничья( попробуем еще раз?)')
        break


