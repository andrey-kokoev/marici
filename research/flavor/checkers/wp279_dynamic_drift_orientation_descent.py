"""WP279: exact orientation-descent audit for WP278's rotation drift."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    drift = sp.Matrix([[0, 1], [-1, 0]])
    reflection = sp.diag(1, -1)
    rotation = sp.Matrix([[0, 1], [-1, 0]])

    reflected_drift = sp.simplify(reflection * drift * reflection.inv())
    rotated_drift = sp.simplify(rotation * drift * rotation.inv())
    reflection_residual = sp.simplify(reflected_drift - drift)
    oriented_residual = sp.simplify(rotated_drift - drift)

    # Introduce an orientation pseudoscalar omega that flips under reflection.
    omega = sp.symbols("omega", nonzero=True)
    physical_drift = omega * drift
    transformed_with_pseudoscalar = sp.simplify((-omega) * reflected_drift)
    pseudoscalar_residual = sp.simplify(transformed_with_pseudoscalar - physical_drift)

    # Observability determinant changes sign with orientation but its Gram
    # determinant remains positive; faithfulness and descent are distinct.
    sensor = sp.Matrix([[1, 0]])
    tower = sensor.col_join(sensor * drift)
    reflected_sensor = sensor * reflection.inv()
    reflected_tower = reflected_sensor.col_join(reflected_sensor * reflected_drift)
    gram_det = sp.factor((tower.T * tower).det())
    reflected_gram_det = sp.factor((reflected_tower.T * reflected_tower).det())

    checks = {
        "rotation_drift_preserved_by_oriented_rotation": oriented_residual == sp.zeros(2),
        "rotation_drift_flips_under_reflection": reflected_drift == -drift,
        "full_O2_descent_fails": reflection_residual != sp.zeros(2),
        "orientation_pseudoscalar_repairs_covariance": pseudoscalar_residual == sp.zeros(2),
        "unoriented_score_tower_remains_rank_two": tower.rank() == 2 and reflected_tower.rank() == 2,
        "faithfulness_gram_is_orientation_blind": gram_det == reflected_gram_det == 1,
        "descent_and_observability_are_independent": tower.rank() == 2 and reflection_residual != sp.zeros(2),
        "deliberate_rank_implies_descent_claim_fails": reflected_drift != drift,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP279",
        "theorem_domain": "WP278 two-dimensional deviation module before an orientation tensor is admitted",
        "candidate_drift": [[int(value) for value in drift.row(i)] for i in range(2)],
        "oriented_rotation_conjugate": [[int(value) for value in rotated_drift.row(i)] for i in range(2)],
        "reflection_conjugate": [[int(value) for value in reflected_drift.row(i)] for i in range(2)],
        "reflection_residual": [[int(value) for value in reflection_residual.row(i)] for i in range(2)],
        "pseudoscalar_repair": "A_phys=omega*J with omega changing sign under orientation reversal",
        "score_tower_gram_determinants": {"original": str(gram_det), "reflected": str(reflected_gram_det)},
        "contextual_partition": "the time-score tower remains faithful in either chart, but the direction of time rotation is not the same quotient operation until an orientation pseudoscalar is supplied",
        "classification": "WP278 is a faithful dynamic architecture on an oriented deviation module; on the unoriented full groupoid its drift fails descent despite rank-two observability and reachability",
        "first_nonfaithful_arrow": "chart rotation generator -> quotient-defined source drift",
        "smallest_exact_falsifier": "Q=diag(1,-1) gives Q*J*Q^-1=-J while the observation Gram determinant remains one",
        "remaining_authority_gate": "derive an orientation/CP-odd pseudoscalar from the flavor source and state its stabilizer groupoid, or replace J by a drift built entirely from already admitted quotient tensors",
        "reference_port_rule": "adjoining an external orientation defines a new relational experiment over the orientation-preserving stabilizer; it does not reveal an absolute orientation of the original module",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp279_dynamic_drift_orientation_descent.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
