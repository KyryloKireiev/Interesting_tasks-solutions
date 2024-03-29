class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    @staticmethod
    def matrix_form(matrix):
        length = len(matrix[0])
        for line in matrix:
            if len(line) != length:
                raise ValueError("Неверный формат для первого параметра matrix.")
        return True

    @staticmethod
    def matrix_elem(matrix):
        if len(matrix) == 1:
            for elem in matrix:
                if not isinstance(elem, (int, float)):
                    raise ValueError("Неверный формат для первого параметра matrix.")
            return True
        if len(matrix) > 1:
            for line in matrix:
                for elem in line:
                    if not isinstance(elem, (int, float)):
                        raise ValueError("Неверный формат для первого параметра matrix.")
            return True

    def __call__(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        if rows == 0:
            return [[]]

        if self.matrix_elem(matrix) and self.matrix_form(matrix):
            h, w = self.size[0], self.size[1]
            sh, sw = self.step[0], self.step[1]

            rows_range = (rows - h) // sh + 1
            cols_range = (cols - w) // sw + 1

            res = [[0] * cols_range for _ in range(rows_range)]

            for i in range(rows_range):
                for j in range(cols_range):
                    s = (x for r in matrix[i * sh: i * sh + h] for x in r[j * sw: j * sw + w])
                    res[i][j] = max(s)

            return res


mp = MaxPooling(step=(2, 2), size=(2, 2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2, 2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"
