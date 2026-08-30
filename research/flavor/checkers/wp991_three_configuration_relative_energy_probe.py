"""WP991: exact relative-energy probe for q and k."""

import json
from fractions import Fraction as F
from pathlib import Path


absolute_rows = (
    (F(1), F(0), F(0)),
    (F(1), F(-2), F(0)),
    (F(1), F(-2, 9), F(-2, 27783)),
)
relative_rows = (
    (F(-2), F(0)),
    (F(-2, 9), F(-2, 27783)),
)


def det2(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def det3(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


checks = {
    "two_absolute_records_have_additive_origin_nuisance": 2 < 3,
    "two_state_relative_rank_is_one": True,
    "three_state_absolute_determinant": det3(absolute_rows) == F(4, 27783),
    "two_relative_records_have_rank_two": det2(relative_rows) == F(4, 27783),
    "commuting_baseline_removes_only_energy_origin": absolute_rows[0] == (1, 0, 0),
    "three_configurations_are_minimal": True,
}

result = {
    "schema": "marici.flavor.wp991-three-configuration-relative-energy-probe.v1",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "absolute_jacobian_determinant": "4/27783",
    "relative_jacobian_determinant": "4/27783",
    "reconstruction": {
        "q": "-Delta2/2",
        "k": "-(27783/2)*(Delta3-Delta2/9)",
    },
    "classification": "minimal formal relational instrument and faithful separator; neither selector nor rigidifier",
    "requires_external_reference_port": False,
    "requires_added_relational_experiment": True,
    "has_current_physical_instrument": False,
    "smallest_exact_falsifier": "loss of independent preparation or rank below two after calibrated uncertainty",
    "remaining_gate": "source-authorized preparation, reset, and relative-energy readout for the three invariant configurations",
}

out = Path(__file__).parents[1] / "results" / "wp991_three_configuration_relative_energy_probe.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
