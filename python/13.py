from dataclasses import dataclass
from functools import cmp_to_key
from itertools import zip_longest


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip_longest(left, right, fillvalue=None):
            if l is None:
                return -1
            if r is None:
                return 1
            cmp = compare(l, r)
            if cmp != 0:
                return cmp
        return 0

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    return compare(left, right)

@dataclass
class PacketPair:
    index: int
    a: int | list[list[int] | int]
    b: int | list[list[int] | int]


    def compare_packets(self):
        return compare(self.a, self.b) < 0


def load_data(path='data/13.txt') -> list[PacketPair]:
    with open(path) as file:
        content = file.read()
    pairs: list[PacketPair] = []
    for index, pair in enumerate(content.split('\n\n')):
        a_b = pair.split('\n')
        pairs.append(PacketPair(index+1, eval(a_b[0]), eval(a_b[1])))
    return pairs


if __name__ == "__main__":
    pairs = load_data('data/13.txt')

    assert PacketPair(1, [1,1,3,1,1], [1,1,5,1,1]).compare_packets()
    assert PacketPair(2, [[1],[2,3,4]], [[1],4]).compare_packets()
    assert not PacketPair(3, [9], [[8,7,6]]).compare_packets()
    assert PacketPair(4, [[4,4],4,4], [[4,4],4,4,4]).compare_packets()
    assert not PacketPair(5, [7,7,7,7], [7,7,7]).compare_packets()
    assert PacketPair(6, [], [3]).compare_packets()
    assert not PacketPair(7, [[[]]], [[]]).compare_packets()
    assert not PacketPair(8, [1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]).compare_packets()

    # Part 1
    print(sum([pair.index for pair in pairs if pair.compare_packets()]))

    # Part 2
    packets = []
    for p in pairs:
        packets.append(p.a)
        packets.append(p.b)
    packets.append([[2]])
    packets.append([[6]])


    packets = sorted(packets, key=cmp_to_key(compare))
    a, b = packets.index([[2]]) + 1, packets.index([[6]]) + 1
    print(a*b)



