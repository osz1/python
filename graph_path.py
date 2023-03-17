#       1
#      /|\
#     2 | 3
#    /|\|/ \
#   4 | 5   6
#    \|/ \ /
#     7   8

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

graf1 = {
    1: [2, 3, 5],
    2: [4, 5, 7],
    3: [5, 6],
    4: [7],
    5: [7, 8],
    6: [8],
    7: [],
    8: []
}
s = []
def utvonalak(graf, kezdo, veg, ut=[]):
    s.append(kezdo)
    ut = ut + [kezdo]
    if kezdo == veg:
        return [ut]
    if kezdo not in graf:
        return []
    utak = []
    for csucs in graf[kezdo]:
        if csucs == s[0]:
            utak.append([False])
            print('Kör!')
            break
        if csucs not in ut:
            ujutak = utvonalak(graf, csucs, veg, ut)
            for ujut in ujutak:
                utak.append(ujut)
    return utak
print(sorted(utvonalak(graf1, 1, 7), key=len))
