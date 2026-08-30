"""Exact Higgs gauge and reference-port audit for WP412."""

import json
from pathlib import Path

import sympy as sp


phi, h, c, mu2, lam, v0 = sp.symbols(
    "phi h c mu2 lambda v0", positive=True, real=True
)

# Radial representative of the gauge-invariant Higgs potential.  The center of
# SU(2) sends the doublet to minus itself, so the source potential is even.
V = (-mu2 + c) * phi**2 / 2 + lam * phi**4 / 4
absolute_tadpole = sp.diff(V, phi).subs(phi, 0)
center_invariance = sp.simplify(V.subs(phi, -phi) - V)

# Freeze the c=0 broken vacuum as a reference port, then expand phi=v0+h.
vacuum_shell = {lam * v0**2: mu2}
expanded = sp.expand(V.subs(phi, v0 + h))
relative_tadpole = sp.expand(sp.diff(expanded, h).subs(h, 0)).subs(vacuum_shell)
relative_curvature = sp.expand(sp.diff(expanded, h, 2).subs(h, 0)).subs(vacuum_shell)
shift_jacobian = sp.Matrix([relative_curvature, relative_tadpole]).jacobian([c])

# At the c-dependent equilibrium, the first derivative vanishes.  This proves
# that the tadpole belongs to comparison with the frozen reference, not to an
# absolute gauge-invariant source at the new vacuum.
vc = sp.sqrt((mu2 - c) / lam)
recentered_tadpole = sp.simplify(sp.diff(V, phi).subs(phi, vc))

# A literal linear doublet source is odd under the gauge-center action unless a
# transforming spurion/reference is added.
J = sp.symbols("J", nonzero=True, real=True)
linear_source = J * phi
linear_center_defect = sp.simplify(linear_source.subs(phi, -phi) - linear_source)

checks = {
    "gauge_even_source_has_no_absolute_tadpole": absolute_tadpole == 0,
    "radial_potential_respects_center": center_invariance == 0,
    "fixed_reference_curvature_shift_is_affine": sp.diff(relative_curvature, c, 2) == 0 and sp.diff(relative_curvature, c) == 1,
    "same_knob_generates_relative_tadpole": sp.diff(relative_tadpole, c) == v0,
    "joint_shift_tangent_has_two_nonzero_components": all(entry != 0 for entry in shift_jacobian),
    "recentering_removes_relative_tadpole": recentered_tadpole == 0,
    "literal_linear_source_breaks_center_without_spurion": linear_center_defect != 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP412",
    "title": "Higgs relative-tadpole reference port",
    "real_scalar": "the observed Standard Model Higgs radial mode",
    "gauge_invariant_context_operator": "c H-dagger H",
    "fixed_reference_readouts": {
        "curvature": str(sp.factor(relative_curvature)),
        "relative_tadpole": str(sp.factor(relative_tadpole)),
        "common_knob_tangent": [str(entry) for entry in shift_jacobian],
    },
    "new_groupoid": "broken-phase experiment with the c=0 vacuum retained as a relational reference port",
    "classification": "real scalar and exact common affine shifts only in a relational reference experiment; no executable physical c control admitted",
    "smallest_exact_falsifier": "recentring at the c-dependent equilibrium makes the tadpole vanish identically",
    "remaining_gate": "an executable source-derived operation varying c plus independent curvature and fixed-reference force/displacement calibration",
    "checks": checks,
    "passed": all(checks.values()),
}

if not result["passed"]:
    raise SystemExit("WP412 exact checks failed")

out = Path(__file__).parents[1] / "results" / "wp412_higgs_reference_port.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
