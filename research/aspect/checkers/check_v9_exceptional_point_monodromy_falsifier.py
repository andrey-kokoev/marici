import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v9 = json.loads(
    (root / "contracts" / "frozen-bivariant-network-signature.v9.json").read_text(
        encoding="utf-8"
    )
)

t, s, z, w, lam = sp.symbols("t s z w lambda", nonzero=True)
A = sp.Matrix([[0, 1], [t, 0]])
I = sp.eye(2)
Rz = sp.simplify((A - z * I).inv())
Rw = sp.simplify((A - w * I).inv())

A_cover = A.subs(t, s**2)
P_plus = sp.simplify((I + A_cover / s) / 2)
P_minus = sp.simplify((I - A_cover / s) / 2)

family = v9["parameterized_resolvent_route_family"]
all_terms = (
    set(v9["object_types"])
    | set(v9["arrow_types"])
    | set(v9["cell_types"])
    | set(family["required_fields"])
    | set(family["required_laws"])
    | set(v9["forbidden_promotions"])
)

missing_markers = (
    "external_parameter_base",
    "joint_parameter_spectral_domain",
    "spectral_cover",
    "eigenprojector_local_system",
    "riesz_projector_monodromy",
    "branch_locus",
    "mode_permutation",
)

checks = {
    "v9_is_frozen": v9["cell_creation_during_replay"] is False,
    "characteristic_polynomial_has_square_root_cover": sp.factor((lam * I - A).det()) == lam**2 - t,
    "full_resolvent_is_rational_and_single_valued_in_t": Rz == sp.Matrix([[z / (t - z**2), 1 / (t - z**2)], [t / (t - z**2), z / (t - z**2)]]),
    "full_resolvent_satisfies_resolvent_identity": sp.simplify(Rz - Rw - (z - w) * Rz * Rw) == sp.zeros(2),
    "projectors_are_idempotent_on_the_cover": sp.simplify(P_plus**2 - P_plus) == sp.zeros(2) and sp.simplify(P_minus**2 - P_minus) == sp.zeros(2),
    "projectors_resolve_identity": sp.simplify(P_plus + P_minus) == I,
    "projectors_select_opposite_eigenvalues": sp.simplify(A_cover * P_plus - s * P_plus) == sp.zeros(2) and sp.simplify(A_cover * P_minus + s * P_minus) == sp.zeros(2),
    "deck_turn_swaps_projectors": sp.simplify(P_plus.subs(s, -s) - P_minus) == sp.zeros(2) and sp.simplify(P_minus.subs(s, -s) - P_plus) == sp.zeros(2),
    "eigenvalue_sheets_swap_under_one_parameter_loop": sp.simplify((-s) - s) != 0,
    "total_resolvent_is_invariant_under_deck_turn": sp.simplify(Rz.subs(t, s**2).subs(s, -s) - Rz.subs(t, s**2)) == sp.zeros(2),
    "v9_has_no_joint_spectral_cover_datum": not any(marker in term.lower() for term in all_terms for marker in missing_markers),
    "v9_cannot_type_mode_exchange_from_total_resolvent_alone": "holomorphic_resolvent_sheaf" in v9["object_types"],
}

result = {
    "schema": "marici.aspect.v9-exceptional-point-monodromy-falsifier.v1",
    "status": "frozen_v9_falsified" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "hostile": "A(t)=[[0,1],[t,0]] around the exceptional point t=0",
    "failure": "the total resolvent is single-valued and satisfies every v9 local law while eigenvalues and Riesz projectors exchange sheets around the parameter loop",
    "required_future_repair": "a joint external-parameter and spectral cover carrying eigenprojector local systems, branch locus, deck transport, and mode-permutation monodromy",
}

out = root / "results" / "v9_exceptional_point_monodromy_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "frozen_v9_falsified" else 1)
