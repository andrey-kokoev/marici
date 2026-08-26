"""Exact periodic-lattice support witness for the six WP539 contexts."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp524 = load("wp524_euclidean_h0_estimator.json")
wp535 = load("wp535_six_port_bilocal_instrument.json")
wp539 = load("wp539_common_ensemble_resolvent_contexts.json")
wp520 = load("wp520_finite_propagator_bs_kernel.json")

z = sp.symbols("z")
kernel = sp.sympify(
    wp520["aligned_bs_kernel"]["exact_witness_rational_function"],
    locals={"z": z},
)
_, denominator = [sp.expand(value) for value in sp.fraction(kernel)]
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

# Periodic direction with N=24, a=1 GeV^-1 and even Fourier indices.  The
# scale is an independently declared QCD scale-setting witness, not a fit to
# the flavor poles or target ratio.
site_count = 24
lattice_spacing_GeV_inverse = sp.Integer(1)
mode_indices = (0, 2, 4, 6, 8, 10)
lattice_nodes = tuple(
    sp.expand_trig(
        4
        * sp.sin(sp.pi * mode / site_count) ** 2
        / lattice_spacing_GeV_inverse**2
    )
    for mode in mode_indices
)
lattice_nodes = tuple(sp.radsimp(sp.simplify(value)) for value in lattice_nodes)

contexts = sp.Matrix.hstack(
    *[(node * sp.eye(degree) - A).inv() * B for node in lattice_nodes]
)
determinant = sp.radsimp(sp.factor(contexts.det()))
five_context_ranks = [
    contexts[:, [column for column in range(degree) if column != omitted]].rank()
    for omitted in range(degree)
]

channel_count = len(wp535["raw_estimator"]["operator_channels"])
ward_map = sp.kronecker_product(contexts.T, sp.eye(channel_count))

extent_GeV_inverse = site_count * lattice_spacing_GeV_inverse
minimum_nonzero_continuum_momentum = 2 * sp.pi / extent_GeV_inverse
minimum_nonzero_lattice_momentum_squared = lattice_nodes[1]

# Hostile alias: n and N-n have identical lattice momentum squared.
aliased_modes = (0, 2, 4, 6, 8, 16)
aliased_nodes = tuple(
    sp.radsimp(
        sp.simplify(
            4
            * sp.sin(sp.pi * mode / site_count) ** 2
            / lattice_spacing_GeV_inverse**2
        )
    )
    for mode in aliased_modes
)
aliased_contexts = sp.Matrix.hstack(
    *[(node * sp.eye(degree) - A).inv() * B for node in aliased_nodes]
)

checks = {
    "dependencies_passed": all(bool(packet["passed"]) for packet in (wp524, wp535, wp539)),
    "six_supported_modes_are_declared": len(mode_indices) == degree == 6,
    "exact_nodes_match_expected_algebraic_values": lattice_nodes
    == (0, 2 - sp.sqrt(3), 1, 2, 3, sp.sqrt(3) + 2),
    "all_supported_nodes_are_distinct": len(set(lattice_nodes)) == degree,
    "all_supported_nodes_avoid_timelike_poles": all(monic.subs(z, node) != 0 for node in lattice_nodes),
    "periodic_lattice_context_matrix_has_rank_six": contexts.rank() == 6,
    "periodic_lattice_context_determinant_is_nonzero": determinant != 0,
    "every_supported_five_context_deletion_has_rank_five": all(rank == 5 for rank in five_context_ranks),
    "four_channel_supported_map_has_rank_twenty_four": ward_map.rank() == 24,
    "hostile_periodic_alias_repeats_a_node": len(set(aliased_nodes)) == 5,
    "hostile_periodic_alias_lowers_rank_to_five": aliased_contexts.rank() == 5,
    "finite_extent_has_nonzero_momentum_gap": minimum_nonzero_continuum_momentum > 0,
    "lattice_momentum_gap_is_positive": minimum_nonzero_lattice_momentum_squared > 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP540",
    "domain": "A one-direction periodic lattice support witness for WP539's six deterministic resolvent contexts, using WP524's standard nearest-neighbor lattice momentum.",
    "lattice_support_witness": {
        "site_count": site_count,
        "lattice_spacing_GeV_inverse": str(lattice_spacing_GeV_inverse),
        "spatial_extent_GeV_inverse": str(extent_GeV_inverse),
        "mode_indices": list(mode_indices),
        "lattice_momentum_squares_GeV_squared": [str(value) for value in lattice_nodes],
        "minimum_nonzero_continuum_momentum_GeV": str(minimum_nonzero_continuum_momentum),
        "minimum_nonzero_lattice_momentum_squared_GeV_squared": str(minimum_nonzero_lattice_momentum_squared),
        "scale_authority": "The a=1 GeV^-1 witness is fixed before the rank calculation and must be replaced in a physical run by ordinary QCD scale setting, independent of flavor-pole or target-ratio data.",
    },
    "rank_certificate": {
        "context_rank": contexts.rank(),
        "context_determinant": str(determinant),
        "five_context_deletion_ranks": five_context_ranks,
        "four_channel_complex_rank": ward_map.rank(),
        "real_estimator_dimension": 2 * ward_map.rows,
    },
    "periodic_alias_falsifier": {
        "mode_indices": list(aliased_modes),
        "lattice_momentum_squares_GeV_squared": [str(value) for value in aliased_nodes],
        "context_rank": aliased_contexts.rank(),
        "conclusion": "Modes n and N-n can alias in qhat^2. Choosing mode 16 instead of 10 repeats the node of mode 8 and lowers rank to five.",
    },
    "theorem": "A concrete N=24 periodic direction supports six exact distinct lattice momentum-squared contexts with rank six. With the four Ward channels the supported postprocessing map has complex rank 24. Periodic momentum labels alone are not sufficient: an exact n versus N-n alias lowers the context rank to five.",
    "classification": "Exact kinematic-support and alias-control witness. It supplies a realizable momentum grammar for WP539 without fitting flavor data, but it is not continuum-extrapolated or detector-calibrated data.",
    "selector": False,
    "instrument": "The discrete momentum support is now explicit. Physical realization still requires QCD scale setting, multiple lattice spacings and volumes, the four renormalized bilocal channel measurements, threshold matching, and the common 48-real covariance.",
    "smallest_exact_falsifier": "Replace mode 10 by its periodic alias mode 16. The last two qhat-squared values coincide at 3 and context rank falls exactly from six to five.",
    "remaining_gate": "Preregister a scale-setting observable, lattice spacings, volumes, momentum tuples, renormalization and contact-subtraction scheme, then generate the common four-channel B_s correlator dataset and continuum covariance.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp540_periodic_lattice_context_support.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
