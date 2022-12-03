# Link to puzzle: https://adventofcode.com/2022/day/3

def parse_file():
    with open('input.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]


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


def solve1(sacks):
    score = 0
    for sack in sacks:
        match = find_match(sack)
        score += value(match)
    print(score)


def solve2(sacks):
    score = find_match_2(sacks)
    print(score)


if __name__ == "__main__":
    solve1(parse_file())
    solve2(parse_file())
