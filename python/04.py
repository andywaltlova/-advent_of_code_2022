from utils import get_input


def convert_to_ranges(data):
    ranges = []
    for pairs in data:
        a,b = pairs.split(',')
        a_start, a_end = a.split('-')
        b_start, b_end = b.split('-')
        a_range = range(int(a_start), int(a_end)+1)
        b_range = range(int(b_start), int(b_end)+1)
        ranges.append([a_range, b_range])
    return ranges

def part_one(data):
    ranges = convert_to_ranges(data)
    count = 0
    for a, b in ranges:
        a , b = set(a), set(b)
        if a.issubset(b) or b.issubset(a):
            count += 1
    return count

def part_two(data):
    ranges = convert_to_ranges(data)
    count = 0
    for a, b in ranges:
        a , b = set(a), set(b)
        if a.intersection(b):
            count += 1
    return count


if __name__ == "__main__":
    path = 'data/04.txt'
    data = get_input(path)

    # First-part
    print(part_one(data))

    # Second-part
    print(part_two(data))
