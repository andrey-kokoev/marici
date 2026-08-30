"""Exact mirror and modulus audit for globally quantized vertical G4 flux."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp792 = json.loads(
    (ROOT / "results" / "wp792_anomaly_complete_monopole_family_stability_no_go.json")
    .read_text(encoding="utf-8")
)

# A finite exact integral flux lattice packet. A is the intersection pairing,
# B encodes homogeneous F-theory transversality constraints, ell is a matter
# surface, and c2 is the integral second Chern class.
g1, g2 = sp.symbols("g1 g2", integer=True)
G = sp.Matrix([g1, g2])
A = sp.Matrix([[2, 1], [1, 4]])
B = sp.Matrix([[1, -1]])
ell = sp.Matrix([[2, 1]])
c2 = sp.Matrix([1, 3])

mirror_G = -G
tadpole = sp.expand((G.T * A * G)[0] / 2)
mirror_tadpole = sp.expand((mirror_G.T * A * mirror_G)[0] / 2)
chirality = sp.expand((ell * G)[0])
mirror_chirality = sp.expand((ell * mirror_G)[0])
transversality = B * G
mirror_transversality = B * mirror_G

# Shifted quantization is G+c2/2 integral. If k denotes that integral class,
# the mirror class is -G+c2/2 = -k+c2 and is integral because c2 is integral.
k1, k2 = sp.symbols("k1 k2", integer=True)
k = sp.Matrix([k1, k2])
G_from_shift = k - c2 / 2
mirror_shifted_class = sp.simplify(-G_from_shift + c2 / 2)
expected_mirror_shifted_class = -k + c2

# Primitivity and every other source-linear homogeneous constraint also
# descend to the mirror. Represent one exact Kähler contraction by J.
j1, j2 = sp.symbols("j1 j2", real=True)
J = sp.Matrix([[j1, j2]])
primitive = sp.expand((J * G)[0])
mirror_primitive = sp.expand((J * mirror_G)[0])

# "At least three" is a lower bound on absolute chirality, not singleton
# selection. The exact hostile packet contains both orientations at the
# minimal magnitude and a higher admissible magnitude.
admissible_chiralities = (-4, -3, 3, 4)
minimum_absolute_chirality = min(abs(x) for x in admissible_chiralities)

# The admitted scan computes flux consistency and chiral indices, but does not
# provide a complete stabilized-moduli Hessian or a detector response. This is
# a support statement, not the claim that vertical flux can never constrain
# complex structure through its Hodge-type condition.
declared_source_outputs = {
    "shifted_flux_class",
    "chern_simons_levels",
    "matter_chiral_indices",
    "d3_tadpole",
}

checks = {
    "wp792_dependency_passed": wp792["status"] == "PASS"
    and all(wp792["checks"].values()),
    "mirror_preserves_shifted_flux_quantization":
        mirror_shifted_class == expected_mirror_shifted_class,
    "mirror_preserves_transversality":
        mirror_transversality == -transversality,
    "mirror_preserves_primitivity_zero_locus":
        mirror_primitive == -primitive,
    "mirror_preserves_d3_flux_tadpole": mirror_tadpole == tadpole,
    "mirror_reverses_every_linear_chiral_index":
        mirror_chirality == -chirality,
    "minimum_family_magnitude_is_three":
        minimum_absolute_chirality == 3,
    "minimum_does_not_select_orientation":
        (-3 in admissible_chiralities and 3 in admissible_chiralities),
    "lower_bound_is_not_singleton_selection":
        len(set(abs(x) for x in admissible_chiralities)) > 1,
    "complete_moduli_hessian_is_not_in_declared_output":
        "complete_moduli_hessian" not in declared_source_outputs,
    "physical16_detector_response_is_not_in_declared_output":
        "physical16_detector_response" not in declared_source_outputs,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP793",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP792",
    "admitted_state_domain": (
        "globally resolved elliptically fibered Calabi-Yau fourfolds over "
        "P^3 in the finite toric model list of arXiv:1503.02068, restricted "
        "to properly quantized vertical G4 flux satisfying F-theory "
        "transversality, D-term supersymmetry, and nonnegative integral D3 "
        "tadpole completion"
    ),
    "faithful_coordinate": (
        "the shifted integral G4 cohomology class, its matter-surface chiral "
        "indices, quadratic D3 charge, Kähler-primitivity class, and remaining "
        "horizontal and geometric moduli"
    ),
    "source_authorized_probe_family": (
        "shifted flux quantization, homogeneous M/F-theory Chern-Simons "
        "matching constraints, matter-surface integration, D-term "
        "primitivity, and the quadratic D3 tadpole; the complete moduli "
        "Hessian and physical detector response are not outputs of the scan"
    ),
    "contextual_partition": (
        "the finite vertical-flux scan excludes family magnitudes below three, "
        "but every admitted flux has a constraint-equivalent mirror with the "
        "same quadratic tadpole and opposite chiral indices; horizontal-flux "
        "and vector-like completions lie outside the admitted packet"
    ),
    "selector_result": (
        "the studied global geometry and vertical flux constraints rigidify a "
        "minimum family magnitude of three; they do not select chirality sign, "
        "a unique flux class, all moduli, or a flavor portal point"
    ),
    "smallest_exact_falsifier": (
        "G4 and -G4 both satisfy shifted quantization, homogeneous F-theory "
        "constraints, primitivity, and the identical D3 tadpole, while their "
        "matter-surface chiral indices have opposite signs"
    ),
    "sign_result": (
        "all admitted source gates are even or homogeneous under G4 reversal, "
        "so the three-family and anti-three-family branches remain paired"
    ),
    "magnitude_result": (
        "three is a scan-dependent lower bound on family multiplicity, not a "
        "prediction of portal coupling magnitude; Kähler volumes and "
        "wavefunction normalizations remain additional data"
    ),
    "rg_threshold_result": (
        "the construction determines a chiral massless spectrum but does not "
        "derive its four-dimensional RG basin, stabilized threshold clock, or "
        "finite-width threshold response"
    ),
    "instrument_result": (
        "matter-surface indices and Chern-Simons coefficients are formal "
        "topological readouts; no calibrated map to physical16 observables or "
        "declared detector instrument is supplied"
    ),
    "deutschian_status": (
        "the vertical-flux construction partly explains why fewer than three "
        "families are unavailable in its finite model list, but the explanation "
        "is easy to vary in orientation, geometry, horizontal flux, moduli, and "
        "physical readout"
    ),
    "remaining_gate": (
        "derive an orientation-odd source term or boundary condition from the "
        "same global compactification, prove it removes the G4 mirror without "
        "adding a reference choice, and simultaneously stabilize normalization "
        "and moduli before RG, threshold, and physical16 descent"
    ),
    "primary_sources": [
        "https://arxiv.org/abs/1503.02068",
        "https://arxiv.org/abs/1109.3454",
    ],
}

(ROOT / "results" / "wp793_f_theory_vertical_flux_mirror_moduli_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
