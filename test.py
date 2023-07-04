class Board:
    board = ['default value']
    shot_list = []
    ship_list = []

class Player:
    self_board = Board()
    opponent_board = Board()

class User(Player):

    def ask(self):
        print('t')


class AI(Player):
    def ask(self):
        print('t')


ivan = User()
pc = AI()

print(ivan.self_board.board)
print(ivan.opponent_board.board)
print(pc.self_board.board)
print(pc.opponent_board.board)

ivan.self_board.board[0] = 'ivan_self'
print(ivan.self_board.board)
print(ivan.opponent_board.board)
print(pc.self_board.board)
print(pc.opponent_board.board)
#
# ivan.opponent_board.board[0] = 'ivan_opponent'
# print(ivan.self_board.board)
# print(ivan.opponent_board.board)
# print(pc.self_board.board)
# print(pc.opponent_board.board)
#
# pc.self_board.board[0] = 'pc_self'
# print(ivan.self_board.board)
# print(ivan.opponent_board.board)
# print(pc.self_board.board)
# print(pc.opponent_board.board)
#
# pc.opponent_board.board[0] = 'pc_opponent'
# print(ivan.self_board.board)
# print(ivan.opponent_board.board)
# print(pc.self_board.board)
# print(pc.opponent_board.board)
#
print(ivan.self_board)
print(ivan.opponent_board)
print(pc.self_board)
print(pc.opponent_board)

class Player:
    def __init__(self, board, opponent_board):
        self.self_board = board
        self.opponent_board = opponent_board