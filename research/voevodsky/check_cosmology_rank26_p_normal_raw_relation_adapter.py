"""Raw-relation adapter for the rank-26 p-normal protocol.

This is not the Bockstein computation.  It verifies that the existing complete
labelled Laurent relation generator can be evaluated at the p-normal point and
sampled in the two integral p-normal directions nx,ny.  It also verifies the
finite-difference interpolation contract and tangent identity d_nx-d_ny=d_(nx-ny)
for raw relation rows before quotient reduction.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))

import check_rank26_total_energy_triple_relation_module as rees  # noqa: E402

VOE_RESULTS = ROOT / "research" / "voevodsky" / "results"
OUT = VOE_RESULTS / "cosmology_rank26_p_normal_raw_relation_adapter.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def point_add(point: tuple[int, int, int], direction: tuple[int, int, int], scale: int) -> tuple[int, int, int]:
    return tuple(a + scale * b for a, b in zip(point, direction, strict=True))  # type: ignore[return-value]


def row_sub(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    return rees.combine((left, right), (1, -1))


def row_support_stats(rows: list[dict[int, int]]) -> dict[str, int]:
    sizes = [len(row) for row in rows]
    return {
        "row_count": len(rows),
        "nonzero_rows": sum(1 for size in sizes if size),
        "min_support": min(sizes),
        "max_support": max(sizes),
        "total_support": sum(sizes),
    }


def sampled_rows(columns: dict, point: tuple[int, int, int], direction: tuple[int, int, int]) -> list[list[dict[int, int]]]:
    return [
        list(rees.raw_relations(point_add(point, direction, offset), columns))
        for offset in rees.OFFSETS
    ]


def derivative_rows(columns: dict, point: tuple[int, int, int], direction: tuple[int, int, int]) -> tuple[list[dict[int, int]], int]:
    samples = sampled_rows(columns, point, direction)
    counts = {len(rows) for rows in samples}
    assert len(counts) == 1
    check_rows = list(rees.raw_relations(point_add(point, direction, rees.CHECK_OFFSET), columns))
    assert len(check_rows) == next(iter(counts))
    first_weights = rees.interpolation_weights(1)
    check_weights = rees.evaluation_weights(rees.CHECK_OFFSET)
    derivatives = []
    checked = 0
    for rows_at_offsets, check in zip(zip(*samples, strict=True), check_rows, strict=True):
        predicted_check = rees.combine(rows_at_offsets, check_weights)
        assert row_sub(predicted_check, check) == {}
        derivatives.append(rees.combine(rows_at_offsets, first_weights))
        checked += 1
    return derivatives, checked


def main() -> None:
    protocol = load(VOE_RESULTS / "cosmology_rank26_p_normal_protocol_gate.json")
    materialization_gap = load(VOE_RESULTS / "cosmology_rank26_p_normal_materialization_gap.json")
    assert protocol["passed"] is True
    assert materialization_gap["passed"] is True

    p_covector = tuple(protocol["p_normal_covector"])
    point = tuple(protocol["test_point_xyz"])
    nx = tuple(protocol["integral_unit_normals"]["nx"])
    ny = tuple(protocol["integral_unit_normals"]["ny"])
    tangent = tuple(protocol["integral_unit_normals"]["p_tangent_difference"])
    assert sum(a * b for a, b in zip(p_covector, point)) == 0
    assert sum(a * b for a, b in zip(p_covector, nx)) == 1
    assert sum(a * b for a, b in zip(p_covector, ny)) == 1
    assert sum(a * b for a, b in zip(p_covector, tangent)) == 0

    low_labels, columns = rees.column_packet()
    width = len(columns)
    special_rows = list(rees.raw_relations(point, columns))
    nx_derivatives, nx_checked = derivative_rows(columns, point, nx)
    ny_derivatives, ny_checked = derivative_rows(columns, point, ny)
    tangent_derivatives, tangent_checked = derivative_rows(columns, point, tangent)
    assert nx_checked == ny_checked == tangent_checked == len(special_rows)

    tangent_identity_failures = 0
    tangent_nonzero = 0
    for dx, dy, dt in zip(nx_derivatives, ny_derivatives, tangent_derivatives, strict=True):
        diff = row_sub(dx, dy)
        if diff:
            tangent_nonzero += 1
        if row_sub(diff, dt):
            tangent_identity_failures += 1
    assert tangent_identity_failures == 0

    result = {
        "schema": "marici.voevodsky.cosmology-rank26-p-normal-raw-relation-adapter.v1",
        "status": "raw_labelled_relation_rows_adapt_to_p_normal_sampling_before_quotient_reduction",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_rank26_p_normal_protocol_gate.json",
            "research/voevodsky/results/cosmology_rank26_p_normal_materialization_gap.json",
            "research/benincasa/check_rank26_total_energy_triple_relation_module.py",
        ],
        "field": rees.base.PRIME,
        "ambient_relation_degree": rees.AMBIENT,
        "low_cutoff": rees.CUTOFF,
        "column_count": width,
        "low_column_count": len(low_labels),
        "p_normal_point": list(point),
        "p_normal_covector": list(p_covector),
        "directions": {"nx": list(nx), "ny": list(ny), "p_tangent": list(tangent)},
        "special_relation_rows": row_support_stats(special_rows),
        "interpolation_checks": {
            "offsets": list(rees.OFFSETS),
            "check_offset": rees.CHECK_OFFSET,
            "nx_rows_checked": nx_checked,
            "ny_rows_checked": ny_checked,
            "p_tangent_rows_checked": tangent_checked,
            "degree_six_check_passed": True,
        },
        "derivative_support_stats": {
            "nx": row_support_stats(nx_derivatives),
            "ny": row_support_stats(ny_derivatives),
            "p_tangent": row_support_stats(tangent_derivatives),
        },
        "tangent_identity": {
            "identity": "D_nx(row)-D_ny(row)=D_(nx-ny)(row) for every raw labelled relation row",
            "rows_checked": len(special_rows),
            "nonzero_tangent_difference_rows": tangent_nonzero,
            "failures": tangent_identity_failures,
            "passed": True,
        },
        "what_this_does_not_do": [
            "does not compute the quotient by the special exact image",
            "does not compute the quotient by the p-tangent derived-relation span",
            "does not identify a surviving rank-one Bockstein line",
            "does not map any line to the tau_p horn column",
            "does not construct a physical period",
        ],
        "next_gate": "stream nx, ny, and p-tangent derivative rows into a modular quotient-rank engine together with the special exact image",
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
