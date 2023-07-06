from random import randint

class ShotExceptions:
    def __init__(self, x, y):  # ship_list shot_list
        self.x = x
        self.y = y

    def in_board(self):
        if 1 <= self.x <= 6 and 1 <= self.y <= 6:
            return True
        else:
            return 'BoardOutException'


# c = ShotExceptions(2, 3)
# print(c.in_board())


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def in_set (self, *args):
        return (self.x, self.y) in set(*args)

# w = [(2, 4), (2, 5), (2, 6)]
# v = Dot(2, 3)
#
# print('v in w = ', v in set(w), v, set(w))
# print('in_dot function: ', v.in_set(w))


class Ship:
    def __init__(self, lenth):
        self.lenth = lenth

    def dots(self):
        ship = []
        ship_dots = []
        self.direction = 'h' if randint(0,1) == 0 else 'v'
        self.x = randint(1, 7 - self.lenth) if self.direction == 'h' else randint(1, 6)
        self.y = randint(1, 7 - self.lenth) if self.direction == 'v' else randint(1, 6)
        ship = [self.lenth, self.direction, self.x, self.y, self.lenth]
        dx, dy = 0, 0
        for i in range(0, self.lenth):
            ship_dots.append((self.x + dx, self.y + dy))
            if self.direction == 'h':
                dx += 1
            else:
                dy += 1
        return ship_dots, ship

S = Ship(3)
ship_dots, ship = S.dots()
print(f'точки: {ship_dots}, корабль: {ship}')
print(S.x)


class Board:
    board = [['O' for i in range(0,6)] for j in range(0,6)]
    shot_list = []
    ship_list = []

    def add_ship(self, ship_dots):
        ok = True
        for i in ship_dots:
            x, y = i[0], i[1]
            ok = ok * True if self.board[y-1][x-1] == 'O' else False
        if ok:
            for i in ship_dots:
                x, y = i[0], i[1]
                self.board[y - 1][x - 1] = '8'
        return ok

    def contour(self, ship_dots):
        contour = set()
        for i in ship_dots:
            x, y = i[0], i[1]
            cell_contour = {(min(6, x + 1), y), (max(1, x - 1), y), (x, min(6, y + 1)), (x, max(1, y - 1))}
            contour = contour.union(cell_contour)
        contour = contour.difference(ship_dots)
        return contour

# B = Board()
# print('countour: ', B.contour([(5, 2), (5, 3), (5, 4)]))
#
# board =[['O' for i in range(0, 6)] for j in range(0,6)]
# for i in board:
#     print(i)

    def show_board (self, hid):
        field = [[' ', 1, 2, 3, 4, 5, 6]]
        for i in range(1, 6):
            field.append([i, self.board[i][0], self.board[i][1], self.board[i][2], self.board[i][3], self.board[i][4], self.board[i][5]])
        for i in range (0,6):
            print(' |'.join(map(str, field[i])))

# b1 = Board()
# print('ща будет доска')
# b1.show_board(True)

    def shot(self, x, y):
        if 1 <= x <= 6 and 1 <= y <= 6:
            shot = Dot(x,y)
            if shot.in_set(self.shot_list):
                print('DoubleShot')
                return False
            else:
                self.shot_list.append((x, y))
                return True
        else:
            print('BoardOutException')
            return False


shot_list = [(3, 2), (4, 2), (5, 2)]
x, y = 3, 3
b1 = Board()
print('ща будет выстрел')
print(b1.shot(x, y))


class Player:
    self_board = Board()
    opponent_board = Board()
    def move(self):
        x, y = self.opponent_board.board.ask()
        if not (x, y).issubset(set(self_board.shot_list)):
            self_board.shot_list.append((x, y))
            if (x, y).issubset(set(opponent_board.ship_list)):
                on_target = True
                self.opponent_board.board[y - 1][x - 1] = 'X'
            else:
                on_target = False
                self.opponent_board.board[y - 1][x - 1] = 'T'
        return on_target

class User(Player):

    def ask(self):   # допилить выход из функции
        _end = False
        while not _end:
            try:
                x, y = input('Input X and Y by space:\t').split()
                x = int(x)
                y = int(y)
            except ValueError as e:
                print(e)
                _end = False
            else:
                _end = shot(x, y)
        return x, y
class AI(Player):
    def ask(self):
        x = randint(1, 6)
        y = randint(1, 6)
        return x, y






#
# inp = False
# while not inp:
#     a = ShutExceptions()
#     x, y, inp = a.check_inp()
# print(x, y, inp)
#
#
# def ask(self):
#     try:
#         x, y = input('Input X and Y by space:\t').split()
#         self.x = int(x)
#         self.y = int(y)
#     except ValueError as e:
#         print(e)
#         return None, None, False
#     else:
#         return a.in_board(self.x, self.y)
# #
#
# class Ship:
#
#     def dots(self, s):
#         ship_dots = []
#         for i in s:
#             dx, dy = 0, 0
#             print('s=', s)
#             for j in range(0, i[0]):
#                 ship_dots.append((i[2] + dy, i[3] + dx))
#                 if i[1] == 'h':
#                     dx += 1
#                 else:
#                     dy += 1
#         return ship_dots
#
#
# p_ships = [[3, 'h', 2, 3, 3], [2, 'v', 1, 4, 2],]
# ship = Ship()
# # print(ship.dots(p_ships))
# # print(set(ship.dots(p_ships)))
#
# class Board:
#     board = None
#     hid = None
#     alive = None
#     # def __init__(self, board, ship, hid, alive):
#     #     self.field = board
#     #     self.ship = ship
#     #     self.hid = hid
#     #     self.alive = alive
#
#     def add_ship(self, list):
#         s = []
#         ship = Ship()
#         for n, value in enumerate(list):
#             _dots_set = set(ship.dots(s)) if len(s) > 0 else set()
#             print('ship:', ship)
#             bad_place = True
#             while bad_place:
#                 _s = []
#                 _s.append(value)
#                 _s.append('h' if randint(0,1) == 0 else 'v')
#                 _s.append(randint(1, 7 - list[n]) if _s[1] == 'h' else randint(1, 6))
#                 _s.append(randint(1, 7 - list[n]) if _s[1] == 'v' else randint(1, 6))
#                 _s.append(value)
#                 print('_s = ', _s)
#                 _S = []
#                 _S.append(_s)
#                 build_ship = Ship()
#                 build_ship_set = set(build_ship.dots(_S))
#                 bad_place = bool(_dots_set.intersection(build_ship_set))
#                 print('Ships = ', _dots_set, '\n', s)
#                 print('build_ship = ', build_ship_set, '\n', _s)
#                 print('bad place = ', bad_place)
#                 k = input()
#                 if bad_place == False:
#                     s.append(_s)
#                     print('False _s = ', s)
#         print('_S = ',_S)
#         print('s = ',s)
#         return(s)
#
# #     def counour(self, one_ship):
# #
# #     def show_board(self, board, ship, hid):
# #
#
# list = (3, 2, 2, 1, 1, 1, 1)
# player_board = Board()
# s = player_board.add_ship(list)
# print('player ships:', s)