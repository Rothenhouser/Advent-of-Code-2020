"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""
import re
from collections import defaultdict
from typing import Callable, Dict


def matches(re_str):
    def _matcher(string):
        return bool(re.match(re.compile(re_str), string))

    return _matcher


def valid_height(s):
    try:
        n, suffix = int(s[:-2]), s[-2:]
    except ValueError:
        return False

    if suffix == "cm":
        return 150 <= int(n) <= 193
    elif suffix == "in":
        return 59 <= int(n) <= 76
    else:
        return False


def match(re_str):
    def _match(string):
        return bool(re.match(re.compile(f"^{re_str}$"), string))

    return _match


REQUIRED_FIELDS = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"}

VALIDATORS: Dict[str, Callable[[str], bool]] = defaultdict(
    lambda: lambda s: False,
    {
        "byr": lambda s: 1920 <= int(s) <= 2002,
        "iyr": lambda s: 2010 <= int(s) <= 2020,
        "eyr": lambda s: 2020 <= int(s) <= 2030,
        "hgt": valid_height,
        "hcl": match(r"#[a-z0-9]{6}"),
        "ecl": match(r"amb|blu|brn|gry|grn|hzl|oth"),
        "pid": match(r"\d{9}"),
        "cid": lambda _: True,
    },
)


def handle_value_errors(fn, arg):
    try:
        return fn(arg)
    except ValueError:
        return False


def evaluate(raw):
    vals = []
    valids = 0
    for pp in raw.split("\n\n"):
        elems = pp.split()
        ppd = {k: v for k, v in map(lambda e: e.split(":"), elems)}
        # Subset operator apparently works with keys.
        # if all(handle_value_errors(VALIDATORS[fname], ppd[fname]) for fname in ppd):
        if REQUIRED_FIELDS <= ppd.keys() and all(
            VALIDATORS[fname](ppd[fname]) for fname in ppd
        ):
            vals.append(ppd["pid"])
            # print(ppd["byr"])
            valids += 1
    print(sorted(set(vals)))
    print(set(map(len, vals)))
    return valids


if __name__ == "__main__":
    # print(evaluate(open("day4_valid.in").read()))
    # print(evaluate(open("day4_invalid.in").read()))
    print(evaluate(open("day4.in").read()))
