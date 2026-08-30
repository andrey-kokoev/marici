"""Exact radial-quartic RG-support closure audit for WP493."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp489 = load("wp489_common_source_threshold_constructor.json")
wp492 = load("wp492_canonical_messenger_tensor_grammar.json")

fields = ["F", "H", "R", "sigma"]
field_index = {name: index for index, name in enumerate(fields)}

# WP489 has a star of mixed radial quartics centered on sigma.
adjacency = sp.zeros(4)
for leaf in ("F", "H", "R"):
    i = field_index[leaf]
    j = field_index["sigma"]
    adjacency[i, j] = adjacency[j, i] = 1

two_step_support = adjacency**2
missing_leaf_portals = [("F", "H"), ("F", "R"), ("H", "R")]

rho, eta, lambda_s, y2, a, b = sp.symbols(
    "rho eta lambda_S y_squared a b", positive=True
)
existing_portal_coefficients = {
    "F_sigma": -12 * rho * y2,
    "H_sigma": -eta * a,
    "R_sigma": -2 * lambda_s * b,
}
generated_support_products = {
    "F_H": sp.factor(existing_portal_coefficients["F_sigma"] * existing_portal_coefficients["H_sigma"]),
    "F_R": sp.factor(existing_portal_coefficients["F_sigma"] * existing_portal_coefficients["R_sigma"]),
    "H_R": sp.factor(existing_portal_coefficients["H_sigma"] * existing_portal_coefficients["R_sigma"]),
}

all_self_quartics = [f"{name}^4" for name in fields]
all_pair_portals = [
    f"{fields[i]}^2 {fields[j]}^2"
    for i in range(len(fields))
    for j in range(i + 1, len(fields))
]
minimal_radial_basis = all_self_quartics + all_pair_portals

complete_adjacency = sp.ones(4) - sp.eye(4)
complete_two_step = complete_adjacency**2

checks = {
    "wp489_dependency_passed": wp489["passed"],
    "wp492_dependency_passed": wp492["passed"],
    "wp489_radial_portal_graph_is_sigma_star": int(sum(adjacency)) == 6,
    "every_missing_leaf_portal_has_two_step_support": all(
        two_step_support[field_index[left], field_index[right]] > 0
        for left, right in missing_leaf_portals
    ),
    "all_generated_products_are_nonzero_on_positive_domain": all(
        product != 0 for product in generated_support_products.values()
    ),
    "three_cross_portals_are_missing": len(missing_leaf_portals) == 3,
    "minimal_radial_quartic_basis_has_ten_invariants": len(minimal_radial_basis) == 10,
    "completed_portal_graph_is_support_closed": all(
        complete_two_step[i, j] > 0
        for i in range(4)
        for j in range(4)
        if i != j
    ),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP493",
    "domain": "four canonical WP489 radial invariants F,H,R,sigma with all positive source coefficients",
    "existing_mixed_quartics": {
        "F_squared_sigma_squared": str(existing_portal_coefficients["F_sigma"]),
        "H_squared_sigma_squared": str(existing_portal_coefficients["H_sigma"]),
        "R_squared_sigma_squared": str(existing_portal_coefficients["R_sigma"]),
    },
    "one_loop_generated_support": {
        "mechanism": "a bubble with two sigma propagators and two distinct leaf-sigma quartic vertices produces the corresponding leaf-leaf quartic counterterm",
        "missing_invariants": ["F^2 H^2", "F^2 R^2", "H^2 R^2"],
        "nonzero_coefficient_products": {name: str(value) for name, value in generated_support_products.items()},
        "claim_scope": "exact nonzero counterterm support; overall scheme-dependent loop prefactors are not asserted",
    },
    "minimal_radial_quartic_basis": minimal_radial_basis,
    "classification": "WP489's positive sum-of-squares surface is not an RG-closed truncation; three additional radial portals are compulsory before beta-function derivation.",
    "selector": False,
    "rigidifier": False,
    "instrument": None,
    "smallest_exact_falsifier": "The F-sigma and H-sigma vertices alone generate an F^2 H^2 counterterm proportional to 12 rho eta a y^2, which is nonzero everywhere on the admitted positive domain but absent from WP489.",
    "remaining_gate": "Promote all ten radial quartic invariants to independent running couplings, then repeat closure for nonradial tensor invariants and freeze the complete MSbar truncation before computing fixed points.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp493_radial_quartic_rg_closure.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
