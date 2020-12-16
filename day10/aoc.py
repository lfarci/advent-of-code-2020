def read_joltage_ratings(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return [ int(line.strip()) for line in lines ]

def get_builtin_adapter_rating(joltage_ratings, difference = 3):
    return max(joltage_ratings) + difference

def is_connectable_adapter(input_jolt_rating, ouput_jolt_rating):
    for difference in [1, 2, 3]:
        if ouput_jolt_rating - difference == input_jolt_rating:
            return True
    return False

def find_connectable_adapter(input_rating, adapters, tested):
    for adapter_rating in adapters:
        is_connectable = is_connectable_adapter(input_rating, adapter_rating)
        is_tested = tested[adapters.index(adapter_rating)]
        if not is_tested and is_connectable:
            return adapter_rating
    return None

def get_adapters_chain(source, adapters, device):
    adapters = sorted(adapters)
    tested = [ False for a in adapters ]
    current = source
    chain = []
    while not all(tested):
        connectable = find_connectable_adapter(current, adapters, tested)
        chain.append(connectable)
        tested[adapters.index(connectable)] = True
        current = connectable
    return [source] + chain + [device]

def get_joltage_differences_distribution(source, adapters, device):
    chain = get_adapters_chain(source, adapters, device)
    distribution = {}
    for i in range(1, len(chain)):
        difference = chain[i] - chain[i - 1]
        if difference in distribution:
            distribution[difference] += 1
        else:
            distribution[difference] = 1
    return distribution

def main():
    joltage_ratings = read_joltage_ratings("./input.txt")
    differences_distribution = get_joltage_differences_distribution(
        source=0,
        adapters=joltage_ratings,
        device=get_builtin_adapter_rating(joltage_ratings)
    )
    answer = differences_distribution[1] * differences_distribution[3]
    print(f"Answer: {answer} (part 1)")

if __name__ == "__main__":
    main()