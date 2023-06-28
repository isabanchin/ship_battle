# class CheckInp:
#     def check_inp(self):
#         try:
#             x, y = input('Input X and Y by space:\t').split()
#             self.x = int(x)
#             self.y = int(y)
#         except ValueError as e:
#             print(e)
#             return None, None, False
#         else:
#             return self.x, self.y, True
#
# class Dot:
#     def dot(self, x, y):
#         if 1 <= x <= 6 and 1 <= y <= 6:
#             self.x = x
#             self.y = y
#             return self.x, self.y, True
#         else:
#             print('BoardOutException')
#             return None, None, False
#
# inp = False
# while not inp:
#     a = CheckInp()
#     x, y, inp = a.check_inp()
#     if inp:
#         a = Dot()
#         x, y, inp = a.dot(x, y)
# print(x, y, inp)
# print(a.x, a.y)


class Ship:
    def __init__(self, s):
        self.s = s

    def dots(self):
        ship_dots = []
        for i in self.s:
            dx, dy = 0, 0
            for j in range(0,i[0]):
                ship_dots.append((i[1] + dy, i[2] + dx))
                if i[3] == 'h':
                    dx += 1
                else:
                    dy += 1
        return ship_dots


p_ships = [[3, 2, 3, 'h', 3], [2, 1, 4, 'v', 2],]
ship = Ship(p_ships)
print(ship.dots())

