lst = list(map(int, input().split()))

print(lst)


for i in range(len(lst) - 1):
    for elem in range(0, len(lst) - 1 - i):
        if lst[elem + 1] <= lst[elem]:
            lst[elem], lst[elem + 1] = lst[elem + 1], lst[elem]
        else:
            continue

print(*lst)


"""
Вводится список целых чисел в одну строку через пробел. 
Необходимо выполнить его сортировку по возрастанию 
(неубыванию) методом всплывающего пузырька.

При первом проходе перебираем все соседние пары элементов 
и если значение предыдущего элемента (слева) больше значения следующего (справа), 
то они меняются местами. (На рисунке 3 и 2 меняются местами). 
Следующая пара - это 3 и 6. Они уже выстроены по возрастанию, 
поэтому ничего не делаем и переходим к следующей паре 6 и -1. 
Меняем значения местами и видим, 
что на последнем месте находится максимальное значение 6, 
что нам и нужно.

При втором проходе делаем все то же самое, 
но доходим до предпоследнего элемента, 
так как последнее значение 6 уже отсортировано. 
На третьем проходе исключаем уже последние два элемента и так далее. 
То есть, в этом алгоритме достаточно сделать N-1 проходов, где N - длина списка.
"""