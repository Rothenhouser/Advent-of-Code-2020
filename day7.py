import re
from collections import defaultdict

example_rules = """
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

EXAMPLE = example_rules.strip().split("\n")
FILE_INPUT = open("day7.in").readlines()

GOLD = "shiny gold"


def parse_rules_to_flat_dict(rules_strs, inserter):
    contents = defaultdict(list, {})
    for rule_str in rules_strs:
        # re.match goes only beginning of string, so no ^ necessary
        [outer_bag] = re.match(re.compile(r"(\w* \w*) bags"), rule_str).groups()
        contains = re.findall(re.compile(r"(\d+) (\w+ \w+) bag"), rule_str)
        inserter(outer_bag, contains, contents)
    return contents


def inside_out(outer_bag, inner_bags, contained_in):
    for _n, inner_bag in inner_bags:
        contained_in[inner_bag].append(outer_bag)


def outside_in(outer_bag, inner_bags, containing):
    containing[outer_bag] = [(int(n), bag) for n, bag in inner_bags]


def bags_containing_gold(rules_strs):
    flat_dict = parse_rules_to_flat_dict(rules_strs, inside_out)
    return _lookup_outer(flat_dict[GOLD], flat_dict)


def _lookup_outer(outer_bags, flat_dict):
    obsc = set()
    for outer in outer_bags:
        obsc |= {outer}
        if outer in flat_dict:
            obsc |= _lookup_outer(flat_dict[outer], flat_dict)
    return obsc


def gold_bag_contains(rules_strs):
    flat_dict = parse_rules_to_flat_dict(rules_strs, outside_in)
    return _count_bags_in(flat_dict[GOLD], flat_dict)


def _count_bags_in(inner_bags, flat_dict):
    n_bags = 0
    for n, bag in inner_bags:
        n_bags += n
        n_bags += n * _count_bags_in(flat_dict[bag], flat_dict)
    return n_bags


if __name__ == "__main__":
    # print(len(bags_containing_gold(EXAMPLE)))
    print(len(bags_containing_gold(FILE_INPUT)))
    print(gold_bag_contains(FILE_INPUT))
