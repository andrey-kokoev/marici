"""Exact compact U(1) clockwork kernel, gap, and source-fiber audit."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp795 = json.loads(
    (ROOT / "results" / "wp795_domain_wall_inflow_overlap_fiber.json")
    .read_text(encoding="utf-8")
)

q = sp.symbols("q", integer=True, positive=True)
g, m = sp.symbols("g m", positive=True, real=True)

# Four sites and three oriented links with compact charges (1,-q).
C = sp.Matrix([
    [1, -q, 0, 0],
    [0, 1, -q, 0],
    [0, 0, 1, -q],
])
K = sp.simplify(C.T * C)
v = sp.Matrix([1, 1 / q, 1 / q**2, 1 / q**3])
norm = sp.sqrt(sum(x**2 for x in v))
vhat = sp.simplify(v / norm)

# The nonzero squared masses are eigenvalues of C C^T times m^2.
q3_gears = (C * C.T).subs(q, 3)
gear_eigenvalues = sorted(
    [sp.simplify(x) for x in q3_gears.eigenvals().keys()],
    key=lambda x: float(x),
)
expected_gears = [
    10 - 3 * sp.sqrt(2),
    10,
    10 + 3 * sp.sqrt(2),
]

# Endpoint couplings and oriented contrast.
coupling_left = sp.simplify(g * vhat[0])
coupling_right = sp.simplify(g * vhat[3])
contrast = sp.simplify(coupling_left - coupling_right)

# Reverse the incidence orientation without changing the physical spectrum.
J = sp.zeros(4)
for i in range(4):
    J[i, 3 - i] = 1
K_reversed = sp.simplify(J * K * J)
vhat_reversed = sp.simplify(J * vhat)
reversed_contrast = sp.simplify(
    g * vhat_reversed[0] - g * vhat_reversed[3]
)

# Compactness admits multiple integer q values; their endpoint ratios differ.
ratio_q2 = sp.simplify((vhat[3] / vhat[0]).subs(q, 2))
ratio_q3 = sp.simplify((vhat[3] / vhat[0]).subs(q, 3))

checks = {
    "wp795_dependency_passed": wp795["status"] == "PASS"
    and all(wp795["checks"].values()),
    "incidence_annihilates_clockwork_profile": C * v == sp.zeros(3, 1),
    "kernel_is_one_dimensional": len(C.nullspace()) == 1,
    "normalized_profile_has_unit_gram":
        sp.simplify((vhat.T * vhat)[0]) == 1,
    "q_three_gears_match_exact_spectrum":
        gear_eigenvalues == expected_gears,
    "q_three_has_strict_gear_gap": expected_gears[0] > 0,
    "endpoint_ratio_is_q_to_minus_three":
        sp.simplify(coupling_right / coupling_left) == q**-3,
    "chain_reversal_preserves_mass_spectrum":
        K_reversed.eigenvals() == K.eigenvals(),
    "chain_reversal_reverses_endpoint_contrast":
        sp.simplify(reversed_contrast + contrast) == 0,
    "integer_charge_quantization_does_not_select_q":
        ratio_q2 == sp.Rational(1, 8)
        and ratio_q3 == sp.Rational(1, 27),
    "overall_zero_mode_coupling_depends_on_free_g":
        sp.diff(coupling_left, g) == vhat[0],
    "heavy_thresholds_depend_on_free_m":
        sp.diff(m**2 * expected_gears[0], m)
        == 2 * m * expected_gears[0],
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP796",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP795",
    "admitted_state_domain": (
        "a four-site compact U(1)^4 clockwork with three oriented Higgs links "
        "of integer charges (1,-q), q>1, common link scale m, gauge coupling "
        "g, external matter localized at declared sites, and its complete "
        "zero-mode plus three-gear spectrum"
    ),
    "faithful_coordinate": (
        "integer q, chain length and orientation, normalized null vector, "
        "endpoint assignment, absolute gauge coupling, full gear spectrum, "
        "and every localized matter coupling"
    ),
    "source_authorized_probe_family": (
        "the integer charge-incidence matrix, its positive Gram operator, "
        "the unique kernel profile, gear eigenvalues, and localized coupling "
        "measurements"
    ),
    "contextual_partition": (
        "for fixed q, length, orientation, and endpoint labels the kernel "
        "uniquely fixes all relative zero-mode couplings; different integer q, "
        "reversed chains, and continuous g,m remain distinct admitted sources"
    ),
    "selector_result": (
        "clockwork is a genuine relative-coupling selector and gapped "
        "presentation rigidifier conditional on its charge incidence; it does "
        "not select that incidence, its orientation, or absolute scale"
    ),
    "smallest_exact_falsifier": (
        "q=2 and q=3 are both compact integer-charge chains but give endpoint "
        "ratios 1/8 and 1/27; reversing either chain preserves the gear spectrum "
        "and reverses the endpoint portal contrast"
    ),
    "sign_result": (
        "the oriented incidence and assignment of species to endpoints fix "
        "the contrast sign, but the reversed incidence is an equally admitted "
        "compact source"
    ),
    "magnitude_result": (
        "the relative suppression q^-N is exact after q and N are chosen, "
        "while the absolute coupling depends on g and the normalization and "
        "the heavy scale depends on m"
    ),
    "rg_threshold_result": (
        "the exact unbroken U(1) kernel protects the relative charge profile "
        "and the positive Gram spectrum supplies a basin gap; actual gauge "
        "running and gear thresholds still depend on matter content, g, and m"
    ),
    "instrument_result": (
        "localized zero-mode couplings and gear resonances are physical "
        "channels in principle, but no derived map identifies them with the "
        "faithful physical16 flavor response or fixes detector calibration"
    ),
    "deutschian_status": (
        "the incidence matrix hard-to-vary explains the relative profile and "
        "gear spectrum, but q, length, orientation, endpoint species, g, and m "
        "are easy-to-vary source choices"
    ),
    "remaining_gate": (
        "derive the asymmetric integer incidence, its endpoint species map, "
        "and absolute g,m from one non-mirror-completable source history, then "
        "compute matter-dependent RG, finite gear thresholds, and physical16 "
        "detector response"
    ),
    "primary_sources": [
        "https://arxiv.org/abs/1610.07962",
        "https://arxiv.org/abs/1708.03564",
        "https://arxiv.org/abs/1709.02392",
    ],
}

(ROOT / "results" / "wp796_compact_clockwork_relative_portal_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
