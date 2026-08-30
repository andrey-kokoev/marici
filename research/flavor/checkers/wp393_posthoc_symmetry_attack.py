"""WP393: exact post-hoc symmetry construction attack on the revised DPC."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def reflection_for(vector):
    p, q = vector
    normal = sp.Matrix([-q, p])
    norm2 = (vector.T*vector)[0]
    return sp.simplify((vector*vector.T-normal*normal.T)/norm2)

def main():
    p, q = sp.symbols("p q", real=True, nonzero=True)
    v = sp.Matrix([p, q])
    n = sp.Matrix([-q, p])
    S = reflection_for(v)
    fixed_constraint = sp.simplify(S-sp.eye(2))
    v1, v2 = sp.Matrix([1, 2]), sp.Matrix([2, 1])
    S1, S2 = reflection_for(v1), reflection_for(v2)
    first_fixed_basis = fixed_constraint.subs({p: 1, q: 2}).nullspace()[0]
    checks = {
        "custom_reflection_is_involution": sp.simplify(S*S-sp.eye(2)) == sp.zeros(2),
        "target_direction_fixed": sp.simplify(S*v-v) == sp.zeros(2, 1),
        "orthogonal_direction_reversed": sp.simplify(S*n+n) == sp.zeros(2, 1),
        "custom_reflection_trace_zero": sp.simplify(sp.trace(S)) == 0,
        "custom_reflection_determinant_minus_one": sp.simplify(S.det()) == -1,
        "fixed_intertwiner_space_dimension_one": len(fixed_constraint.nullspace()) == 1,
        "first_arbitrary_target_fixed_by_its_symmetry": S1*v1 == v1,
        "second_arbitrary_target_fixed_by_its_symmetry": S2*v2 == v2,
        "first_symmetry_does_not_fix_second_target": S1*v2 != v2,
        "distinct_targets_require_distinct_posthoc_symmetries": S1 != S2,
        "first_fixed_space_exactly_target_line": sp.det(sp.Matrix.hstack(first_fixed_basis, v1)) == 0,
        "hostile_ratio_can_be_arbitrary_rational": reflection_for(sp.Matrix([3, 7]))*sp.Matrix([3, 7]) == sp.Matrix([3, 7]),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP393",
        "admitted_state_domain": "any nonzero response direction in a calibrated real two-dimensional response space with a chosen positive Euclidean pairing",
        "faithful_quotient_coordinate": "the projective response direction in the physical16 tangent plane",
        "source_authorized_probe_family": "custom Z2 reflections and their one-dimensional fixed intertwiner spaces",
        "contextual_partition": "every nonzero response ray has its own reflection symmetry with a unique fixed line; a fixed prior symmetry distinguishes only its own ray",
        "classification": "exact post-hoc construction showing that existence of a one-dimensional intertwiner is not explanatory without independent symmetry and metric authority",
        "custom_reflection": str(S),
        "first_target_reflection": str(S1),
        "second_target_reflection": str(S2),
        "smallest_exact_falsifier": "the unrelated target rays (1,2) and (2,1) each admit a Z2 action with one-dimensional Hom, but require different custom reflections",
        "remaining_physical_instrument_gate": "freeze the symmetry action, response metric, and representation embedding before revealing the flavor target, then test its unique predicted ray against physical16",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp393_posthoc_symmetry_attack.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
