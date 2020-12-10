def read_parent(parent_string):
    return parent_string.strip().rsplit(' ', 1)[0]

def read_children_strings(line):
    children_strings = line[0:-1].split(',')
    return [ child_string.lstrip() for child_string in children_strings]

def read_child(child_string):
    color_strings = child_string.split()[1:3]
    return " ".join(color_strings)

def read_children(children_string, empty_bag_string = "no other bags"):
    children_strings = read_children_strings(children_string)
    children = []
    for child_string in children_strings:
        if child_string != empty_bag_string:
            children.append(read_child(child_string))
    return children

def read_rule(line):
    words = line.split("contain", 1)
    parent = read_parent(words[0])
    children = read_children(words[-1])
    return { parent: children }

def read_rules_from_input(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    rules = {}
    for line in lines:
        rules.update(read_rule(line.strip()))
    return rules

def exist_way_to(root_color, target_color, rules):
    print(f"root: {root_color} target: {target_color}")
    if root_color == target_color:
        print("\tFound a match")
        return True
    elif len(rules[root_color]) == 0:
        print("\tEnd node")
        return False
    else:
        flags = []
        for color in rules[root_color]:
            print(f"\tGoing down to {color}")
            flags.append(exist_way_to(color, target_color, rules))
        return any(flags)

def main():
    rules = read_rules_from_input("./input.txt")

    # print(read_rule("dim tan bags contain 3 shiny teal bags, 5 bright white bags, 4 striped bronze bags."))

    print(f"{exist_way_to('posh crimson', 'shiny gold', rules)}")

    # count = 0
    # for color in rules.keys():
    #     if exist_way_to(color, 'shiny gold', rules):
    #         count += 1

    # print(f"Number of bag colors that can eventually contain at least one shiny gold bag: {count}")

    # Note: 227 is too high

if __name__ == "__main__":
    main()