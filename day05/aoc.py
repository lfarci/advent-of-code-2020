import math

def read_boarding_passes_from_input(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def find_middle(min, max):
    return min + math.ceil((max - min) / 2)

def binary_search(selectors, lower_selector, upper_selector, min, max):
    selector = 0
    middle = find_middle(min, max)
    while selector < len(selectors):
        if selectors[selector] == lower_selector:
            max = middle
        if selectors[selector] == upper_selector:
            min = middle
        middle = find_middle(min, max)
        selector += 1
    return min

def find_row(row_selectors, min_row = 0, max_row = 127):
    return binary_search(
        selectors=row_selectors,
        lower_selector='F',
        upper_selector='B',
        min=min_row,
        max=max_row
    )

def find_column(column_selectors, min_col = 0, max_col = 7):
    return binary_search(
        selectors=column_selectors,
        lower_selector='L',
        upper_selector='R',
        min=min_col,
        max=max_col
    )

def seat_id(row, column, nseats_by_row = 8):
    return row * nseats_by_row + column

def find_seat_id(boarding_pass, row_selector_len = 7):
    row_selector = boarding_pass[:row_selector_len]
    col_selector = boarding_pass[row_selector_len:]
    return seat_id(find_row(row_selector), find_column(col_selector))

def main():
    boarding_passes = read_boarding_passes_from_input("./input.txt")
    seat_ids = [find_seat_id(bp) for bp in boarding_passes]
    print(f"The highest seat ID on a boarding pass is {max(seat_ids)}")

if __name__ == "__main__":
    main()


