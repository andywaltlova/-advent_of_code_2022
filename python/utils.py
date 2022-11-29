def get_input(path: str, convert_fce=str) -> list[str]:
    with open(path) as f:
        lines = [convert_fce(line.strip()) for line in f.readlines()]
    return lines

def get_number_input(path: str) -> list[int]:
    return get_input(path, int)
