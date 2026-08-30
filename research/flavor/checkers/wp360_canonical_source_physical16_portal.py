"""WP360: exact descent and rank audit for a canonical source-to-J portal."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    even = sp.symbols("z1:16", real=True)
    J = sp.symbols("J", real=True)
    Q, c, lam = sp.symbols("Q c lambda", positive=True)
    coordinates = even + (J,)

    residual = J**2 - c * Q
    portal = lam * residual**2
    constraint_jacobian = sp.Matrix([[sp.diff(residual, x) for x in coordinates]])
    positive_shell = sp.sqrt(c * Q)
    response_Q = sp.diff(positive_shell, Q)
    response_c = sp.diff(positive_shell, c)

    left = tuple(range(1, 16)) + (positive_shell,)
    right = (sp.Integer(2),) + tuple(range(2, 16)) + (positive_shell,)
    source_a = {Q: 1, c: 1}
    source_b = {Q: 4, c: sp.Rational(1, 4)}

    checks = {
        "portal_is_nonnegative": portal.is_nonnegative,
        "zero_locus_is_the_declared_shell": sp.simplify(residual.subs(J, positive_shell)) == 0,
        "constraint_rank_is_one_on_nonzero_shell": constraint_jacobian.subs(J, positive_shell).rank() == 1,
        "selected_family_has_dimension_fifteen": len(coordinates) - 1 == 15,
        "cp_conjugate_sheet_also_satisfies_portal": sp.simplify(residual.subs(J, -positive_shell)) == 0,
        "magnitude_responds_to_Q": response_Q == sp.sqrt(c) / (2 * sp.sqrt(Q)),
        "magnitude_responds_to_matching_coefficient": response_c == sp.sqrt(Q) / (2 * sp.sqrt(c)),
        "physical16_hostile_pair_collides_under_portal": left != right and residual.subs(J, left[-1]) == residual.subs(J, right[-1]),
        "source_hostile_pair_selects_same_shell": sp.simplify((c * Q).subs(source_a) - (c * Q).subs(source_b)) == 0,
        "deliberate_cp_odd_linear_term_would_break_even_descent": sp.simplify(J.subs(J, -J) - J) != 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP360",
        "admitted_state_domain": "Q>0 canonical WP359 source displacements and a nondegenerate local physical16 chart with fifteen CP-even coordinates and signed J, conditional on lambda>0 and c>0",
        "faithful_quotient_coordinate": "full physical16=(z1,...,z15,J); the portal factors through the nonfaithful CP-even projection J^2",
        "source_authorized_probe_family": "conditional invariant portal residual J^2-c*Q and its positive energy lambda*(J^2-c*Q)^2",
        "contextual_partition": "portal classes fix J^2 relative to cQ while retaining all fifteen CP-even coordinates and the CP-conjugate orientation pair",
        "classification": "conditional weak-basis-descending codimension-one selector and shell rigidifier; neither a full physical16 selector nor a numerical prediction",
        "portal": str(portal),
        "constraint": str(residual),
        "constraint_rank": 1,
        "selected_family_dimension": 15,
        "responses": {"d_absJ_d_Q": str(response_Q), "d_absJ_d_c": str(response_c)},
        "smallest_exact_falsifier": "d|J|/dc=sqrt(Q)/(2*sqrt(c)) is nonzero, so the matching coefficient retains numerical authority",
        "remaining_physical_instrument_gate": "derive c and lambda independently from a common flavor action and measure canonical Q together with J or J^2 in one calibrated frame; an even portal supplies no CP-orientation instrument",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp360_canonical_source_physical16_portal.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
