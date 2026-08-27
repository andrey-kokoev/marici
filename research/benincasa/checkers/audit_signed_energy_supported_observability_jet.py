#!/usr/bin/env python3
import json
from fractions import Fraction as F
from pathlib import Path


def det3(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def dot(row, col):
    return sum((x * y for x, y in zip(row, col)), F(0))


def rank3(m):
    if det3(m):
        return 3
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            for a in range(3):
                for b in range(a + 1, 3):
                    if m[i][a] * m[j][b] - m[i][b] * m[j][a]:
                        return 2
    return 1 if any(x for row in m for x in row) else 0


def show(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


mu = [F(1), F(0), F(0)]
rho = [F(1), F(-1), F(1)]       # Res_{v=0}(v lambda_E)
tau0 = [F(-1), F(-1, 2), F(1, 2)]
tau1 = [F(0), F(-1, 4), F(0)]  # d/dv(mu R_E^T)|_{v=0}
k = [F(0), F(1), F(1)]

# Derivative at v=0 of the cleared integral transport row
# (-2(v-2), 2, v-2).
delta_int = [F(-2), F(0), F(1)]

ordinary = [mu, rho, tau0]
jet = [mu, rho, tau1]
jet_int = [mu, rho, delta_int]
a2_augmented = [mu, rho, mu]  # Entry 285 maps q_top primitively.

assert rank3(ordinary) == 2
assert all(dot(row, k) == 0 for row in ordinary)
assert dot(tau1, k) == F(-1, 4)
assert rank3(jet) == 3
assert det3(jet) == F(1, 4)
assert dot(delta_int, k) == 1
assert rank3(jet_int) == 3
assert abs(det3(jet_int)) == 1
assert rank3(a2_augmented) == 2

packet = {
    "schema": "marici.benincasa.signed_energy_supported_observability_jet.v1",
    "status": "pass",
    "basis": ["q_top", "q_wall1", "q_wall2"],
    "ordinary_supported_rows": [[show(x) for x in row] for row in ordinary],
    "ordinary_rank": rank3(ordinary),
    "ordinary_kernel_generator": [show(x) for x in k],
    "a2_top_specialization_row": [show(x) for x in mu],
    "a2_augmented_rank": rank3(a2_augmented),
    "first_normal_transport_row": [show(x) for x in tau1],
    "first_normal_value_on_kernel": show(dot(tau1, k)),
    "rational_jet_determinant": show(det3(jet)),
    "integral_conormal_row": [show(x) for x in delta_int],
    "integral_conormal_value_on_kernel": show(dot(delta_int, k)),
    "integral_jet_determinant": show(det3(jet_int)),
    "classification": {
        "ordinary_costalk": "rank two with kernel q_wall1+q_wall2",
        "finite_A2_map": "primitive on q_top but redundant for this kernel",
        "first_normal_grade": "detects the kernel and gives a unimodular integral completion",
        "new_carrier_datum": False,
    },
}

out = Path(__file__).resolve().parents[1] / "results" / "signed_energy_supported_observability_jet.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
