#!/usr/bin/env python3

from aocd import get_puzzle

def parse(puzzle):
    out = []
    for line in puzzle.input_data.splitlines():
        out.append(line)

    grid = {}
    ants = {}
    for oi, o in enumerate(out):
        for ci, c in enumerate(o):
            grid[(oi, ci)] = c
            if c != '.':
                ants.setdefault(c, [])
                ants[c].append((oi, ci))

    return grid, ants

# TODO Refactor into common library
def print_answers(puzzle, part, answer):
    print(f'Part {part} - {type(puzzle).__name__}: {answer}', end='')
    if hasattr(puzzle, 'answers'):
        expected = puzzle.answers[part-1]
        print(f' ({expected})')
    else:
        print()

def print_grid(grid):
    min_x = min([x for x, y in grid.keys()])
    max_x = max([x for x, y in grid.keys()])
    min_y = min([y for x, y in grid.keys()])
    max_y = max([y for x, y in grid.keys()])

    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            print(grid[(i, j)], end='')
        print()
    print()

def solve_p1(puzzle):
    grid, ants = parse(puzzle)

    print_grid(grid)

    for ant, spots in ants.items():
        for a in spots:
            for b in spots:
                if a == b: continue

                yd = a[0] - b[0]
                xd = a[1] - b[1]

                new_coor = (a[0] + yd, a[1] + xd)
                if new_coor in grid:
                    grid[new_coor] = '#'

    print_grid(grid)
    tot = sum([x == '#' for x in grid.values()])

    print_answers(puzzle, 1, tot)
    

def solve_p2(puzzle):
    grid, ants = parse(puzzle)

    print_grid(grid)

    for ant, spots in ants.items():
        for a in spots:
            for b in spots:
                if a == b: continue

                yd = a[0] - b[0]
                xd = a[1] - b[1]

                new_coor = (a[0] - yd, a[1] - xd)
                while new_coor in grid:
                    grid[new_coor] = '#'
                    new_coor = (new_coor[0] - yd, new_coor[1] - xd)

    print_grid(grid)
    tot = sum([x == '#' for x in grid.values()])

    print_answers(puzzle, 2, tot)

# TODO Refactor into common library
puzzle = get_puzzle(day=8, year=2024)
examples = puzzle.examples

for ex in examples: solve_p1(ex)
solve_p1(puzzle)

for ex in examples: solve_p2(ex)
solve_p2(puzzle)