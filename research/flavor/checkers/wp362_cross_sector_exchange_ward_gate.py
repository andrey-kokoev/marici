"""WP362: exact Ward-normalization audit for a cross-sector exchange port."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    alpha = sp.symbols("alpha", real=True, positive=True)
    K = sp.Matrix([[1, -alpha], [-alpha, alpha**2]])
    identity_action = sp.eye(2)
    exchange = sp.Matrix([[0, 1], [1, 0]])

    product_group_residual = sp.simplify(identity_action.T * K * identity_action - K)
    exchange_residual = sp.simplify(exchange.T * K * exchange - K)
    ward_equation = sp.factor(exchange_residual[0, 0])
    ward_roots = sp.solve(ward_equation, alpha)
    positive_ward_roots = [root for root in ward_roots if root.is_positive]
    hostile_residual = exchange_residual.subs(alpha, 2)
    unit_residual = exchange_residual.subs(alpha, 1)

    v_minus = sp.Matrix([1, -1])
    v_plus = sp.Matrix([1, 1])
    K_unit = K.subs(alpha, 1)

    checks = {
        "separate_singlet_groupoid_imposes_no_constraint": product_group_residual == sp.zeros(2),
        "exchange_is_an_involution": exchange**2 == sp.eye(2),
        "exchange_ward_equations_have_unit_positive_root_only": positive_ward_roots == [sp.Integer(1)],
        "unit_portal_is_exchange_invariant": unit_residual == sp.zeros(2),
        "hostile_alpha_two_violates_exchange": hostile_residual != sp.zeros(2),
        "unit_portal_penalizes_antisymmetric_line": K_unit * v_plus == sp.zeros(2, 1) and K_unit * v_minus == 2 * v_minus,
        "unit_portal_has_rank_one": K_unit.rank() == 1,
        "deliberate_exchange_residual_is_nonzero": any(entry != 0 for entry in hostile_residual),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP362",
        "admitted_state_domain": "the two dimensionless invariant ports x=J^2 and y=Q/M2; existing authority is only the product of flavor weak-basis and effective-source reparameterization groupoids",
        "faithful_quotient_coordinate": "full physical16 and the WP359 source quotient remain separate; the proposed exchange enlarges the experiment to paired relational states modulo its stabilizer groupoid",
        "source_authorized_probe_family": "existing separate singlet probes, plus a hypothetical cross-sector exchange P acting on (J^2,Q/M2)",
        "contextual_partition": "without P every alpha>0 is equally typed; with an admitted exchange Ward identity the positive family collapses to alpha=1",
        "classification": "algebraically sufficient unit-normalization selector conditional on a new relational exchange experiment; not currently an admitted physical flavor operation",
        "quadratic_matrix": str(K),
        "exchange_matrix": str(exchange),
        "exchange_residual": str(exchange_residual),
        "positive_ward_roots": [str(root) for root in positive_ward_roots],
        "hostile_alpha_two_residual": str(hostile_residual),
        "selected_shell_if_interface_exists": "J^2=Q/M2",
        "smallest_exact_falsifier": "P^T*K_2*P-K_2 is nonzero, although alpha=2 passes all pre-exchange symmetry and dimensional gates",
        "remaining_physical_instrument_gate": "construct a source-derived common two-port representation and an executable calibrated operation implementing or testing the J^2 <-> Q/M2 exchange; otherwise P is unauthorized parallelization",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp362_cross_sector_exchange_ward_gate.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
