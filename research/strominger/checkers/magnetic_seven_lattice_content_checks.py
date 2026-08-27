"""Exact checks locating the magnetic factor seven in affine lattice content."""
import json
import math
from pathlib import Path


rows = []
for g in range(2, 101):
    x, y = 2 * g + 7, 3 * g + 7
    content = math.gcd(x, y)
    expected = math.gcd(g, 7)
    rows.append(
        {
            "g": g,
            "coefficients": [x, -y],
            "content": content,
            "expected": expected,
            "primitive": [x // content, -y // content],
        }
    )

tests = {
    "content_identity_g_2_through_100": all(r["content"] == r["expected"] for r in rows),
    "unimodular_combination_recovers_g": all(
        (3 * g + 7) - (2 * g + 7) == g for g in range(2, 101)
    ),
    "affine_frame_determinant_is_minus_seven": 2 * 7 - 3 * 7 == -7,
    "seven_content_exactly_at_multiples_of_seven": all(
        (r["content"] == 7) == (r["g"] % 7 == 0) for r in rows
    ),
    "primitive_vector_has_unit_content": all(
        math.gcd(abs(r["primitive"][0]), abs(r["primitive"][1])) == 1 for r in rows
    ),
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_seven_lattice_content_checks.py",
    "passed": all(tests.values()),
    "tests": tests,
    "sample_multiples_of_seven": [r for r in rows if r["g"] % 7 == 0][:5],
    "verdict": "seven is affine cocircuit content, not bare C2 coherence",
}

out = Path(__file__).resolve().parents[1] / "results" / "magnetic_seven_lattice_content_checks.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
