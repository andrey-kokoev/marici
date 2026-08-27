"""Exact scalar models for residual-generated equalizer and coequalizer."""
import json
import math
from pathlib import Path


integer_models = []
for d in (0, 1, 2, 7, 14):
    integer_models.append(
        {
            "residual": d,
            "kernel": "Z" if d == 0 else "0",
            "cokernel": "Z" if d == 0 else ("0" if abs(d) == 1 else f"Z/{abs(d)}"),
        }
    )

p = 7
field_models = []
for f in range(p):
    for g in range(p):
        d = (f - g) % p
        kernel = [x for x in range(p) if d * x % p == 0]
        image = {d * x % p for x in range(p)}
        field_models.append(
            {
                "f": f,
                "g": g,
                "residual": d,
                "kernel_size": len(kernel),
                "cokernel_size": p // len(image),
            }
        )

tests = {
    "magnetic_degree_seven_has_cokernel_only": next(
        row for row in integer_models if row["residual"] == 7
    )
    == {"residual": 7, "kernel": "0", "cokernel": "Z/7"},
    "zero_residual_retains_both_sides": next(
        row for row in integer_models if row["residual"] == 0
    )
    == {"residual": 0, "kernel": "Z", "cokernel": "Z"},
    "f7_nonzero_residual_is_isomorphism": all(
        (row["residual"] == 0)
        or (row["kernel_size"] == 1 and row["cokernel_size"] == 1)
        for row in field_models
    ),
    "f7_zero_residual_has_full_kernel_and_cokernel": all(
        row["kernel_size"] == 7 and row["cokernel_size"] == 7
        for row in field_models
        if row["residual"] == 0
    ),
    "id_minus_negation_is_two_and_exact": next(
        row for row in field_models if row["f"] == 1 and row["g"] == 6
    )["residual"]
    == 2,
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "deutschian_residual_kernel_cokernel_checks.py",
    "passed": all(tests.values()),
    "tests": tests,
    "integer_models": integer_models,
    "verdict": "in additive sectors the two closure variances are kernel and cokernel of one residual",
    "scope_boundary": "no canonical residual is implied outside additive enrichment",
}

out = Path(__file__).resolve().parents[1] / "results" / "deutschian_residual_kernel_cokernel_checks.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
