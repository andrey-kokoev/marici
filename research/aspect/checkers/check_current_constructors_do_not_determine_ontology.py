from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    histories = ("plus", "minus")

    coarse_state = {"plus": "single", "minus": "single"}
    fine_state = {"plus": "phase_plus", "minus": "phase_minus"}

    coarse_constructors = {
        "Z": {"single": "balanced"},
    }
    fine_constructors = {
        "Z": {"phase_plus": "balanced", "phase_minus": "balanced"},
        "X": {"phase_plus": "plus", "phase_minus": "minus"},
    }

    coarse_current_records = {
        history: coarse_constructors["Z"][coarse_state[history]] for history in histories
    }
    fine_current_records = {
        history: fine_constructors["Z"][fine_state[history]] for history in histories
    }
    assert coarse_current_records == fine_current_records == {
        "plus": "balanced",
        "minus": "balanced",
    }

    coarse_ontically_identical = coarse_state["plus"] == coarse_state["minus"]
    fine_ontically_identical = fine_state["plus"] == fine_state["minus"]
    assert coarse_ontically_identical
    assert not fine_ontically_identical

    coarse_nomologically_equivalent = all(
        table[coarse_state["plus"]] == table[coarse_state["minus"]]
        for table in coarse_constructors.values()
    )
    fine_nomologically_equivalent = all(
        table[fine_state["plus"]] == table[fine_state["minus"]]
        for table in fine_constructors.values()
    )
    assert coarse_nomologically_equivalent
    assert not fine_nomologically_equivalent

    fine_x_records = {
        history: fine_constructors["X"][fine_state[history]] for history in histories
    }
    assert fine_x_records == {"plus": "plus", "minus": "minus"}

    current_record_selects_unique_theory = coarse_current_records != fine_current_records
    assert not current_record_selects_unique_theory

    result = {
        "schema": "marici.aspect.current-constructors-do-not-determine-ontology.v1",
        "status": "pass",
        "histories": list(histories),
        "admitted_constructor": "Z",
        "coarse_current_records": coarse_current_records,
        "fine_current_records": fine_current_records,
        "current_records_identical_across_theories": coarse_current_records == fine_current_records,
        "coarse_state_space_cardinality": len(set(coarse_state.values())),
        "fine_state_space_cardinality": len(set(fine_state.values())),
        "coarse_histories_ontically_identical": coarse_ontically_identical,
        "fine_histories_ontically_identical": fine_ontically_identical,
        "coarse_histories_nomologically_equivalent": coarse_nomologically_equivalent,
        "fine_histories_nomologically_equivalent": fine_nomologically_equivalent,
        "fine_X_constructor_records": fine_x_records,
        "current_record_selects_unique_theory": current_record_selects_unique_theory,
        "verdict": "Coarse and fine theories predict the same complete Z-record table while disagreeing on state-space cardinality, ontic identity, nomological equivalence, and the possible X intervention. Current constructor equivalence cannot bootstrap the maximal constructor set or ontology; states, laws, and possibilities must be conjectured and tested jointly.",
        "claim_boundary": "finite two-history observational underdetermination under one restricted constructor table; does not imply global equivalence or equal explanatory quality of all theories",
    }
    output = Path(__file__).parents[1] / "results" / "current_constructors_do_not_determine_ontology.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
