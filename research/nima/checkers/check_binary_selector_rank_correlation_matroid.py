"""GF(2) selector rank and left-nullspace correlation witnesses."""

from itertools import product


def rank_mod2(matrix):
    a = [row[:] for row in matrix]
    rows = len(a)
    columns = len(a[0]) if rows else 0
    rank = 0
    for column in range(columns):
        pivot = next((r for r in range(rank, rows) if a[r][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for r in range(rows):
            if r != rank and a[r][column]:
                a[r] = [x ^ y for x, y in zip(a[r], a[rank])]
        rank += 1
    return rank


def affine_image(matrix, offset):
    columns = len(matrix[0])
    return {
        tuple(
            offset[row]
            ^ sum(matrix[row][column] * state[column] for column in range(columns)) % 2
            for row in range(len(matrix))
        )
        for state in product((0, 1), repeat=columns)
    }


shared = [[1], [1]]
shared_image = affine_image(shared, [0, 0])
assert rank_mod2(shared) == 1
assert len(shared_image) == 2 ** rank_mod2(shared)
assert shared_image == {(0, 0), (1, 1)}
for output in shared_image:
    assert (output[0] + output[1]) % 2 == 0

independent = [[1, 0], [0, 1]]
independent_image = affine_image(independent, [0, 0])
assert rank_mod2(independent) == 2
assert len(independent_image) == 4

three_outputs = [[1, 0], [0, 1], [1, 1]]
three_image = affine_image(three_outputs, [0, 0, 0])
assert rank_mod2(three_outputs) == 2
assert len(three_image) == 4
for output in three_image:
    assert sum(output) % 2 == 0

print("shared-pointer rank/image:", rank_mod2(shared), sorted(shared_image))
print("shared-pointer circuit:", [1, 1])
print("independent rank/image size:", rank_mod2(independent), len(independent_image))
print("three-choice circuit parity:", [1, 1, 1])
print("PASS: selector joint freedom equals GF(2) rank; circuits expose correlation")
