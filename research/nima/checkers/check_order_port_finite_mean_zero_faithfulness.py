from fractions import Fraction


def order_matrix(size):
    return [
        [Fraction((i > j) - (i < j)) for j in range(size)]
        for i in range(size)
    ]


def rank(matrix):
    a = [row[:] for row in matrix]
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


for size in range(2, 11):
    matrix = order_matrix(size)
    expected_rank = size if size % 2 == 0 else size - 1
    assert rank(matrix) == expected_rank

    joint = [[Fraction(1) for _ in range(size)]] + matrix
    assert rank(joint) == size

    alternating = [Fraction(1 if i % 2 == 0 else -1) for i in range(size)]
    if size % 2:
        assert all(
            sum(a * b for a, b in zip(row, alternating)) == 0
            for row in matrix
        )
        assert sum(alternating) == 1

print("even fibers: order matrix is invertible")
print("odd fibers: sole alternating kernel has nonzero mean")
print("averaging plus order is jointly faithful for sizes 2 through 10")
