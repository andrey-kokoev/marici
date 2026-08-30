from fractions import Fraction


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    if not a:
        return 0
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


def grade_matrix(labels, grade_count):
    return [
        [Fraction(label) ** grade for label in labels]
        for grade in range(grade_count)
    ]


for fiber_size in range(2, 9):
    labels = list(range(1, fiber_size + 1))
    for grades in range(1, fiber_size + 2):
        observed_rank = rank(grade_matrix(labels, grades))
        assert observed_rank == min(fiber_size, grades)

fixed_grade_count = 4
larger_fiber = list(range(1, fixed_grade_count + 3))
assert rank(grade_matrix(larger_fiber, fixed_grade_count)) < len(larger_fiber)

print("distinct grades have generalized Vandermonde rank")
print("each fixed finite fiber becomes observable at finite grade")
print("no fixed grade truncation observes fibers of unbounded size")
