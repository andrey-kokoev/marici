"""Assemble the correctly typed physical soft--triangle graded observer."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text())


def main():
    tangent = load("rank26-physical-soft-triangle-closure.json")
    strict = load("x1-soft-physical-strict-transform.json")
    smoothing = load("soft-triangle-node-smoothing.json")
    transport = load("soft-triangle-global-vanishing-transport.json")
    recovery = load("soft-triangle-source-port-recovery.json")

    ordinary_rank = tangent["records"]["physical_soft_triangle_tangent"]["tangent_closure_rank"]
    assert ordinary_rank == 1
    assert strict["checks"]["measure_jacobian_cancels_soft_square_root"]
    assert strict["checks"]["normalized_source_form_exact"]
    assert smoothing["physical_first_order_nonzero_count"] == 0
    assert smoothing["physical_second_order_first_count"] == 4
    assert transport["generic_cycle_coefficient"] == 4
    assert recovery["zeroth_source_port_recovers_second_normal_line"]
    assert recovery["source_factor_sign_on_open_chamber"] == "strictly_positive"
    assert all(not node["annihilates_supported_line"] for node in recovery["node_restrictions"])

    # Rees grades are independent by construction: the ordinary tangent line
    # is grade zero, there is no first-normal class, and the node line is born
    # at grade two.  Each has a nonzero source-normalized scalar readout.
    graded_source_dimensions = {"0": ordinary_rank, "1": 0, "2": 1}
    graded_observer_ranks = {"0": 1, "1": 0, "2": 1}
    result = {
        "schema": "marici.benincasa.physical-soft-triangle-graded-observer.v1",
        "status": "passed",
        "physical_locus": ["X1=0", "X2=X3=p>0"],
        "generic_X1_soft_fiber_is_not_physical": True,
        "graded_source_dimensions": graded_source_dimensions,
        "graded_observer_ranks": graded_observer_ranks,
        "total_reduced_rank": 2,
        "physical_observer_kernel_dimension": 0,
        "ordinary_grade_witness": "rank-one physical tangent source with unit strict-transform measure and nonzero positive-cut phase",
        "second_grade_witness": "four oriented endpoint costalks map to 4*alpha_positive_cut and the source factor is strictly positive",
        "first_normal_grade": "zero",
        "classification": "the correctly pulled-back physical soft-triangle object is rank two and its source scalar ports are jointly faithful",
        "scope_warning": "this does not activate the generic rank-20 X1-soft algebraic module or supply an interacting tensor vertex",
    }
    output = HERE / "physical-soft-triangle-graded-observer.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
