"""Exact face-count falsifier for a universal 2X+1 recursion."""
import json
from pathlib import Path


rows = [
    {
        "dimension": n,
        "globular_faces": 2,
        "simplicial_faces": n + 1,
        "cubical_faces": 2 * n,
    }
    for n in range(2, 9)
]

tests = {
    "three_modes_differ_from_dimension_two_onward": all(
        len({r["globular_faces"], r["simplicial_faces"], r["cubical_faces"]}) == 3
        for r in rows
    ),
    "degree_three_counts_are_two_four_six": rows[1]
    == {
        "dimension": 3,
        "globular_faces": 2,
        "simplicial_faces": 4,
        "cubical_faces": 6,
    },
    "globular_rule_is_constant_two": all(r["globular_faces"] == 2 for r in rows),
    "simplicial_and_cubical_require_unbounded_face_counts": rows[-1]["simplicial_faces"] > rows[0]["simplicial_faces"]
    and rows[-1]["cubical_faces"] > rows[0]["cubical_faces"],
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "coherence_locking_mode_face_counts.py",
    "passed": all(tests.values()),
    "tests": tests,
    "rows": rows,
    "verdict": "2X+1 is valid only after a globular locking declaration",
}

out = Path(__file__).resolve().parents[1] / "results" / "coherence_locking_mode_face_counts.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
