from functools import reduce

field = [list(l.strip()) for l in open("day3.in").readlines()]


def count_trees(field, down, right):
    width = len(field[0])
    max_down = len(field) - 1
    trees = 0
    idown = 0
    iright = 0

    while idown <= max_down:
        if field[idown][iright] == "#":
            trees += 1

        idown += down
        iright += right
        if iright > width - 1:
            iright = iright - width

    return trees


rules = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))

print(reduce(lambda a, b: a * b, [count_trees(field, *dr) for dr in rules]))
