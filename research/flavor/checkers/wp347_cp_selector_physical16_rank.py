"""WP347: exact physical16 rank audit of the CP-domain selector branch."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    even_coordinates = sp.symbols("z1:16", real=True)
    cp_odd = sp.symbols("j", real=True)
    cp_scale = sp.symbols("c0", real=True, positive=True)
    physical_coordinates = even_coordinates + (cp_odd,)
    shell_constraint = cp_odd**2 - cp_scale**2
    shell_jacobian = sp.Matrix([[sp.diff(shell_constraint, coordinate) for coordinate in physical_coordinates]])
    positive_branch_constraint = cp_odd - cp_scale
    branch_jacobian = sp.Matrix([[sp.diff(positive_branch_constraint, coordinate) for coordinate in physical_coordinates]])
    hostile_left = tuple(range(1, 16)) + (cp_scale,)
    hostile_right = (sp.Integer(2),) + tuple(range(2, 16)) + (cp_scale,)
    cp_probe = lambda point: point[-1]
    shell_probe = lambda point: sp.simplify(point[-1] ** 2)
    checks = {
        "physical_coordinate_count_is_16": len(physical_coordinates) == 16,
        "cp_shell_constraint_has_rank_one_away_from_zero": shell_jacobian.subs(cp_odd, cp_scale).rank() == 1,
        "positive_branch_constraint_has_rank_one": branch_jacobian.rank() == 1,
        "selected_branch_retains_fifteen_free_coordinates": len(physical_coordinates) - branch_jacobian.rank() == 15,
        "cp_conjugation_preserves_even_coordinates": all(coordinate.subs(cp_odd, -cp_odd) == coordinate for coordinate in even_coordinates),
        "cp_conjugation_flips_odd_coordinate": cp_odd.subs(cp_odd, -cp_odd) == -cp_odd,
        "hostile_points_are_physically_distinct": hostile_left != hostile_right,
        "hostile_points_share_cp_odd_readout": cp_probe(hostile_left) == cp_probe(hostile_right),
        "hostile_points_share_shell_readout": shell_probe(hostile_left) == shell_probe(hostile_right),
        "hostile_points_both_satisfy_positive_branch": sp.simplify(hostile_left[-1] - cp_scale) == 0 and sp.simplify(hostile_right[-1] - cp_scale) == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP347",
        "admitted_state_domain": "a local physical16 chart with fifteen CP-even coordinates z1 through z15 and one CP-odd coordinate j, away from degeneracies",
        "faithful_quotient_coordinate": "the full tuple (z1,...,z15,j), not the CP-domain coordinate alone",
        "source_operation": "WP327 shell selection j^2=c0^2 followed conditionally by positive-orientation selection j=c0",
        "shell_constraint_jacobian": [[str(value) for value in row] for row in shell_jacobian.tolist()],
        "positive_branch_jacobian": [[str(value) for value in row] for row in branch_jacobian.tolist()],
        "constraint_rank": 1,
        "selected_family_dimension": 15,
        "hostile_pair": {
            "left": [str(value) for value in hostile_left],
            "right": [str(value) for value in hostile_right],
            "common_cp_coordinate": str(cp_scale),
        },
        "contextual_partition": "CP-domain probes partition physical16 only by j or j^2; every class retains the fifteen CP-even coordinates",
        "classification": "a genuine conditional selector of one CP coordinate and orientation, but neither a selector of a full physical16 point nor a faithful physical16 readout",
        "smallest_exact_falsifier": "two physical16 points differing only in z1 both satisfy j=c0 and have identical complete CP-domain readouts",
        "remaining_physical_instrument_gate": "derive source operations constraining the fifteen CP-even coordinates and their common matching to the CP selector; CP-domain calibration cannot supply those missing arrows",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp347_cp_selector_physical16_rank.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
