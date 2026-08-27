#!/usr/bin/env python3
"""Exact finite check of the bordered valuation common refinement."""

from fractions import Fraction


depth = 3
dimension = depth + 1

# S e_k = e_{k+1}; matrix columns encode basis images.
shift = [[Fraction(0) for _ in range(dimension)] for _ in range(dimension)]
for k in range(depth):
    shift[k + 1][k] = Fraction(1)


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def multiply(left, right):
    return [
        [sum(left[i][k] * right[k][j] for k in range(dimension))
         for j in range(dimension)]
        for i in range(dimension)
    ]


identity = [[Fraction(i == j) for j in range(dimension)]
            for i in range(dimension)]
ss_star = multiply(shift, transpose(shift))
s_star_s = multiply(transpose(shift), shift)
left_defect = [[identity[i][j] - ss_star[i][j]
                for j in range(dimension)] for i in range(dimension)]
right_defect = [[identity[i][j] - s_star_s[i][j]
                 for j in range(dimension)] for i in range(dimension)]

expected_left = [[Fraction(i == 0 and j == 0) for j in range(dimension)]
                 for i in range(dimension)]
expected_right = [[Fraction(i == depth and j == depth)
                   for j in range(dimension)] for i in range(dimension)]

assert left_defect == expected_left
assert right_defect == expected_right

q = Fraction(1, 2)
transfer = sum(q ** k for k in range(dimension))
assert transfer == Fraction(15, 8)

print("input_defect=primitive_projection")
print("terminal_defect=cutoff_boundary")
print("boundary_transfer=finite_Euler_polynomial")
print("common_refinement=bordered_valuation_colligation")

