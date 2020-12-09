from functools import reduce

group_answers = open("day6.in").read().replace("\n\n", "|").replace("\n", "").split("|")
print(sum(map(len, map(set, group_answers))))

print(
    sum(
        len(reduce(lambda a, b: a & b, map(set, one_group)))
        for one_group in [g.split("\n") for g in open("day6.in").read().split("\n\n")]
    )
)
