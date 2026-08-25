#!/usr/bin/env python3
"""WP56: exact algebra and source-completeness gate for proposed CP vacua."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/flavor/sources/2607.27315v1.txt"
OUT = ROOT / "research/flavor/results/wp56_spontaneous_cp_selector_gate.json"


def main() -> None:
    z = sp.cos(sp.pi / 4) + sp.I * sp.sin(sp.pi / 4)
    proposed_ratio = sp.simplify(sp.expand_complex(sp.I * (1 - z) / (1 + z)))
    evaluated_ratio = sp.simplify(sp.tan(sp.pi / 8))
    printed_rhs = sp.simplify(sp.I * sp.tan(sp.pi / 8))

    text = SOURCE.read_text(encoding="utf-8")
    chart = json.loads((ROOT / "research/flavor/results/nine_link_exact_checks.json").read_text())
    u3 = chart["checks"]["u3q_rotation"]

    source_markers = {
        "proposal_is_modal": "For instance, CP could be spontaneously broken" in text,
        "multiple_pictures_not_unique_operation": "There are several simple pictures" in text,
        "theory_deferred": "We defer a discussion of these theoretical possibilities to future work" in text,
        "z4_phase_claim_present": "purely real or purely imaginary" in text,
        "z8_equal_magnitude_claim_present": "equal magnitudes but phases that are multiples" in text,
    }
    descent_obstruction = (
        u3["zero_pattern_destroyed"]
        and u3["phase_changed_under_rotation"]
        and all(u3["symbolic_invariants_equal"].values())
        and all(u3["concrete_invariants_equal"].values())
    )
    gates = {
        "z8_ratio_evaluates_exactly_to_tan_pi_over_8": sp.simplify(proposed_ratio - evaluated_ratio) == 0,
        "printed_i_tan_rhs_has_nonzero_residual": sp.simplify(proposed_ratio - printed_rhs) != 0,
        "source_explicitly_marks_uv_picture_as_deferred": all(source_markers.values()),
        "chart_phase_law_fails_full_weak_basis_descent": descent_obstruction,
        "no_admitted_unique_selector_operation": all(source_markers.values()) and descent_obstruction,
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.flavor.spontaneous-cp-selector-gate.v1",
        "arithmetic": "exact SymPy cyclotomic algebra plus exact source-string and prior invariant gates",
        "candidate": "illustrative Z4/Z8 spontaneous-CP flavon vacuum relations in the declared source",
        "exact_chart_relation": "i(1-exp(i*pi/4))/(1+exp(i*pi/4)) = tan(pi/8)",
        "source_residual": "the extracted source prints i*tan(pi/8); exact algebra leaves a nonzero residual against that RHS",
        "source_completeness": {
            **source_markers,
            "declared_potential": False,
            "declared vacuum-selection dynamics": False,
            "declared map to full physical16": False,
            "declared physical instrument": False,
        },
        "descent": "no for the resulting sparse loop-phase datum; an exact U(3)_Q orbit preserves physical invariants while destroying support and changing that phase",
        "contextual_partition": "fixed phases partition sparse presentations only; no quotient-level partition is admitted",
        "classification": {
            "selector": False,
            "rigidifier": True,
            "both": False,
            "physical_instrument": "none declared",
        },
        "smallest_exact_falsifier": "the prior exact 3/5,4/5 U(3)_Q rotation: invariant physical orbit, destroyed sparse support, changed loop phase",
        "remaining_gate": "a complete UV action/potential with a selected vacuum orbit and a weak-basis-invariant map from that orbit to a proper physical16 family",
        "gates": gates,
        "conclusion": "The proposed discrete-CP pictures exactly rigidify chart phase algebra but do not yet define a source-generated selector on the physical quotient.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": sum(gates.values()), "total": len(gates), "output": str(OUT.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
