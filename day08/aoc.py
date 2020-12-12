from parse import *

def parse_instruction(line):
    parsed = parse("{} {}", line)
    return {
        "operation": parsed[0],
        "argument": int(parsed[1]),
        "executed": False
    }

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
    while not boot_code[index]["executed"]:
        state = execute(boot_code[index], index, accumulator)
        boot_code[index]["executed"] = True
        accumulator = state["accumulator"]
        index = state["next"]
    return accumulator

def main():
    boot_code = read_boot_code_from("./input.txt")
    accumulator = run(boot_code)
    print(f"Accumulator before infinite loop: {accumulator} (part 1)")

if __name__ == "__main__":
    main()