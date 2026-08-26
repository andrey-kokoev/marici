from itertools import permutations
import json
from pathlib import Path


def transpose(matrix):
    return tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix)))


def multiply(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0])))
        for i in range(len(left))
    )


def permutation_matrix(perm):
    return tuple(tuple(1 if perm[i] == j else 0 for j in range(3)) for i in range(3))


def parity(perm):
    inversions = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def action(left, kernel, right):
    return multiply(multiply(transpose(left), kernel), right)


perms = tuple(permutations(range(3)))
matrices = {perm: permutation_matrix(perm) for perm in perms}
even = tuple(perm for perm in perms if parity(perm) == 1)
odd = tuple(perm for perm in perms if parity(perm) == -1)

I = permutation_matrix((0, 1, 2))
P = permutation_matrix((1, 2, 0))
PT = transpose(P)

# Independent family relabellings make every permutation cross-block gauge
# equivalent to the identity.
independent_orbit = {
    action(matrices[left], I, matrices[right])
    for left in perms
    for right in perms
}
assert len(independent_orbit) == 6
assert P in independent_orbit and PT in independent_orbit

# A shared identity alignment E=I leaves only the diagonal subgroup.
alignment_stabilizer = tuple(
    (left, right)
    for left in perms
    for right in perms
    if action(matrices[left], I, matrices[right]) == I
)
assert len(alignment_stabilizer) == 6
assert all(left == right for left, right in alignment_stabilizer)

# Diagonal S3 still conjugates the two cyclic orientations.
diagonal_orbit = {
    action(matrices[perm], P, matrices[perm])
    for perm in perms
}
assert diagonal_orbit == {P, PT}
assert any(action(matrices[perm], P, matrices[perm]) == PT for perm in odd)

# An alternating cubic carrier is preserved only by A3=C3. Under that
# stabilizer the two orientations occupy distinct orbits.
oriented_stabilizer = tuple(perm for perm in perms if parity(perm) == 1)
assert len(oriented_stabilizer) == 3
oriented_orbit_P = {action(matrices[perm], P, matrices[perm]) for perm in oriented_stabilizer}
oriented_orbit_PT = {action(matrices[perm], PT, matrices[perm]) for perm in oriented_stabilizer}
assert oriented_orbit_P == {P}
assert oriented_orbit_PT == {PT}
assert oriented_orbit_P.isdisjoint(oriented_orbit_PT)

result = {
    "schema": "marici.nima.flavor-alignment-orientation-stabilizers.v1",
    "independent_family_group_order": 36,
    "permutation_cross_block_orbit_size": len(independent_orbit),
    "alignment_stabilizer_order": len(alignment_stabilizer),
    "diagonal_s3_cyclic_orbit_size": len(diagonal_orbit),
    "alternating_carrier_stabilizer_order": len(oriented_stabilizer),
    "oriented_clockwise_orbit_size": len(oriented_orbit_P),
    "oriented_counterclockwise_orbit_size": len(oriented_orbit_PT),
    "oriented_orbits_disjoint": oriented_orbit_P.isdisjoint(oriented_orbit_PT),
    "verdict": (
        "A shared pairing aligns the two families but does not orient them. "
        "An alternating cubic carrier is additionally required to reduce the "
        "residual diagonal S3 to C3 and separate P from P transpose."
    ),
}

output = Path(__file__).parents[1] / "results" / "flavor-alignment-orientation-stabilizers.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
