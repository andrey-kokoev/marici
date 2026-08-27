"""Exact 5D supersymmetric-prepotential typing audit."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp787 = json.loads(
    (ROOT / "results" / "wp787_su4_cubic_orientation_portal_fiber.json")
    .read_text(encoding="utf-8")
)

a, r, level, s = sp.symbols("a r level s", real=True)
level_pos, s_pos = sp.symbols("level_pos s_pos", positive=True)

# Restriction of the standard 5D cubic prepotential to
# T=diag(1,1,1,-3), with r=1/g_5^2.
prepotential = sp.expand(6 * r * a**2 - 4 * level * a**3)
kinetic_metric = sp.diff(prepotential, a, 2)
mirror_metric_residual = sp.simplify(
    kinetic_metric.subs({a: -a, level: -level}, simultaneous=True)
    - kinetic_metric
)

# Exact fixed-point-face positivity witness: r=0, level>0, a=-s<0.
fixed_face_metric = sp.simplify(
    kinetic_metric.subs({r: 0, level: level_pos, a: -s_pos})
)

# Unbroken supersymmetry leaves the Coulomb coordinate with zero potential.
coulomb_potential = sp.Integer(0)
coulomb_force = sp.diff(coulomb_potential, a)
coulomb_hessian = sp.diff(coulomb_potential, a, 2)

weights = (1, 1, 1, -3)
signed_masses = tuple(sp.expand(q * a) for q in weights)
scalar_mass_squares = tuple(sp.expand(m**2) for m in signed_masses)
mirror_scalar_mass_squares = tuple(
    sp.expand(m.subs(a, -a)) for m in scalar_mass_squares
)
threshold_ratio = sp.simplify(sp.Abs(signed_masses[3]) / sp.Abs(signed_masses[0]))

triplet_mass_square = scalar_mass_squares[0]
singlet_mass_square = scalar_mass_squares[3]
even_contrast = sp.expand(triplet_mass_square - singlet_mass_square)
scale_hostile_ratio = sp.simplify(
    even_contrast.subs(a, 2 * a) / even_contrast
)

checks = {
    "wp787_dependency_passed": wp787["status"] == "PASS"
    and all(wp787["checks"].values()),
    "restricted_prepotential_is_cubic": prepotential
    == -4 * a**3 * level + 6 * a**2 * r,
    "cubic_prepotential_changes_kinetic_metric": sp.simplify(
        kinetic_metric - (-24 * a * level + 12 * r)
    )
    == 0,
    "mirror_level_and_coordinate_preserve_metric": mirror_metric_residual == 0,
    "fixed_point_face_positivity_selects_relative_half_ray": fixed_face_metric
    == 24 * level_pos * s_pos,
    "supersymmetric_coulomb_force_is_zero": coulomb_force == 0,
    "supersymmetric_coulomb_hessian_is_zero": coulomb_hessian == 0,
    "gauge_fixed_signed_masses_have_three_plus_one_weights": signed_masses
    == (a, a, a, -3 * a),
    "scalar_mass_operator_is_orientation_even": scalar_mass_squares
    == mirror_scalar_mass_squares,
    "relative_threshold_ratio_is_three": threshold_ratio == 3,
    "induced_even_contrast_is_minus_eight_a_squared": even_contrast == -8 * a**2,
    "coulomb_modulus_changes_contrast_by_factor_four": scale_hostile_ratio == 4,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP788",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP787",
    "admitted_state_domain": (
        "the SU(4) Coulomb ray, a formal 5D N=1 cubic prepotential with inverse "
        "gauge coupling r and Chern-Simons level, its positive kinetic cone, "
        "and a fundamental hypermultiplet with weights (1,1,1,-3)"
    ),
    "faithful_coordinate": (
        "signed Coulomb coordinate a, signed level, inverse gauge coupling r, "
        "kinetic metric, signed BPS masses, and scalar mass squares"
    ),
    "source_authorized_probe_family": (
        "prepotential derivatives and gauge-fixed hypermultiplet weights; the "
        "formal fixed-point face r=0 is tested conditionally and is not claimed "
        "as an established SU(4) ultraviolet completion"
    ),
    "contextual_partition": (
        "the positive kinetic cone fixes the sign of a relative to the level at "
        "r=0, while scalar masses and thresholds retain only a squared "
        "orientation and leave every magnitude along the allowed half-ray"
    ),
    "selector_result": (
        "extended gauge structure removes an independent matter-vertex eta and "
        "can orient a Coulomb half-ray, but it supplies no potential selecting "
        "a point and its scalar operator is orientation even"
    ),
    "smallest_exact_falsifier": (
        "a=-s and a=-2s lie in the same positive fixed-face cone for positive "
        "level, have the same quantized level and threshold ratio three, but "
        "their scalar portal contrasts differ by a factor four"
    ),
    "rg_result": (
        "even granting the r=0 fixed-point face, the Coulomb modulus is a flat "
        "direction; fixed-point authority does not select its relevant vacuum "
        "coordinate or compactification clock"
    ),
    "threshold_result": (
        "the relative 3:1 mass threshold is gauge fixed, but the absolute "
        "threshold is proportional to |a| and remains free"
    ),
    "instrument_result": (
        "mass spectroscopy can read the 3:1 ratio but is blind to a->-a; a "
        "signed interference or chirality channel and its calibration remain "
        "absent"
    ),
    "deutschian_status": (
        "the prepotential makes relative charges and a positivity half-ray hard "
        "to vary, but it does not explain the Coulomb point, absolute scale, or "
        "signed physical portal"
    ),
    "remaining_gate": (
        "a source-derived supersymmetry-breaking or boundary operation must lift "
        "the Coulomb modulus at a unique point while retaining the quantized "
        "level relation, then survive compactification thresholds and reach a "
        "signed calibrated instrument"
    ),
    "primary_sources": [
        "https://arxiv.org/abs/hep-th/9702198",
        "https://arxiv.org/abs/hep-th/0609078",
    ],
}
(ROOT / "results" / "wp788_5d_susy_prepotential_coulomb_modulus_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
