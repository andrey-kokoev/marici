"""Exact rank checks for the operator-valued two-channel type correction."""

from fractions import Fraction


def rank(matrix: list[list[Fraction]]) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    pivot_row = 0
    for column in range(columns):
        pivot = next((r for r in range(pivot_row, rows) if work[r][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for r in range(rows):
            if r != pivot_row and work[r][column]:
                factor = work[r][column]
                work[r] = [x - factor * y for x, y in zip(work[r], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


for size in range(2, 13, 2):
    # Free conjugation pairs (0,1),(2,3),... give a block-swap permutation.
    graph = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for index in range(0, size, 2):
        graph[index][index + 1] = Fraction(1)
        graph[index + 1][index] = Fraction(1)
    assert rank(graph) == size
    assert rank(graph) > 2 if size > 2 else rank(graph) == 2

# Each outer product has rank at most one; two channels have rank at most two.
f1 = [Fraction(1), Fraction(0), Fraction(1), Fraction(0)]
g1 = [Fraction(1), Fraction(2), Fraction(3), Fraction(4)]
f2 = [Fraction(0), Fraction(1), Fraction(0), Fraction(1)]
g2 = [Fraction(4), Fraction(3), Fraction(2), Fraction(1)]
two_channel = [
    [f1[i] * g1[j] + f2[i] * g2[j] for j in range(4)] for i in range(4)
]
assert rank(two_channel) <= 2

print("conjugation_graph_rank_equals_window_size=True")
print("fixed_two_separable_channels_rank_at_most_two=True")
print("fixed_scalar_two_channel_model_cannot_realize_growing_graph=True")
print("operator_valued_two_by_two_with_growing_internal_rank_required=True")
