from fractions import Fraction
import json
from pathlib import Path


def matmul(a, b):
    return [
        [sum(x * y for x, y in zip(row, col)) for col in zip(*b)]
        for row in a
    ]


def subtract(a, b):
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def commutator(a, b):
    return subtract(matmul(a, b), matmul(b, a))


def flatten(a):
    return [x for row in a for x in row]


def rank(vectors):
    if not vectors:
        return 0
    a = [[Fraction(x) for x in row] for row in vectors]
    nrows = len(a)
    ncols = len(a[0])
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, nrows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        scale = a[r][c]
        a[r] = [x / scale for x in a[r]]
        for i in range(nrows):
            if i != r and a[i][c]:
                scale = a[i][c]
                a[i] = [x - scale * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def independent_append(basis, candidate):
    old_rank = rank([flatten(x) for x in basis])
    new_rank = rank([flatten(x) for x in basis + [candidate]])
    if new_rank > old_rank:
        basis.append(candidate)
        return True
    return False


def lie_closure(generators):
    basis = []
    for generator in generators:
        independent_append(basis, generator)
    changed = True
    while changed:
        changed = False
        snapshot = list(basis)
        for a in snapshot:
            for b in snapshot:
                if independent_append(basis, commutator(a, b)):
                    changed = True
    return basis


def e(i, j):
    out = [[Fraction(0)] * 3 for _ in range(3)]
    out[i][j] = Fraction(1)
    return out


def trace(a):
    return sum(a[i][i] for i in range(3))


f = e(1, 0)
r = [
    [Fraction(0), Fraction(-1), Fraction(0)],
    [Fraction(1), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(0)],
]
w = e(0, 2)
w_dual = e(2, 0)

tail = lie_closure([f, r])
forward_wall = lie_closure([f, r, w])
full = lie_closure([f, r, w, w_dual])

assert len(tail) == 3
assert len(forward_wall) == 5
assert len(full) == 8
assert all(trace(x) == 0 for x in full)

identity = [
    [Fraction(1), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(1)],
]
assert rank([flatten(x) for x in full + [identity]]) == 9

result = {
    "tail_generators": ["jet shear", "Fourier quarter-turn"],
    "tail_lie_dimension": len(tail),
    "tail_lie_algebra": "sl2",
    "one_way_wall_lie_dimension": len(forward_wall),
    "one_way_wall_is_full_sl3": False,
    "dual_wall_lie_dimension": len(full),
    "dual_wall_lie_algebra": "sl3",
    "identity_adjoined_dimension": 9,
    "determinant_direction_completion": "gl3",
    "analytic_dual_wall_incidence_constructed": False,
    "orientation_implied_by_lie_closure": False,
    "verdict": "the finite source generators close the full operator algebra only after dual wall incidence",
}

out = Path(__file__).parents[1] / "results" / "rh-source-lie-closure.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
