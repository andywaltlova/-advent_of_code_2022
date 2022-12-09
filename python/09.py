from utils import get_input


def is_diagonal(tail, head):
    up_right_diagonal = tail['x'] == head['x'] - 1 and tail['y'] == head['y'] + 1
    up_left_diagonal = tail['x'] == head['x'] - 1 and tail['y'] == head['y'] - 1
    down_right_diagonal = tail['x'] == head['x'] + 1 and tail['y'] == head['y'] + 1
    down_left_diagonal = tail['x'] == head['x'] + 1 and tail['y'] == head['y'] - 1
    return any([down_left_diagonal, down_right_diagonal, up_left_diagonal, up_right_diagonal])

def is_on_top(tail, head):
    return (head['x'],head['y']) == (tail['x'],tail['y'])

def is_adjacent(tail, head):
    left = tail['x'] == head['x'] and tail['y'] == head['y'] - 1
    right = tail['x'] == head['x'] and tail['y'] == head['y'] + 1
    down = tail['x'] == head['x'] + 1 and tail['y'] == head['y']
    up = tail['x'] == head['x'] - 1 and tail['y'] == head['y']
    return is_diagonal(tail, head) or  up or down or right or left

def move_tail(tail, head, direction):
    # move head
    match direction:
        case 'R':
            head['y'] += 1
        case 'L':
            head['y'] -= 1
        case 'U':
            head['x'] -= 1
        case 'D':
            head['x'] += 1

    # check when don't move
    if is_adjacent(tail, head) or is_on_top(tail, head):
        return tail, head

    # move tail
    if head['x'] == tail['x'] and tail['y'] == head['y'] - 2:
        # move one up
        tail['y'] += 1
    elif head['x'] == tail['x'] and tail['y'] == head['y'] + 2:
        # move one down
        tail['y'] -= 1
    elif head['x'] + 2 == tail['x'] and tail['y'] == head['y']:
        # move one right
        tail['x'] -= 1
    elif head['x'] - 2 == tail['x'] and tail['y'] == head['y']:
        # move one left
        tail['x'] += 1
    # Check if one of the diagonal positions 1-8
    # # 2 # 3 # #
    # 1 # T # 4 #
    # # T H T # #
    # 8 # T # 5 #
    # # 7 # 6 # #
    is_2 = head['x'] - 2 == tail['x'] and tail['y'] == head['y'] - 1
    is_3 = head['x'] - 2 == tail['x'] and tail['y'] == head['y'] + 1

    is_7 = head['x'] + 2 == tail['x'] and tail['y'] == head['y'] - 1
    is_6 = head['x'] + 2 == tail['x'] and tail['y'] == head['y'] + 1

    is_1 = head['x'] - 1 == tail['x'] and tail['y'] == head['y'] - 2
    is_8 = head['x'] + 1 == tail['x'] and tail['y'] == head['y'] - 2

    is_4 = head['x'] - 1 == tail['x'] and tail['y'] == head['y'] + 2
    is_5 = head['x'] + 1 == tail['x'] and tail['y'] == head['y'] + 2

    if is_1 or is_8:
        tail = {'x': head['x'], 'y': head['y'] - 1}
    if is_4 or is_5:
        tail = {'x': head['x'], 'y': head['y'] + 1}
    if is_2 or is_3:
        tail = {'x': head['x'] - 1, 'y': head['y']}
    if is_7 or is_6:
        tail = {'x': head['x'] + 1, 'y': head['y']}
    return tail, head



def part_one(data):
    positions = set()
    head = {'x': 0, 'y': 0}
    tail = {'x': 0, 'y': 0}
    for step in data:
        direction, distance = step.split(' ')
        for i in range(int(distance)):
            # print(f'{direction} {distance}({i})')
            tail, head = move_tail(tail, head, direction)
            # print(tail, head)
            positions.add((tail['x'], tail['y']))
    return len(positions)

def part_two(data):
    # please no ..
    pass


if __name__ == "__main__":
    path = 'data/09.txt'
    data = get_input(path)

    # First-part
    print(part_one(data))

    # Second-part
    print(part_two(data))
