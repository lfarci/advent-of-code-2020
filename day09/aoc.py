from parse import *
import copy

def parse_instruction(line):
    parsed = parse("{} {}", line)
    return {"operation": parsed[0], "argument": int(parsed[1])}

def read_lines_from(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines

def read_numbers_from(path):
    numbers = []
    for line in read_lines_from(path):
        numbers.append(int(line.strip()))
    return numbers

def find_summing_pair(number, preamble):
    for i in range(0, len(preamble)):
        for j in range(i, len(preamble)):
                sum = preamble[i] + preamble[j]
                if sum == number and preamble[i] != preamble[j]:
                    return (preamble[i], preamble[j])
    return -1

def exist_summing_pair(number, preamble):
    return find_summing_pair(number, preamble) != -1

def find_intruder(xmas_numbers, preamble_size = 25):
    index = preamble_size
    found = False
    while index < len(xmas_numbers) and not found:
        preamble = xmas_numbers[index - preamble_size : index]
        found = not exist_summing_pair(xmas_numbers[index], preamble)
        index += 1
    return xmas_numbers[index - 1]

def find_contiguous_range(xmas_numbers, number):
    range_size = 2
    contiguous_range = None
    while contiguous_range == None:
        index = 0
        while index < len(xmas_numbers):
            current_range = xmas_numbers[index : index + range_size]
            if sum(current_range) == number:
                contiguous_range = current_range
            index += 1
        range_size += 1
    return contiguous_range

def main():
    numbers = read_numbers_from("./input.txt")
    intruder = find_intruder(numbers, 25)
    contiguous_range = find_contiguous_range(numbers, intruder)
    print(f"First intruder: {intruder} (part 1)")
    print(f"Contiguous range: {min(contiguous_range) + max(contiguous_range)} (part 2)")

if __name__ == "__main__":
    main()