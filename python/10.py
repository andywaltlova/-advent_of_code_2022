from utils import get_input


def move_n_cycles(strengths, register, cycle_num, n):
    for _ in range(n):
        cycle_num += 1

        if cycle_num in range(20, 221, 40):
            strengths.append(register * cycle_num)

        # Part 2
        sprite = [register-1, register, register+1]
        pixel = '#' if (cycle_num-1) % 40 in sprite else '.'
        print(pixel, end='')
        if cycle_num in range(40, 241, 40):
            print()

    return cycle_num


def do_instructions(data):
    strengths = []
    cycle_num = 0
    register = 1
    for line in data:
        match line[:4]:
            case 'addx':
                move_n_cycles(strengths, register, cycle_num, 2)
                register += int(line[5:])
                cycle_num += 2
            case 'noop':
                move_n_cycles(strengths, register, cycle_num, 1)
                cycle_num += 1
    return sum(strengths)





if __name__ == "__main__":
    path = 'data/10.txt'
    data = get_input(path)

    print(do_instructions(data))