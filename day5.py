C = {
    "F": 0,
    "L": 0,
    "B": 1,
    "R": 1,
}


def code_as_bin(code):
    return "".join(str(C[l]) for l in code)


def seat_id(code):
    bin_code = code_as_bin(code)
    row, column = int(bin_code[:7], 2), int(bin_code[7:], 2)
    return row * 8 + column


def ordered_seat_id(code):
    return int(code_as_bin(code), 2)


if __name__ == "__main__":
    print(seat_id("FBFBBFFRLR"))

    print(max(seat_id(l.strip()) for l in open("day5.in").readlines()))

    seat_codes = [l.strip() for l in open("day5.in").readlines()]

    ids_to_ordered = {seat_id(c): ordered_seat_id(c) for c in seat_codes}

    max_ordered_seat_id = ordered_seat_id("BBBBBBBRRR")
    missing_front_passed = False

    all_taken_seats = [ordered_seat_id(c) for c in seat_codes]
    for expected_seat_id in range(max_ordered_seat_id):
        if not missing_front_passed:
            if expected_seat_id in all_taken_seats:
                missing_front_passed = True
        else:
            if expected_seat_id not in all_taken_seats:
                print("mine")
                print(expected_seat_id)
                b = bin(expected_seat_id)
                print(int(b[2:-3], 2) * 8 + int(b[-3:], 2))
                # yes they're identical

                break
