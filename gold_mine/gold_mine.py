import numpy

m = numpy.random.randint(1, 10)  # row
n = numpy.random.randint(2, 10)  # column
gold_mine = numpy.random.randint(1, 100, size=(m, n))

print(gold_mine)

mining_path = [[[] for j in range(n)] for i in range(m)]
gold_quantity = numpy.zeros((m, n))
for column in range((n - 1), -1, -1):
    for row in range(m):
        if column == (n - 1):
            right = 0
        else:
            right = gold_quantity[row][column + 1]

        if (row == 0) or (column == (n - 1)):
            right_up = 0
        else:
            right_up = gold_quantity[row - 1][column + 1]

        if (row == (m - 1)) or (column == (n - 1)):
            right_down = 0
        else:
            right_down = gold_quantity[row + 1][column + 1]

        max_gold_quantity = max(right, right_up, right_down)

        if max_gold_quantity:
            if right == max_gold_quantity:
                path = [(row, (column + 1))] + mining_path[row][column + 1]
            elif right_up == max_gold_quantity:
                path = [((row - 1), (column + 1))] + mining_path[row - 1][column + 1]
            elif right_down == max_gold_quantity:
                path = [((row + 1), (column + 1))] + mining_path[row + 1][column + 1]
        else:
            path = []

        gold_quantity[row][column] = gold_mine[row][column] + max_gold_quantity
        mining_path[row][column] = path

max_mined_gold_quantity = 0
max_mined_gold_path = None
for row in range(m):
    if gold_quantity[row][0] > max_mined_gold_quantity:
        max_mined_gold_quantity = gold_quantity[row][0]
        max_mined_gold_path = [(row, 0)] + mining_path[row][0]

gold_mineut = []
for ut in max_mined_gold_path:
    gold_mineut.append(gold_mine[ut[0]][ut[1]])

print(max_mined_gold_quantity, gold_mineut, max_mined_gold_path)
