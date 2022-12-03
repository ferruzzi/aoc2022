# Link to puzzle: https://adventofcode.com/2022/day/3
from utils import provide_inputs


def find_match(sack):
    half = len(sack) // 2
    return [item for item in sack[half:] if item in sack[:half]][0]


def value(item: str):
    return (ord(item.lower()) - 96) + (item.isupper() * 26)


def find_match_2(sacks, score=0):
    try:
        this_match = [item for item in sacks[0] if (item in sacks[1]) and (item in sacks[2])][0]
        return find_match_2(sacks[3:], score + value(this_match))
    except IndexError:
        return score


@provide_inputs
def solve1(inputs):
    score = 0
    for sack in inputs:
        match = find_match(sack)
        score += value(match)
    assert score == 7845
    print(f'pt1: {score}')


@provide_inputs
def solve2(inputs):
    score = find_match_2(inputs)
    assert score == 2790
    print(f'pt2: {score}')


if __name__ == "__main__":
    solve1()
    solve2()
