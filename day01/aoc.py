
def line_to_number(line):
    return int(line.strip())

def read_numbers_from_input(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return [line_to_number(line) for line in lines]

def find_summing_pair(numbers, target):
    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
                if (numbers[i] + numbers[j]) == target:
                    return (numbers[i], numbers[j])
    return -1

def find_summing_threesome(numbers, target):
    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
            for h in range(0, len(numbers)):
                if (numbers[i] + numbers[j] + numbers[h]) == target:
                    return (numbers[i], numbers[j], numbers[h])
    return -1

def main():
    numbers = read_numbers_from_input("./input.txt")
    pair = find_summing_pair(numbers, 2020)
    threesome = find_summing_threesome(numbers, 2020)
    print(f"{pair[0]} + {pair[1]} = {pair[0] + pair[1]}")
    print(f"{pair[0]} * {pair[1]} = {pair[0] * pair[1]}")
    print(f"{threesome[0]} + {threesome[1]} + {threesome[2]} = {threesome[0] + threesome[1] + threesome[2]}")
    print(f"{threesome[0]} * {threesome[1]} * {threesome[2]} = {threesome[0] * threesome[1] * threesome[2]}")

if __name__ == "__main__":
    main()