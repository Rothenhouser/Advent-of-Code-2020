import re

rules = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

EXAMPLE = rules.strip().split("\n")
FILE_INPUT = open("day7.in").readlines()

GOLD = "shiny gold"


def parse_rules_to_flat_dict(rules_strs):
    contained_in = {}
    for rule_str in rules_strs:
        # re.match goes only beginning of string, so no ^ necessary
        [outer_bag] = re.match(re.compile(r"(\w* \w*) bags"), rule_str).groups()
        contains = re.findall(re.compile(r"(\d+) (\w+ \w+) bag"), rule_str)
        for _n, inner_bag in contains:
            insert(inner_bag, outer_bag, contained_in)

    return contained_in


def insert(inner_bag, outer_bag, contained):
    if inner_bag in contained:
        contained[inner_bag].append(outer_bag)
    else:
        contained[inner_bag] = [outer_bag]


def find_gold(flat_dict):
    return _lookup_outer(flat_dict[GOLD], flat_dict)


def _lookup_outer(outer_bags, flat_dict):
    obsc = set()
    for outer in outer_bags:
        obsc |= {outer}
        if outer in flat_dict:
            obsc |= _lookup_outer(flat_dict[outer], flat_dict)
    return obsc


if __name__ == "__main__":
    print(len(find_gold(parse_rules_to_flat_dict(EXAMPLE))))
    print(len(find_gold(parse_rules_to_flat_dict(FILE_INPUT))))
