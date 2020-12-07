import re

def byr_validator(value):
    try:
        return 1920 <= int(value) and int(value) <= 2002
    except ValueError:
        return False

def iyr_validator(value):
    try:
        return 2010 <= int(value) and int(value) <= 2020
    except ValueError:
        return False

def eyr_validator(value):
    try:
        return 2020 <= int(value) and int(value) <= 2030
    except ValueError:
        return False

def hgt_validator(value):
    if re.match(r"^[0-9]{3}cm$", value):
        return 150 <= int(value[0:-2]) and int(value[0:-2]) <= 193
    elif re.match(r"^[0-9]{2}in$", value):
        return 59 <= int(value[0:-2]) and int(value[0:-2]) <= 76
    else:
        return False

def hcl_validator(value):
    return bool(re.match(r"^#([a-f0-9]{6})$", value))

def ecl_validator(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def pid_validator(value):
    return bool(re.match(r"^[0-9]{9}$", value))