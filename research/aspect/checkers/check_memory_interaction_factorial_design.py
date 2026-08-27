from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


def recover(table: dict[str, F]) -> dict[str, F]:
    source = table["DE"]
    detector = table["E"] - source
    electronics = table["D"] - source
    interaction = table["none"] - table["E"] - table["D"] + source
    return {
        "source": source,
        "detector": detector,
        "electronics": electronics,
        "interaction": interaction,
    }


def main() -> None:
    source, detector, electronics, interaction = F(1, 8), F(1, 16), F(3, 32), F(1, 32)
    invariant_source_table = {
        "none": source + detector + electronics + interaction,
        "D": source + electronics,
        "E": source + detector,
        "DE": source,
    }
    assert invariant_source_table == {
        "none": F(5, 16), "D": F(7, 32), "E": F(3, 16), "DE": F(1, 8)
    }
    assert recover(invariant_source_table) == {
        "source": source,
        "detector": detector,
        "electronics": electronics,
        "interaction": interaction,
    }

    # Reset-induced source shifts generate a second realization. The four
    # science records alone still admit an invariant-source factorial fit.
    source_monitor = {
        "none": source,
        "D": source + F(1, 64),
        "E": source - F(1, 64),
        "DE": source + F(1, 32),
    }
    shifted_science = {
        "none": source_monitor["none"] + detector + electronics + interaction,
        "D": source_monitor["D"] + electronics,
        "E": source_monitor["E"] + detector,
        "DE": source_monitor["DE"],
    }
    naive_fit = recover(shifted_science)
    assert naive_fit["source"] == F(5, 32)
    assert naive_fit["interaction"] == F(1, 16)
    assert naive_fit != {
        "source": source,
        "detector": detector,
        "electronics": electronics,
        "interaction": interaction,
    }

    # An independent optical source tap is recorded under all four reset
    # conditions. Subtracting it restores the nuisance factorial exactly.
    source_removed = {
        condition: shifted_science[condition] - source_monitor[condition]
        for condition in shifted_science
    }
    assert source_removed == {
        "none": detector + electronics + interaction,
        "D": electronics,
        "E": detector,
        "DE": F(0),
    }
    corrected_interaction = (
        source_removed["none"] - source_removed["E"] - source_removed["D"] + source_removed["DE"]
    )
    assert corrected_interaction == interaction

    result = {
        "schema": "marici.aspect.memory-interaction-factorial-design.v1",
        "status": "pass",
        "reset_conditions": ["none", "detector", "electronics", "detector+electronics"],
        "invariant_source_table": {key: str(value) for key, value in invariant_source_table.items()},
        "recovered_invariant_components": {key: str(value) for key, value in recover(invariant_source_table).items()},
        "interaction_contrast": "C_none-C_E-C_D+C_DE",
        "shifted_source_monitor": {key: str(value) for key, value in source_monitor.items()},
        "shifted_science_table": {key: str(value) for key, value in shifted_science.items()},
        "naive_shifted_fit": {key: str(value) for key, value in naive_fit.items()},
        "science_factorial_alone_separates_source_shift": False,
        "source_tap_corrected_interaction": str(corrected_interaction),
        "verdict": "The four reset combinations identify one detector-electronics interaction only under source invariance; a condition-keyed independent source tap is required to separate reset-induced source shifts.",
        "claim_boundary": "two binary ideal reset actuators, one detector-electronics interaction, additive source-monitor readout; no higher interactions or monitor back-action",
    }
    output = Path(__file__).parents[1] / "results" / "memory_interaction_factorial_design.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
