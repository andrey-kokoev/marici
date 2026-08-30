import hashlib
import json
from pathlib import Path

import sympy as sp


I = sp.I
h = sp.Rational(1, 2)


def matrix(sign):
    z13 = sign * I * h
    return sp.Matrix(
        [
            [3, 0, z13, h],
            [0, 3, h, 0],
            [sp.conjugate(z13), h, 3, h],
            [h, 0, h, 3],
        ]
    )


M_plus = matrix(1)
M_minus = matrix(-1)
assert M_minus == sp.conjugate(M_plus)
assert M_plus == M_plus.conjugate().T

# Strict diagonal dominance proves positivity.
row_sums = [sum(abs(M_plus[i, j]) for j in range(4) if i != j) for i in range(4)]
assert all(3 > value for value in row_sums)

lam = sp.symbols("lambda")
char_plus = sp.expand(M_plus.charpoly(lam).as_expr())
char_minus = sp.expand(M_minus.charpoly(lam).as_expr())
assert char_plus == char_minus
assert all(abs(M_plus[i, j]) == abs(M_minus[i, j]) for i in range(4) for j in range(4))


def cycles(M):
    w123 = sp.simplify(M[0, 1] * M[1, 2] * sp.conjugate(M[0, 2]))
    w1234 = sp.simplify(M[0, 1] * M[1, 2] * M[2, 3] * sp.conjugate(M[0, 3]))
    w134 = sp.simplify(M[0, 2] * M[2, 3] * sp.conjugate(M[0, 3]))
    return w123, w1234, w134


c_plus = cycles(M_plus)
c_minus = cycles(M_minus)
assert c_plus[:2] == c_minus[:2] == (0, 0)
assert c_plus[2] == I / 8
assert c_minus[2] == -I / 8

payload = {
    "status": "pass",
    "theorem": "continuous_gauge_invariants_require_cycle_products",
    "nominal_fundamental_products": ["0", "0"],
    "surviving_cycle_products": ["+I/8", "-I/8"],
    "shared_edge_magnitudes": True,
    "shared_characteristic_polynomial": str(char_plus),
    "strict_diagonal_dominance_row_sums": [str(x) for x in row_sums],
    "generic_coordinates": "fundamental normalized holonomies",
    "closure_coordinates": "edge magnitudes and unnormalized simple-cycle products",
    "theta_application_frozen": True,
}
canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

output = Path(__file__).parents[1] / "results" / "continuous-cycle-invariants.json"
output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(payload, sort_keys=True))
