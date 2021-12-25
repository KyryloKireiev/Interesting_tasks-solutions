n = int(input())
counter = 1
m = 0
n_list = [[0] * n for z in range(n)]

i = 0
j = 0


n_list[n//2][n//2] = n*n

for v in range(n//2):
    #Заполнение верхней горизонтальной матрицы
    for i in range(n-m):
        n_list[v][i+v] = counter
        counter += 1

    #Заполнение правой вертикальной матрицы
    for i in range(v+1, n-v):
        n_list[i][-v-1] = counter
        counter += 1

    #Заполнение нижней горизонтальной матрицы
    for i in range(v+1, n-v):
        n_list[-v-1][-i-1] = counter
        counter += 1

    #Заполнение левой вертикальной матрицы
    for i in range(v+1, n-(v+1)):
        n_list[-i-1][v] = counter
        counter += 1
    m += 2


for row in n_list:
    print(' '.join([str(elem) for elem in row]))