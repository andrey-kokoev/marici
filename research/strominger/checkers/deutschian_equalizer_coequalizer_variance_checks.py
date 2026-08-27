"""Exact F7 comparison of equalizer restriction and coequalizer collapse."""
import json
from pathlib import Path


p = 7
C = list(range(p))
f = {x: x for x in C}
g = {x: (-x) % p for x in C}
equalizer = [x for x in C if f[x] == g[x]]
residual_image = sorted({(f[x] - g[x]) % p for x in C})
coequalizer_size = p // len(residual_image)

tests = {
    "both_parallel_routes_faithful": len(set(f.values())) == p and len(set(g.values())) == p,
    "equalizer_is_zero_subobject": equalizer == [0],
    "equalizer_inclusion_is_monic": len(set(equalizer)) == len(equalizer),
    "route_residual_is_surjective": residual_image == C,
    "coequalizer_is_zero_object": coequalizer_size == 1,
    "variance_changes_disposition": len(equalizer) == 1 and coequalizer_size == 1,
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "deutschian_equalizer_coequalizer_variance_checks.py",
    "passed": all(tests.values()),
    "tests": tests,
    "equalizer_elements": equalizer,
    "residual_image": residual_image,
    "coequalizer_cardinality": coequalizer_size,
    "verdict": "equalizer restricts source states while coequalizer collapses records",
}

out = Path(__file__).resolve().parents[1] / "results" / "deutschian_equalizer_coequalizer_variance_checks.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
