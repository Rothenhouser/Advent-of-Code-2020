trees = 0
pos_from_left = 0
width = len(".....#....#...#.#..........#...")

with open("day3.in") as f:
    for l in f.readlines():
        p = l[pos_from_left]
        if p == "#":
            trees += 1
        pos_from_left += 3
        if pos_from_left > width - 1:
            pos_from_left = pos_from_left - width
