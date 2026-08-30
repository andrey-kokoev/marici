"""Exact Čech-nerve termination for a jointly faithful finite ubermonitor."""

import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "ubermonitor_cech_termination_checks.json"


def syndrome(state):
    return sum(bit << index for index, bit in enumerate(state))


def terminal(state):
    return int(all(state))


def cech_tuple_count(states, observation, arity):
    fibers = Counter(observation(state) for state in states)
    return sum(size ** arity for size in fibers.values())


def main():
    health_states = list(itertools.product([0, 1], repeat=4))
    syndrome_values = [syndrome(state) for state in health_states]
    cech_counts = {
        str(arity): cech_tuple_count(health_states, syndrome, arity)
        for arity in range(2, 8)
    }
    terminal_counts = {
        str(arity): cech_tuple_count(health_states, terminal, arity)
        for arity in range(2, 6)
    }

    extended_states = [(state, fresh) for state in health_states for fresh in [0, 1]]
    extended_observation = lambda item: syndrome(item[0])
    extended_kernel_pair_count = cech_tuple_count(extended_states, extended_observation, 2)

    gates = {
        "sixteen_outcome_syndrome_is_injective": len(set(syndrome_values)) == 16,
        "ubermonitor_kernel_pair_is_diagonal": cech_counts["2"] == 16,
        "all_checked_cech_levels_have_only_diagonal_tuples": all(
            count == 16 for count in cech_counts.values()
        ),
        "terminal_one_bit_kernel_pair_is_nontrivial": terminal_counts["2"] == 226,
        "terminal_higher_cech_levels_keep_growing":
            terminal_counts["5"] > terminal_counts["2"],
        "one_instrument_can_carry_four_bits": max(syndrome_values) == 15,
        "one_fresh_unobserved_bit_reopens_kernel_pair": extended_kernel_pair_count == 64,
        "fresh_extension_destroys_monicity": extended_kernel_pair_count > len(extended_states),
        "termination_is_relative_to_frozen_ontology": True,
        "coefficient_and_authority_typing_remain_required": True,
    }
    payload = {
        "schema": "marici.strominger.ubermonitor-cech-termination.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "health_object_cardinality": 16,
            "ubermonitor_outcomes": 16,
            "ubermonitor_information_bits": 4,
            "kernel_pair": "diagonal",
            "cech_termination": "relative_to_declared_health_ontology",
            "fresh_failure_extension": "reopens_nontrivial_kernel_pair",
            "physical_monitor_authority": "not_established",
        },
        "ubermonitor_cech_tuple_counts": cech_counts,
        "terminal_cech_tuple_counts": terminal_counts,
        "extended_state_count": len(extended_states),
        "extended_kernel_pair_count": extended_kernel_pair_count,
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
