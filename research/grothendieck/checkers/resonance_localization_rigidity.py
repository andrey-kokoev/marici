V = tuple((a, b) for a in range(2) for b in range(2))


def add(x, y):
    return ((x[0] + y[0]) % 2, (x[1] + y[1]) % 2)


def action(x):
    # Order-three automorphism of V4.
    return (x[1], (x[0] + x[1]) % 2)


def twisted_norm(x):
    return add(add(x, action(x)), action(action(x)))


images = [twisted_norm(x) for x in V]
assert images == [(0, 0)] * 4

matrix = [[0 for _ in V] for _ in V]
index = {x: i for i, x in enumerate(V)}
for column, image in enumerate(images):
    matrix[index[image]][column] = 1


def rank_mod(rows, p):
    a = [[value % p for value in row] for row in rows]
    rank = 0
    for column in range(len(a[0])):
        pivot = next((r for r in range(rank, len(a)) if a[r][column]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][column], -1, p)
        a[rank] = [(inverse * value) % p for value in a[rank]]
        for r in range(len(a)):
            if r != rank and a[r][column]:
                factor = a[r][column]
                a[r] = [(x - factor * y) % p for x, y in zip(a[r], a[rank])]
        rank += 1
    return rank


ranks = {p: rank_mod(matrix, p) for p in (2, 3, 5, 7)}
assert ranks == {2: 1, 3: 1, 5: 1, 7: 1}
assert 4 % 3 != 0 and ranks[3] < 4

print({
    "control": "A4->C3, n=3",
    "twisted_norm_images": images,
    "linearization_ranks": ranks,
    "degree_four_is_unit_mod_three": True,
    "checks": "pass",
})
