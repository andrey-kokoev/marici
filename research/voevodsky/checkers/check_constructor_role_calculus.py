#!/usr/bin/env python3
"""Validate constructor-role gates and deliberate failures without dependencies."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "research/voevodsky/contracts/constructor-role-calculus.v1.json"
RESULT = ROOT / "research/voevodsky/results/constructor_role_calculus.json"

contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
roles = contract["roles"]
order = contract["substitution_order"]

required_roles = {
    "subgroup_restriction",
    "quotient_descent",
    "comparison_cell",
    "presentation_lift",
    "forward_synthesis",
    "determinant_counterterm",
    "essential_observer",
    "finite_defect_repair",
    "real_comparison",
    "graph_adjoint",
    "ambient_adjoint",
    "boundary_trace",
    "thick_bulk_complement",
    "relative_phase_observer",
}

checks: dict[str, bool] = {}
checks["schema"] = contract["schema"] == "marici.voevodsky.constructor-role-calculus.v1"
checks["roles_present"] = required_roles <= set(roles)
checks["substitution_gate_order"] = order == [
    "source_target",
    "arity_variance",
    "support_labels",
    "required_cells",
    "numeric_equality",
]
checks["quotient_requires_kernel_gate"] = (
    "kernel_triviality_or_declared_invariant_coinvariant_constructor"
    in roles["quotient_descent"]["required_cells"]
)
checks["essential_requires_calkin_gate"] = (
    "positive_invertible_calkin_gramian"
    in roles["essential_observer"]["required_cells"]
)
checks["graph_ambient_rungs_distinct"] = (
    roles["graph_adjoint"]["source_rung"]
    != roles["ambient_adjoint"]["source_rung"]
    and roles["graph_adjoint"]["variance"]
    != roles["ambient_adjoint"]["variance"]
)
checks["forward_counterterm_arity_distinct"] = (
    roles["forward_synthesis"]["arity"]
    != roles["determinant_counterterm"]["arity"]
)
checks["forward_counterterm_variance_distinct"] = (
    roles["forward_synthesis"]["variance"]
    != roles["determinant_counterterm"]["variance"]
)

forbidden = {(x["from"], x["to"]): x for x in contract["forbidden_promotions"]}
checks["lift_not_essential"] = ("presentation_lift", "essential_observer") in forbidden
checks["trace_not_essential_conditioned"] = (
    forbidden[("boundary_trace", "essential_observer")]["condition"]
    == "finite_dimensional_boundary_and_infinite_dimensional_graph_source"
)
checks["counterterm_not_forward"] = (
    "source arity" in forbidden[("determinant_counterterm", "forward_synthesis")]["reason"]
)
checks["graph_not_ambient"] = ("graph_adjoint", "ambient_adjoint") in forbidden

# Deliberate failures return their first nonzero obstruction in gate order.
examples = {
    "mixed_counterterm_as_forward_loading": {
        "source_target": "graded tensor/scalar line != labelled source/radial graph",
        "arity_variance": "bilinear parameter-dependent != linear fixed",
    },
    "trace_as_infinite_graph_essential_observer": {
        "required_cells": "finite-rank trace has zero Calkin Gramian",
    },
    "graph_adjoint_as_ambient_adjoint": {
        "source_target": "graph-domain source != ambient source",
    },
    "fourier_half_turn_as_quotient_image_of_generator_square": {
        "required_cells": "C4 quotient sends generator square to identity",
    },
}
expected = {x["id"]: x["expected_first_failure"] for x in contract["deliberate_failures"]}
observed = {}
for identifier, obstructions in examples.items():
    first = next(gate for gate in order if gate in obstructions)
    observed[identifier] = {
        "first_failure": first,
        "residual": obstructions[first],
        "expected": expected[identifier],
        "passed": first == expected[identifier],
    }
checks["all_deliberate_failures_localized"] = all(x["passed"] for x in observed.values())
checks["deliberate_failures_nonzero"] = all(bool(x["residual"]) for x in observed.values())

result = {
    "schema": "marici.voevodsky.constructor-role-calculus-check.v1",
    "contract": str(CONTRACT.relative_to(ROOT)).replace("\\", "/"),
    "contract_sha256": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
    "checks": checks,
    "deliberate_failures": observed,
    "passed": all(checks.values()),
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": result["passed"], "check_count": len(checks)}))
raise SystemExit(0 if result["passed"] else 1)
