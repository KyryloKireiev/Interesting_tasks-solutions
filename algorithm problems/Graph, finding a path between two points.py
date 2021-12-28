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

#print(dict_graph)


def find_path(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    if start not in graph:
        return None

    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path: return path

    return None


m = int(input())

for i in range(m):
    end_class, start_class = input().split(' ')
    if find_path(dict_graph, start_class, end_class) != None:
        print("Yes")
    else:
        print("No")