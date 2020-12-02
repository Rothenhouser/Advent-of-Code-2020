from typing import List, Tuple

Rule = Tuple[str, List[int]]


def parse_rule(rule: str) -> Rule:
    n, letter = rule.split(" ")
    positions = list(map(int, n.split("-")))
    return letter, positions


def evaluate(rule: Rule, pwd: str) -> bool:
    letter, positions = rule
    return sum(pwd[i - 1] == letter for i in positions) == 1


def eval_rule(line: str) -> bool:
    rule_str, pwd = (part.strip() for part in line.split(":"))
    return evaluate(parse_rule(rule_str), pwd)


count = sum(map(eval_rule, open("day2.in").readlines()))
