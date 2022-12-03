from utils import get_input


def get_priority(char):
    prio = ord(char) - 38
    if char.islower():
        prio = ord(char) - 96
    return prio

def part_one(data):
    commons = []
    for rucksack in data:
        middle = len(rucksack) // 2
        c_1, c_2 = set(rucksack[:middle]), set(rucksack[middle:])
        commons.append(c_1.intersection(c_2).pop())
    return sum([get_priority(c) for c in commons])

def part_two(data):
    commons = []
    for i in range(3, len(data)+1, 3):
        a, b, c = data[i-3:i]
        common = set(a) & set(b) & set(c)
        commons.append(common.pop())
    return sum([get_priority(c) for c in commons])


if __name__ == "__main__":
    path = 'data/03.txt'
    data = get_input(path)

    # First-part
    print(part_one(data))

    # Second-part
    print(part_two(data))
