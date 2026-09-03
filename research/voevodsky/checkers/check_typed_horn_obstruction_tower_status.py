from __future__ import annotations

import json
from pathlib import Path


TOWER = Path("research/voevodsky/horn-filling-obstruction-tower-v1.json")
MARKOV = Path("research/voevodsky/results/five_sort_markov_analytic_section.json")
EDGE = Path("research/voevodsky/results/sector_overlap_edge_contract.json")
CENSUS = Path("research/voevodsky/results/cross_sector_bridge_admission_v2.json")


def main() -> None:
    tower = json.loads(TOWER.read_text(encoding="utf-8"))
    markov = json.loads(MARKOV.read_text(encoding="utf-8"))
    edge = json.loads(EDGE.read_text(encoding="utf-8"))
    census = json.loads(CENSUS.read_text(encoding="utf-8"))
    assert all(document["passed"] is True for document in [markov, edge, census])
    levels = tower["level_semantics"]
    assert [level["dimension"] for level in levels] == list(range(5))
    assert (markov["object_sort_count"], markov["cell_class_count"], markov["law_class_count"]) == (5, 6, 5)
    internal = tower["markov_internal_tower"]
    assert [internal[f"dimension_{n}"] for n in range(5)] == ["realized", "realized", "filled", "filled", "filled_for_declared_laws"]
    cross = tower["cross_sector_tower"]
    assert census["admitted_sector_vertices"] == 1 and edge["admitted_edges"] == 0
    assert cross["first_obstruction_dimension"] == 1 and cross["dimension_1"] == "boundary_incomplete"
    assert all(cross[f"dimension_{n}"].startswith("undefined") for n in (2, 3, 4))
    assert tower["mixed_tower"]["status"] == "undefined"
    result = {
        "schema": "marici.voevodsky.typed-horn-obstruction-tower-status.v1",
        "status": "typed_obstruction_tower_verified",
        "tower_levels_checked": len(levels),
        "markov_internal_highest_filled_dimension": 4,
        "markov_scope_limited_to_declared_laws": True,
        "cross_sector_admitted_vertices": 1,
        "cross_sector_first_obstruction_dimension": 1,
        "cross_sector_higher_obstructions_defined": False,
        "mixed_horns_defined": False,
        "undefined_not_coerced_to_zero_or_failure": True,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
