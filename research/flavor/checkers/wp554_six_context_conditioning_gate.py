"""Exact rank and high-precision conditioning audit for WP540 contexts."""

import json
from pathlib import Path

import mpmath as mp
import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp520 = load("wp520_finite_propagator_bs_kernel.json")
wp540 = load("wp540_periodic_lattice_context_support.json")
wp541 = load("wp541_twisted_continuum_context_ladder.json")

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
contexts = sp.Matrix.hstack(
    *[(node * sp.eye(degree) - A).inv() * B for node in nodes]
)
determinant = sp.factor(contexts.det())

mp.mp.dps = 100
numeric_contexts = mp.matrix(
    [
        [mp.mpf(str(sp.N(contexts[i, j], 110))) for j in range(degree)]
        for i in range(degree)
    ]
)
_, singular_matrix, _ = mp.svd(numeric_contexts)
singular_values = [singular_matrix[i] for i in range(degree)]
spectral_condition = singular_values[0] / singular_values[-1]

inverse_contexts = contexts.inv()
infinity_norm = max(
    sum(abs(mp.mpf(str(sp.N(contexts[i, j], 110)))) for j in range(degree))
    for i in range(degree)
)
inverse_infinity_norm = max(
    sum(abs(mp.mpf(str(sp.N(inverse_contexts[i, j], 110)))) for j in range(degree))
    for i in range(degree)
)
infinity_condition = infinity_norm * inverse_infinity_norm
resolution_floor = mp.mpf("1e-6")

checks = {
    "dependencies_passed": bool(wp540["passed"] and wp541["passed"]),
    "six_exact_supported_nodes": len(nodes) == degree == 6,
    "exact_context_matrix_has_rank_six": contexts.rank() == 6,
    "exact_determinant_is_nonzero": determinant != 0,
    "smallest_singular_value_is_positive": singular_values[-1] > 0,
    "spectral_condition_exceeds_ten_million": spectral_condition > 10**7,
    "infinity_condition_exceeds_ten_million": infinity_condition > 10**7,
    "unit_hostile_response_is_below_resolution_floor": singular_values[-1]
    < resolution_floor,
    "resolution_times_condition_exceeds_one": resolution_floor
    * spectral_condition
    > 1,
}
checks = {name: bool(value) for name, value in checks.items()}


def decimal(value, digits=18):
    return mp.nstr(value, digits)


result = {
    "work_package": "WP554",
    "domain": "The exact WP540 six-node companion-resolvent context matrix on the frozen WP520 source witness, before a measured covariance metric is available.",
    "nodes_GeV_squared": [str(node) for node in nodes],
    "exact_rank": contexts.rank(),
    "exact_determinant_nonzero": bool(determinant != 0),
    "determinant_decimal": decimal(sp.N(determinant, 40)),
    "conditioning": {
        "working_decimal_precision": mp.mp.dps,
        "singular_values": [decimal(value) for value in singular_values],
        "spectral_condition_number": decimal(spectral_condition),
        "infinity_norm_condition_number": decimal(infinity_condition),
        "hostile_absolute_resolution_floor": decimal(resolution_floor),
        "resolution_times_spectral_condition": decimal(
            resolution_floor * spectral_condition
        ),
    },
    "contextual_partition": "At zero tolerance the exact matrix gives singleton coefficient classes. At nonzero tolerance, x and y are equivalent when the covariance-whitened norm of C(x-y) is below the declared detection threshold; the actual partition is undefined until measured covariance is supplied.",
    "classification": "Exact-rank confirmation plus high-precision conditioning criticism of an unexecuted instrument; neither selector nor source-law modification.",
    "selector": bool(wp541.get("selector", False)),
    "rigidifier": bool(contexts.rank() == 6),
    "instrument": "The twist contexts are executable in principle, but physical separation requires the smallest singular value of the full covariance-whitened response and an independently declared detection threshold.",
    "smallest_exact_falsifier": "The exact determinant remains nonzero, yet the unit right-singular hostile has response norm about 9.03e-7, below the declared 1e-6 diagnostic floor. Exact rank therefore does not imply resolution-robust faithfulness.",
    "remaining_gate": "Generate the WP542 data and full covariance, whiten the complete scale-renormalization-context response, preregister the admitted source displacement norm and detection threshold, and show the smallest singular value survives continuum, volume, drift, and uncertainty completion.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp554_six_context_conditioning_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
