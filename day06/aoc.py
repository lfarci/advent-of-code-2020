def read_lines_from_input(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return [line.rstrip() for line in lines]

def read_groups_answers_from(lines):
    groups_answers = []
    current_group_answers = ""
    for line in lines:
        if line == "":
            groups_answers.append(current_group_answers.split())
            current_group_answers = ""
        else:
            current_group_answers += f"{line} "
    groups_answers.append(current_group_answers.split())
    return groups_answers

def count_unique_positive(group_answers):
    answers = []
    for person_answers in group_answers:
        for answer in person_answers:
            if answer not in answers:
                answers.append(answer)
    return len(answers)

def count_occurences(group_answers):
    answers = {}
    for person_answers in group_answers:
        for answer in person_answers:
            answers[answer] = answers[answer] + 1 if answer in answers else 1
    return answers

def count_unanimous(group_answers):
    occurences = count_occurences(group_answers)
    count = 0
    for occurence in occurences.values():
        if occurence == len(group_answers):
            count += 1
    return count

def sum_counts(groups_answers, counter):
    total = 0
    for group_answer in groups_answers:
        total += counter(group_answer)
    return total

def main():
    lines = read_lines_from_input("./input.txt")
    groups_answers = read_groups_answers_from(lines)
    unique_positive_count = sum_counts(groups_answers, count_unique_positive)
    unanimous_count = sum_counts(groups_answers, count_unanimous)

    print(f"The sum of unique positive answers counts is {unique_positive_count} (part 1)")
    print(f"The sum of unanimous answers counts is {unanimous_count} (part 2)")

if __name__ == "__main__":
    main()