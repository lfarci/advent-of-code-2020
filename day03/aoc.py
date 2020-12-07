import copy

class Forest():

    def __init__(self, grid):
        self.grid = grid

    def height(self):
        return len(self.grid)

    def width(self):
        return len(self.grid[0])

    def at(self, position):
        row = position["row"]
        column = position["column"]
        if self.width() <= position["column"]:
            column = position["column"] % self.width()
        if self.height() < position["row"]:
            row = len(self.grid) - 1
        return self.grid[row][column]

    def is_tree_at(self, position):
        return self.at(position) == "#"

    def is_arrival(self, position):
        return position["row"] >= self.height() - 1

def read_forest_from_input(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return [list(line[0:len(line) - 1]) for line in lines]

def count_trees_from(forest, position, bottom, right):
    tree_counter = 0
    current_position = copy.deepcopy(position)
    while not forest.is_arrival(current_position):
        current_position["row"] += bottom
        current_position["column"] += right
        if forest.is_tree_at(current_position):
            tree_counter += 1
    return tree_counter

def main():
    forest = Forest(read_forest_from_input("./input.txt"))
    start = {"row": 0, "column": 0}
    result = count_trees_from(forest, start, 1, 3)
    print("--- Part 1 ---")
    print(f"Number of encountered trees: {result} trees")
    print("--- Part 2 ---")
    results = [
        count_trees_from(forest, start, 1, 1),
        count_trees_from(forest, start, 1, 3),
        count_trees_from(forest, start, 1, 5),
        count_trees_from(forest, start, 1, 7),
        count_trees_from(forest, start, 2, 1),
    ]
    total = results[0]
    for n in results[1:]:
        total *= n
    print(f"Multiplication of results: {total}")


if __name__ == "__main__":
    main()