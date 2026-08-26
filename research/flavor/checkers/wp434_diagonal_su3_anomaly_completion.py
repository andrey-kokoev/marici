"""Exact anomaly audit for diagonal quark-generation SU(3)_F."""

import json
from fractions import Fraction
from pathlib import Path


root = Path(__file__).parents[1]
wp433 = json.loads((root / "results" / "wp433_two_adjoint_gauge_clock_obstruction.json").read_text(encoding="utf-8"))

fields = {
    "Q_L": {"multiplicity": 6, "cubic_sign": 1, "hypercharge": Fraction(1, 6)},
    "u_R_conjugate": {"multiplicity": 3, "cubic_sign": -1, "hypercharge": Fraction(-2, 3)},
    "d_R_conjugate": {"multiplicity": 3, "cubic_sign": -1, "hypercharge": Fraction(1, 3)},
}

cubic_anomaly = sum(row["multiplicity"] * row["cubic_sign"] for row in fields.values())
mixed_f2_y_without_common_index = sum(
    row["multiplicity"] * row["hypercharge"] for row in fields.values()
)

q_only_cubic = fields["Q_L"]["multiplicity"] * fields["Q_L"]["cubic_sign"]
q_only_f2_y = fields["Q_L"]["multiplicity"] * fields["Q_L"]["hypercharge"]

checks = {
    "Q_only_flavor_gauging_is_cubically_anomalous": q_only_cubic == 6,
    "Q_only_mixed_flavor_hypercharge_anomaly_is_nonzero": q_only_f2_y != 0,
    "diagonal_quark_flavor_cubic_anomaly_cancels": cubic_anomaly == 0,
    "diagonal_quark_flavor_mixed_hypercharge_anomaly_cancels": mixed_f2_y_without_common_index == 0,
    "no_spectator_multiplicity_is_needed": sum(row["multiplicity"] for row in fields.values()) == 12,
    "wp433_SU3_mass_shape_dependency_passed": wp433["passed"] and wp433["SU3_mass_gram_rank"] == 8,
    "central_U1_is_not_part_of_declared_gauge_group": wp433["U3_kernel_dimension"] == 1 and wp433["SU3_mass_gram_rank"] == 8,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP434",
    "title": "Diagonal quark-flavor SU(3) anomaly completion",
    "gauge_group": "diagonal SU(3)_F acting on Q_L, u_R, d_R generations",
    "left_handed_field_packet": {
        name: {
            "multiplicity": row["multiplicity"],
            "cubic_sign": row["cubic_sign"],
            "hypercharge": str(row["hypercharge"]),
        }
        for name, row in fields.items()
    },
    "SU3F_cubic_anomaly": cubic_anomaly,
    "SU3F_squared_U1Y_anomaly_without_common_index": str(mixed_f2_y_without_common_index),
    "spectator_fermions_required_for_these_anomalies": 0,
    "classification": "anomaly-free spectatorless diagonal SU(3)_F grammar compatible with the WP433 adjoint mass shape",
    "groupoid_change": "new gauged diagonal relational theory, not a weak-basis gauge fixing",
    "smallest_exact_falsifier": "a nonzero cubic or mixed-hypercharge anomaly coefficient for the declared quark packet",
    "remaining_gate": "dynamical flavons, selected g_F f/v, flavor-current bounds and instrument, and frozen spectral widths and residues",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp434_diagonal_su3_anomaly_completion.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
