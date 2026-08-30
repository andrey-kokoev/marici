"""Exact WP634 continuous-phase and sign-cycle incidence audit."""
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
fields = ("Q", "Hu", "Hd", "sigma", "AuL", "AuR", "BuL", "BuR",
          "AdL", "AdR", "BdL", "BdR", "u", "d", "S", "X")
rows = {
    "YHu": {"Q": -1, "Hu": -1, "AuR": 1},
    "YSu": {"AuL": -1, "S": 1, "BuR": 1},
    "YXu": {"BuL": -1, "X": 1, "u": 1},
    "YHd": {"Q": -1, "Hd": 1, "AdR": 1},
    "YSd": {"AdL": -1, "S": 1, "BdR": 1},
    "YXd": {"BdL": -1, "X": 1, "d": 1},
    "ZAu": {"sigma": 1, "AuL": -1, "AuR": 1},
    "ZBu": {"sigma": 1, "BuL": -1, "BuR": 1},
    "ZAd": {"sigma": 1, "AdL": -1, "AdR": 1},
    "ZBd": {"sigma": 1, "BdL": -1, "BdR": 1},
}
matrix = [[F(row.get(field, 0)) for field in fields] for row in rows.values()]

def rank(a):
    a = [r[:] for r in a]
    m, n, pivot_row = len(a), len(a[0]), 0
    for col in range(n):
        pivot = next((r for r in range(pivot_row, m) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(m):
            if r != pivot_row and a[r][col]:
                q = a[r][col]
                a[r] = [x - q * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
    return pivot_row

mod2_dependencies = []
for bits in itertools.product((0, 1), repeat=len(matrix)):
    if any(bits) and all(sum(bits[i] * int(matrix[i][j])
                             for i in range(len(matrix))) % 2 == 0
                         for j in range(len(fields))):
        mod2_dependencies.append(bits)

checks = {
    "ten_interactions_registered": len(matrix) == 10,
    "sixteen_fields_registered": len(fields) == 16,
    "signed_incidence_has_full_row_rank": rank(matrix) == 10,
    "continuous_phase_cycle_nullity_is_zero": len(matrix) - rank(matrix) == 0,
    "sign_cycle_kernel_is_zero": mod2_dependencies == [],
    "up_doublet_is_conjugated": rows["YHu"]["Hu"] == -1,
    "up_down_hypercharge_gap_is_one": F(2, 3) - F(-1, 3) == 1,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP634", "status": "PASS", "checks": checks,
    "incidence_shape": [10, 16], "continuous_rank": rank(matrix),
    "continuous_cycle_nullity": 0, "sign_cycle_count": 0,
    "classification": "no internal rephasing-invariant interference cycle; neither selector nor instrument",
    "smallest_exact_falsifier": "full row rank ten of the signed interaction incidence",
    "successor_gate": "add an independently derived gauge-legal cycle-closing carrier and recompute thresholds",
}
(ROOT / "results" / "wp634_messenger_incidence_cycle_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

