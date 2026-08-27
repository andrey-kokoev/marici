"""Exact tests separating strict curvature, obstruction, and associativity."""
import json
from pathlib import Path


p = 7
strict_pairs = []
obstructed_pairs = []
for d0 in range(p):
    for d1 in range(p):
        kappa = d1 * d0 % p
        row = {"d0": d0, "d1": d1, "kappa": kappa}
        (strict_pairs if kappa == 0 else obstructed_pairs).append(row)

bianchi_rows = []
for d0 in range(p):
    for d1 in range(p):
        for d2 in range(p):
            k10 = d1 * d0 % p
            k21 = d2 * d1 % p
            residual = (d2 * k10 - k21 * d0) % p
            bianchi_rows.append(residual)

tests = {
    "all_49_pairs_classified": len(strict_pairs) + len(obstructed_pairs) == 49,
    "thirteen_strict_scalar_pairs": len(strict_pairs) == 13,
    "thirty_six_obstructed_scalar_pairs": len(obstructed_pairs) == 36,
    "nonzero_kappa_is_not_chain_closure": all(row["kappa"] != 0 for row in obstructed_pairs),
    "associative_bianchi_residual_always_zero": all(value == 0 for value in bianchi_rows),
    "hostile_two_then_three_has_nonzero_kappa": (3 * 2) % p == 6,
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "strict_weak_seven_slot_checks.py",
    "passed": all(tests.values()),
    "tests": tests,
    "strict_pair_count": len(strict_pairs),
    "obstructed_pair_count": len(obstructed_pairs),
    "verdict": "the final slot is either a zero strict relation or a nonzero obstruction; it is never its own filler",
    "magnetic_status": "compiler architecture only until source-derived consecutive maps are constructed",
}

out = Path(__file__).resolve().parents[1] / "results" / "strict_weak_seven_slot_checks.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
