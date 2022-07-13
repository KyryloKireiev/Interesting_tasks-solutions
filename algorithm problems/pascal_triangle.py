def get_str(lst):
    return ' '.join(map(str, lst))


size = 10
pascal_triangle_lst = []

for i in range(size):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = pascal_triangle_lst[i - 1][j - 1] + pascal_triangle_lst[i - 1][j]
    pascal_triangle_lst.append(row)

width = len(get_str(pascal_triangle_lst[-1]))


for line in pascal_triangle_lst:
    print(get_str(line).center(width))