from random import randint


class Cell:

    def __init__(self, mine: bool, around_mines=0, fl_open=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    pole = []
    mask_pole = []

    def __init__(self, N, M):
        self.N = N
        self.M = M

    def init(self):
        self.pole = [[0] * self.N for i in range(self.N)]

        iteration = 0
        while iteration < self.M:
            i = randint(0, self.N - 1)
            j = randint(0, self.N - 1)

            if self.pole[i][j] == 0:
                self.pole[i][j] = "*"
                iteration += 1

        self.mask_pole = [[0] * (self.N + 2) for i in range(self.N + 2)]

        for i in range(self.N):
            for j in range(self.N):

                if self.pole[i][j] == "*":
                    self.mask_pole[i + 1][j + 1] = "*"

        for i in range(1, self.N + 1):
            for j in range(1, self.N + 1):
                if self.mask_pole[i][j] == "*":
                    try:
                        self.mask_pole[i - 1][j - 1] += 1
                    except TypeError:
                        pass

                    try:
                        self.mask_pole[i][j - 1] += 1
                    except TypeError:
                        pass

                    try:
                        self.mask_pole[i + 1][j - 1] += 1
                    except TypeError:
                        pass

                    try:
                        self.mask_pole[i - 1][j] += 1
                    except TypeError:
                        pass

                    try:
                        self.mask_pole[i + 1][j] += 1
                    except TypeError:
                        pass

                    try:
                        self.mask_pole[i - 1][j + 1] += 1
                    except TypeError:
                        pass

                    try:
                        self.mask_pole[i][j + 1] += 1
                    except TypeError:
                        pass

                    try:
                        self.mask_pole[i + 1][j + 1] += 1
                    except TypeError:
                        pass

        for i in range(self.N):
            for j in range(self.N):
                self.pole[i][j] = self.mask_pole[i + 1][j + 1]

        for i in range(self.N):
            for j in range(self.N):

                if type(self.pole[i][j]) == int:
                    self.pole[i][j] = Cell(around_mines=self.pole[i][j], mine=False)
                else:
                    self.pole[i][j] = Cell(around_mines=0, mine=True)

    def show(self):
        for line in self.pole:
            for elem in line:
                if elem.fl_open == True:
                    print("#", end=" ")

                if elem.mine == False and elem.fl_open == False:
                    print(elem.around_mines, end=" ")

                if elem.mine == True and elem.fl_open == False:
                    print("*", end=" ")

            print()


pole_game = GamePole(N=10, M=12)
pole_game.init()

pole_game.show()


"""

p = GamePole(5, 2)
p.init()

lst = p.pole
new_lst = p.mask_pole

for line in lst:
    print(*line)

print()

for line in new_lst:
    print(*line)

p.show()
"""

assert isinstance(pole_game, GamePole) and hasattr(GamePole, 'init') and hasattr(GamePole, 'show')

Cell.__doc__

N = 10
M = 10


def get_around_mines(i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or jj < 0 or ii >= N or jj >= N:
                continue
            if pole_game.pole[ii][jj].mine:
                n += 1
    return n


for i in range(N):
    for j in range(N):
        if not pole_game.pole[i][j].mine:
            assert pole_game.pole[i][j].around_mines == get_around_mines(i,
                                                                         j), f"неверное число мин вокруг клетки с индексами {i, j}"