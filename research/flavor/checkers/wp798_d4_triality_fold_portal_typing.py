"""Exact D4 triality-fold typing for the asymmetric flavor portal."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp797 = json.loads(
    (ROOT / "results" / "wp797_affine_g2_root_coroot_portal_typing.json")
    .read_text(encoding="utf-8")
)

# Affine D4^(1): node order (a,c,o1,o2,o3), with central node c.
H = sp.Matrix([
    [2, -1, 0, 0, 0],
    [-1, 2, -1, -1, -1],
    [0, -1, 2, 0, 0],
    [0, -1, 0, 2, 0],
    [0, -1, 0, 0, 2],
])
d4_marks = sp.Matrix([1, 2, 1, 1, 1])

# Triality fixes a,c and cycles the three finite outer nodes.
P = sp.Matrix([
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
])

# Integral invariant, orbit-average, and canonically normalized bases.
F_sum = sp.Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1],
])
F_average = F_sum * sp.diag(1, 1, sp.Rational(1, 3))
F_normalized = F_sum * sp.diag(1, 1, 1 / sp.sqrt(3))

G_sum = sp.simplify(F_sum.T * H * F_sum)
G_average = sp.simplify(F_average.T * H * F_average)
G_normalized = sp.simplify(F_normalized.T * H * F_normalized)

profile_sum = sp.Matrix([1, 2, 1])
profile_average = sp.Matrix([1, 2, 3])
profile_normalized = sp.Matrix([1, 2, sp.sqrt(3)])

expected_sum_spectrum = [0, 5 - sp.sqrt(7), 5 + sp.sqrt(7)]
expected_average_spectrum = [
    0,
    (7 - sp.sqrt(7)) / 3,
    (7 + sp.sqrt(7)) / 3,
]
expected_normalized_spectrum = [0, 2, 4]


def spectrum(matrix):
    return sorted(matrix.eigenvals().keys(), key=lambda x: float(x))


checks = {
    "wp797_dependency_passed": wp797["status"] == "PASS"
    and all(wp797["checks"].values()),
    "affine_d4_marks_are_null": H * d4_marks == sp.zeros(5, 1),
    "triality_has_order_three": P**3 == sp.eye(5) and P != sp.eye(5),
    "triality_preserves_d4_gram": P.T * H * P == H,
    "integral_fold_is_fixed_by_triality": P * F_sum == F_sum,
    "integral_fold_gram_is_twisted_affine_g2":
        G_sum == sp.Matrix([[2, -1, 0], [-1, 2, -3], [0, -3, 6]]),
    "integral_fold_kernel_is_121": G_sum * profile_sum == sp.zeros(3, 1),
    "orbit_average_kernel_is_123":
        G_average * profile_average == sp.zeros(3, 1),
    "normalized_kernel_is_12sqrt3":
        G_normalized * profile_normalized == sp.zeros(3, 1),
    "all_three_profiles_are_same_d4_vector":
        F_sum * profile_sum
        == F_average * profile_average
        == F_normalized * profile_normalized
        == d4_marks,
    "sum_spectrum_has_exact_gap":
        spectrum(G_sum) == expected_sum_spectrum,
    "average_spectrum_has_exact_gap":
        spectrum(G_average) == expected_average_spectrum,
    "normalized_spectrum_has_exact_gap":
        spectrum(G_normalized) == expected_normalized_spectrum,
    "orbit_sum_has_index_three_over_average":
        F_sum[:, 2] == 3 * F_average[:, 2],
    "triple_is_coordinate_dependent_not_a_new_physical_ray":
        profile_sum != profile_average
        and F_sum * profile_sum == F_average * profile_average,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP798",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP797",
    "admitted_state_domain": (
        "the affine D4^(1) root lattice with its order-three triality "
        "automorphism, restricted to the three-dimensional invariant "
        "subspace in integral orbit-sum, rational orbit-average, and "
        "canonically normalized bases"
    ),
    "faithful_coordinate": (
        "the underlying D4 invariant vector together with its charge lattice, "
        "kinetic metric, electric or magnetic polarization, node-to-species "
        "map, overall scale, RG completion, thresholds, and physical16 readout"
    ),
    "source_authorized_probe_family": (
        "the D4 Gram form, triality action, invariant-subspace embeddings, "
        "folded Gram forms, exact kernels, and exact nonzero spectra"
    ),
    "contextual_partition": (
        "the profiles (1,2,1), (1,2,3), and (1,2,sqrt(3)) are coordinate "
        "descriptions of the same D4 null vector in orbit-sum, orbit-average, "
        "and normalized bases; they are not three distinct physical points"
    ),
    "selector_result": (
        "triality makes the orbit multiplicity three and long-short "
        "asymmetry unavoidable after D4 and the Z3 twist are admitted, but it "
        "does not select a portal value; the fold is a geometric rigidifier "
        "and a conditional representation selector"
    ),
    "smallest_exact_falsifier": (
        "the same source null vector has invariant-lattice coordinates "
        "(1,2,1) and orbit-average coordinates (1,2,3), while canonical "
        "normalization gives (1,2,sqrt(3)); treating the displayed 3 as a "
        "coupling prediction is therefore basis dependent"
    ),
    "sign_result": (
        "triality fixes the central-versus-three-orbit incidence but neither "
        "the sign of the null vector nor the map from folded nodes to the two "
        "physical flavor species"
    ),
    "magnitude_result": (
        "orbit cardinality fixes integral incidence, while kinetic "
        "normalization and the overall gauge or compactification coefficient "
        "remain source fibers"
    ),
    "rg_threshold_result": (
        "the folded quadratic forms have exact gaps, but this is not a "
        "matter-complete RG basin or finite threshold theorem; the Z3-twisted "
        "D4 constructions do not by themselves yield the Standard Model "
        "flavor completion"
    ),
    "instrument_result": (
        "no declared experiment maps a triality-invariant D4 mode into a "
        "calibrated perturbation of the faithful physical16 quotient"
    ),
    "deutschian_status": (
        "triality explains why an orbit of size three and a triple bond are "
        "hard to vary, but the claimed portal value changes under equally "
        "natural source-coordinate choices and remains easy to vary at the "
        "representation, normalization, and readout interfaces"
    ),
    "remaining_gate": (
        "derive a chiral electric matter action and kinetic pairing from the "
        "same triality-twisted source so that the invariant lattice, species "
        "assignment, normalization, beta functions, thresholds, and "
        "physical16 detector Jacobian are co-generated"
    ),
    "primary_sources": [
        "https://arxiv.org/abs/1311.0507",
        "https://arxiv.org/abs/1601.02077",
        "https://arxiv.org/abs/1207.7205",
    ],
}

(ROOT / "results" / "wp798_d4_triality_fold_portal_typing.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
