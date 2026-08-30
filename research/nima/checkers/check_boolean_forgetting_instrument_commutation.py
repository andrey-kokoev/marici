from fractions import Fraction as F
import json
from pathlib import Path


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def dephase(projectors, rho):
    out = [[F(0) for _ in rho[0]] for _ in rho]
    for p in projectors:
        out = add(out, mul(mul(p, rho), p))
    return out


def kron(a, b):
    return [[a[i // len(b)][j // len(b[0])] * b[i % len(b)][j % len(b[0])]
             for j in range(len(a[0]) * len(b[0]))]
            for i in range(len(a) * len(b))]


def apply_local(projectors, rho, side):
    ident = [[F(1), F(0)], [F(0), F(1)]]
    lifted = [kron(p, ident) if side == 0 else kron(ident, p) for p in projectors]
    return dephase(lifted, rho)


def encode_matrix(a):
    return [[str(x) for x in row] for row in a]


I = [[F(1), F(0)], [F(0), F(1)]]
Z = [[F(1), F(0)], [F(0), F(-1)]]
N = [[F(4, 5), F(3, 5)], [F(3, 5), F(-4, 5)]]
PZ = [scale(F(1, 2), add(I, Z)), scale(F(1, 2), add(I, scale(-1, Z)))]
PN = [scale(F(1, 2), add(I, N)), scale(F(1, 2), add(I, scale(-1, N)))]
rho = [[F(1), F(0)], [F(0), F(0)]]

zn = dephase(PZ, dephase(PN, rho))
nz = dephase(PN, dephase(PZ, rho))
residual = add(zn, scale(-1, nz))
assert residual != [[F(0), F(0)], [F(0), F(0)]]

# Independent ports commute as maps. Matrix units span all two-qubit operators.
for i in range(4):
    for j in range(4):
        unit = [[F(int(r == i and c == j)) for c in range(4)] for r in range(4)]
        left_then_right = apply_local(PN, apply_local(PZ, unit, 0), 1)
        right_then_left = apply_local(PZ, apply_local(PN, unit, 1), 0)
        assert left_then_right == right_then_left

# The same-carrier hostile becomes admissible exactly when the channels commute.
zz = dephase(PZ, dephase(PZ, rho))
assert zz == dephase(PZ, rho)

result = {
    "schema": "marici.nima.boolean-forgetting-instrument-commutation.v1",
    "same_carrier_commutes": False,
    "same_carrier_residual": encode_matrix(residual),
    "independent_port_basis_checks": 16,
    "independent_ports_commute": True,
    "commuting_hostile_passes": True,
    "verdict": "Boolean forgetting is authorized only for commuting instrument ports; general occurrence deletion is ordered and partial."
}

out = Path(__file__).parents[1] / "results" / "boolean-forgetting-instrument-commutation.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
