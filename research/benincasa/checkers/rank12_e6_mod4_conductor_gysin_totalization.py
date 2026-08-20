"""Integral contraction of the conductor complex tensored with the support simplex."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/rank12-e6-mod4-conductor-gysin-totalization.json"
MOD = 4

# External simplex chain groups S_q have dimensions 1,3,3,1 for q=0..3.
dS = {
    1: [[1, 1, 1]],
    2: [[-1, 0, 1], [1, -1, 0], [0, 1, -1]],
    3: [[1], [1], [1]],
}
hS = {
    0: [[1], [0], [0]],
    1: [[0, 1, 0], [0, 0, 0], [0, 0, -1]],
    2: [[0, 1, 0]],
}
dims = [1, 3, 3, 1]

def mv(matrix, vector, mod=None):
    out = [sum(a * b for a, b in zip(row, vector)) for row in matrix]
    return [x % mod for x in out] if mod else out

def add(a, b, mod=None):
    out = [x + y for x, y in zip(a, b)]
    return [x % mod for x in out] if mod else out

# Verify d h + h d = identity on the augmented simplex over Z.
for q, dim in enumerate(dims):
    for i in range(dim):
        v = [1 if j == i else 0 for j in range(dim)]
        lhs = [0] * dim
        if q in hS:
            lhs = add(lhs, mv(dS[q + 1], mv(hS[q], v)))
        if q in dS:
            lhs = add(lhs, mv(hS[q - 1], mv(dS[q], v)))
        assert lhs == v, (q, i, lhs, v)

# Internal conductor chain C_1 -> C_0 is multiplication by two.  Verify the
# signed tensor homotopy K(c_p tensor s_q)=(-1)^p c_p tensor h_S(s_q)
# on every basis vector modulo four.
def accumulate(dst, key, value):
    dst[key] = (dst.get(key, 0) + value) % MOD

def D(state):
    out = {}
    for (p, q, i), coeff in state.items():
        if p == 1:
            accumulate(out, (0, q, i), 2 * coeff)
        if q > 0:
            sign = -1 if p % 2 else 1
            for row in range(dims[q - 1]):
                accumulate(out, (p, q - 1, row), sign * dS[q][row][i] * coeff)
    return {k: v for k, v in out.items() if v % MOD}

def K(state):
    out = {}
    for (p, q, i), coeff in state.items():
        if q < 3:
            sign = -1 if p % 2 else 1
            for row in range(dims[q + 1]):
                accumulate(out, (p, q + 1, row), sign * hS[q][row][i] * coeff)
    return {k: v for k, v in out.items() if v % MOD}

for p in (0, 1):
    for q, dim in enumerate(dims):
        for i in range(dim):
            basis = {(p, q, i): 1}
            lhs = D(K(basis))
            for key, value in K(D(basis)).items():
                accumulate(lhs, key, value)
            lhs = {k: v for k, v in lhs.items() if v % MOD}
            assert lhs == basis, (p, q, i, lhs)

packet = {
    "schema": "marici.benincasa.rank12_e6_mod4_conductor_gysin_totalization.v1",
    "coefficient_ring": "Z/4",
    "internal_complex": "[Z/4 --2--> Z/4]",
    "external_simplex_dimensions": dims,
    "external_contraction": {"h0": hS[0], "h1": hS[1], "h2": hS[2]},
    "tensor_homotopy": "K(c_p tensor s_q)=(-1)^p c_p tensor h_S(s_q)",
    "checked_basis_vectors": sum(dims) * 2,
    "total_homology": 0,
    "local_mod2_grades_survive_after_full_totalization": False,
    "interpretation": "The two mod-two conductor grades are killed by the source-derived external support coherences. They are associated-grade coefficient data, not a global supported class.",
    "new_carrier_datum": False,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))
