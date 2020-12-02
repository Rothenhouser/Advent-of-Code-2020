from typing import Tuple

Rule = Tuple[str, int, int]


def parse_rule(rule: str) -> Rule:
    n, letter = rule.split(" ")
    min_n, max_n = map(int, n.split("-"))
    return letter, min_n, max_n


def evaluate(rule: Rule, pwd: str) -> bool:
    letter, min_n, max_n = rule
    return min_n <= pwd.count(letter) <= max_n


def eval_rule(line: str) -> bool:
    rule_str, pwd = (part.strip() for part in line.split(":"))
    return evaluate(parse_rule(rule_str), pwd)


count = sum(map(eval_rule, open("day2.in").readlines()))
