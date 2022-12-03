# Link to puzzle: https://adventofcode.com/2022/day/3
from utils import provide_inputs


@provide_inputs
def parse_file(inputs):
    result = []
    tmp_dict = []

    for line in inputs:
        try:
            tmp_dict.append(int(line))
        except ValueError:
            result.append(tmp_dict)
            tmp_dict = []

    return result


def solve():
    parsed_file = parse_file()
    subtotals = [sum(elf) for elf in parsed_file]
    pt1 = max(subtotals)
    assert pt1 == 70720
    print(f'pt 1: found {pt1} solution: 70720')
    top_three = sorted(subtotals, reverse=True)[:3]
    pt2 = sum(top_three)
    assert pt2 == 207148
    print(f'pt 2: {pt2}')


if __name__ == "__main__":
    solve()
