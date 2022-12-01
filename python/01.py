from utils import get_input


def get_elfs(data):
    elfs = []
    elf = 0
    for calories in data:
        if calories != '':
            elf += int(calories)
        else:
            elfs.append(elf)
            elf = 0
    return elfs

def part_one(data):
    return max(get_elfs(data))

def part_two(data):
    return sum(sorted(get_elfs(data), reverse=True)[:3])


if __name__ == "__main__":
    path = 'data/01.txt'
    data = get_input(path)

    # First-part
    print(part_one(data))

    # Second-part
    print(part_two(data))


    # Shorter alternative
    elfs = [sum(map(int,elf.strip(',').split(','))) for elf in open('data/01.txt').read().replace('\n',',').split(',,')]
    part1 = max(elfs)
    part2 = sum(sorted(elfs, reverse=True)[:3])
    print(part1, part2)
