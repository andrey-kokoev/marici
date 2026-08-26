"""Exact constructor-fiber obstruction to physical16-to-pole descent."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp129 = load("wp129_rival_source_identification.json")
wp557 = load("wp557_physical16_gramian_pullback_gate.json")

L = sp.Matrix([[1, 1, 1]])
Q = sp.eye(3)
hostile = sp.Matrix([1, -1, 0])

phi_entries = sp.symbols("p0:3")
Phi = sp.Matrix(phi_entries)
factorization_solution = sp.solve(list(Phi * L - Q), phi_entries, dict=True)
low_kernel = L.nullspace()
pole_kernel = Q.nullspace()

checks = {
    "dependencies_passed": bool(wp129["all_pass"] and wp557["passed"]),
    "three_rival_constructors": len(wp129["rivals"]) == 3,
    "low_energy_rank_matches_wp129": L.rank() == wp129["low_energy_rank"] == 1,
    "low_energy_kernel_matches_wp129": len(low_kernel)
    == wp129["low_energy_kernel_dimension"]
    == 2,
    "threshold_rank_matches_wp129": Q.rank()
    == wp129["formal_threshold_rank"]
    == 3,
    "threshold_kernel_matches_wp129": len(pole_kernel)
    == wp129["formal_threshold_kernel_dimension"]
    == 0,
    "hostile_is_in_low_energy_kernel": L * hostile == sp.zeros(1, 1),
    "hostile_is_not_in_pole_kernel": Q * hostile != sp.zeros(3, 1),
    "kernel_inclusion_fails": any(
        Q * vector != sp.zeros(3, 1) for vector in low_kernel
    ),
    "no_linear_descent_factorization_exists": factorization_solution == [],
    "rank_alone_forbids_factorization": Q.rank() > L.rank(),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP558",
    "domain": "The bounded WP129 family of three inequivalent UV constructors matched to one common low-energy physical16/EFT packet.",
    "maps": {
        "low_energy_normal_form": [[str(x) for x in row] for row in L.tolist()],
        "pole_signature_normal_form": [[str(x) for x in row] for row in Q.tolist()],
        "descent_equation": "Q=phi composed with L",
        "linear_criterion": "kernel(L) subset kernel(Q)",
    },
    "contextual_partitions": {
        "low_energy": wp129["low_energy_partition"],
        "formal_threshold": wp129["formal_threshold_partition"],
    },
    "hostile_constructor_displacement": {
        "vector": [str(x) for x in hostile],
        "low_energy_response": [str(x) for x in L * hostile],
        "pole_response": [str(x) for x in Q * hostile],
    },
    "descent": {
        "exists_on_unrestricted_low_energy_quotient": False,
        "reason": "The pole signature is not constant on the low-energy constructor fiber; no linear factorization exists and kernel inclusion fails.",
        "repair": "Restrict the constructor class by independent authority or add a constructor/threshold reference port, defining a new relational experiment.",
    },
    "classification": "Constructor-fiber non-descent theorem; neither selector nor physical threshold instrument.",
    "selector": False,
    "rigidifier": False,
    "instrument": "WP129's threshold signatures are formal. No calibrated experiment resolves the three constructor grammars on the admitted domain.",
    "smallest_exact_falsifier": "The displacement (1,-1,0) has zero low-energy response and nonzero pole response, so pole data cannot be a function of the common physical16 record.",
    "remaining_gate": "Freeze a constructor class independently, derive its physical16-to-pole map and full weak-basis descent, or build a new threshold-reference experiment with calibrated support and covariance. Numerical source selection remains separate.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp558_constructor_fiber_pole_descent.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
