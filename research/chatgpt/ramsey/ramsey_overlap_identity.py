#!/usr/bin/env python3
"""Exact tests of an edge-rooted, fourth-order Ramsey overlap identity.

For any simple graph K,
  sum_{ab in E(K)} binom(|N(a) intersect N(b)|, 2)
      = 6 * (# K4 vertex sets) + (# induced K4-minus-edge vertex sets).

Checks every four-vertex coloring, then the 4x4 rook and Shrikhande graphs.
Uses only the Python standard library. The graph examples are standard;
this is a reproducible check, not a claim of new Ramsey bounds.
"""
from itertools import combinations, product
from math import comb


def matrix(n, predicate):
    return [[int(i != j and predicate(i, j)) for j in range(n)] for i in range(n)]


def multiply(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def complement(a):
    return [[int(i != j) - a[i][j] for j in range(len(a))]
            for i in range(len(a))]


def clique_count(a, k):
    return sum(all(a[i][j] for i, j in combinations(s, 2))
               for s in combinations(range(len(a)), k))


def check_overlap(a):
    n = len(a)
    a2 = multiply(a, a)
    lhs = sum(comb(a2[i][j], 2)
              for i, j in combinations(range(n), 2) if a[i][j])
    tetrahedra = clique_count(a, 4)
    diamonds = sum(sum(a[i][j] for i, j in combinations(s, 2)) == 5
                   for s in combinations(range(n), 4))
    assert lhs == 6 * tetrahedra + diamonds
    return lhs, tetrahedra, diamonds


def check_multiplication_table(k):
    n = len(k)
    u = complement(k)
    k2, ku, u2 = multiply(k, k), multiply(k, u), multiply(u, u)
    for i in range(n):
        for j in range(n):
            identity = int(i == j)
            assert k2[i][j] == 6 * identity + 2 * k[i][j] + 2 * u[i][j]
            assert ku[i][j] == 3 * k[i][j] + 4 * u[i][j]
            assert u2[i][j] == 9 * identity + 6 * k[i][j] + 4 * u[i][j]


def main():
    edges = tuple(combinations(range(4), 2))
    for mask in range(1 << len(edges)):
        present = {e for bit, e in enumerate(edges) if mask & (1 << bit)}
        a = matrix(4, lambda i, j: tuple(sorted((i, j))) in present)
        check_overlap(a)
    print('Overlap identity checked on all 64 labeled four-vertex graphs.')

    vertices = list(product(range(4), repeat=2))
    steps = {(1, 0), (3, 0), (0, 1), (0, 3), (1, 1), (3, 3)}
    rook = matrix(16, lambda i, j:
                  vertices[i][0] == vertices[j][0] or
                  vertices[i][1] == vertices[j][1])
    shrikhande = matrix(16, lambda i, j:
                        ((vertices[j][0] - vertices[i][0]) % 4,
                         (vertices[j][1] - vertices[i][1]) % 4) in steps)
    for name, k in [('Rook', rook), ('Shrikhande', shrikhande)]:
        check_multiplication_table(k)
        overlap, k4, diamond = check_overlap(k)
        u = complement(k)
        print(f'{name}: identical stated multiplication table verified; '
              f'overlapping triangle pairs={overlap}, red K4={k4}, '
              f'induced red diamonds={diamond}, white K5={clique_count(u, 5)}')


if __name__ == '__main__':
    main()
