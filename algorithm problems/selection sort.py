lst = list(map(int, input().split()))

print(lst)


for i in range(len(lst)):
    for elem in range(i, len(lst)):
        if lst[elem] <= lst[i]:
            lst[i], lst[elem] = lst[elem], lst[i]

print(lst)


"""
Большой подвиг 6. Вводится список целых чисел в одну строку через пробел. 
Необходимо выполнить его сортировку выбором по возрастанию (неубыванию). 

Вначале мы рассматриваем первый элемент списка и ищем второй 
минимальный относительно первого элемента (включая и его). 
На рисунке - это последний элемент со значением -1. Затем, 
меняем местами первый и последний элементы. Переходим ко второму элементу списка и 
повторяем эту же процедуру, но относительно второго элемента 
(то есть, первый уже не рассматриваем). На рисунке минимальный элемент - это 2, 
поэтому менять местами здесь ничего не нужно. Переходим к 3-му элементы со значением 6. 
Относительно него находим минимальный элемент - это 3. Меняем их местами. 

"""