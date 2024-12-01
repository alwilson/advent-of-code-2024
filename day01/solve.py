#!/usr/bin/env python3

from aocd import get_puzzle

def parse(puzzle):
    left = []
    right = []
    for line in puzzle.input_data.splitlines():
        match line.split():
            case [lhs, rhs]:
                left.append( int(lhs))
                right.append(int(rhs))
    return left, right

# TODO Refactor into common library
def print_answers(puzzle, part, answer):
    print(f'Part {part} - {type(puzzle).__name__}: {answer}', end='')
    if hasattr(puzzle, 'answers'):
        expected = puzzle.answers[part-1]
        print(f' ({expected})')
    else:
        print()

def solve_p1(puzzle):
    l, r = parse(puzzle)
    l.sort()
    r.sort()
    diffs = [abs(i-j) for i, j in zip(l,r)]

    print_answers(puzzle, 1, sum(diffs))

def solve_p2(puzzle):
    l, r = parse(puzzle)
    counts = {}
    for ri in r:
        counts.setdefault(ri, 0)
        counts[ri] += 1

    tot = []
    for li in l:
        if li in counts:
            tot.append(li * counts[li])

    print_answers(puzzle, 2, sum(tot))

# TODO Refactor into common library
puzzle = get_puzzle(day=1, year=2024)
examples = puzzle.examples

for ex in examples: solve_p1(ex)
solve_p1(puzzle)

for ex in examples: solve_p2(ex)
solve_p2(puzzle)
