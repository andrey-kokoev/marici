"""WP392: exact representation-multiplicity attack on the flavor DPC."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    g1, g2 = sp.symbols("g1 g2", real=True)
    p, q, r, s = sp.symbols("p q r s", real=True)
    rho_L = sp.Matrix([[-1]])
    rho_R = -sp.eye(2)
    v = sp.Matrix([g1, g2])
    intertwiner_residual = sp.simplify(rho_R*v-v*rho_L[0, 0])
    constraint_matrix = rho_R-rho_L[0, 0]*sp.eye(2)
    A = sp.Matrix([[p, q], [r, s]])
    commutator = sp.simplify(A*rho_R-rho_R*A)
    hostile_A = sp.Matrix([[0, 1], [0, 0]])
    hostile_v = sp.Matrix([0, 1])
    hostile_Av = hostile_A*hostile_v
    hostile_wedge = sp.det(sp.Matrix.hstack(hostile_v, hostile_Av))
    v1, v2 = sp.Matrix([1, 1]), sp.Matrix([1, 2])
    joint = v1*v1.T+v2*v2.T
    checks = {
        "source_line_is_one_dimensional": rho_L.shape == (1, 1),
        "source_group_relation_exact": rho_L**2 == sp.eye(1),
        "response_group_relation_exact": rho_R**2 == sp.eye(2),
        "every_coupling_vector_is_intertwiner": intertwiner_residual == sp.zeros(2, 1),
        "intertwiner_space_dimension_two": len(constraint_matrix.nullspace()) == 2,
        "arbitrary_rg_mixing_commutes_with_cp": commutator == sp.zeros(2),
        "allowed_rg_mixing_rotates_hostile_vector": hostile_wedge != 0,
        "hostile_rotation_exact": hostile_Av == sp.Matrix([1, 0]),
        "distinct_ratios_both_symmetry_allowed": rho_R*v1 == -v1 and rho_R*v2 == -v2,
        "two_allowed_contexts_jointly_full_rank": joint.det().is_positive,
        "single_response_copy_would_have_hom_dimension_one": len((sp.Matrix([[-1]])+sp.eye(1)).nullspace()) == 1,
        "calibrated_ratio_not_fixed_by_intertwining": not intertwiner_residual.has(g1) and not intertwiner_residual.has(g2),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP392",
        "admitted_state_domain": "a multiplicity-one CP-odd source line L and a two-coordinate CP-odd response R=L direct-sum L",
        "faithful_quotient_coordinate": "the physical response direction in the two-dimensional CP-odd multiplicity space",
        "source_authorized_probe_family": "exact group representations, intertwiner space, symmetry-allowed RG commutant, and two-context joint rank",
        "contextual_partition": "all coupling ratios are symmetry-equivalent as allowed intertwiners; different contexts can choose noncollinear directions while respecting the same CP representation",
        "classification": "exact counterexample to the stated DPC implication from multiplicity-one middle channel to unique protected response direction",
        "source_representation": str(rho_L),
        "response_representation": str(rho_R),
        "intertwiner_dimension": len(constraint_matrix.nullspace()),
        "hostile_rg_generator": str(hostile_A),
        "hostile_joint_determinant": str(joint.det()),
        "smallest_exact_falsifier": "L is one-dimensional and occurs once as the source, yet R=L direct-sum L admits the independent intertwiners (1,1) and (1,2), whose joint Gram response has positive determinant",
        "remaining_physical_instrument_gate": "replace source multiplicity one by a derived one-dimensional intertwiner space Hom_G(L,R), prove the RG commutant preserves its image, and calibrate its embedding in physical16",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp392_dpc_multiplicity_attack.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
