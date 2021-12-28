# the task
# https://stepik.org/lesson/24463/step/7?unit=6771

# graph documentation
# http://www.infocity.kiev.ua/prog/python/content/pytonesse_3.shtml

dict_graph = {}

n = int(input())

for i in range(n):
    a, *b = input().replace(":", " ").split()
    if a not in dict_graph:
        dict_graph[a] = b
    else:
        for key, value in dict_graph:
            if key == value:
                dict_graph[key] = value + b

print(dict_graph)


def find_path(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    if start not in graph:
        return None

    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return path
    return None


m = int(input())
exceptions_lst = []

new_lst = []

for i in range(m):
    search_ex = input()
    for exception in exceptions_lst:
        if find_path(dict_graph, search_ex, exception) != None:
            new_lst.append(search_ex)
    exceptions_lst.append(search_ex)

super_list = []

for el in new_lst:
    if el not in super_list:
        super_list.append(el)

for el in super_list:
    print(el)


# exceptions for check
"""
4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError

"""
'''
4
BaseException
Exception : BaseException
LookupError : Exception 
KeyError : LookupError
2
BaseException
KeyError
'''