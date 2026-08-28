import itertools
import json
from pathlib import Path

import sympy as sp


I = sp.I
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -I], [I, 0]])
s3 = sp.diag(1, -1)
eye2 = sp.eye(2)
kron = sp.kronecker_product
gammas = [kron(s1, s1), kron(s2, s1), kron(s3, s1), kron(eye2, s2), kron(eye2, s3)]
C = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, -1], [-1, 0, 0, 0], [0, 1, 0, 0]])
phi = sp.Matrix([1, 2, 3, 5])
phi_tilde = C * phi


def B(x):
    return sp.Matrix.hstack(*[C * gamma * x for gamma in gammas])


def q(x):
    return C * x


y = sp.symbols("y1:7")
zero = sp.zeros(4, 1)
K = sp.Matrix.vstack(
    sp.Matrix.hstack(y[0] * B(phi), y[2] * q(phi_tilde), y[3] * q(phi), zero),
    sp.Matrix.hstack(y[1] * B(phi_tilde), zero, y[4] * q(phi_tilde), y[5] * q(phi)),
)

coordinate_indices = (0, 1, 2, 5)
expected_coranks = {
    (): 0,
    (0,): 2,
    (1,): 2,
    (2,): 1,
    (5,): 1,
    (0, 1): 5,
    (0, 2): 3,
    (0, 5): 3,
    (1, 2): 3,
    (1, 5): 3,
    (2, 5): 2,
    (0, 1, 2): 6,
    (0, 1, 5): 6,
    (0, 2, 5): 4,
    (1, 2, 5): 4,
    (0, 1, 2, 5): 7,
}

computed = {}
for size in range(5):
    for subset in itertools.combinations(coordinate_indices, size):
        rank = K.subs({y[index]: 0 for index in subset}).rank()
        computed[subset] = 8 - rank

weights = {0: 2, 1: 2, 2: 1, 5: 1}
tests = {
    "all_sixteen_strata_match": computed == expected_coranks,
    "single_y1_corank_two": computed[(0,)] == 2,
    "single_y2_corank_two": computed[(1,)] == 2,
    "single_y3_corank_one": computed[(2,)] == 1,
    "single_y6_corank_one": computed[(5,)] == 1,
    "y1_y2_has_one_coherent_excess": computed[(0, 1)] == weights[0] + weights[1] + 1,
    "y1_y3_y6_is_additive": computed[(0, 2, 5)] == weights[0] + weights[2] + weights[5],
    "y2_y3_y6_is_additive": computed[(1, 2, 5)] == weights[1] + weights[2] + weights[5],
    "maximal_coordinate_intersection_has_one_coherent_excess": computed[(0, 1, 2, 5)] == sum(weights.values()) + 1,
    "full_mass_nullity_is_twice_K_corank": 2 * computed[(0, 1)] == 10,
}

passed = sum(bool(v) for v in tests.values())
rows = []
for subset, corank in computed.items():
    rows.append({
        "vanishing": [f"y{index + 1}" for index in subset],
        "rank_K": 8 - corank,
        "corank_K": corank,
        "full_mass_nullity": 2 * corank,
    })

result = {
    "work_package": "WP890",
    "status": "PASS" if passed == len(tests) else "FAIL",
    "summary": {"passed": passed, "total": len(tests), "all_passed": passed == len(tests)},
    "classification": "additive_port_coranks_plus_one_coherent_excess",
    "strata": rows,
    "single_port_corank_weights": {"y1": 2, "y2": 2, "y3": 1, "y6": 1},
    "coherent_excess_condition": "subsets containing both y1=0 and y2=0 gain one additional K-kernel dimension",
    "frame_boundary": "total kernel projector is canonical; branch splitting is not canonical at corank greater than one",
    "remaining_gate": "a source-declared loop and connection on a chosen higher-corank kernel bundle",
    "tests": tests,
}

output = Path(__file__).parents[1] / "results" / "wp890_spin5_coordinate_divisor_intersection_strata.json"
output.write_text(json.dumps(result, indent=2, default=bool) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
