"""Rank audit for the Euler conormal map after ordinary u=0 specialization."""

from fractions import Fraction as Q

# R = Q[a]/(a^4), basis 1,a,a^2,a^3.  The specialized Euler vector is
# (a/4,0,0), so its coefficient map is multiplication by a/4.
matrix = [[Q(0) for _ in range(4)] for _ in range(4)]
for source_degree in range(4):
    target_degree = source_degree + 1
    if target_degree < 4:
        matrix[target_degree][source_degree] = Q(1, 4)


def rank(rows):
    rows = [row[:] for row in rows]
    pivot_row = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(pivot_row, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][col]
        rows[pivot_row] = [x / scale for x in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row and rows[i][col]:
                c = rows[i][col]
                rows[i] = [x - c * y for x, y in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
    return pivot_row


assert rank(matrix) == 3
assert all(matrix[row][3] == 0 for row in range(4))
print("conormal length = 4")
print("rank after ordinary u=0 specialization = 3")
print("kernel = span{a^3}")
print("verdict: the top Cartier layer requires derived u-specialization")
