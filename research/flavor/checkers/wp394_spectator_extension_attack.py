"""WP394: exact spectator-extension underdetermination attack."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    v = sp.Matrix([1, 2])
    n = sp.Matrix([-2, 1])
    S = (v*v.T-n*n.T)/(v.dot(v))
    Eplus = sp.diag(1, 1, 1)
    Eplus[:2, :2] = S
    Eminus = sp.diag(1, 1, -1)
    Eminus[:2, :2] = S
    flavor_projector = sp.Matrix([[1, 0, 0], [0, 1, 0]])
    restriction_plus = flavor_projector*Eplus*flavor_projector.T
    restriction_minus = flavor_projector*Eminus*flavor_projector.T
    spectator = sp.Matrix([0, 0, 1])
    fixed_plus = (Eplus-sp.eye(3)).nullspace()
    fixed_minus = (Eminus-sp.eye(3)).nullspace()
    checks = {
        "plus_extension_is_involution": Eplus*Eplus == sp.eye(3),
        "minus_extension_is_involution": Eminus*Eminus == sp.eye(3),
        "extensions_have_identical_flavor_restriction": restriction_plus == restriction_minus,
        "common_flavor_restriction_fixes_target": restriction_plus*v == v,
        "common_flavor_restriction_reverses_complement": restriction_plus*n == -n,
        "plus_extension_makes_spectator_even": Eplus*spectator == spectator,
        "minus_extension_makes_spectator_odd": Eminus*spectator == -spectator,
        "plus_extension_allows_linear_spectator_invariant": (Eplus*spectator)[2] == 1,
        "minus_extension_forbids_linear_spectator_invariant": (Eminus*spectator)[2] == -1,
        "full_fixed_dimensions_differ": len(fixed_plus) == 2 and len(fixed_minus) == 1,
        "flavor_fixed_line_same_in_both": sp.det(sp.Matrix.hstack(fixed_minus[0][:2, :], v)) == 0,
        "extensions_are_distinct": Eplus != Eminus,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP394",
        "admitted_state_domain": "the WP393 two-dimensional flavor response plus one independently observable real spectator coordinate",
        "faithful_quotient_coordinate": "the flavor response ray together with the spectator parity readout",
        "source_authorized_probe_family": "direct-sum symmetry extensions, fixed spaces, and spectator parity selection rules",
        "contextual_partition": "both extensions make identical flavor predictions; the spectator is even in one extension and odd in the other",
        "classification": "exact underdetermination of global constructor content by a preregistered flavor-only symmetry",
        "flavor_reflection": str(S),
        "even_spectator_extension": str(Eplus),
        "odd_spectator_extension": str(Eminus),
        "smallest_exact_falsifier": "S_v direct-sum +1 and S_v direct-sum -1 agree on every flavor vector but predict opposite spectator parity",
        "remaining_physical_instrument_gate": "derive the symmetry action on at least one independently accessible spectator sector and test its selection rule without using flavor data",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp394_spectator_extension_attack.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
