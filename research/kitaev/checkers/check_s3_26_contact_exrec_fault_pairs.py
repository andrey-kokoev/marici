#!/usr/bin/env python3
"""Enumerate macro single faults and fault pairs in the 26-contact schedule."""

from __future__ import annotations

import itertools
import json
from collections import Counter
from pathlib import Path


CONTACTS = (
    [(f"holonomy_compute_{i}", (f"d{i}", "H")) for i in range(4)]
    + [
        ("relative_forward_1", ("d0", "R")),
        ("relative_forward_2", ("d1", "R")),
        ("relative_forward_3", ("d0", "R")),
        ("transporter_align", ("d0", "H")),
    ]
    + [(f"fourier_forward_{i}", ("d0", "H")) for i in range(4)]
    + [
        ("flux_label_copy", ("H", "L")),
        ("charge_label_copy", ("d0", "L")),
    ]
    + [(f"fourier_reverse_{i}", ("d0", "H")) for i in range(4)]
    + [
        ("transporter_unalign", ("d0", "H")),
        ("relative_reverse_1", ("d0", "R")),
        ("relative_reverse_2", ("d1", "R")),
        ("relative_reverse_3", ("d0", "R")),
    ]
    + [(f"holonomy_uncompute_{i}", (f"d{i}", "H")) for i in reversed(range(4))]
)


def fault_classes():
    classes = []
    for index, (name, blocks) in enumerate(CONTACTS):
        classes.append((f"C{index}:{name}", "contact", index, None))
        for block in blocks:
            classes.append((f"R{index}:{block}", "recovery", index, block))
    return classes


def simulate(selected):
    multiplicities = Counter(selected)
    errors = Counter()
    malignant = False
    first_failure = None
    for index, (name, blocks) in enumerate(CONTACTS):
        contact_key = f"C{index}:{name}"
        contact_faults = multiplicities[contact_key]
        if contact_faults:
            for block in blocks:
                errors[block] += contact_faults
                if errors[block] >= 2 and not malignant:
                    malignant = True
                    first_failure = {"step": index, "block": block, "stage": "contact"}
        for block in blocks:
            recovery_key = f"R{index}:{block}"
            recovery_faults = multiplicities[recovery_key]
            if recovery_faults:
                errors[block] += recovery_faults
                if errors[block] >= 2 and not malignant:
                    malignant = True
                    first_failure = {"step": index, "block": block, "stage": "recovery"}
            else:
                # An ideal distance-three recovery clears zero or one rail
                # error, but cannot repair two; the latter was marked above.
                if errors[block] <= 1:
                    errors[block] = 0
        errors += Counter()  # remove zero/negative entries
    return malignant, first_failure, dict(errors)


def main():
    assert len(CONTACTS) == 26
    classes = fault_classes()
    assert len(classes) == 78

    singles = []
    for fault in classes:
        malignant, first_failure, residual = simulate((fault[0],))
        assert not malignant
        assert all(count <= 1 for count in residual.values())
        singles.append({"fault": fault[0], "residual": residual})

    pair_rows = []
    malignant_by_stage = Counter()
    for left_index, right_index in itertools.combinations_with_replacement(range(len(classes)), 2):
        left = classes[left_index][0]
        right = classes[right_index][0]
        malignant, first_failure, residual = simulate((left, right))
        if malignant:
            malignant_by_stage[first_failure["stage"]] += 1
        pair_rows.append(
            {
                "left": left,
                "right": right,
                "malignant": malignant,
                "first_failure": first_failure,
                "residual": residual,
            }
        )
    malignant_count = sum(row["malignant"] for row in pair_rows)
    assert len(pair_rows) == 78 * 79 // 2
    assert malignant_count > 0

    result = {
        "schema": "marici.kitaev.s3-26-contact-exrec-fault-pairs.v1",
        "contact_schedule": [
            {"index": i, "name": name, "incident_blocks": list(blocks)}
            for i, (name, blocks) in enumerate(CONTACTS)
        ],
        "macro_fault_classes": len(classes),
        "single_faults": {
            "enumerated": len(singles),
            "malignant": 0,
            "maximum_residual_errors_per_block": 1,
            "rows": singles,
        },
        "fault_pairs": {
            "enumerated_with_repeated_class": len(pair_rows),
            "malignant": malignant_count,
            "benign": len(pair_rows) - malignant_count,
            "malignant_by_first_failure_stage": dict(sorted(malignant_by_stage.items())),
            "rows": pair_rows,
        },
        "model": {
            "contact_fault": "adds one rail error to each incident encoded block",
            "recovery_fault": "conservatively fails to clear its input and adds one rail error to that block",
            "ideal_recovery": "clears zero or one rail error and flags two as uncorrectable by distance three",
            "repeated_macro_class": "represents two distinct microscopic faults inside the same contact or recovery module",
        },
        "scope_boundary": "This is exhaustive for the 78 declared contact/recovery macro fault classes. It is not a microscopic malignant-pair count inside Choi-state verification or the absent nonstabilizer factories.",
        "verdict": "All 78 macro single faults are contained to one residual rail error per encoded block. The complete 3081 macro-pair table identifies exactly where distance-three recovery can be exceeded; a physical threshold coefficient still requires microscopic gate layouts for resource-state factories.",
    }
    output = Path(__file__).parents[1] / "results" / "s3-26-contact-exrec-fault-pairs.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k not in {"single_faults", "fault_pairs"}}, indent=2, sort_keys=True))
    print(json.dumps({"single_faults": len(singles), "pairs": len(pair_rows), "malignant_pairs": malignant_count}, sort_keys=True))


if __name__ == "__main__":
    main()
