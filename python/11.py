from copy import deepcopy
from dataclasses import dataclass
from math import prod
from typing import Callable


@dataclass
class Monkey:
    num: int
    items: list[int]
    operation: Callable
    test_worry_level: Callable
    divisor: int
    inspected: int = 0

    def make_turn(self, common_divisor=None):
        for item in self.items:
            inspection = self.operation(item)
            # print(f' Worry level: {after_inspection}')
            if not common_divisor:
                after_inspection = inspection // 3
            else:
                after_inspection = inspection % common_divisor
            # print(f' Bored worry level: {after_bored_item}')

            monkey_to_throw_to = MONKEYS[self.test_worry_level(after_inspection)]
            monkey_to_throw_to.catch(after_inspection)
            # print(f' Throwed to monkey number {monkey_to_throw_to.num}')

            self.inspected += 1
        self.items = []

    def catch(self, item):
        self.items.append(item)


if __name__ == "__main__":
    # Too lazy to parse the monkeys from file ...
    m_0 = Monkey(
        0,
        [83, 97, 95, 67],
        lambda old: old * 19,
        lambda item: 2 if item % 17 == 0 else 7,
        divisor = 17,
    )

    m_1 = Monkey(
        1,
        [71, 70, 79, 88, 56, 70],
        lambda old: old + 2,
        lambda item: 7 if item % 19 == 0 else 0,
        divisor = 19,
    )

    m_2 = Monkey(
        2,
        [98, 51, 51, 63, 80, 85, 84, 95],
        lambda old: old + 7,
        lambda item: 4 if item % 7 == 0 else 3,
        divisor = 7,
    )

    m_3 = Monkey(
        3,
        [77, 90, 82, 80, 79],
        lambda old: old + 1,
        lambda item: 6 if item % 11 == 0 else 4,
        divisor = 11,
    )

    m_4 = Monkey(
        4,
        [68],
        lambda old: old * 5,
        lambda item: 6 if item % 13 == 0 else 5,
        divisor = 13,
    )

    m_5 = Monkey(
        5,
        [60, 94],
        lambda old: old + 5,
        lambda item: 1 if item % 3 == 0 else 0,
        divisor = 3,
    )

    m_6 = Monkey(
        6,
        [81, 51, 85],
        lambda old: old * old,
        lambda item: 5 if item % 5 == 0 else 1,
        divisor = 5,
    )

    m_7 = Monkey(
        7,
        [98, 81, 63, 65, 84, 71, 84],
        lambda old: old + 3,
        lambda item: 2 if item % 2 == 0 else 3,
        divisor = 2,
    )

    MONKEYS = {
        0: m_0,
        1: m_1,
        2: m_2,
        3: m_3,
        4: m_4,
        5: m_5,
        6: m_6,
        7: m_7
    }

    # Part 1
    # for i in range(20):
    #     for monkey in MONKEYS.values():
    #         # print(f'--- MONKEY {monkey.num} ---')
    #         monkey.make_turn()
    # monkeys = sorted([m for m in MONKEYS.values()], key=lambda m: m.inspected)[-2:]
    # print(monkeys[0].inspected * monkeys[1].inspected)

    # Part 2 - beware to run without part 1 to not modify monkeys ...
    common_divisor = prod([m.divisor for m in MONKEYS.values()])
    for i in range(10_000):
        for monkey in MONKEYS.values():
            # print(f'--- MONKEY {monkey.num} ---')
            monkey.make_turn(common_divisor)
    monkeys = sorted([m for m in MONKEYS.values()], key=lambda m: m.inspected)[-2:]
    print(monkeys[0].inspected * monkeys[1].inspected)
