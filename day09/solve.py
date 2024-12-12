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

def solve_p1(puzzle):
    out = parse(puzzle)
    out = out[0]

    fs = []
    fid = 0
    is_free_space = False
    for o in out:
        if is_free_space:
            for _ in range(int(o)):
                fs.append(None)
            is_free_space = False
        else:
            for _ in range(int(o)):
                fs.append(fid)
            fid += 1
            is_free_space = True

    i = 0
    e = len(fs)-1
    while True:
        if i >= len(fs): break
        if i == e: break
        if fs[i] is not None:
            i += 1
            continue

        while e > i and fs[e] is None:
            e -= 1
        next_fid = fs[e]
        fs[i] = next_fid
        fs[e] = None

        i += 1

    chksum = 0
    for fi, f in enumerate(fs):
        if f is None: break
        chksum += fi * f

    print_answers(puzzle, 1, chksum)
    

def solve_p2(puzzle):
    out = parse(puzzle)
    out = out[0]

    fs = []
    fid = 0
    is_free_space = False
    for o in out:
        if is_free_space:
            if int(o) > 0:
                fs.append((None, int(o)))
            is_free_space = False
        else:
            fs.append((fid, int(o), False))
            fid += 1
            is_free_space = True

    while True:
        ti = len(fs)
        found = False
        for r in fs[::-1]:
            ti -= 1
            if r[0] is not None and r[2] is False:
                t = r
                found = True
                break

        if not found: break

        found = False
        for fi, f in enumerate(fs):
            if fi >= ti: break
            if f[0] is None and f[1] == t[1]:
                fs[ti] = (None, t[1])
                fs[fi] = (t[0], t[1], True)
                found = True
                break
            if f[0] is None and f[1] > t[1]:
                fs[ti] = (None, t[1])
                fs[fi] = (t[0], t[1], True)
                fs.insert(fi+1, (None, f[1] - t[1]))
                found = True
                break
        
        if not found:
            fs[ti] = (t[0], t[1], True)

    chksum = 0
    fi = 0
    for f in fs:
        if f[0] is None:
            fi += f[1]
        else:
            for _ in range(f[1]):
                chksum += fi * f[0]
                fi += 1

    print_answers(puzzle, 2, chksum)

# TODO Refactor into common library
puzzle = get_puzzle(day=9, year=2024)
examples = puzzle.examples

for ex in examples: solve_p1(ex)
solve_p1(puzzle)

for ex in examples: solve_p2(ex)
solve_p2(puzzle)