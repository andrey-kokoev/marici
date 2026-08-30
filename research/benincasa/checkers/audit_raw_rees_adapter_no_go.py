#!/usr/bin/env python3
"""Show that the raw E^-2 e6 coefficient cannot define the residue adapter."""

import json
from fractions import Fraction
from pathlib import Path


raw_double_pole = Fraction(1, 8)

# Under Omega -> Omega + h*e6/E, differentiation contributes -h*e6/E^2.
def transformed_double_pole(h):
    return raw_double_pole - h


gauges = {
    "raw_frame": Fraction(0),
    "kummer_normalized": Fraction(1, 8),
    "alternate": Fraction(1, 16),
}
transformed = {name: transformed_double_pole(h) for name, h in gauges.items()}

checks = {
    "raw_coefficient_is_one_over_eight": transformed["raw_frame"]
    == Fraction(1, 8),
    "kummer_rees_shift_removes_double_pole": transformed["kummer_normalized"] == 0,
    "alternate_shift_changes_coefficient": transformed["alternate"]
    == Fraction(1, 16),
    "coefficient_is_not_rees_gauge_invariant": len(set(transformed.values())) == 3,
}

if not all(checks.values()):
    raise SystemExit(f"failed checks: {[key for key, ok in checks.items() if not ok]}")

packet = {
    "schema": "marici.benincasa.raw_rees_adapter_no_go.v1",
    "raw_arrow": "[E^-2 e6] nabla(Omega111)=1/8",
    "rees_shear": "Omega111 -> Omega111 + h*e6/E",
    "transformation_law": "b -> b-h",
    "gauges": {key: str(value) for key, value in gauges.items()},
    "transformed_double_poles": {
        key: str(value) for key, value in transformed.items()
    },
    "checks": checks,
    "verdict": (
        "The raw second-Rees coefficient is not a canonical map from the "
        "Leray-soft relational residue to Ext(q0,e6). It is removable and "
        "continuously variable under admitted Rees shears. The universal "
        "relational cell remains defined, but its coefficient realization is "
        "still absent."
    ),
}

out = Path(__file__).resolve().parents[1] / "results" / "raw_rees_adapter_no_go.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))
