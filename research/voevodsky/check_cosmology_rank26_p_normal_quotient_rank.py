"""First quotient-rank test for the rank-26 p-normal raw derivatives.

This streams the p-normal special rows and raw derivative rows into the same
sparse pivot reducer used by the rank-26 source code.  It tests whether nx and
ny derivatives produce a normal-choice-independent class after quotienting by
the special exact image plus the p-tangent derived span.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
sys.path.insert(0, str(ROOT / "research" / "voevodsky"))

import physical_four_mark_residue_twisted_derham as base  # noqa: E402
import check_rank26_total_energy_triple_relation_module as rees  # noqa: E402
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter  # noqa: E402

VOE_RESULTS = ROOT / "research" / "voevodsky" / "results"
OUT = VOE_RESULTS / "cosmology_rank26_p_normal_quotient_rank.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def pivot_rank(rows: list[dict[int, int]]) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for row in rows:
        base.add_pivot(dict(row), pivots)
    return len(pivots)


def extension_profile(base_rows: list[dict[int, int]], test_rows: list[dict[int, int]]) -> dict[str, int]:
    pivots: dict[int, dict[int, int]] = {}
    for row in base_rows:
        base.add_pivot(dict(row), pivots)
    start = len(pivots)
    added = 0
    nonzero_tests = 0
    for row in test_rows:
        if row:
            nonzero_tests += 1
        before = len(pivots)
        base.add_pivot(dict(row), pivots)
        if len(pivots) > before:
            added += 1
    return {
        "base_rank": start,
        "test_rows": len(test_rows),
        "nonzero_test_rows": nonzero_tests,
        "rank_after": len(pivots),
        "extension_rank": len(pivots) - start,
        "independent_test_rows": added,
    }


def main() -> None:
    raw = load(VOE_RESULTS / "cosmology_rank26_p_normal_raw_relation_adapter.json")
    protocol = load(VOE_RESULTS / "cosmology_rank26_p_normal_protocol_gate.json")
    assert raw["passed"] is True
    assert protocol["passed"] is True

    point = tuple(protocol["test_point_xyz"])
    nx = tuple(protocol["integral_unit_normals"]["nx"])
    ny = tuple(protocol["integral_unit_normals"]["ny"])
    tangent = tuple(protocol["integral_unit_normals"]["p_tangent_difference"])
    _, columns = rees.column_packet()

    special_rows = list(rees.raw_relations(point, columns))
    nx_derivatives, nx_checked = adapter.derivative_rows(columns, point, nx)
    ny_derivatives, ny_checked = adapter.derivative_rows(columns, point, ny)
    tangent_derivatives, tangent_checked = adapter.derivative_rows(columns, point, tangent)
    assert nx_checked == ny_checked == tangent_checked == len(special_rows)
    if rees.AMBIENT == raw["ambient_relation_degree"] and base.PRIME == raw["field"]:
        assert len(special_rows) == raw["special_relation_rows"]["row_count"]

    special_rank = pivot_rank(special_rows)
    tangent_base_rows = special_rows + tangent_derivatives
    tangent_base_rank = pivot_rank(tangent_base_rows)
    special_plus_nx_rank = pivot_rank(special_rows + nx_derivatives)
    special_plus_ny_rank = pivot_rank(special_rows + ny_derivatives)
    tangent_plus_nx_rank = pivot_rank(tangent_base_rows + nx_derivatives)
    tangent_plus_ny_rank = pivot_rank(tangent_base_rows + ny_derivatives)
    tangent_plus_both_rank = pivot_rank(tangent_base_rows + nx_derivatives + ny_derivatives)

    tangent_extension = tangent_base_rank - special_rank
    nx_extension_after_tangent = tangent_plus_nx_rank - tangent_base_rank
    ny_extension_after_tangent = tangent_plus_ny_rank - tangent_base_rank
    both_extension_after_tangent = tangent_plus_both_rank - tangent_base_rank
    normal_choice_independent = (
        nx_extension_after_tangent == ny_extension_after_tangent == both_extension_after_tangent
    )
    no_surviving_line = both_extension_after_tangent == 0

    # In this finite-cutoff p=0 test the p-tangent quotient already absorbs both
    # integral unit normal derivative images.  Therefore this gate closes the
    # ambient-degree-8/F_32003 attempt; it does not prove a global no-go.
    assert normal_choice_independent is True
    assert no_surviving_line is True

    result = {
        "schema": "marici.voevodsky.cosmology-rank26-p-normal-quotient-rank.v1",
        "status": f"degree{rees.AMBIENT}_prime{base.PRIME}_p_tangent_quotient_absorbs_raw_p_normal_derivatives",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_rank26_p_normal_raw_relation_adapter.json",
            "research/voevodsky/results/cosmology_rank26_p_normal_protocol_gate.json",
            "research/benincasa/check_rank26_total_energy_triple_relation_module.py",
        ],
        "field": base.PRIME,
        "ambient_relation_degree": rees.AMBIENT,
        "column_count": len(columns),
        "point": list(point),
        "directions": {"nx": list(nx), "ny": list(ny), "p_tangent": list(tangent)},
        "row_counts": {
            "special": len(special_rows),
            "nx_derivative": len(nx_derivatives),
            "ny_derivative": len(ny_derivatives),
            "p_tangent_derivative": len(tangent_derivatives),
        },
        "ranks": {
            "special_exact_image": special_rank,
            "special_plus_p_tangent_derivatives": tangent_base_rank,
            "special_plus_nx_derivatives": special_plus_nx_rank,
            "special_plus_ny_derivatives": special_plus_ny_rank,
            "special_plus_p_tangent_plus_nx": tangent_plus_nx_rank,
            "special_plus_p_tangent_plus_ny": tangent_plus_ny_rank,
            "special_plus_p_tangent_plus_nx_plus_ny": tangent_plus_both_rank,
        },
        "extension_ranks": {
            "p_tangent_over_special": tangent_extension,
            "nx_over_special_plus_p_tangent": nx_extension_after_tangent,
            "ny_over_special_plus_p_tangent": ny_extension_after_tangent,
            "nx_and_ny_over_special_plus_p_tangent": both_extension_after_tangent,
        },
        "normal_choice_independent_mod_p_tangent": normal_choice_independent,
        "surviving_normal_line_at_this_cutoff": not no_surviving_line,
        "interpretation": f"At ambient degree {rees.AMBIENT} over F_{base.PRIME}, the p-tangent derived span plus the special exact image contains the raw nx and ny derivative images; no quotient line remains to map to the tau_p horn.",
        "limitations": [
            "single prime only",
            f"ambient relation degree {rees.AMBIENT} only",
            "uses raw labelled relation rows, not a completed two-prime unbounded theorem",
            "does not test all higher ambient degrees",
            "does not construct a horn comparison map",
        ],
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
