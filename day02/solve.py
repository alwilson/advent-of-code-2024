#!/usr/bin/env python3

from aocd import get_puzzle

def parse(puzzle):
    out = []
    for line in puzzle.input_data.splitlines():
        out.append([int(i) for i in line.split()])
    return out

# TODO Refactor into common library
def print_answers(puzzle, part, answer):
    print(f'Part {part} - {type(puzzle).__name__}: {answer}', end='')
    if hasattr(puzzle, 'answers'):
        expected = puzzle.answers[part-1]
        print(f' ({expected})')
    else:
        print()

def follows_rules(level):
    diffs = [i-j for i, j in zip(level[:-1], level[1:])]

    not_over_3 = all([abs(i) <= 3 for i in diffs])
    all_positive = all([i > 0 for i in diffs])
    all_negative = all([i < 0 for i in diffs])

    if not_over_3 and (all_positive or all_negative):
        return True

def solve_p1(puzzle):
    out = parse(puzzle)

    tot = 0
    for level in out:
        if follows_rules(level):
            tot += 1

    print_answers(puzzle, 1, tot)

def solve_p2(puzzle):
    out = parse(puzzle)

    tot = 0
    for level in out:
        # print(level, tot)
        if follows_rules(level):
            tot += 1
        else:
            # Try removing one element at a time
            for i in range(len(level)):
                lvl = level[:i] + level[i+1:]
                if follows_rules(lvl):
                    tot += 1
                    break

    print_answers(puzzle, 2, tot)

# TODO Refactor into common library
puzzle = get_puzzle(day=2, year=2024)
examples = puzzle.examples

for ex in examples: solve_p1(ex)
solve_p1(puzzle)

for ex in examples: solve_p2(ex)
solve_p2(puzzle)
