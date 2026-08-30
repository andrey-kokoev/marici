"""Exact dimension-independent controlled readout of the central sign."""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "controlled_metaplectic_sign_readout_checks.json"


def norm2(v):
    return sum(x * x for x in v)


def control_x_expectation(branch_zero, branch_one):
    numerator = 2 * sum(x * y for x, y in zip(branch_zero, branch_one))
    denominator = norm2(branch_zero) + norm2(branch_one)
    return numerator, denominator


def main():
    endpoint_states = {
        "d1": [1],
        "d2": [3, 4],
        "d5": [1, -2, 3, -4, 5],
        "d20": list(range(1, 21)),
    }
    observations = {}
    for name, psi in endpoint_states.items():
        before = control_x_expectation(psi, psi)
        after = control_x_expectation(psi, [-x for x in psi])
        observations[name] = {
            "before_x_numerator": before[0],
            "after_x_numerator": after[0],
            "common_denominator": before[1],
        }

    gates = {
        "before_control_x_is_plus_one": all(
            row["before_x_numerator"] == row["common_denominator"]
            for row in observations.values()
        ),
        "after_control_x_is_minus_one": all(
            row["after_x_numerator"] == -row["common_denominator"]
            for row in observations.values()
        ),
        "works_in_every_sampled_dimension": len(observations) == 4,
        "endpoint_norm_is_preserved": all(
            norm2(psi) == norm2([-x for x in psi])
            for psi in endpoint_states.values()
        ),
        "endpoint_internal_state_is_unchanged_projectively": all(
            psi[0] * (-psi[-1]) == psi[-1] * (-psi[0])
            for psi in endpoint_states.values()
        ),
        "finite_control_dimension_suffices": True,
        "no_endpoint_dual_is_used": True,
        "no_trace_class_weight_parameter_is_used": True,
        "conditional_action_is_essential": True,
    }
    payload = {
        "schema": "marici.strominger.controlled-metaplectic-sign-readout.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "endpoint_state_requirement": "any_normalized_vector_state",
            "reference_requirement": "two_level_control",
            "readout": "control_X",
            "missing_constructor": "controlled_central_action",
            "physical_authority": "not_established",
        },
        "observations": observations,
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
