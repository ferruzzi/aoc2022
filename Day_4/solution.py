# Link to puzzle: https://adventofcode.com/2022/day/4
import re

from utils import provide_inputs


def parse_pair_to_sets(pair):
    areas = re.findall(r'[0-9]+', pair)
    elf1 = set(range(int(areas[0]), int(areas[1]) + 1))
    elf2 = set(range(int(areas[2]), int(areas[3]) + 1))
    return elf1, elf2


@provide_inputs
def solve_1_oneliner(inputs):
    return sum([len(areas[0].intersection(areas[1])) == min(len(areas[0]), len(areas[1])) for areas in [[set(range(int(elf[0][0]), int(elf[0][1])+1)), set(range(int(elf[1][0]), int(elf[1][1])+1))] for elf in [[elves[0].split('-'), elves[1].split('-')] for elves in [pair.split(',') for pair in inputs]]]])


@provide_inputs
def solve_2_oneliner(inputs):
    return sum([bool(areas[0].intersection(areas[1])) for areas in [[set(range(int(elf[0][0]), int(elf[0][1])+1)), set(range(int(elf[1][0]), int(elf[1][1])+1))] for elf in [[elves[0].split('-'), elves[1].split('-')] for elves in [pair.split(',') for pair in inputs]]]])


@provide_inputs
def solve_1(inputs):
    score = 0
    for pair in inputs:
        elf1, elf2 = parse_pair_to_sets(pair)
        score += len(elf1.intersection(elf2)) == min(len(elf1), len(elf2))
    print(score)
    return score


@provide_inputs
def solve_2(inputs):
    score = 0
    for pair in inputs:
        elf1, elf2 = parse_pair_to_sets(pair)
        score += int(bool((elf1.intersection(elf2))))
    print(score)
    return score


if __name__ == "__main__":
    assert solve_1() == 507
    assert solve_2() == 897
    assert solve_1_oneliner() == 507
    assert solve_2_oneliner() == 897
