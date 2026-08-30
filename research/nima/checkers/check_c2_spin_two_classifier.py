"""Exact dependency-free classifier for the 2x2 C2 spin-two action."""

from itertools import product


I = ((1, 0), (0, 1))
NEG_I = ((-1, 0), (0, -1))
Q = ((1, 0), (0, -1))


def transpose(a):
    return tuple(zip(*a))


def multiply(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def negate(a):
    return tuple(tuple(-x for x in row) for row in a)


def add(a, b):
    return tuple(
        tuple(a[i][j] + b[i][j] for j in range(2))
        for i in range(2)
    )


def is_orthogonal(r):
    return multiply(transpose(r), r) == I


def is_involution(r):
    return multiply(r, r) == I


def flips_q(r):
    return multiply(multiply(transpose(r), Q), r) == negate(Q)


def anticommutes(r):
    return add(multiply(r, Q), multiply(Q, r)) == ((0, 0), (0, 0))


# Enumerating {-1,0,1} entries is complete after the algebraic derivation:
# anticommutation forces zero diagonal and orthogonality forces off-diagonal
# entries to be signs.
candidates = []
for entries in product((-1, 0, 1), repeat=4):
    r = (entries[:2], entries[2:])
    if is_orthogonal(r) and is_involution(r) and flips_q(r):
        candidates.append(r)

expected = [
    ((0, -1), (-1, 0)),
    ((0, 1), (1, 0)),
]

quarter_turns = [
    ((0, -1), (1, 0)),
    ((0, 1), (-1, 0)),
]

assert candidates == expected
assert all(anticommutes(r) for r in candidates)
assert all(is_orthogonal(r) and flips_q(r) for r in quarter_turns)
assert all(multiply(r, r) == NEG_I for r in quarter_turns)
assert all(not is_involution(r) for r in quarter_turns)

certificate = {
    "schema": "marici.c2_spin_two_classifier.v1",
    "dimension": 2,
    "q_signature": [1, 1],
    "solution_count_in_q_eigenbasis": len(candidates),
    "solutions": candidates,
    "c4_false_positives_rejected": True,
}

print("certificate:", certificate)
print("quarter-turn false positives:", quarter_turns)
print("PASS: exactly two C2 quadrature swaps; C4 rotations rejected")
