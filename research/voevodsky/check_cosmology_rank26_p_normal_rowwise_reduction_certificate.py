"""Rowwise reduction certificate for p-normal derivatives modulo S+T at degree 14."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
sys.path.insert(0, str(ROOT / "research" / "voevodsky"))

import physical_four_mark_residue_twisted_derham as base  # noqa: E402
import check_rank26_total_energy_triple_relation_module as rees  # noqa: E402
import check_cosmology_rank26_p_normal_raw_relation_adapter as adapter  # noqa: E402

RES = ROOT / "research" / "voevodsky" / "results"
OUT = RES / f"cosmology_rank26_p_normal_rowwise_reduction_certificate_p{base.PRIME}.json"


def load(name: str) -> dict:
    return json.loads((RES / name).read_text(encoding="utf-8"))


def reduce_row(row: dict[int, int], pivots: dict[int, dict[int, int]]) -> dict[int, int]:
    row = dict(row)
    while row:
        pivot = max(row)
        coefficient = row[pivot]
        existing = pivots.get(pivot)
        if existing is None:
            return row
        for column, value in existing.items():
            base.add_value(row, column, -coefficient * value)
    return row


def pivot_digest(pivots: dict[int, dict[int, int]]) -> str:
    digest = hashlib.sha256()
    for pivot in sorted(pivots):
        digest.update(f"P{pivot}:".encode())
        for column, value in sorted(pivots[pivot].items()):
            digest.update(f"{column}={value};".encode())
    return digest.hexdigest()


def main() -> None:
    protocol = load("cosmology_rank26_p_normal_protocol_gate.json")
    anti = load("cosmology_rank26_p_normal_absorption_not_tautological.json")
    assert protocol["passed"] and anti["passed"]
    assert rees.AMBIENT == 14

    point = tuple(protocol["test_point_xyz"])
    nx = tuple(protocol["integral_unit_normals"]["nx"])
    ny = tuple(protocol["integral_unit_normals"]["ny"])
    tangent = tuple(protocol["integral_unit_normals"]["p_tangent_difference"])
    _, columns = rees.column_packet()
    special = list(rees.raw_relations(point, columns))
    dx, cx = adapter.derivative_rows(columns, point, nx)
    dy, cy = adapter.derivative_rows(columns, point, ny)
    dt, ct = adapter.derivative_rows(columns, point, tangent)
    assert cx == cy == ct == len(special)

    pivots: dict[int, dict[int, int]] = {}
    for row in special:
        base.add_pivot(dict(row), pivots)
    special_rank = len(pivots)
    for row in dt:
        base.add_pivot(dict(row), pivots)
    base_rank = len(pivots)
    assert base_rank - special_rank == 113

    family_results = {}
    for name, rows in (("nx", dx), ("ny", dy)):
        nonzero_input = 0
        zero_residue = 0
        nonzero_residue = 0
        residue_support = 0
        residue_hash = hashlib.sha256()
        for index, row in enumerate(rows):
            if row:
                nonzero_input += 1
            residue = reduce_row(row, pivots)
            if residue:
                nonzero_residue += 1
                residue_support += len(residue)
                residue_hash.update(f"{index}:{sorted(residue.items())}".encode())
            else:
                zero_residue += 1
        assert nonzero_residue == 0 and zero_residue == len(rows)
        family_results[name] = {
            "rows": len(rows),
            "nonzero_input_rows": nonzero_input,
            "zero_remainders": zero_residue,
            "nonzero_remainders": nonzero_residue,
            "total_nonzero_remainder_support": residue_support,
            "nonzero_remainder_sha256": residue_hash.hexdigest(),
        }

    result = {
        "schema": "marici.voevodsky.cosmology-rank26-p-normal-rowwise-reduction-certificate.v1",
        "status": "every_degree14_p_normal_derivative_row_reduces_to_zero_mod_S_plus_T",
        "field": base.PRIME,
        "ambient_relation_degree": rees.AMBIENT,
        "point": list(point),
        "column_count": len(columns),
        "special_row_count": len(special),
        "special_rank": special_rank,
        "S_plus_T_rank": base_rank,
        "T_over_S_rank": base_rank - special_rank,
        "normalized_S_plus_T_pivot_sha256": pivot_digest(pivots),
        "rowwise_reduction": family_results,
        "certificate_meaning": "Each original nx and ny derivative row, without adjoining any normal row as a new pivot, has zero remainder against the fixed normalized S+T pivot basis.",
        "stronger_than_extension_rank_summary": True,
        "limitations": ["degree 14 finite cutoff", "one field per result file", "coefficients of reductions are not retained", "no uniform ambient-degree chain homotopy"],
        "relative_bockstein_constructed": False,
        "physical_period_constructed": False,
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
