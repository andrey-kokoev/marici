"""Exact one-loop CW hostile: identical shape, variable attaching degree."""
import json
from pathlib import Path


fixtures = []
for m in (0, 1, 2, 7, 14):
    fixtures.append(
        {
            "degree": m,
            "cell_inventory": {"0_cells": 1, "1_cells": 1, "2_cells": 1},
            "coarse_attachment": "one two-cell fills one loop",
            "boundary_matrix": [m],
            "H1": "Z" if m == 0 else ("0" if abs(m) == 1 else f"Z/{abs(m)}"),
            "torsion_order": None if m == 0 else abs(m),
        }
    )

tests = {
    "all_coarse_shapes_identical": len(
        {
            (tuple(row["cell_inventory"].items()), row["coarse_attachment"])
            for row in fixtures
        }
    )
    == 1,
    "homology_varies_with_degree": len({row["H1"] for row in fixtures}) == len(fixtures),
    "degree_one_has_no_residue": next(row for row in fixtures if row["degree"] == 1)["H1"] == "0",
    "degree_seven_has_seven_residue": next(row for row in fixtures if row["degree"] == 7)["H1"] == "Z/7",
    "degree_fourteen_retains_two_and_seven_content": next(
        row for row in fixtures if row["degree"] == 14
    )["H1"]
    == "Z/14",
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "deutschian_attaching_degree_falsifier.py",
    "passed": all(tests.values()),
    "tests": tests,
    "fixtures": fixtures,
    "verdict": "unweighted attachment shape does not determine the invariant quotient",
    "missing_constructor": "coefficient- and orientation-typed attaching morphism",
}

out = Path(__file__).resolve().parents[1] / "results" / "deutschian_attaching_degree_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
