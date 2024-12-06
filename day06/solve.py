#!/usr/bin/env python3

from aocd import get_puzzle

def parse(puzzle):
    out = []
    for line in puzzle.input_data.splitlines():
        out.append(line)

    grid = {}
    start = None
    for oi, o in enumerate(out):
        for ci, c in enumerate(o):
            grid[(oi, ci)] = c
            if c in ['^', 'v', '<', '>']:
                start = (oi, ci)

    return grid, start

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

def solve_p1(puzzle):
    grid, start = parse(puzzle)

    dir_lu = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    dir = dir_lu[grid[start]]

    while True:
        grid[start] = 'X'
        next_coor = (start[0] + dir[0], start[1] + dir[1])
        if next_coor in grid:
            if grid[next_coor] == '#':
                dir = (dir[1], -dir[0])
            else:
                start = next_coor
        else:
            break

    tot_Xs = sum([v == 'X' for v in grid.values()])

    print_answers(puzzle, 1, tot_Xs)

def solve_p2(puzzle):
    grid, start = parse(puzzle)
    orig_start = start

    dir_lu = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    dir = dir_lu[grid[start]]
    orig_dir = dir

    while True:
        grid[start] = 'X'
        next_coor = (start[0] + dir[0], start[1] + dir[1])
        if next_coor in grid:
            if grid[next_coor] == '#':
                dir = (dir[1], -dir[0])
            else:
                start = next_coor
        else:
            break

    crate_spots = [xy for xy in grid.keys() if grid[xy] == 'X' and xy != orig_start]
    spots = []
    MAX_STEPS = len(grid.keys())
    print(f'{MAX_STEPS=}')
    for cs in crate_spots:
        start = orig_start
        dir   = orig_dir
        steps = 0
        while steps < MAX_STEPS:
            next_coor = (start[0] + dir[0], start[1] + dir[1])
            if next_coor in grid:
                if grid[next_coor] == '#' or next_coor == cs:
                    dir = (dir[1], -dir[0])
                else:
                    start = next_coor
                    steps += 1
            else:
                break
        if steps == MAX_STEPS:
            spots.append(cs)

    print_answers(puzzle, 2, len(spots))

# TODO Refactor into common library
puzzle = get_puzzle(day=6, year=2024)
examples = puzzle.examples

for ex in examples: solve_p1(ex)
solve_p1(puzzle)

for ex in examples: solve_p2(ex)
solve_p2(puzzle)