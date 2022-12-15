from utils import get_input


def load_cave(data):
    cave = {}
    for rocks in data:
        rocks = rocks.split(' -> ')
        for start in range(len(rocks)-1):
            rock_start_x, rock_start_y = map(int, rocks[start].split(','))
            rock_end_x, rock_end_y = map(int, rocks[start+1].split(','))

            cave[(rock_start_x, rock_start_y)] = '#'
            cave[(rock_end_x, rock_end_y)] = '#'

            if rock_start_x == rock_end_x:
                # vertical
                range_start = min([rock_start_y, rock_end_y])
                range_end = max([rock_start_y, rock_end_y])
                for y in range(range_start+1, range_end+1):
                    cave[(rock_start_x, y)] = '#'
            if rock_start_y == rock_end_y:
                # horizontal
                range_start = min([rock_start_x, rock_end_x])
                range_end = max([rock_start_x, rock_end_x])
                for x in range(range_start+1, range_end+1):
                    cave[(x, rock_start_y)] = '#'
    void_start = max([y for _, y in cave])
    return cave, void_start

def sand_can_fall(cave, void_start, sand:tuple[int,int], is_void_floor, sand_source) -> tuple[int,int]:
    sand_x, sand_y = sand

    if not is_void_floor and sand_y >= void_start:
        # Falls into void
        return sand, True

    sand_in_all_directions = []

    directions = [(0, 1), (-1, 1), (1, 1)]
    for x, y in directions:
        new_sand = (sand_x + x, sand_y + y)

        tile = cave.get(new_sand, '.')

        ## Part 2
        if is_void_floor and new_sand[1] == void_start + 2:
            tile = '#'
        sand_in_all_directions.append(tile)
        ##

        # Keeps falling down
        if tile == '.':
            return new_sand, False

    ## Part 2, end if all directions of original sand are full of sand
    if sand == sand_source and all(map(lambda tile: tile == 'o', sand_in_all_directions)):
        return sand, True

    # Should trigger rest
    return sand, False

def falling_sand(cave, void_start, sand_source=(500,0), is_void_floor=False):
    sand = sand_source
    while (res := sand_can_fall(cave, void_start, sand, is_void_floor, sand_source)):
        new_sand, is_void = res

        if is_void:
            return False # reached void

        if new_sand == sand:
            break # sand should rest

        # update possition and keep falling
        sand = new_sand

    # Save rest position
    cave[new_sand] = 'o'
    return True

def part_one(cave, void_start):
    sand_counter = 0
    while falling_sand(cave, void_start):
        sand_counter += 1
    return sand_counter

def part_two(cave, void_start):
    sand_counter = 0
    while falling_sand(cave, void_start, is_void_floor=True):
        sand_counter += 1
    return sand_counter + 1

if __name__ == "__main__":
    path = 'data/14.txt'
    data = get_input(path)

    # First-part
    print(part_one(*load_cave(data)))

    # Second-part
    print(part_two(*load_cave(data)))
