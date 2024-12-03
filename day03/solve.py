#!/usr/bin/env python3

from aocd import get_puzzle
import re

def parse(puzzle):
    out = []
    for line in puzzle.input_data.splitlines():
        out.append(line)
    return out

# TODO Refactor into common library
def print_answers(puzzle, part, answer):
    print(f'Part {part} - {type(puzzle).__name__}: {answer}', end='')
    if hasattr(puzzle, 'answers'):
        expected = puzzle.answers[part-1]
        print(f' ({expected})')
    else:
        print()

def solve_p1(puzzle):
    out = parse(puzzle)

    tot = []
    for o in out:
        matches = re.findall(r'mul\((\d+)\,(\d+)\)', o)
        for m in matches:
            tot.append(int(m[0]) * int(m[1]))

    print_answers(puzzle, 1, sum(tot))

def solve_p2(puzzle):
    out = parse(puzzle)
    # Workaround for missing p2 examples
    if type(puzzle).__name__ == "Example":
        out = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

    tot = []
    mult_on = True
    for o in out:
        matches = re.findall(r'mul\((\d+)\,(\d+)\)|(do)\(\)|(don\'t)\(\)', o)
        for m in matches:
            if m[2] != '':
                mult_on = True
                continue
            if m[3] != '':
                mult_on = False
                continue

            if mult_on:
                tot.append(int(m[0]) * int(m[1]))

    print_answers(puzzle, 2, sum(tot))

# TODO Refactor into common library
puzzle = get_puzzle(day=3, year=2024)
examples = puzzle.examples

for ex in examples: solve_p1(ex)
solve_p1(puzzle)

for ex in examples: solve_p2(ex)
solve_p2(puzzle)
