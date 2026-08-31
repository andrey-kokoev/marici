import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
N = 23
J = Fraction(N - 1, 2)


def zero(n):
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def matmul(A, B):
    n = len(A)
    out = zero(n)
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                aik = A[i][k]
                for j in range(n):
                    if B[k][j]:
                        out[i][j] += aik * B[k][j]
    return out


def add(A, B, scale=Fraction(1)):
    return [[a + scale * b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def commutator(A, B):
    return add(matmul(A, B), matmul(B, A), Fraction(-1))


def norm1(A):
    return sum(abs(x) for row in A for x in row)


def diag(values):
    out = zero(len(values))
    for i, v in enumerate(values):
        out[i][i] = Fraction(v)
    return out


# Integral sl2 action on the spin-j=(N-1)/2 irreducible representation.
# Basis v_a has H-weight N-1-2a; F v_a=(a+1)v_{a+1};
# E v_a=(N-a)v_{a-1}.
H = diag([N - 1 - 2 * a for a in range(N)])
E = zero(N)
F = zero(N)
for a in range(N):
    if a + 1 < N:
        F[a + 1][a] = Fraction(a + 1)
    if a > 0:
        E[a - 1][a] = Fraction(N - a)

assert matmul(E, F) and matmul(F, E)
assert commutator(E, F) == H
assert commutator(H, E) == [[Fraction(2) * x for x in row] for row in E]
assert commutator(H, F) == [[Fraction(-2) * x for x in row] for row in F]

# Distinct H weights plus a connected E/F weight chain is an exact finite
# irreducibility certificate for this module.
weights = [H[a][a] for a in range(N)]
assert len(set(weights)) == N
adjacency = [set() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if E[i][j] or F[i][j]:
            adjacency[i].add(j)
            adjacency[j].add(i)
seen = {0}
stack = [0]
while stack:
    u = stack.pop()
    for v in adjacency[u]:
        if v not in seen:
            seen.add(v)
            stack.append(v)
assert seen == set(range(N))

# Casimir in this normalization is 2*j*(j+1)=264 on every weight.
H2 = matmul(H, H)
EF = matmul(E, F)
FE = matmul(F, E)
half_H2 = [[x / 2 for x in row] for row in H2]
Casimir = add(add(EF, FE), half_H2)
expected_casimir = Fraction(2) * J * (J + 1)
assert expected_casimir == 264
assert Casimir == diag([expected_casimir] * N)

# Representation-derived degeneracy: only scalar mass/residue operators commute
# with the irreducible sl2 cell.  The 22+1 block clock does not.
M_good = diag([1] * N)
M_split = diag([1] * 22 + [4])
assert norm1(commutator(M_good, E)) == 0
assert norm1(commutator(M_good, F)) == 0
assert norm1(commutator(M_good, H)) == 0
split_E_norm = norm1(commutator(M_split, E))
split_F_norm = norm1(commutator(M_split, F))
assert split_E_norm > 0 or split_F_norm > 0
split_nonzero_positions = [
    [i, j, str(commutator(M_split, F)[i][j])]
    for i in range(N)
    for j in range(N)
    if commutator(M_split, F)[i][j]
]
assert split_nonzero_positions


def normalized_response(masses):
    R0 = Fraction(len(masses))
    R1 = sum((Fraction(m) / (Fraction(m) + 1) for m in masses), Fraction(0))
    return R1 / R0


good_response = normalized_response([1] * N)
split_response = normalized_response([1] * 22 + [4])
assert good_response == Fraction(1, 2)
assert split_response == Fraction(59, 115)

# The WP1036 k=2 datum is an external two-port arity in this packet; the spin
# cell derives the 23-fold internal multiplet, not yet the port arity.
ports = ("left", "right")
assert len(ports) == 2
assert N * len(ports) == 46

result = {
    "schema": "marici.flavor.wp1054.v1",
    "status": "PASS",
    "question": "Can an irreducible representation turn WP1053's 23 declared pole atoms into a degeneracy theorem?",
    "representation": {
        "algebra": "sl2",
        "spin_j": str(J),
        "dimension_formula": "2j+1",
        "dimension": N,
        "weights": [str(w) for w in weights],
        "casimir": str(expected_casimir),
        "irreducibility_witness": "distinct H weights and one connected E/F weight chain",
    },
    "derived_pole_data": {
        "internal_atom_count_C": N,
        "external_ports_k": list(ports),
        "common_mass2": "1",
        "unit_residues": "identity spectral projector",
        "normalized_R1_over_R0": str(good_response),
    },
    "reducible_clock_hostile": {
        "mass2_histogram": {"1": 22, "4": 1},
        "commutes_with_irreducible_sl2": False,
        "commutator_norm_E": str(split_E_norm),
        "commutator_norm_F": str(split_F_norm),
        "nonzero_F_commutator_positions": split_nonzero_positions,
        "normalized_R1_over_R0": str(split_response),
    },
    "classification": "conditional irreducible-multiplet constructor: spin 11 supplies a 23-dimensional pole cell, Schur scalar residues, and a common clock; a 22+1 clock is not an operator on that irreducible cell",
    "remaining_gate": "derive spin j=11, the external two-port arity, and the common mass scale from the actual source representation/dynamics; irreducibility alone does not select j or k",
    "claim_boundary": "exact finite sl2 module and Schur degeneracy witness; no anomaly completeness, UV action, or physical momentum calibration is claimed",
    "disposition": "productive: WP1053's atom list is upgraded to an explicit representation certificate and a reducible-block falsifier",
}

(ROOT / "results" / "wp1054_irreducible_spin11_pole_cell.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1054 PASS:", J, N, expected_casimir, good_response, split_response)
