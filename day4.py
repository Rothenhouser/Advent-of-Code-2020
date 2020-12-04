raws = open("day4.in").read().split("\n\n")

FIELDS = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"}

valids = 0
for pp in raws:
    elems = pp.split()
    ppd = {k: v for k, v in map(lambda e: e.split(":"), elems)}
    # Subset operator apparently works with keys.
    if FIELDS <= ppd.keys():
        valids += 1

print(valids)
