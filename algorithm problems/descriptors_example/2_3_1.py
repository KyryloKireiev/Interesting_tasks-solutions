class FloatValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify(value)
        setattr(instance, self.name, value)

    def verify(self, number):
        if type(number) is not float:
            raise TypeError("Присваивать можно только вещественный тип данных.")


class Cell:

    value = FloatValue()

    def __init__(self, value):
        self.value = value


class TableSheet:

    def __init__(self, N, M):
        self.N = N
        self.M = M

        self.cells = [[Cell(0.0)] * self.M for row in range(self.N)]

    def fill_table(self):
        number = 1.0

        for i in range(self.N):
            for j in range(self.M):
                self.cells[i][j] = Cell(number)
                number += 1


c1 = Cell(1.45)
print(c1.value)

c2 = Cell(0.374982)
print(c2.value)


table = TableSheet(5, 3)
table.fill_table()

for line in table.cells:
    for elem in line:
        print(elem.value, end=" ")
    print()

res = [int(x.value) for row in table.cells for x in row]
assert res == list(range(1, 16))

assert isinstance(table, TableSheet)
assert len(table.cells) == 5 and len(table.cells[0]) == 3

assert type(table.cells) == list

res = [int(x.value) for row in table.cells for x in row]
assert res == list(range(1, 16))

table.cells[0][0].value = 1.0
x = table.cells[1][0].value



try:
    table.cells[0][0].value = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

