from fractions import Fraction


def rank(matrix):
    if not matrix:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next(
            (row for row in range(pivot_row, rows) if a[row][col]),
            None,
        )
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        value = a[pivot_row][col]
        a[pivot_row] = [x / value for x in a[pivot_row]]
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = a[row][col]
            a[row] = [
                x - factor * y
                for x, y in zip(a[row], a[pivot_row])
            ]
        pivot_row += 1
    return pivot_row


# Columns are boundaries in the visible two-dimensional even sector.
full_boundary = [[-1], [1]]
decimated_boundary = []

full_h0_rank = 2 - rank(full_boundary)
decimated_h0_rank = 2 - rank(decimated_boundary)

assert full_h0_rank == 1
assert decimated_h0_rank == 2

print("full graded complex: one visible quotient class")
print("odd-mediator deletion: two apparent quotient classes")
print("the additional decimated class is an alias")
