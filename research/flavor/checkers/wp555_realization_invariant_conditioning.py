"""Exact similarity audit of WP554 context conditioning."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp520 = load("wp520_finite_propagator_bs_kernel.json")
wp554 = load("wp554_six_context_conditioning_gate.json")

z = sp.symbols("z")
kernel = sp.sympify(
    wp520["aligned_bs_kernel"]["exact_witness_rational_function"],
    locals={"z": z},
)
_, denominator = sp.fraction(kernel)
denominator = sp.expand(denominator / sp.LC(sp.Poly(denominator, z)))
coefficients = sp.Poly(denominator, z).all_coeffs()
degree = sp.degree(denominator, z)

A = sp.zeros(degree)
for row in range(degree - 1):
    A[row, row + 1] = 1
for column, coefficient in enumerate(reversed(coefficients[1:])):
    A[degree - 1, column] = -coefficient
B = sp.zeros(degree, 1)
B[degree - 1, 0] = 1
nodes = (0, 2 - sp.sqrt(3), 1, 2, 3, 2 + sp.sqrt(3))
C = sp.Matrix.hstack(*[(node * sp.eye(degree) - A).inv() * B for node in nodes])

# The exact whitening similarity makes the context matrix the identity. A
# separate diagonal similarity makes the same realization badly conditioned.
T_white = C.inv()
C_white = sp.simplify(T_white * C)
T_stretch = sp.diag(10**6, 1, 1, 1, 1, 1)
C_stretch = T_stretch * C

# Exact similarity covariance of an arbitrary output row and transfer kernel.
c = sp.Matrix([sp.symbols("c0:6")])
A_prime = T_stretch * A * T_stretch.inv()
B_prime = T_stretch * B
c_prime = c * T_stretch.inv()
resolvent_intertwining = sp.simplify(
    (z * sp.eye(degree) - A_prime) * T_stretch
    - T_stretch * (z * sp.eye(degree) - A)
)
output_intertwining = sp.simplify(c_prime * T_stretch - c)
input_intertwining = sp.simplify(B_prime - T_stretch * B)

# The source metric must transform contragrediently. This gives an exact
# invariant Gram matrix even though raw Euclidean singular values change.
G = sp.eye(degree)
G_prime = C.T * C
gram_original = C.T * G * C
gram_prime = C_white.T * G_prime * C_white

mp.mp.dps = 90


def spectral_condition(matrix):
    numeric = mp.matrix(
        [
            [mp.mpf(str(sp.N(matrix[i, j], 100))) for j in range(matrix.cols)]
            for i in range(matrix.rows)
        ]
    )
    _, singular, _ = mp.svd(numeric)
    return singular[0] / singular[matrix.rows - 1]


original_condition = spectral_condition(C)
stretched_condition = spectral_condition(C_stretch)

checks = {
    "wp554_dependency_passed": bool(wp554["passed"]),
    "exact_context_matrix_is_invertible": C.det() != 0,
    "whitening_similarity_gives_identity_exactly": C_white == sp.eye(6),
    "whitened_raw_condition_is_exactly_one": C_white.norm(2) == 1
    and C_white.inv().norm(2) == 1,
    "similarity_preserves_transfer_function_exactly": resolvent_intertwining
    == sp.zeros(6)
    and output_intertwining == sp.zeros(1, 6)
    and input_intertwining == sp.zeros(6, 1),
    "similarity_preserves_context_rank": C_white.rank() == C.rank() == 6,
    "raw_condition_changes_by_many_orders": stretched_condition > 10**11
    and original_condition > 10**7,
    "transported_source_metric_preserves_gram_exactly": gram_prime
    == gram_original,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP555",
    "domain": "All similarity-equivalent six-state realizations of the frozen WP520 scalar resolvent at the six WP540 contexts.",
    "exact_similarity": {
        "rules": ["A_prime=T A T^-1", "B_prime=T B", "c_prime=c T^-1", "C_prime=T C"],
        "transfer_function_invariant": bool(
            resolvent_intertwining == sp.zeros(6)
            and output_intertwining == sp.zeros(1, 6)
            and input_intertwining == sp.zeros(6, 1)
        ),
        "rank_invariant": C_white.rank(),
    },
    "hostile_realizations": {
        "wp554_companion_condition": mp.nstr(original_condition, 18),
        "exact_whitened_condition": "1",
        "diagonal_stretched_condition": mp.nstr(stretched_condition, 18),
        "physical_kernel": "identical in all three realizations",
    },
    "metric_repair": {
        "source_metric_rule": "G_prime=T^-T G T^-1",
        "invariant_gram_rule": "(T C)^T G_prime (T C)=C^T G C",
        "exact_gram_invariant": bool(gram_prime == gram_original),
    },
    "correction_to_wp554": "The unweighted companion-chart condition numbers are valid presentation diagnostics but carry no physical resolution authority. The claimed unit hostile is withdrawn until an independent source metric or admitted displacement domain is supplied.",
    "contextual_partition": "Only a partition defined by the transported source metric, measured observation covariance, and declared detection threshold descends across equivalent realizations.",
    "classification": "Full-realization quotient correction and invariant metric gate; neither selector nor executed physical instrument.",
    "selector": bool(wp554["selector"]),
    "rigidifier": bool(C.rank() == 6),
    "instrument": "Still absent. Requires a source-generated displacement metric or admitted domain plus measured WP542 covariance in physical detector units.",
    "smallest_exact_falsifier": "Choose T=C^-1. The same transfer function and rank-six context family then has context matrix I_6 and raw condition number one rather than the WP554 value.",
    "remaining_gate": "Define the source metric independently of the companion chart, measure the full WP542 observation covariance, transport both through every realization and scheme map, and test the smallest generalized singular value against a preregistered threshold.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp555_realization_invariant_conditioning.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
