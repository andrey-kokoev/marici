#!/usr/bin/env python3
"""Phase-native resource compression for exact D(S3) Wilson gates."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
SOURCE = K / "results" / "s3-wilson-phase-polynomial-resources.json"
BASELINE = K / "results" / "s3-wilson-nonlinear-clifford-t-escape.json"
OUT = K / "results" / "s3-wilson-phase-native-compression.json"


def monomial_cost(degree: int, coefficient: int) -> tuple[int, int, str]:
    """Return conservative (T count, clean ancillas, constructor)."""
    coefficient %= 8
    assert coefficient in {2, 4, 6}, "Wilson quarter exponents must be even"
    if degree == 1:
        return 0, 0, "single-qubit diagonal Clifford"
    if coefficient in {2, 6}:
        # Compute conjunction of the first d-1 variables, use the exact 3T
        # CS/CS-dagger gadget with the last variable, then uncompute.
        ladder = max(0, degree - 2)
        return 14 * ladder + 3, ladder, "conjunction ladder + 3T CS phase + uncompute"
    if degree == 2:
        return 0, 0, "CZ Clifford"
    # CCZ costs 7T; higher controlled-Z gates compute d-3 controls into
    # reusable work bits, apply CCZ, and uncompute.
    ladder = degree - 3
    return 14 * ladder + 7, ladder, "conjunction ladder + 7T CCZ phase + uncompute"


def compress(record: dict, parity_record: dict | None) -> dict:
    terms = []
    nonlinear_total = 0
    max_ancillas = 0
    for mask_text, coefficient in sorted(
        record["divisibility_audit"]["multilinear_coefficients_mod8"].items(),
        key=lambda item: int(item[0]),
    ):
        if not coefficient % 8:
            continue
        mask = int(mask_text)
        degree = mask.bit_count()
        t_count, ancillas, constructor = monomial_cost(degree, coefficient)
        nonlinear_total += t_count
        max_ancillas = max(max_ancillas, ancillas)
        terms.append({
            "mask": mask,
            "degree": degree,
            "coefficient_mod8": coefficient,
            "T_count_upper_bound": t_count,
            "clean_ancillas": ancillas,
            "constructor": constructor,
        })
    candidates = [{"name": "phase-native nonlinear compiler", "T_count": nonlinear_total}]
    if parity_record is not None and parity_record["realizable"]:
        candidates.append({"name": "optimal ancilla-free parity compiler",
                           "T_count": parity_record["minimum_T_count"]})
    selected = min(candidates, key=lambda item: item["T_count"])
    return {
        "terms": terms,
        "candidate_compilers": candidates,
        "selected_upper_bound": selected,
        "maximum_reusable_clean_ancillas": 0 if selected["name"].startswith("optimal") else max_ancillas,
        "optimality_claimed": selected["name"].startswith("optimal"),
    }


def main() -> None:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    logical = {
        label: compress(record, record)
        for label, record in source["logical_quarter_evolutions"].items()
    }
    controlled = {
        label: compress(record, None)
        for label, record in source["controlled_quarter_evolutions"].items()
    }
    old_logical = max(item["T_count_upper_bound_using_exact_7T_Toffoli"]
                      for item in baseline["logical_quarter_evolutions"].values())
    old_controlled = max(item["T_count_upper_bound_using_exact_7T_Toffoli"]
                         for item in baseline["controlled_quarter_evolutions"].values())
    new_logical = max(item["selected_upper_bound"]["T_count"] for item in logical.values())
    new_controlled = max(item["selected_upper_bound"]["T_count"] for item in controlled.values())
    assert old_logical == 70 and old_controlled == 154
    assert new_logical < old_logical and new_controlled < old_controlled
    assert logical["D"]["selected_upper_bound"]["T_count"] == 4
    assert logical["E"]["selected_upper_bound"]["T_count"] == 4
    result = {
        "schema": "marici.kitaev.s3-wilson-phase-native-compression.v1",
        "inputs_sha256": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (SOURCE, BASELINE)
        },
        "library": {
            "CS_or_inverse_T_count": 3,
            "CCZ_T_count": 7,
            "Toffoli_compute_uncompute_pair_T_count": 14,
            "all_counts_are_exact_for_components": True,
        },
        "logical": logical,
        "controlled": controlled,
        "worst_case_compression": {
            "logical_before": old_logical,
            "logical_after": new_logical,
            "controlled_before": old_controlled,
            "controlled_after": new_controlled,
        },
        "verdict": "Phase-native CS and CCZ gadgets sharply reduce the conservative exact Clifford+T upper bounds while preserving the same source and clean-ancilla assumptions. These are compiler upper bounds, not physical costs or global optima.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
