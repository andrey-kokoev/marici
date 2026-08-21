"""Verify the closed weight-two GPL formulas against their defining integrals."""

import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_exact_qed_bell_onset import g2, g2_quadrature, solve_wz


mp.mp.dps = 35

if __name__ == "__main__":
    y, x = mp.mpf("0.42"), mp.mpf("0.3")
    triples = (
        (y, -y * x),
        (-y * x, -y * (1 - x)),
        (-y * (1 - x), y),
    )
    letters = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    rows = []
    for region, (xi, xj) in enumerate(triples, 1):
        w, z = solve_wz(xi, xj)
        for endpoint_name, endpoint in (("w", w), ("z", z)):
            for a, b in letters:
                error = abs(g2(a, b, endpoint) - g2_quadrature(a, b, endpoint))
                rows.append(
                    {
                        "region": region,
                        "endpoint": endpoint_name,
                        "a": a,
                        "b": b,
                        "absolute_error": str(error),
                    }
                )
    max_error = max(mp.mpf(row["absolute_error"]) for row in rows)
    worst = sorted(rows, key=lambda row: mp.mpf(row["absolute_error"]), reverse=True)[:5]
    print(json.dumps({"comparisons": len(rows), "max_error": str(max_error), "worst": worst}))
    assert max_error < mp.mpf("1e-30")
    payload = {
        "schema": "marici.exact-qed-weight-two-polylog-reduction.v1",
        "comparison_count": len(rows),
        "maximum_absolute_error": str(max_error),
        "verdict": "The closed dilogarithmic formulas reproduce the defining GPL quadratures in all three physical regions.",
        "scope": "Numerical branch-equivalence gate at one generic below-threshold kinematic point.",
        "rows": rows,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
    out = Path(__file__).parent / "results" / "exact-qed-polylog-reduction.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
