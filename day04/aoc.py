from parse import *
import validators as v

def parse_field(field_str):
    parsed = parse("{}:{}", field_str)
    return {parsed[0]: parsed[1]}

def parse_passport(passport_str):
    field_strs = passport_str.split()
    fields = []
    for field_str in field_strs:
        fields.append(parse_field(field_str))
    return fields

def read_lines_from_input(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return [line.rstrip() for line in lines]

def read_passports_from(lines):
    passports = []
    current_passport = ""
    for line in lines:
        if line == "":
            passports.append(parse_passport(current_passport.strip()))
            current_passport = ""
        else:
            current_passport += f"{line} "
    passports.append(parse_passport(current_passport.strip()))
    return passports

def in_passport(key, passport):
    return any(key in field for field in passport)

def has_required_fields(passport, requirements = {}):
    for field, params in requirements.items():
        if params["required"] and not in_passport(field, passport):
            return False
    return True

def has_valid_fields(passport, requirements):
    validations = []
    for field in passport:
        key = list(field.keys())[0]
        value = list(field.values())[0]
        validator = requirements[key]["validator"]
        if validator != None:
            validations.append(validator(value))
    return all(validations)

def is_valid(p, r):
    return has_required_fields(p, r) and has_valid_fields(p, r)

def count_valid_passports(passports, requirements):
    count = 0
    for passport in passports:
        if is_valid(passport, requirements):
            count += 1
    return count

def main():
    lines = read_lines_from_input("./input.txt")
    passports = read_passports_from(lines)

    requirements = {
        "byr": { "required": True, "validator": v.byr_validator},
        "iyr": { "required": True, "validator": v.iyr_validator},
        "eyr": { "required": True, "validator": v.eyr_validator},
        "hgt": { "required": True, "validator": v.hgt_validator},
        "hcl": { "required": True, "validator": v.hcl_validator},
        "ecl": { "required": True, "validator": v.ecl_validator},
        "pid": { "required": True, "validator": v.pid_validator},
        "cid": { "required": False, "validator": None}
    }

    print(f"Number of valid passports: {count_valid_passports(passports, requirements)}")

if __name__ == "__main__":
    main()