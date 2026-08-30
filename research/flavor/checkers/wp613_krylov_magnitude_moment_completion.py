"""Exact WP613 Krylov-magnitude fiber and three-moment completion."""

import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

eigenvalues = sp.Matrix([1, 2, 3])
moment_matrix = sp.Matrix(
    [[1, 1, 1], [1, 2, 3], [1, 4, 9]]
)

p = sp.Matrix([sp.Rational(1, 13), sp.Rational(6, 13), sp.Rational(6, 13)])
q = sp.Matrix([sp.Rational(2, 13), sp.Rational(2, 13), sp.Rational(9, 13)])

p_product = sp.prod(p)
q_product = sp.prod(q)
p_moments = moment_matrix * p
q_moments = moment_matrix * q
p_reconstructed = sp.simplify(moment_matrix.inv() * p_moments)
q_reconstructed = sp.simplify(moment_matrix.inv() * q_moments)

# Central measured CKM magnitudes from flavor-nine-link-conventions.md.
vus, vub, vcb = 0.22517, 0.003763, 0.04189
vcd, vtd, vts = 0.22503, 0.00863, 0.04117
vud = math.sqrt(1 - vus**2 - vub**2)
vcs = math.sqrt(1 - vcd**2 - vcb**2)
vtb = math.sqrt(1 - vub**2 - vcb**2)
columns = {
    "d": [vud**2, vcd**2, vtd**2],
    "s": [vus**2, vcs**2, vts**2],
    "b": [vub**2, vcb**2, vtb**2],
}
normalized_columns = {
    name: [value / sum(values) for value in values]
    for name, values in columns.items()
}
normalized_products = {
    name: 27 * math.prod(values) for name, values in normalized_columns.items()
}

checks = {
    "hostile_probabilities_are_normalized": sum(p) == 1 and sum(q) == 1,
    "hostile_probabilities_are_distinct_not_permutations": p != q
    and sorted(p) != sorted(q),
    "hostile_pair_has_same_krylov_magnitude_factor": p_product
    == q_product
    == sp.Rational(36, 2197),
    "hostile_pair_has_different_first_moment": p_moments[1]
    == sp.Rational(31, 13)
    and q_moments[1] == sp.Rational(33, 13),
    "hostile_pair_has_different_second_moment": p_moments[2]
    == sp.Rational(79, 13)
    and q_moments[2] == sp.Rational(91, 13),
    "three_moment_vandermonde_is_invertible": moment_matrix.det() == 2,
    "three_moments_reconstruct_p": p_reconstructed == p,
    "three_moments_reconstruct_q": q_reconstructed == q,
    "measured_columns_are_positive_normalized": all(
        all(value > 0 for value in values)
        and abs(sum(values) - 1) < 1e-15
        for values in normalized_columns.values()
    ),
    "measured_columns_are_strictly_nondemocratic": all(
        max(values) - min(values) > 0.5 for values in normalized_columns.values()
    ),
    "measured_krylov_products_are_strictly_interior": all(
        0 < value < 1 for value in normalized_products.values()
    ),
    "measured_products_are_far_below_democratic_maximum": all(
        value < 0.01 for value in normalized_products.values()
    ),
}

if not all(checks.values()):
    raise SystemExit(f"WP613 check failed: {checks}")

result = {
    "work_package": "WP613",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "state_domain": "normalized seed spectral weights p_i on a nondegenerate three-level Hermitian evolution",
    "krylov_magnitude_coordinate": "kappa=27 product_i p_i in [0,1]",
    "exact_hostile_fiber": [
        ["1/13", "6/13", "6/13"],
        ["2/13", "2/13", "9/13"],
    ],
    "hostile_common_product": "36/2197",
    "source_probe_completion": "moments mu_0,mu_1,mu_2 with mu_k=sum_i a_i^k p_i",
    "contextual_partition": "kappa has non-singleton fibers; the three-moment Vandermonde record is faithful when the spectrum is nondegenerate",
    "measured_normalized_products": normalized_products,
    "classification": "Krylov magnitude is a positive nonfaithful readout; the moment tower repairs readout faithfulness but neither operation selects a seed distribution",
    "smallest_exact_falsifier": "the two displayed probability triples have equal Krylov magnitude and distinct first moments",
    "selector_gate": "derive a source law for the moment values or full weight vector; coefficient-free product extremization selects a boundary or the democratic point, not the measured hierarchical columns",
    "instrument": "charged-current branching fractions measure p_i for spectral seeds; moment combinations are executable summaries of that record, not independent source dynamics",
}

out = ROOT / "results" / "wp613_krylov_magnitude_moment_completion.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
