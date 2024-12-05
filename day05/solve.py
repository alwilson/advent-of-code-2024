#!/usr/bin/env python3

from aocd import get_puzzle
import z3

def parse(puzzle):
    out = []
    for line in puzzle.input_data.splitlines():
        out.append(line)

    # build up rules, which have a '|' and page orders
    rules = {}
    orderings = []
    for o in out:
        if '|' in o:
            pages = o.split('|')
            rules.setdefault(pages[0], [])
            rules[pages[0]].append(pages[1])
        elif ',' in o:
            pages = o.split(',')
            orderings.append(pages)

    return rules, orderings

# TODO Refactor into common library
def print_answers(puzzle, part, answer):
    print(f'Part {part} - {type(puzzle).__name__}: {answer}', end='')
    if hasattr(puzzle, 'answers'):
        expected = puzzle.answers[part-1]
        print(f' ({expected})')
    else:
        print()

def solve_p1(puzzle):
    rules, orderings = parse(puzzle)

    # print(rules)
    # print(orderings)

    tot = []
    for ordering in orderings:
        passing = True
        for oi, o in enumerate(ordering[:-1]):
            for p in ordering[oi+1:]:
                if p in rules and o in rules[p]:
                    # print(f'breaks rule: {o} in {p}')
                    passing = False
                    break
        # print(f'{ordering=}, {passing=}')
        if passing:
            tot.append(int(ordering[len(ordering)//2]))

    print(tot)
    print_answers(puzzle, 1, sum(tot))

def solve_p2(puzzle):
    rules, orderings = parse(puzzle)

    failed = []
    for ordering in orderings:
        passing = True
        for oi, o in enumerate(ordering[:-1]):
            for p in ordering[oi+1:]:
                if p in rules and o in rules[p]:
                    passing = False
                    break
        if not passing:
            failed.append(ordering)

    # print(failed)
    tot = []
    for fs in failed:
        # Use solver to follow ordering rules
        # except that this is probably the worst way to encode this
        # and this could probably be done faaar faster with a simple sort function...
        s = z3.Solver()
        page_nums = [z3.BitVec(f'p{i}', 8) for i in range(len(fs))]
        for p in page_nums: s.add(z3.Or([p == int(f) for f in fs]))
        s.add(z3.Distinct(page_nums))

        for rule, pages in rules.items():
            for pi, p in enumerate(page_nums):
                s.add(z3.Implies(z3.Or([p2 == int(rule) for p2 in page_nums[pi+1:]]), z3.And([p != int(pv) for pv in pages])))

        if s.check() == z3.sat:
            m = s.model()
            ordered_pages = [m[p] for p in page_nums]
            print(ordered_pages)
            tot.append(ordered_pages[len(ordered_pages)//2].as_long())
        else:
            print('unsat')
            exit(-1)

    # print(tot)

    print_answers(puzzle, 2, sum(tot))

# TODO Refactor into common library
puzzle = get_puzzle(day=5, year=2024)
examples = puzzle.examples

for ex in examples: solve_p1(ex)
solve_p1(puzzle)

for ex in examples: solve_p2(ex)
solve_p2(puzzle)
