# class newNode:
# def __init__(self, data):
# self.data = data
# self.left = self.middle = self.right = None
# root1 = newNode(1)
# root1.left = newNode(2)
# root1.right = newNode(3)
# root1.left.left = newNode(4)
# root1.left.right = root1.middle = root1.right.left = newNode(5)
# root1.right.right = newNode(6)
# root1.left.left.right = root1.left.middle = root1.left.right.left = root1.middle.left = root1.right.left.left = newNode(7)
# root1.left.right.right = root1.middle.right = root1.right.left.right = root1.right.right.left = newNode(8)

#       1
#      /|\
#     2 | 3
#    /|\|/ \
#   4 | 5   6
#    \|/ \ /
#     7   8

graph1 = {
    1: [2, 3, 5],
    2: [4, 5, 7],
    3: [5, 6],
    4: [7],
    5: [7, 8],
    6: [8],
    7: [],
    8: [],
}

# kör ellenőrzés
s = []


def paths_in_graph(graph, start, end, path=[]):
    s.append(start)  # kör ellenőrzés

    path = path + [start]

    if start == end:
        return [path]

    if start not in graph:
        return []

    paths = []
    for edge in graph[start]:
        # kör ellenőrzés
        if edge == s[0]:
            paths.append([False])
            print("Kör!")
            break

        if edge not in path:
            new_paths = paths_in_graph(graph, edge, end, path)
            for new_path in new_paths:
                paths.append(new_path)

    return paths


print(sorted(paths_in_graph(graph1, 1, 7), key=len))
