from copy import deepcopy

from utils import get_input


def get_stacks(data):
    stacks: dict[int, list[int]] = {}
    for line in data:
        # End of stacks
        if line[1].isdigit():
            break

        stack_num = 0
        for crate_index in range(1, len(line)+1, 4):
            stack_num +=1

            crate = line[crate_index]
            if crate == ' ':
                continue
            if stack_num in stacks:
                stacks[stack_num].insert(0, crate)
            else:
                stacks[stack_num] = [crate]
    return stacks

def get_rearrangment_steps(data):
    steps = []
    for line in data:
        if line.startswith('move'):
            _, num, _, from_stack, _, to_stack = line.split(' ')
            steps.append((int(num), int(from_stack), int(to_stack)))
    return steps

def get_the_top_crates(stacks):
    return ''.join([stacks[i][-1] for i in range(1,10)])

def part_one(steps, stacks):
    for num, from_stack, to_stack in steps:
        for i in range(num):
            crate = stacks[from_stack].pop()
            stacks[to_stack].append(crate)
    return stacks

def part_two(steps, stacks):
    for num, from_stack, to_stack in steps:
        # Get crates
        crates = stacks[from_stack][-num:]
        # Put them to new stacks
        stacks[to_stack] = stacks[to_stack] + crates
        # Delete from original stack
        stacks[from_stack] = stacks[from_stack][:-num]
    return stacks


if __name__ == "__main__":
    path = 'data/05.txt'
    data = get_input(path)
    stacks = get_stacks(data)
    steps = get_rearrangment_steps(data)

    # First-part
    print(get_the_top_crates(part_one(steps, deepcopy(stacks))))

    # Second-part
    print(get_the_top_crates(part_two(steps, deepcopy(stacks))))

