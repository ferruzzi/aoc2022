# Link to puzzle: https://adventofcode.com/2022/day/3

def parse_file():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    result = []
    tmp_dict = []

    for line in lines:
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
    print(f'pt 1: {pt1}')
    top_three = sorted(subtotals, reverse=True)[:3]
    pt2 = sum(top_three)
    print(f'pt 2: {pt2}')


if __name__ == "__main__":
    solve()
