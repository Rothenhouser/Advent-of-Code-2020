group_answers = open("day6.in").read().replace("\n\n", "|").replace("\n", "").split("|")
print(sum(map(len, map(set, group_answers))))
