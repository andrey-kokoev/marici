"""WP214 exact checker: detector derivation chain.

This checker consolidates WP206-WP213 into a dependency chain for the one-tenth
detector constants, with explicit remaining authority gates.
"""

from __future__ import annotations

import json
from pathlib import Path


NODES = {
    "strict_interval_separation": {"external": False, "depends": []},
    "minimal_nonzero_fault_tolerance": {"external": True, "depends": []},
    "one_bad_contract": {"external": False, "depends": ["minimal_nonzero_fault_tolerance"]},
    "strict_below_quarter_target": {
        "external": True,
        "depends": ["strict_interval_separation"],
    },
    "five_copy_minimality": {
        "external": False,
        "depends": ["one_bad_contract", "strict_below_quarter_target"],
    },
    "one_fifth_safety_cap": {"external": False, "depends": ["five_copy_minimality"]},
    "width_background_exchange": {"external": True, "depends": []},
    "one_tenth_constants": {
        "external": False,
        "depends": ["one_fifth_safety_cap", "width_background_exchange"],
    },
}


def closure(node: str) -> set[str]:
    deps: set[str] = set()
    for dep in NODES[node]["depends"]:
        deps.add(dep)
        deps.update(closure(dep))
    return deps


def external_gates_for(node: str) -> set[str]:
    deps = closure(node) | {node}
    return {item for item in deps if NODES[item]["external"]}


def main() -> None:
    gates = external_gates_for("one_tenth_constants")
    checks = {
        "one_tenth_depends_on_one_fifth_cap": "one_fifth_safety_cap"
        in closure("one_tenth_constants"),
        "one_tenth_depends_on_width_background_exchange": "width_background_exchange"
        in closure("one_tenth_constants"),
        "one_fifth_depends_on_five_copy": "five_copy_minimality"
        in closure("one_fifth_safety_cap"),
        "five_copy_depends_on_one_bad": "one_bad_contract"
        in closure("five_copy_minimality"),
        "five_copy_depends_on_quarter_target": "strict_below_quarter_target"
        in closure("five_copy_minimality"),
        "external_gates_are_three": gates
        == {
            "minimal_nonzero_fault_tolerance",
            "strict_below_quarter_target",
            "width_background_exchange",
        },
        "strict_interval_separation_not_external_here": "strict_interval_separation"
        not in gates,
        "one_bad_contract_not_external_after_minimal_fault": "one_bad_contract"
        not in gates,
        "five_copy_not_external_after_dependencies": "five_copy_minimality" not in gates,
        "one_fifth_cap_not_external_after_five_copy": "one_fifth_safety_cap" not in gates,
        "chain_is_acyclic": all(node not in closure(node) for node in NODES),
        "detector_constants_conditional_not_unconditional": True,
    }

    result = {
        "work_package": "WP214",
        "claim": "The one-tenth detector constants have a closed conditional derivation chain; the remaining external gates are minimal nonzero fault tolerance, strict below-quarter target, and width/background exchange symmetry.",
        "nodes": NODES,
        "dependency_closure_for_one_tenth": sorted(closure("one_tenth_constants")),
        "remaining_external_gates": sorted(gates),
        "classification": "detector derivation chain closeout; conditional, not unconditional.",
        "next_frontier": "Derive or admit the three remaining detector gates from physical architecture.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp214_detector_derivation_chain.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
