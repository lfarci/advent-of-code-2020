from parse import *
import copy

def parse_instruction(line):
    parsed = parse("{} {}", line)
    return {"operation": parsed[0], "argument": int(parsed[1])}

def read_lines_from(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines

def read_boot_code_from(path):
    instructions = []
    for line in read_lines_from(path):
        instructions.append(parse_instruction(line.strip()))
    return instructions

def execute(instruction, instruction_idx, accumulator = 0):
    next_instruction_idx = instruction_idx + 1
    if instruction["operation"] == "acc":
        accumulator += instruction["argument"]
    if instruction["operation"] == "jmp":
        next_instruction_idx = instruction_idx + instruction["argument"]
    if instruction["operation"] == "nop":
        pass
    return { "next": next_instruction_idx, "accumulator": accumulator }

def run(boot_code):
    index = 0
    accumulator = 0
    executed = [ False ] * len(boot_code)
    while index < len(boot_code) and not executed[index]:
        state = execute(boot_code[index], index, accumulator)
        executed[index] = True
        accumulator = state["accumulator"]
        index = state["next"]
    return accumulator

def terminates_normally(boot_code):
    index = 0
    executed = [ False ] * len(boot_code)
    while index < len(boot_code) and not executed[index]:
        state = execute(boot_code[index], index)
        executed[index] = True
        index = state["next"]
    return index == len(boot_code)

def fixed(boot_code, corrupted_operations = ["jmp", "nop"]):
    for index, instruction in enumerate(boot_code):
        if instruction["operation"] in corrupted_operations:
            corrupted_operation = instruction["operation"]
            patch = "jmp" if corrupted_operation == "nop" else "nop"
            boot_code[index]["operation"] = patch
            if terminates_normally(boot_code):
                fixed_boot_code = copy.deepcopy(boot_code)
                boot_code[index]["operation"] = corrupted_operation
                return fixed_boot_code
            boot_code[index]["operation"] = corrupted_operation
    return None

def main():
    boot_code = read_boot_code_from("./input.txt")
    print(f"Accumulator before infinite loop: {run(boot_code)} (part 1)")
    print(f"Accumulator after fix: {run(fixed(boot_code))} (part 2)")

if __name__ == "__main__":
    main()