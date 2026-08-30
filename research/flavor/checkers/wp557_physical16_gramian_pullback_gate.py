"""Exact physical16 pullback and complementarity gate for WP556."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp52 = load("wp52_source_selector_audit.json")
wp556 = load("wp556_source_gramian_pairing.json")

# Exact local normal form for the measured-ten projection.
P10 = sp.Matrix.hstack(sp.eye(10), sp.zeros(10, 6))

# A six-state probe that duplicates measured coordinates, and the maximally
# complementary six-coordinate witness allowed by dimension counting.
J_factor = sp.Matrix.hstack(sp.eye(6), sp.zeros(6, 10))
J_complement = sp.Matrix.hstack(sp.zeros(6, 10), sp.eye(6))

G6 = sp.diag(*sp.symbols("g1:7", positive=True))
pullback_factor = J_factor.T * G6 * J_factor
pullback_complement = J_complement.T * G6 * J_complement

stack_factor = P10.col_join(J_factor)
stack_complement = P10.col_join(J_complement)

hostile_displacement = sp.zeros(16, 1)
hostile_displacement[10, 0] = 1

checks = {
    "dependencies_passed": bool(
        all(wp52["gates"].values()) and wp556["passed"]
    ),
    "physical_coordinate_dimension_is_sixteen": P10.cols == 16,
    "measured_projection_rank_is_ten": P10.rank() == 10,
    "six_state_pullback_rank_is_at_most_six": pullback_factor.rank() == 6
    and pullback_complement.rank() == 6,
    "six_state_pullback_has_ten_dimensional_kernel": len(
        pullback_complement.nullspace()
    )
    == 10,
    "factor_through_probe_does_not_improve_measured_rank": stack_factor.rank()
    == 10,
    "factor_through_stack_retains_six_dimensional_kernel": len(
        stack_factor.nullspace()
    )
    == 6,
    "complementary_probe_can_reach_rank_sixteen": stack_complement.rank() == 16,
    "hostile_pair_collapses_in_measured_ten": P10 * hostile_displacement
    == sp.zeros(10, 1),
    "factor_through_probe_also_collapses_hostile": J_factor
    * hostile_displacement
    == sp.zeros(6, 1),
    "complementary_probe_detects_hostile": J_complement * hostile_displacement
    != sp.zeros(6, 1),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP557",
    "domain": "The generic nondegenerate sixteen-dimensional physical flavor quotient, locally composed with measured ten and a hypothetical six-coordinate pullback of the WP556 internal Gramian.",
    "faithful_quotient_coordinate": "physical16",
    "measured_projection": {
        "dimension": 10,
        "rank": int(P10.rank()),
        "kernel_dimension": int(len(P10.nullspace())),
        "wp52_hostile": wp52["hostile_pair"],
    },
    "gramian_pullback": {
        "required_missing_map": "phi: physical16 -> six-state WP556 realization",
        "formula": "G_16=J_phi^T G_6 J_phi",
        "maximum_rank": 6,
        "minimum_local_kernel_dimension": 10,
        "descent_status": "No source-derived phi or physical instrument is admitted.",
    },
    "contextual_partitions": {
        "factor_through_measured_ten": {
            "stacked_rank": int(stack_factor.rank()),
            "kernel_dimension": int(len(stack_factor.nullspace())),
        },
        "maximally_complementary_witness": {
            "stacked_rank": int(stack_complement.rank()),
            "kernel_dimension": int(len(stack_complement.nullspace())),
        },
    },
    "selector_test": "Even stacked rank sixteen would separate points but would not select a proper admissible subfamily. Selection needs an independent source-derived physical law.",
    "classification": "Internal source-geometry rigidifier with a physical16 pullback obstruction; neither selector nor standalone faithful physical probe.",
    "selector": False,
    "rigidifier": bool(wp556["rigidifier"]),
    "instrument": "Absent. Requires a source-derived map from physical16 variations to the six internal resolvent coordinates and a measured probe whose Jacobian is complementary to measured ten.",
    "smallest_exact_falsifier": "Any six-row pullback metric on a sixteen-dimensional domain has rank at most six and kernel dimension at least ten. The explicit factor-through witness leaves the measured-ten stacked rank at ten.",
    "remaining_gate": "Derive phi from admitted flavor dynamics, compute its full weak-basis-invariant Jacobian on the fitted domain, attach a physical instrument and covariance, and prove stacked rank sixteen robustly. A separate transverse source law is still required for selection.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp557_physical16_gramian_pullback_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
