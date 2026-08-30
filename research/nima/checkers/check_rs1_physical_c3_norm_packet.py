"""Exact RS-1 audit of the physical C3 occurrence norm packet."""

import json
from pathlib import Path


def rank_mod(a, p):
    a = [[x % p for x in row] for row in a]
    row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = pow(a[row][col], -1, p)
        a[row] = [(inv * x) % p for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                c = a[i][col]
                a[i] = [(x - c * y) % p for x, y in zip(a[i], a[row])]
        row += 1
    return row


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def block_diag(a, copies):
    n = len(a)
    out = [[0] * (n * copies) for _ in range(n * copies)]
    for c in range(copies):
        for i in range(n):
            for j in range(n):
                out[c * n + i][c * n + j] = a[i][j]
    return out


T = [[1], [1], [1]]
R = [[1, 1, 1]]
N = multiply(T, R)
assert multiply(R, T) == [[3]]
assert multiply(N, N) == [[3 * x for x in row] for row in N]

rows = []
for p in (2, 3, 5, 7):
    rank_n = rank_mod(N, p)
    rank_n2 = rank_mod(multiply(N, N), p)
    homology_dimension = 3 - 2 * rank_n if rank_n2 == 0 else None
    rows.append({
        "characteristic": p,
        "norm_rank": rank_n,
        "norm_square_rank": rank_n2,
        "norm_is_differential": rank_n2 == 0,
        "per_orbit_norm_homology_dimension": homology_dimension,
    })

assert rows[1]["per_orbit_norm_homology_dimension"] == 1
assert all(r["per_orbit_norm_homology_dimension"] is None for i, r in enumerate(rows) if i != 1)

N2 = block_diag(N, 2)
assert rank_mod(N2, 3) == 2
two_orbit_homology_dimension = 6 - 2 * rank_mod(N2, 3)
assert two_orbit_homology_dimension == 2

# Negative control: the free three-channel augmentation kernel also has
# dimension two, but it is one copy of the reduced representation rather
# than norm homology of two source occurrence orbits.
free_augmentation_kernel_dimension = 3 - rank_mod(R, 3)
assert free_augmentation_kernel_dimension == two_orbit_homology_dimension

# The declared all-positive readout annihilates every homology
# representative because ker(N)=ker(R).
kernel_generators = [[1, -1, 0], [0, 1, -1]]
assert all(multiply(R, [[x] for x in v]) == [[0]] for v in kernel_generators)

result = {
    "schema": "marici.rs1.physical-c3-norm-packet.v1",
    "source_identities": {"RT": 3, "N2": "3N", "orbits": 2},
    "characteristic_audit": rows,
    "physical_mod3": {
        "module": "F3[C3]^2",
        "norm_rank": 2,
        "norm_homology_dimension": two_orbit_homology_dimension,
        "readout": "source all-positive occurrence sum",
        "induced_readout_on_norm_homology": "zero",
        "physical_activation_established": False,
    },
    "rank_coincidence_negative_control": {
        "free_augmentation_kernel_dimension": free_augmentation_kernel_dimension,
        "same_dimension": True,
        "typed_identification": False,
        "reason": "one free reduced representation is not two source-orbit norm-homology quotients",
    },
    "verdict": (
        "The equal-energy cosmology packet is a physically sourced nonsemisimple "
        "coefficient packet, but not yet a physically activated relative syndrome: "
        "the declared readout annihilates norm homology. The equal dimension with a "
        "free three-channel kernel is rejected as untyped."
    ),
}

out = Path(__file__).parents[1] / "results" / "rs1-physical-c3-norm-packet.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
