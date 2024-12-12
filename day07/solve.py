#!/usr/bin/env python3

from z3 import *
from aocd import get_puzzle
from alive_progress import alive_bar

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

def solve_for_vals(vals, o_sum, tot, no_concat=True):
        s = Solver()
        numbers = [BitVec(f'n{i}',64) for i in range(len(vals))]
        for i in range(len(vals)):
            s.add(numbers[i] == vals[i])

        # There are +, *, and || concatenation operators
        operator = [BitVec("o{}".format(i), 64) for i in range(len(vals)-1)]
        for i in range(len(vals)-1):
            if no_concat:
                s.add(Or(operator[i] == 0, operator[i] == 2))
            else:
                s.add(Or(operator[i] == 0, operator[i] == 1, operator[i] == 2))
        
        # Build expression
        expr = numbers[0]
        for i in range(len(vals)-1):
            if no_concat:
                expr = If(operator[i] == 0, expr + numbers[i+1],
                       If(operator[i] == 2, expr * numbers[i+1], 0))
            else:
                expr = If(operator[i] == 0, expr + numbers[i+1],
                       If(operator[i] == 1, If(numbers[i+1] < 10, expr*10, If(numbers[i+1] < 100, expr*100, expr*1000)) + numbers[i+1],
                       If(operator[i] == 2, expr * numbers[i+1], 0)))
        
        # Constrain expression to be equal to num
        s.add(expr == o_sum)

        ret = s.check()
        if ret == sat:
            tot.append(o_sum)


def solve_p1(puzzle):
    out = parse(puzzle)

    tot = []
    with alive_bar(len(out)) as bar:
        for o in out:
            o_spl = o.split()
            o_sum = int(o_spl[0][:-1])
            vals = [int(x) for x in o_spl[1:]]

            solve_for_vals(vals, o_sum, tot, no_concat=True)
            bar()
        
    print_answers(puzzle, 1, sum(tot))
    

def solve_p2(puzzle):
    out = parse(puzzle)

    tot = []
    with alive_bar(len(out)) as bar:
        for o in out:
            o_spl = o.split()
            o_sum = int(o_spl[0][:-1])
            vals = [int(x) for x in o_spl[1:]]

            solve_for_vals(vals, o_sum, tot, no_concat=False)
            bar()

    print_answers(puzzle, 2, sum(tot))

# TODO Refactor into common library
puzzle = get_puzzle(day=7, year=2024)
examples = puzzle.examples

for ex in examples: solve_p1(ex)
solve_p1(puzzle)

for ex in examples: solve_p2(ex)
solve_p2(puzzle)