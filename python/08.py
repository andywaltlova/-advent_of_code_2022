from utils import get_input


def get_tree_grid(data):
    tree_grid = {}
    for x in range(len(data)):
        for y in range(len(data[x])):
            tree_grid[(x,y)] = int(data[x][y])
    return tree_grid

def directional_visibility(original_tree, x, y, x_fce, y_fce):
    scenic_score = 0
    while (tree := trees.get((x, y))) is not None:
        scenic_score += 1
        if tree >= original_tree:
            return False, scenic_score
        x = x_fce(x)
        y = y_fce(y)
    return True, scenic_score

def check_visibility(x,y, trees):
    original_tree = trees[(x,y)]
    return  x == 0 or x == MAX_EDGE or y == 0 or y == MAX_EDGE or \
            directional_visibility(original_tree, x-1, y, lambda x: x-1, lambda y: y)[0] or \
            directional_visibility(original_tree, x+1, y, lambda x: x+1, lambda y: y)[0] or \
            directional_visibility(original_tree, x, y-1, lambda x: x, lambda y: y-1)[0] or \
            directional_visibility(original_tree, x, y+1, lambda x: x, lambda y: y+1)[0]

def get_scenic_score(original_tree, x,y, trees):
    if x == 0 or x == MAX_EDGE or y == 0 or y == MAX_EDGE:
        return 0
    return directional_visibility(original_tree, x-1, y, lambda x: x-1, lambda y: y)[1] * \
           directional_visibility(original_tree, x+1, y, lambda x: x+1, lambda y: y)[1] * \
           directional_visibility(original_tree, x, y-1, lambda x: x, lambda y: y-1)[1] * \
           directional_visibility(original_tree, x, y+1, lambda x: x, lambda y: y+1)[1]

def part_one(trees):
    tree_sum = 0
    for x,y in trees:
        tree_sum += check_visibility(x, y, trees)
    return tree_sum

def part_two(trees):
    return max([get_scenic_score(trees[(x,y)], x,y, trees) for x,y in trees])


if __name__ == "__main__":
    path = 'data/08.txt'
    data = get_input(path)
    MAX_EDGE = len(data) - 1
    trees = get_tree_grid(data)

    # First-part
    print(part_one(trees))

    # Second-part
    print(part_two(trees))
