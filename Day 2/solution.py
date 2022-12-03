# Link to puzzle: https://adventofcode.com/2022/day/2

from enum import IntEnum

from utils import provide_inputs

their_plays = ["A", "B", "C"]
my_plays = ["X", "Y", "Z"]


class ThenI(IntEnum):
    win = 6
    lose = 0
    draw = 3


def score_match_pt_1(_match):
    # PT 1
    # Them: A for Rock, B for Paper, and C for Scissors
    # Me: X for Rock, Y for Paper, and Z for Scissors
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # 0 if you lost, 3 if the round was a draw, and 6 if you won
    their_play = their_plays.index(_match[0])
    my_play = my_plays.index(_match[-1])

    score = my_play + 1
    if their_play == my_play:
        score += ThenI.draw
    elif (their_play + 1) % 3 == my_play:
        score += ThenI.win
    else:
        score += ThenI.lose

    return score


def score_match_pt_2(_match):
    # PT 2
    # Them: A for Rock, B for Paper, and C for Scissors
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # 0 if you lost, 3 if the round was a draw, and 6 if you won
    their_play = their_plays.index(_match[0])
    desired_result = _match[-1]

    score = my_plays.index(desired_result) * 3
    if desired_result == "Z":
        # I win
        my_play = my_plays[(their_play + 1) % 3]
    elif desired_result == "X":
        # I lose
        my_play = my_plays[their_play - 1]
    else:
        my_play = my_plays[their_play]
    score += my_plays.index(my_play) + 1
    return score


@provide_inputs
def solve1(inputs):
    total_score = 0
    for match in inputs:
        total_score += score_match_pt_1(match.strip())
    assert total_score == 11150
    print(f'pt 1: {total_score}')


@provide_inputs
def solve2(inputs):
    total_score = 0
    for match in inputs:
        total_score += score_match_pt_2(match.strip())
    assert total_score == 8295
    print(f'pt 2: {total_score}')


if __name__ == "__main__":
    solve1()
    solve2()


