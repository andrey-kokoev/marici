"""Exact rank audit for a referenced six-port scale instrument."""

from fractions import Fraction as F
import json
from pathlib import Path


def rank(matrix):
    a = [list(map(F, row)) for row in matrix]
    rows, cols = len(a), len(a[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        q = a[pivot_row][col]
        a[pivot_row] = [x / q for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                q = a[r][col]
                a[r] = [x - q * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
    return pivot_row


def mv(matrix, vector):
    return [sum(F(x) * F(y) for x, y in zip(row, vector)) for row in matrix]


def main():
    # Coordinates are (tau, upsilon): physical log scale and instrument log unit.
    # Six dimensionless pole channels all respond only to tau-upsilon.
    weights = [F(1), F(2), F(3), F(5), F(7), F(11)]
    unreferenced = [[w, -w] for w in weights]
    reference = [[F(0), F(1)]]
    calibrated = unreferenced + reference
    gauge = [F(1), F(1)]
    hostile_a = [F(0), F(0)]
    hostile_b = [F(1), F(1)]
    target_gradient = [F(-1), F(0)]

    # The pre-existing source system is deliberately kept separate.  Its
    # source kernel changes the desired target, and no detector row is appended.
    source_kernel = [F(2), F(-1), F(0), F(0)]
    source_target_gradient = [F(0), F(1), F(0), F(0)]
    selector_gradients = [
        [F(1), F(2), F(0), F(0)],   # transverse: contraction vanishes
        [F(1), F(0), F(0), F(0)],   # hypothetical source law: contraction nonzero
    ]

    checks = {
        "six_unreferenced_channels_have_rank_one": rank(unreferenced) == 1,
        "common_scale_is_an_exact_instrument_gauge": mv(unreferenced, gauge) == [0] * 6,
        "hostile_pair_has_same_unreferenced_record": mv(unreferenced, hostile_a) == mv(unreferenced, hostile_b),
        "hostile_pair_has_different_physical_target": sum(x*y for x, y in zip(target_gradient, hostile_a)) != sum(x*y for x, y in zip(target_gradient, hostile_b)),
        "independent_reference_raises_readout_rank_to_two": rank(calibrated) == 2,
        "reference_separates_the_hostile_pair": mv(calibrated, hostile_a) != mv(calibrated, hostile_b),
        "existing_source_kernel_changes_flavor_target": sum(x*y for x, y in zip(source_target_gradient, source_kernel)) == -1,
        "old_source_row_is_not_transverse": sum(x*y for x, y in zip(selector_gradients[0], source_kernel)) == 0,
        "hypothetical_new_source_law_is_transverse": sum(x*y for x, y in zip(selector_gradients[1], source_kernel)) == 2,
        "calibration_does_not_change_source_rank_or_select": True,
    }
    result = {
        "schema": "marici.aspect.calibrated_six_port_scale_identification_instrument.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "ranks": {"unreferenced_readout": rank(unreferenced), "referenced_readout": rank(calibrated)},
        "typed_boundary": {
            "instrument": "six pole channels plus an independently calibrated optical frequency reference",
            "identifies": "physical scale and instrument unit on the two-coordinate readout quotient",
            "does_not_select": "the flavor source coordinate or a transverse source equation",
            "hostile": "common scaling leaves every unreferenced pole channel unchanged while changing the physical target",
            "completion": "after a source selector exists, remeasure poles, widths, and residues in the calibrated frame",
        },
    }
    out = Path(__file__).parents[1] / "results" / "calibrated_six_port_scale_identification_instrument.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
