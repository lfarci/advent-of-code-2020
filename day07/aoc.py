def read_parent(parent_string):
    return parent_string.strip().rsplit(' ', 1)[0]

def read_children_strings(line):
    children_strings = line[0:-1].split(',')
    return [ child_string.lstrip() for child_string in children_strings]

def read_child(child_string):
    color_strings = child_string.split()[1:3]
    return { "amount": int(child_string[0]), "color": " ".join(color_strings) }

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
    if len(rules[root_color]) == 0:
        return False
    else:
        flags = []
        for child in rules[root_color]:
            if child["color"] == target_color:
                return True
            else:
                flags.append(exist_way_to(child["color"], target_color, rules))
        return any(flags)

def count_possible_bad_parent_for(child_color, rules):
    count = 0
    for color in rules.keys():
        if exist_way_to(color, child_color, rules):
            count += 1
    return count

def count_children(root_color, nchildren, rules):
    if len(rules[root_color]) == 0:
        return nchildren
    else:
        flags = []
        for child in rules[root_color]:
            ngrandchildren = count_children(child["color"], 0, rules)
            nchildren += child["amount"] + (child["amount"] * ngrandchildren)
        return nchildren

def main():
    rules = read_rules_from_input("./input.txt")
    count_part_01 = count_possible_bad_parent_for('shiny gold', rules)
    count_part_02 = count_children('shiny gold', 0, rules)
    print(f"Number of bag colors that can contain shiny gold bags: {count_part_01} (part 1)")
    print(f"Number of required individual bags: {count_part_02} (part 2)")

if __name__ == "__main__":
    main()