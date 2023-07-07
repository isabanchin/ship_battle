from random import randint

# вводные правила
l = [3, 2, 2, 1, 1, 1, 1]  # набор кораблей
field = 6                  # размер игрового поля, клеток

class Player:
    live = len(l)
    def add_ship(self, l): # ships installing: In: ship lenth list. Out: initional ships and board class attributes
        self.self_board = [['O' for i in range(0, field)] for j in range(0, field)]
        self.ship_list = []
        self.ship_dots = set()
        self.contour_dots = set()
        counter = 0
        for i, value in enumerate(l):
            ok = False
            while not ok:                     # ship rnd one by one
                counter += 1
                if counter == 2000:
                    return False
                lenth = l[i]
                _dots = []
                _contour = set()
                direction = 'h' if randint(0, 1) == 0 else 'v'
                x = randint(1, field + 1 - lenth) if direction == 'h' else randint(1, field)
                y = randint(1, field + 1 - lenth) if direction == 'v' else randint(1, field)
                dx, dy = 0, 0
                for n in range(0, lenth):                                   # every ship and contour dots generation
                    _dots.append((x + dx, y + dy))
                    if direction == 'h':
                        dx += 1
                    else:
                        dy += 1
# check ship is ok:
                ok = False if set(_dots).intersection(set(self.ship_dots)) or set(_dots).intersection(set(self.contour_dots)) else True
# if ok = True then contour dots generation else go back to recycle:
            _contour = set()
            for n in (_dots):  # every ship and contour dots generation
                x, y = n
                _contour = _contour.union(
                    {(max(x - 1, 1), max(y - 1, 1)), (x, max(y - 1, 1)), (min(x + 1, field), max(y - 1, 1)),
                     (max(x - 1, 1), y), (min(x + 1, field), y),
                     (max(x - 1, 1), min(y + 1, field)), (x, min(y + 1, field)),
                     (min(x + 1, field), min(y + 1, field))})
# check ship place is ok:
            ok = False if set(_dots).intersection(self.ship_dots) or set(_dots).intersection(set(self.contour_dots)) else True
# Update self.ship_list, ship_dots, self.contour_dots by new ship:
            self.ship_list.append([l[i], direction, x, y, l[i], _dots, _contour])
            self.ship_dots = self.ship_dots.union(set(_dots))
            self.contour_dots = self.contour_dots.union(_contour.difference(_dots))
# Ships to board:
        for i in self.ship_dots:
            x, y = i[0], i[1]
            self.self_board[y - 1][x - 1] = '■' if self.hide_self_board == False else 'O'
        # print(f'{self}, {self.self_board}')
        return True

    def show_board (self, board):
        one_string = [n for n in range(1, field+1)]  # корявые три строки преобразования - найти способ короче
        one_string.insert(0, ' ')
        console_board = [one_string]
        for i in range(field):
            one_string = board[i].copy()              # корявые три строки преобразования - найти способ короче
            one_string.insert(0, i+1)
            console_board.append(one_string)
        for i in range (0,field+1):
            print(' | '.join(map(str, console_board[i])), '|')

    def shot(self, x, y):
        self.self_board[y - 1][x - 1] = 'T'
        for i in self.ship_list:
            if (x, y) in i[5]:
                i[4] -= 1
                self.self_board[y-1][x-1] = 'X'
                if i[4] == 0:
                    self.live -= 1
                    print(f'{i[0]}-палубный корабль убит, осталось {self.live} кореблей')
                else:
                    print(f'{i[0]}-палубный корабль ранен')
        if self.live == 0:
            return True
        else:
            return False

class User(Player):
    hide_self_board = False
    shot_list = []

    def ask(self):
        _end = False
        while not _end:
            try:
                x, y = input('Input X and Y by space:\t').split()
                x, y = int(x), int(y)
            except ValueError as e:
                print(e)
                _end = False
            else:
                if 1 <= x <= 6 and 1 <= y <= 6:
                    if (x, y) in set(self.shot_list):
                        print("Wrong coordinates: it's alredy shoted")
                    else:
                        _end = True
                else:
                    print('Coordinate out of range from 1 to 6')
        self.shot_list.append((x,y))
        return x, y

class AI(Player):
    hide_self_board = True
    shot_list = []

    def ask(self):
        _end = False
        while not _end:
            x, y = randint(1, field), randint(1, field)
            if (x, y) not in set(self.shot_list):
                _end = True
        print(f'AI shot is {x}, {y}')
        self.shot_list.append((x,y))
        return x, y


user1 = User()
pc1 = AI()
while not user1.add_ship(l):
    pass
while not pc1.add_ship(l):
    pass
print(f'user1 ship count = {len(user1.ship_list)}, ship list: {user1.ship_list}')
print(f'pc1 ship count = {len(pc1.ship_list)}, ship list: {pc1.ship_list}')

while True:
    print('User board:')
    pc1.show_board(user1.self_board)
    print('AI board:')
    user1.show_board(pc1.self_board)

    x, y = user1.ask()
    user1_win = pc1.shot(x, y)
    if user1_win:
        win = 'User'
        break

    x, y = pc1.ask()
    pc1_win = user1.shot(x, y)
    if pc1_win:
        win = 'AI'
        break

print('User board:')
pc1.show_board(user1.self_board)
print('AI board:')
user1.show_board(pc1.self_board)
print(f'Game over. {win} win')


