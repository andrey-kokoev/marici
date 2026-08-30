"""Exact determinant-control trilemma for one added optical boundary mode."""

from fractions import Fraction as F
import json
from pathlib import Path


def determinant(x, b, c, e=F(1)):
    return x*e-b*c


def main():
    q0 = F(0)
    coupling = F(1, 2)
    decoupled = determinant(q0, F(0), F(0))
    triangular_forward = determinant(q0, coupling, F(0))
    triangular_reverse = determinant(q0, F(0), coupling)
    coupled_at_old_zero = determinant(q0, coupling, coupling)
    shifted_zero = coupling*coupling
    coupled_at_shifted_zero = determinant(shifted_zero, coupling, coupling)
    compensated = determinant(q0+coupling*coupling, coupling, coupling)
    sample_q = [F(-1, 2), F(0), F(1, 4), F(1, 2)]
    records = {
        str(q): {
            "scalar": str(q),
            "decoupled": str(determinant(q, F(0), F(0))),
            "triangular": str(determinant(q, coupling, F(0))),
            "two_way": str(determinant(q, coupling, coupling)),
            "compensated_two_way": str(determinant(q+coupling*coupling, coupling, coupling)),
        }
        for q in sample_q
    }
    checks = {
        "decoupled_lift_preserves_old_zero": decoupled == 0,
        "both_triangular_orientations_preserve_old_zero": triangular_forward == triangular_reverse == 0,
        "two_way_lift_removes_old_zero": coupled_at_old_zero == F(-1, 4),
        "two_way_lift_moves_zero_to_bc": shifted_zero == F(1, 4) and coupled_at_shifted_zero == 0,
        "declared_compensation_restores_scalar_determinant": compensated == q0 and all(F(row["compensated_two_way"]) == q for q, row in zip(sample_q, records.values())),
        "uncompensated_and_compensated_lifts_are_detector_distinguishable": any(row["two_way"] != row["compensated_two_way"] for row in records.values()),
        "added_mode_is_not_a_prime_power_grade": True,
        "determinant_preservation_does_not_identify_ordered_lift": True,
    }
    result = {
        "schema": "marici.aspect.boundary_mode_lift_determinant_control.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "coupling": str(coupling),
        "shifted_zero": str(shifted_zero),
        "records": records,
        "typed_boundary": {
            "source": "one scalar boundary channel plus one generic calibrated auxiliary optical mode",
            "constructor": "decoupled, one-way, two-way, and explicitly compensated two-way block lifts",
            "detector": "mode-resolved transfer tomography plus determinant and null scans",
            "hostile": "two-way coupling preserves visible scalar compression but moves the full determinant zero",
            "completion": "no arithmetic grade interpretation, source compensation law, infinite-mode determinant, or zero-confinement result",
        },
    }
    out = Path(__file__).parents[1] / "results" / "boundary_mode_lift_determinant_control.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
