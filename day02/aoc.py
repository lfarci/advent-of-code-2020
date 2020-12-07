from parse import *

def parse_line(line):
    parsed = parse("{}-{} {}: {}", line)
    return {
        "min": int(parsed[0]),
        "max": int(parsed[1]),
        "letter": parsed[2],
        "value": parsed[3],
    }

def read_passwords_from_input(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return [parse_line(line) for line in lines]

def old_job_policy(password, letter, min, max):
    return min <= password.count(letter) and password.count(letter) <= max

def current_job_policy(password, letter, min, max):
    return (password[min - 1] == letter and password[max - 1] != letter) or (password[max - 1] == letter and password[min - 1] != letter)

def count_valid(passwords, is_valid):
    count = 0
    for p in passwords:
        if is_valid(p["value"], p["letter"], p["min"], p["max"]):
            count += 1
    return count

def main():
    passwords = read_passwords_from_input("./input.txt")
    print(f"Number of valid passswords (old job): {count_valid(passwords, old_job_policy)}")
    print(f"Number of valid passswords (current job): {count_valid(passwords, current_job_policy)}")

if __name__ == "__main__":
    main()