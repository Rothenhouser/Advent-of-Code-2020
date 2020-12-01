import itertools

test_data = [1, 2, 3, 2000, 20, 19]


def find_2020(data, n):
    for elems in itertools.combinations_with_replacement(data, n):
        # print(a,b)
        if sum(elems) == 2020:
            return elems
    else:
        raise ValueError


if __name__ == "__main__":
    # print(find_2020(test_data))
    data = list(map(int, open("day1.in").read().split("\n")))
    a, b = find_2020(data, 2)
    print(a, b)
    print(a * b)

    a, b, c = find_2020(data, 3)
    print(a, b, c)
    print(a * b * c)
