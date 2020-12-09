C = {
    "F": 0,
    "L": 0,
    "B": 1,
    "R": 1,
}


def parse_code(code):
    code_as_bin = "".join(str(C[l]) for l in code)
    row, column = int(code_as_bin[:7], 2), int(code_as_bin[7:], 2)
    return row, column


def seat_id(row, column):
    return row * 8 + column


if __name__ == "__main__":
    print(seat_id(*parse_code("FBFBBFFRLR")))
    print(max(seat_id(*parse_code(l.strip())) for l in open("day5.in").readlines()))
