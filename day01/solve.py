#!/usr/bin/env python3

def parse(file):
    left = []
    right = []
    for line in open(file):
        match line.split():
            case [lhs, rhs]:
                left.append( int(lhs))
                right.append(int(rhs))
    return left, right

def solve_p1(file):
    l, r = parse(file)
    l.sort()
    r.sort()
    diffs = [abs(i-j) for i, j in zip(l,r)]
    print(f'Part 1 - {file}: {sum(diffs)}')

def solve_p2(file):
    l, r = parse(file)
    counts = {}
    for ri in r:
        counts.setdefault(ri, 0)
        counts[ri] += 1

    tot = []
    for li in l:
        if li in counts:
            tot.append(li * counts[li])

    print(f'Part 2 - {file}: {sum(tot)}')

solve_p1('./example.txt')
solve_p1('./input.txt')
solve_p2('./example.txt')
solve_p2('./input.txt')