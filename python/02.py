from utils import get_input

oponet_map = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}

points = {
    'A': 1,  # Rock
    'B': 2,  # Paper
    'C': 3,  # Scissors
}

loses_over = {
    'A': 'C',
    'B' : 'A',
    'C': 'B'
}

def part_one(rounds: list[str, str]):
    total = 0
    for oponent, me in rounds:
        score = 0
        if oponent == me: #draw
            score = 3
        elif oponent == loses_over[me]:
            score = 6
        total += score + points[me]
    return total

def part_two(rounds):
    wins_over = {value:key for key,value in loses_over.items()}
    new_data = []
    for play in rounds:
        oponent, me = play.split(' ')
        if me == 'X':
            new_data.append([oponent, loses_over[oponent]])
        elif me == 'Y':
            new_data.append([oponent, oponent])
        elif me == 'Z':
            new_data.append([oponent, wins_over[oponent]])
    return part_one(new_data)

def sync_labels(data):
    return [
        [player.replace(player,oponet_map.get(player, player))
        for player in line.split(' ')]
        for line in data
    ]


if __name__ == "__main__":
    path = 'data/02.txt'
    raw_data = get_input(path)

    data = sync_labels(raw_data)

    # First-part
    print(part_one(data))

    # Second-part
    print(part_two(raw_data))
