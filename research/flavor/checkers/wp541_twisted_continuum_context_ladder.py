"""Exact twisted-boundary continuum ladder for the WP540 context support."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp524 = load("wp524_euclidean_h0_estimator.json")
wp539 = load("wp539_common_ensemble_resolvent_contexts.json")
wp540 = load("wp540_periodic_lattice_context_support.json")
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

nodes = (0, 2 - sp.sqrt(3), 1, 2, 3, 2 + sp.sqrt(3))
spacings = (sp.Integer(1), sp.Rational(1, 2), sp.Rational(1, 3))
physical_extent = sp.Integer(24)
site_counts = tuple(int(physical_extent / spacing) for spacing in spacings)


def twist_packet(spacing, site_count):
    link_angles = tuple(
        sp.simplify(2 * sp.asin(spacing * sp.sqrt(node) / 2))
        for node in nodes
    )
    recovered = tuple(
        sp.simplify(4 * sp.sin(angle / 2) ** 2 / spacing**2)
        for angle in link_angles
    )
    physical_momenta = tuple(sp.simplify(angle / spacing) for angle in link_angles)
    boundary_phases = tuple(sp.simplify(site_count * angle) for angle in link_angles)
    return link_angles, recovered, physical_momenta, boundary_phases


ladders = [twist_packet(spacing, count) for spacing, count in zip(spacings, site_counts)]
recovered_ladders = [packet[1] for packet in ladders]

contexts = sp.Matrix.hstack(
    *[(node * sp.eye(degree) - A).inv() * B for node in nodes]
)

h, u = sp.symbols("h u", positive=True)
physical_momentum_squared = sp.simplify(
    (2 * sp.asin(h * sp.sqrt(u) / 2) / h) ** 2
)
continuum_series = sp.series(physical_momentum_squared, h, 0, 5).removeO()
continuum_limit = sp.limit(physical_momentum_squared, h, 0, dir="+")

# Hostile no-reference experiment: all link angles are zero in one Fourier
# sector, so all six requested contexts coincide at zero.
zero_twist_nodes = tuple(sp.Integer(0) for _ in nodes)
zero_twist_contexts = sp.Matrix.hstack(
    *[(node * sp.eye(degree) - A).inv() * B for node in zero_twist_nodes]
)

checks = {
    "dependencies_passed": all(bool(packet["passed"]) for packet in (wp524, wp539, wp540)),
    "fixed_physical_extent_across_three_spacings": tuple(
        sp.simplify(spacing * count) for spacing, count in zip(spacings, site_counts)
    ) == (24, 24, 24),
    "site_counts_refine_as_24_48_72": site_counts == (24, 48, 72),
    "all_twist_arguments_are_admissible": all(
        spacing * sp.sqrt(node) / 2 < 1
        for spacing in spacings
        for node in nodes
    ),
    "every_spacing_recovers_the_same_six_lattice_nodes": all(
        tuple(sp.simplify(value) for value in recovered) == nodes
        for recovered in recovered_ladders
    ),
    "common_context_matrix_has_rank_six": contexts.rank() == 6,
    "physical_momentum_has_correct_continuum_limit": continuum_limit == u,
    "leading_lattice_momentum_correction_is_exact": continuum_series
    == u + h**2 * u**2 / 12 + h**4 * u**3 / 90,
    "zero_twist_single_sector_is_rank_one": zero_twist_contexts.rank() == 1,
    "twist_port_changes_the_contextual_partition": contexts.rank() != zero_twist_contexts.rank(),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP541",
    "domain": "WP540's six lattice-momentum nodes on a fixed 24 GeV^-1 extent, refined through a=1, 1/2 and 1/3 GeV^-1 with partially twisted valence boundary conditions.",
    "continuum_ladder": {
        "physical_extent_GeV_inverse": str(physical_extent),
        "lattice_spacings_GeV_inverse": [str(value) for value in spacings],
        "site_counts": list(site_counts),
        "fixed_lattice_momentum_squares_GeV_squared": [str(value) for value in nodes],
        "link_angle_rule": "alpha_j(a)=2 asin(a sqrt(z_j)/2)",
        "boundary_phase_rule": "phi_j=N alpha_j modulo 2 pi, accompanied by its Fourier-sector label",
        "physical_momentum_rule": "p_j(a)=alpha_j(a)/a",
        "physical_momentum_squared_continuum_series": str(continuum_series),
        "continuum_limit": str(continuum_limit),
        "boundary_phases_unwrapped": [
            [str(value) for value in packet[3]] for packet in ladders
        ],
    },
    "rank_certificate": {
        "rank_at_every_spacing": contexts.rank(),
        "reason": "The twist rule holds qhat_j^2 fixed at the same six exact distinct nodes, so every spacing uses the same nonsingular resolvent context matrix.",
        "zero_twist_single_sector_rank": zero_twist_contexts.rank(),
    },
    "changed_groupoid": "The twist holonomies and Fourier-sector labels are added reference/control ports. They define a new relational boundary-condition experiment over the stabilizer preserving those holonomies; they do not reveal an absolute phase of the original periodic experiment.",
    "theorem": "A fixed-volume three-spacing twisted-boundary ladder preserves all six exact WP540 lattice-momentum contexts and rank six while the corresponding physical momenta approach their continuum values with an exact even-power expansion. Removing the twist/reference port in one Fourier sector collapses all contexts to zero and rank one.",
    "classification": "Continuum-extrapolation and boundary-control contract for the instrument. It changes the experimental groupoid explicitly, does not alter source dynamics, and does not select t.",
    "instrument": "Kinematic control is executable in principle through partially twisted valence boundary conditions. Physical authority still requires a preregistered scale-setting observable and actual renormalized four-channel B_s correlator measurements at all three spacings with joint systematics.",
    "smallest_exact_falsifier": "Set all twists to zero while retaining one Fourier sector. All six qhat-squared nodes coincide at zero and the context rank falls from six to one.",
    "remaining_gate": "Freeze the QCD scale-setting and renormalization scheme, generate the common bilocal data on the 24, 48 and 72-site ensembles, and fit the exact a^2 and a^4 continuum response with full cross-spacing covariance.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp541_twisted_continuum_context_ladder.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
