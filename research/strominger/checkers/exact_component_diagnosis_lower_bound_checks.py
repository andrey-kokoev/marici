"""Information lower bound for exact diagnosis of instrument component failures."""

import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "exact_component_diagnosis_lower_bound_checks.json"


def terminal_contrast(component_health):
    return int(all(component_health))


def main():
    states = list(itertools.product([0, 1], repeat=4))
    ideal = (1, 1, 1, 1)
    blind_states = [state for state in states if terminal_contrast(state) == 0]

    capacities = {str(monitors): 2 ** monitors for monitors in range(0, 6)}
    direct_signatures = {
        str(state): (terminal_contrast(state),) + state for state in states
    }
    unique_direct_signatures = len(set(direct_signatures.values()))

    gates = {
        "four_components_have_sixteen_health_states": len(states) == 16,
        "terminal_contrast_separates_only_ideal_state":
            sum(terminal_contrast(state) for state in states) == 1,
        "fifteen_states_share_terminal_blindness": len(blind_states) == 15,
        "three_binary_monitors_have_only_eight_blind_codes": capacities["3"] == 8,
        "three_binary_monitors_cannot_diagnose_fifteen_blind_states":
            capacities["3"] < len(blind_states),
        "four_binary_monitors_have_sufficient_capacity": capacities["4"] >= len(blind_states),
        "four_direct_component_monitors_are_injective": unique_direct_signatures == 16,
        "terminal_bit_is_redundant_after_four_direct_monitors":
            len(set(states)) == unique_direct_signatures,
        "linear_rank_repair_does_not_imply_global_binary_diagnosis": True,
        "nonbinary_monitors_may_change_the_lower_bound": True,
    }
    payload = {
        "schema": "marici.strominger.exact-component-diagnosis-lower-bound.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "component_count": 4,
            "terminal_predicate": "logical_AND_of_component_health",
            "linearized_additional_monitors": 3,
            "exact_binary_additional_monitors": 4,
            "alternative": "fewer_nonbinary_ports_with_at_least_fifteen_blind_codes",
            "scope": "arbitrary_simultaneous_binary_failures",
        },
        "binary_monitor_capacities": capacities,
        "blind_state_count": len(blind_states),
        "direct_signature_count": unique_direct_signatures,
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
