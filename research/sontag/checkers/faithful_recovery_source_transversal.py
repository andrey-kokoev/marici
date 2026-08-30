import itertools
import json
from pathlib import Path


full_source = tuple(itertools.product((0, 1), repeat=2))
diagonal_source = ((0, 0), (1, 1))


def q(state):
    system, _memory = state
    return system


def diagonal_section(system):
    return system, system


def zero_section(system):
    return system, 0


def system_record(state):
    return state[0]


def recall_record(state):
    return state[1]


def physically_recovers(section, source):
    return all(section(q(state)) == state for state in source)


def predictively_recovers(section, source, records):
    return all(
        all(record(section(q(state))) == record(state) for record in records)
        for state in source
    )


checks = {
    "diagonal_section_is_right_inverse": all(
        q(diagonal_section(system)) == system for system in (0, 1)
    ),
    "physical_recovery_fails_on_full_source": not physically_recovers(
        diagonal_section, full_source
    ),
    "physical_recovery_holds_on_source_diagonal": physically_recovers(
        diagonal_section, diagonal_source
    ),
    "quotient_is_injective_on_source_diagonal": len(
        {q(state) for state in diagonal_source}
    )
    == len(diagonal_source),
    "multiple_sections_are_system_predictively_adequate": predictively_recovers(
        diagonal_section, full_source, (system_record,)
    )
    and predictively_recovers(zero_section, full_source, (system_record,)),
    "system_predictive_adequacy_is_not_physical_recovery": predictively_recovers(
        zero_section, full_source, (system_record,)
    )
    and not physically_recovers(zero_section, full_source),
    "recall_breaks_diagonal_section_on_full_source": not predictively_recovers(
        diagonal_section, full_source, (system_record, recall_record)
    ),
    "recall_breaks_zero_section_on_full_source": not predictively_recovers(
        zero_section, full_source, (system_record, recall_record)
    ),
}

result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "full_source": [list(state) for state in full_source],
    "source_transversal": [list(state) for state in diagonal_source],
    "classification": {
        "physical_recovery": "left inverse on an independently admitted source domain",
        "predictive_recovery": "future-record equivalence for a frozen Task/test family",
        "representative_selection": "right inverse of forgetting without state-recovery authority",
    },
}

output = Path(__file__).parents[1] / "results" / "faithful_recovery_source_transversal.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

