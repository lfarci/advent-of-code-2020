import math

def read_boarding_passes_from_input(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def find_middle(min, max):
    return min + math.ceil((max - min) / 2)

def binary_search(selectors, lower_selector, upper_selector, min, max):
    selector_idx = 0
    middle = find_middle(min, max)
    while selector_idx < len(selectors):
        if selectors[selector_idx] == lower_selector:
            max = middle
        if selectors[selector_idx] == upper_selector:
            min = middle
        middle = find_middle(min, max)
        selector_idx += 1
    return min

def find_row(row_selectors, min_row = 0, max_row = 127):
    return binary_search(row_selectors, 'F', 'B', min_row, max_row)

def find_column(column_selectors, min_col = 0, max_col = 7):
    return binary_search(column_selectors, 'L', 'R', min_col, max_col)

def seat_id(row, column, nseats_by_row = 8):
    return row * nseats_by_row + column

def find_seat_id(boarding_pass, row_selector_len = 7):
    row_selector = boarding_pass[:row_selector_len]
    col_selector = boarding_pass[row_selector_len:]
    return seat_id(find_row(row_selector), find_column(col_selector))

def find_my_seat(seats_ids):
    sorted_seat_ids = sorted(seats_ids)
    last_seat_id = seats_ids[0]
    for i in range(1, len(sorted_seat_ids)):
        if (sorted_seat_ids[i] - last_seat_id) > 1:
            return sorted_seat_ids[i] - 1
        last_seat_id = sorted_seat_ids[i]
    return None

def main():
    boarding_passes = read_boarding_passes_from_input("./input.txt")
    seat_ids = [find_seat_id(bp) for bp in boarding_passes]
    print(f"The highest seat ID on a boarding pass is {max(seat_ids)} (part 1)")
    print(f"My seat id is {find_my_seat(seat_ids)} (part 2)")

if __name__ == "__main__":
    main()