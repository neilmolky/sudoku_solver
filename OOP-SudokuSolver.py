class Sudoku:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, board):
        self.board = board
        self.vertical = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
        self.horizontal = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []}
        self.box = {"top_left": [], "top_center": [], "top_right": [],
                    "mid_left": [], "mid_center": [], "mid_right": [],
                    "bottom_left": [], "bottom_center": [], "bottom_right": []}
        self.squares = []
        self.solved = []

    def valid(self):
        if len(self.board) == 9:
            for i, row in enumerate(self.board):
                if len(row) != 9:
                    return False
                else:
                    for j, pos in enumerate(row):
                        self.squares.append(Square(i, j, pos))
            return True
        return False

    def solve(self):
        while len(self.solved) < 81:
            for s in self.squares:
                if s.value != 0 and not s.stored:
                    self.horizontal[s.row] += [s.value]
                    print(s.row, self.horizontal[s.row])
                    self.vertical[s.pos] += [s.value]
                    self.box[s.find_box] += [s.value]
                    s.stored = True
                    self.solved.append((s.row, s.pos))
                elif s.value == 0 and not s.stored:
                    duds = set(self.horizontal[s.row] + self.vertical[s.pos] + self.box[s.find_box])
                    s.options = [n for n in Sudoku.numbers if n not in duds]
                    if len(s.options) == 1:
                        print(s.row, s.pos)
                        print(self.board[s.row], s.options)
                        self.board[s.row][s.pos] = s.options[0]
                        s.value = s.options[0]
                else:
                    pass
        return self.board


class Square:
    def __init__(self, row, pos, value):
        self.row = row
        self.pos = pos
        self.value = value
        self.options = []
        self.stored = False

    @property
    def find_box(self):
        if self.row < 3:
            if self.pos < 3:
                return "top_left"
            elif self.pos < 6:
                return "top_center"
            else:
                return "top_right"
        elif self.row < 6:
            if self.pos < 3:
                return "mid_left"
            elif self.pos < 6:
                return "mid_center"
            else:
                return "mid_right"
        else:
            if self.pos < 3:
                return "bottom_left"
            elif self.pos < 6:
                return "bottom_center"
            else:
                return "bottom_right"


def sudoku(puzzle):
    board = Sudoku(puzzle)
    return board.solve() if board.valid() else False