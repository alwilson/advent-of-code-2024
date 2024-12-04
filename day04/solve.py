#!/usr/bin/env python3

from aocd import get_puzzle

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
    out = parse(puzzle)

    grid = {}
    Xs = []
    for oi, o in enumerate(out):
        for i in range(len(o)):
            grid[(oi, i)] = o[i]
            if o[i] == 'X':
                Xs.append((oi, i))

    # print_grid(grid)
    print(f'{len(Xs)=}')

    # Check for XMAS at each X in all directions
    xmas_count = 0
    for x in Xs:
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            xmas_check = 'XMAS'
            xmas_found = True
            for i in range(1, 4):
                next_coor = (x[0] + d[0] * i, x[1] + d[1] * i)
                if next_coor in grid:
                    if grid[next_coor] != xmas_check[i]:
                        xmas_found = False
                        break
                else:
                    xmas_found = False
                    break
            if xmas_found:
                xmas_count += 1

    print_answers(puzzle, 1, xmas_count)

def solve_p2(puzzle):
    out = parse(puzzle)

    if type(puzzle).__name__ == "Example":
        out = ['.M.S............',
               '..A..MSMS....S..',
               '.M.S.MAA....MAS.',
               '..A.ASMSM....MAS',
               '.M.S.M........M.',
               '................',
               'S.S.S.S.S..SSS..',
               '.A.A.A.A...MAS..',
               'M.M.M.M.M..MMM..',
               '................']

    grid = {}
    As = []
    for oi, o in enumerate(out):
        for i in range(len(o)):
            grid[(oi, i)] = o[i]
            if o[i] == 'A':
                As.append((oi, i))

    # print_grid(grid)
    print(f'{len(As)=}')

    # Check for 2 MAS in an X shape about each A in 4 rotations
    mas_count = 0
    for x in As:
        for d in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
            mas_found = True
            mas_check = 'MMSS'

            for c in mas_check:
                next_coor = (x[0] + d[0], x[1] + d[1])
                if next_coor in grid:
                    if grid[next_coor] != c:
                        mas_found = False
                        break
                else:
                    mas_found = False
                    break
                # Rotate 90 degrees
                d = (d[1], -d[0])

            if mas_found:
                mas_count += 1
                break

    print_answers(puzzle, 2, mas_count)

# TODO Refactor into common library
puzzle = get_puzzle(day=4, year=2024)
examples = puzzle.examples

for ex in examples: solve_p1(ex)
solve_p1(puzzle)

for ex in examples: solve_p2(ex)
solve_p2(puzzle)
