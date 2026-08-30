"""Exact affine G2 root/coroot portal typing and source-fiber audit."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp796 = json.loads(
    (ROOT / "results" / "wp796_compact_clockwork_relative_portal_fiber.json")
    .read_text(encoding="utf-8")
)

kappa = sp.symbols("kappa", positive=True, real=True)

# Convention: A_ij = 2(alpha_i, alpha_j)/(alpha_j, alpha_j).
A_finite = sp.Matrix([[2, -1], [-3, 2]])
D_finite_root = sp.diag(1, 3)
G_finite_root = A_finite * D_finite_root

# Nodes are alpha_0=-theta (long), alpha_1 (short), alpha_2 (long), with
# theta=3 alpha_1+2 alpha_2.
A_affine = sp.Matrix([
    [2, 0, -1],
    [0, 2, -1],
    [-1, -3, 2],
])
marks = sp.Matrix([1, 3, 2])
comarks = sp.Matrix([1, 1, 2])

# Right symmetrization is the root Gram form; left symmetrization is the
# dual/coroot Gram form in this convention.
D_root = sp.diag(3, 1, 3)
D_coroot = sp.diag(1, 3, 1)
G_root = A_affine * D_root
G_coroot = D_coroot * A_affine

root_eigenvalues = sorted(G_root.eigenvals().keys(), key=lambda x: float(x))
coroot_eigenvalues = sorted(G_coroot.eigenvals().keys(), key=lambda x: float(x))

expected_root = [0, 7 - sp.sqrt(7), 7 + sp.sqrt(7)]
expected_coroot = [0, 5 - sp.sqrt(7), 5 + sp.sqrt(7)]

checks = {
    "wp796_dependency_passed": wp796["status"] == "PASS"
    and all(wp796["checks"].values()),
    "finite_g2_is_full_rank": A_finite.det() == 1,
    "finite_root_gram_is_positive_definite":
        G_finite_root.det() == 3 and G_finite_root.trace() > 0,
    "affine_g2_has_corank_one": A_affine.rank() == 2,
    "kac_marks_are_left_cartan_null":
        marks.T * A_affine == sp.zeros(1, 3),
    "comarks_are_right_cartan_null":
        A_affine * comarks == sp.zeros(3, 1),
    "marks_are_not_right_cartan_null":
        A_affine * marks != sp.zeros(3, 1),
    "root_symmetrization_is_symmetric": G_root == G_root.T,
    "coroot_symmetrization_is_symmetric": G_coroot == G_coroot.T,
    "root_gram_kernel_is_kac_marks": G_root * marks == sp.zeros(3, 1),
    "coroot_gram_kernel_is_comarks":
        G_coroot * comarks == sp.zeros(3, 1),
    "root_gram_has_exact_positive_gap": root_eigenvalues == expected_root,
    "coroot_gram_has_exact_positive_gap":
        coroot_eigenvalues == expected_coroot,
    "root_and_coroot_profiles_are_inequivalent":
        marks.cross(comarks) != sp.zeros(3, 1),
    "overall_quadratic_scale_is_free":
        sp.diff(kappa * G_root, kappa) == G_root,
    "quadratic_form_does_not_select_kernel_sign":
        (marks.T * G_root * marks)[0]
        == ((-marks).T * G_root * (-marks))[0],
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP797",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP796",
    "admitted_state_domain": (
        "the finite G2 root datum and its untwisted affine extension, with "
        "declared short/long-root convention, Cartan pairing, root and "
        "coroot symmetrizations, positive overall quadratic scale kappa, and "
        "no undeclared map from Dynkin nodes to Standard Model species"
    ),
    "faithful_coordinate": (
        "the labelled affine root datum together with the choice of root or "
        "coroot pairing, node-to-species map, overall scale, RG completion, "
        "threshold state, and physical16 detector response"
    ),
    "source_authorized_probe_family": (
        "Cartan incidence, Kac marks, comarks, the two canonical symmetric "
        "Gram forms, their kernels, and their exact nonzero spectra"
    ),
    "contextual_partition": (
        "finite G2 has no kernel; affine root coupling gives the mark ray "
        "(1,3,2), while affine coroot coupling gives the distinct comark ray "
        "(1,1,2); each ray remains sign-blind and scale-free until an "
        "external representation, orientation, and normalization are named"
    ),
    "selector_result": (
        "affine G2 is a conditional relative-profile selector and gapped "
        "rigidifier after a root-versus-coroot coupling functor is declared; "
        "the bare root datum selects neither that functor nor a flavor portal"
    ),
    "smallest_exact_falsifier": (
        "the same affine G2 Cartan datum admits the symmetric root Gram "
        "kernel (1,3,2) and symmetric coroot Gram kernel (1,1,2); both are "
        "positive semidefinite with a strict gap, so Cartan data alone do not "
        "authorize the desired triple as the executable coupling profile"
    ),
    "sign_result": (
        "long-versus-short orientation is intrinsic to the labelled root "
        "datum, but a quadratic Gram form is invariant under kernel-vector "
        "sign reversal and no node-to-flavor assignment is source-derived"
    ),
    "magnitude_result": (
        "Kac marks fix an integer relative ray only in the root realization; "
        "the overall coefficient kappa and its conversion to portal units "
        "remain continuous source fibers"
    ),
    "rg_threshold_result": (
        "the exact null ray and positive spectral gap are algebraic basin "
        "data, not a completed matter beta function or finite threshold "
        "matching theorem; kappa and the heavy realization remain untyped"
    ),
    "instrument_result": (
        "Dynkin marks and Gram eigenmodes have no declared physical16 "
        "perturbation map or experimentally calibrated detector instrument"
    ),
    "deutschian_status": (
        "G2 makes the triple bond and each conditional kernel hard to vary, "
        "but the root/coroot coupling choice, flavor embedding, sign, scale, "
        "RG completion, thresholds, and readout remain easy to vary"
    ),
    "remaining_gate": (
        "derive from one source action a representation functor that chooses "
        "the root mark ray over the coroot ray, assigns its oriented nodes to "
        "flavor species, normalizes kappa, and co-generates RG, threshold, "
        "and calibrated physical16 response"
    ),
    "primary_sources": [
        "https://arxiv.org/abs/1207.7205",
        "https://arxiv.org/abs/2305.00810",
    ],
}

(ROOT / "results" / "wp797_affine_g2_root_coroot_portal_typing.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
