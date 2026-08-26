"""Exact six-context postprocessing design for the WP538 system pencil."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp524 = load("wp524_euclidean_h0_estimator.json")
wp525 = load("wp525_complex_mass_ward_completion.json")
wp535 = load("wp535_six_port_bilocal_instrument.json")
wp538 = load("wp538_source_six_port_system_pencil.json")

z = sp.symbols("z")
kernel = sp.sympify(
    load("wp520_finite_propagator_bs_kernel.json")["aligned_bs_kernel"][
        "exact_witness_rational_function"
    ],
    locals={"z": z},
)
numerator, denominator = [sp.expand(value) for value in sp.fraction(kernel)]
leading = sp.LC(sp.Poly(denominator, z))
monic = sp.expand(denominator / leading)
coefficients = sp.Poly(monic, z).all_coeffs()
degree = sp.degree(monic, z)

A = sp.zeros(degree)
for row in range(degree - 1):
    A[row, row + 1] = 1
for column, coefficient in enumerate(reversed(coefficients[1:])):
    A[degree - 1, column] = -coefficient
B = sp.zeros(degree, 1)
B[degree - 1, 0] = 1

# Six normalized Euclidean momentum-squared contexts. They are deterministic
# analysis kernels on one correlator ensemble, not six changes of source law.
nodes = tuple(sp.Integer(value) for value in range(degree))
contexts = sp.Matrix.hstack(
    *[(node * sp.eye(degree) - A).inv() * B for node in nodes]
)
context_determinant = sp.factor(contexts.det())
five_context_ranks = [
    contexts[:, [column for column in range(degree) if column != omitted]].rank()
    for omitted in range(degree)
]

# Four Ward channels are measured on the same gauge ensemble. Reweighting the
# common raw channel data gives 24 complex estimators.
channel_count = len(wp535["raw_estimator"]["operator_channels"])
ward_context_map = sp.kronecker_product(contexts.T, sp.eye(channel_count))

# Deliberate collision: two identical momentum contexts must destroy joint
# faithfulness without changing any source coefficient.
collided_nodes = (0, 1, 2, 3, 4, 4)
collided_contexts = sp.Matrix.hstack(
    *[(node * sp.eye(degree) - A).inv() * B for node in collided_nodes]
)

node_denominators = [sp.factor(monic.subs(z, node)) for node in nodes]

checks = {
    "dependencies_passed": all(
        bool(packet["passed"]) for packet in (wp524, wp525, wp535, wp538)
    ),
    "six_declared_euclidean_nodes": len(nodes) == degree == 6,
    "all_context_nodes_avoid_poles": all(value != 0 for value in node_denominators),
    "six_resolvent_contexts_have_rank_six": contexts.rank() == 6,
    "context_determinant_is_exactly_nonzero": context_determinant != 0,
    "every_five_context_deletion_has_rank_five": all(rank == 5 for rank in five_context_ranks),
    "four_ward_channels_give_twenty_four_complex_outputs": ward_context_map.shape == (24, 24),
    "full_ward_context_map_has_rank_twenty_four": ward_context_map.rank() == 24,
    "real_imaginary_covariance_dimension_is_forty_eight": 2 * ward_context_map.rows == 48,
    "colliding_two_contexts_is_deliberately_nonfaithful": collided_contexts.rank() == 5,
    "context_reweighting_does_not_add_a_source_parameter": len(nodes) == 6 and A.free_symbols == set(),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP539",
    "domain": "The WP538 exact companion pencil and WP525 four-channel Ward-complete bilocal family, evaluated on one common Euclidean correlator ensemble.",
    "context_design": {
        "normalized_momentum_squared_nodes": [str(value) for value in nodes],
        "node_unit": "one independently calibrated Euclidean momentum-squared unit; the exact rank theorem is scale-generic away from poles and node collisions",
        "context_matrix_rule": "column j is (z_j I_6-A)^(-1) B",
        "context_matrix_shape": list(contexts.shape),
        "context_matrix_rank": contexts.rank(),
        "context_determinant": str(context_determinant),
        "five_context_deletion_ranks": five_context_ranks,
    },
    "common_ensemble_factorization": {
        "preparation_count": 1,
        "operator_channels": wp535["raw_estimator"]["operator_channels"],
        "deterministic_kernel_count": 6,
        "complex_estimator_count": ward_context_map.rows,
        "real_estimator_count": 2 * ward_context_map.rows,
        "joint_complex_rank": ward_context_map.rank(),
        "rule": "Measure the four renormalized momentum-resolved bilocal channels on common gauge configurations, then apply all six fixed resolvent kernels in postprocessing. Cross-context covariance is retained because no ensemble is split.",
    },
    "hostile_collision": {
        "nodes": [str(value) for value in collided_nodes],
        "rank": collided_contexts.rank(),
        "conclusion": "Repeating one context lowers rank to five; distinct calibrated momentum contexts are necessary, not a cosmetic sampling choice.",
    },
    "theorem": "Six distinct Euclidean resolvent contexts on one common four-channel correlator ensemble give an exact rank-24 complex postprocessing map, equivalent to 48 real estimators. They do not require six different source-law preparations. Every five-context deletion has rank five, and one repeated context is an exact rank-loss falsifier.",
    "classification": "Executable deterministic analysis design conditional on acquiring the common renormalized correlator dataset. It realizes algebraic context closure as postprocessing, not as source control, and it neither selects t nor repairs an absent source selector.",
    "instrument": "Partially typed: one common ensemble, four Ward channels, six calibrated Euclidean momentum contexts, deterministic complex kernels, and a 48-real joint covariance. No existing B_s dataset supplies the required renormalized bilocal correlators.",
    "smallest_exact_falsifier": "Replace the final node 5 by 4. The six-context matrix rank falls exactly from six to five, and the 24-channel map loses four complex dimensions.",
    "remaining_gate": "Choose an independently calibrated physical momentum unit and lattice volume that realize six distinct supported contexts; compute the four renormalized bilocal channels with contact subtraction, continuum and finite-volume control, threshold matching, and the full common-ensemble covariance.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp539_common_ensemble_resolvent_contexts.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
