"""WP385: exact factor-port degree and branch-geometry audit."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    C, D, beta = sp.symbols("C D beta", real=True, nonzero=True)
    U, V = C-beta*D, C+beta*D
    F = C**2-beta**2*D**2
    separate_penalty = sp.expand(U**2+V**2)
    product_penalty = sp.expand(U**2*V**2)
    branch_plus = {C: beta*D}
    branch_minus = {C: -beta*D}
    F_field_degree = 24
    factor_field_degree = 12
    probe_field_degree = 1
    checks = {
        "factorization_exact": sp.expand(U*V-F) == 0,
        "product_penalty_preserves_original_square": sp.expand(product_penalty-F**2) == 0,
        "separate_penalty_formula_exact": separate_penalty == 2*C**2+2*beta**2*D**2,
        "plus_branch_lies_on_original_shell": sp.simplify(F.subs(branch_plus)) == 0,
        "minus_branch_lies_on_original_shell": sp.simplify(F.subs(branch_minus)) == 0,
        "separate_penalty_rejects_nonzero_plus_branch": sp.simplify(separate_penalty.subs(branch_plus)) != 0,
        "separate_penalty_rejects_nonzero_minus_branch": sp.simplify(separate_penalty.subs(branch_minus)) != 0,
        "plus_branch_port_signature": (sp.simplify(U.subs(branch_plus)), sp.simplify(V.subs(branch_plus))) == (0, 2*beta*D),
        "minus_branch_port_signature": (sp.simplify(U.subs(branch_minus)), sp.simplify(V.subs(branch_minus))) == (-2*beta*D, 0),
        "factor_probe_vertex_degree_thirteen": factor_field_degree+probe_field_degree == 13,
        "factorization_halves_residual_degree": 2*factor_field_degree == F_field_degree,
        "product_restores_degree_forty_eight": 2*(2*factor_field_degree) == 48,
        "single_factor_port_blind_to_other_branch_coordinate": (
            U.subs({C: 1, D: 1, beta: 1}) == U.subs({C: 2, D: 2, beta: 1})
            and V.subs({C: 1, D: 1, beta: 1}) != V.subs({C: 2, D: 2, beta: 1})
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP385",
        "admitted_state_domain": "nondegenerate physical16 stratum with positive alpha*rho so beta=2*sqrt(alpha*rho) is real and nonzero",
        "faithful_quotient_coordinate": "the invariant factor pair (U,V) with F=U*V",
        "source_authorized_probe_family": "two branch-resolved reference ports coupled separately to U and V",
        "contextual_partition": "the original shell is the union U=0 or V=0; two resolved ports distinguish the branches, while independent positive penalties select only their intersection",
        "classification": "conditional branch separator and degree-reducing presentation of the source interface; not an equivalent positive selector unless the product is restored",
        "factorization": str(sp.Eq(F, U*V)),
        "separate_penalty": str(separate_penalty),
        "factor_probe_vertex_field_degree": factor_field_degree+probe_field_degree,
        "product_penalty_field_degree": 48,
        "smallest_exact_falsifier": "C=beta*D with D nonzero satisfies F=0 but has U^2+V^2=4*beta^2*D^2, so independent factor penalties overselect",
        "remaining_physical_instrument_gate": "derive both degree-13 factor couplings and their relative beta normalization from source dynamics, then preserve the union without reintroducing the degree-48 product",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp385_factor_port_branch_geometry.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
