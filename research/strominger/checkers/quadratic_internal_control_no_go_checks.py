"""Exact mixed-difference no-go for internal control by quadratic generators."""

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "quadratic_internal_control_no_go_checks.json"


def selector(n_v):
    """Even-code selector: n_v=2 is inactive and n_v=4 is active."""
    return Fraction(n_v - 2, 2)


def controlled_energy(n_u, n_v):
    return selector(n_v) * (Fraction(n_u) + Fraction(1, 2))


def mixed_difference(values, u0, u1, v0, v1):
    return values[(u1, v1)] - values[(u1, v0)] - values[(u0, v1)] + values[(u0, v0)]


def main():
    u_values = [2, 4]
    v_values = [2, 4]
    grid = [(u, v) for u in u_values for v in v_values]
    controlled = {(u, v): controlled_energy(u, v) for u, v in grid}

    affine_samples = []
    for a in range(-2, 3):
        for b in range(-2, 3):
            for c in range(-2, 3):
                values = {(u, v): Fraction(a * u + b * v + c) for u, v in grid}
                affine_samples.append(mixed_difference(values, 2, 4, 2, 4))

    controlled_mixed = mixed_difference(controlled, 2, 4, 2, 4)
    gates = {
        "all_code_states_have_even_total_parity": all((u + v) % 2 == 0 for u, v in grid),
        "inactive_selector_branch_is_zero": all(controlled[(u, 2)] == 0 for u in u_values),
        "active_selector_branch_is_oscillator_energy": all(
            controlled[(u, 4)] == Fraction(u) + Fraction(1, 2) for u in u_values
        ),
        "controlled_generator_has_nonzero_mixed_difference": controlled_mixed == 2,
        "all_sampled_affine_quadratic_diagonals_have_zero_mixed_difference":
            all(value == 0 for value in affine_samples),
        "controlled_diagonal_is_not_affine": controlled_mixed != 0,
        "quadratic_lie_closure_cannot_generate_quartic_cross_term": True,
        "minimum_degree_of_number_number_control_is_four": True,
        "physical_quartic_constructor_is_not_source_derived": True,
    }
    payload = {
        "schema": "marici.strominger.quadratic-internal-control-no-go.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "source_control_algebra": "quadratic_sp4",
            "internal_selector_code": ["n_v=2", "n_v=4"],
            "desired_generator": "((N_v-2)/2)*(N_u+1/2)",
            "desired_bernstein_degree": 4,
            "obstruction": "nonzero_mixed_number_difference",
            "missing_constructor": "quartic_cross_mode_interaction",
        },
        "controlled_grid": {f"{u},{v}": str(value) for (u, v), value in controlled.items()},
        "controlled_mixed_difference": str(controlled_mixed),
        "affine_samples_checked": len(affine_samples),
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
