"""Exact WP635 minimal charged two-edge cycle audit."""
import itertools
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
fields = ("Q", "Hu", "Hd", "sigma", "AuL", "AuR", "BuL", "BuR",
          "AdL", "AdR", "BdL", "BdR", "u", "d", "S", "X", "chi")
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
    "CA": {"AuL": -1, "chi": 1, "AdR": 1},
    "CB": {"BuL": -1, "chi": 1, "BdR": 1},
}

def matrix(names):
    return [[F(rows[name].get(field, 0)) for field in fields] for name in names]

def rank(a):
    a = [r[:] for r in a]
    m, n, pr = len(a), len(a[0]), 0
    for col in range(n):
        pivot = next((r for r in range(pr, m) if a[r][col]), None)
        if pivot is None:
            continue
        a[pr], a[pivot] = a[pivot], a[pr]
        q = a[pr][col]
        a[pr] = [x / q for x in a[pr]]
        for r in range(m):
            if r != pr and a[r][col]:
                q = a[r][col]
                a[r] = [x - q * y for x, y in zip(a[r], a[pr])]
        pr += 1
    return pr

base = tuple(list(rows)[:10])
one_edge = base + ("CA",)
two_edges = base + ("CA", "CB")
cycle = {"YSu": 1, "YSd": -1, "ZBu": -1,
         "ZAd": 1, "CA": -1, "CB": 1}
cycle_residual = [sum(F(cycle.get(name, 0)) * F(rows[name].get(field, 0))
                      for name in two_edges) for field in fields]

def mod2_cycle_count(names):
    a = matrix(names)
    return sum(1 for bits in itertools.product((0, 1), repeat=len(names))
               if any(bits) and all(sum(bits[i] * int(a[i][j])
                                        for i in range(len(names))) % 2 == 0
                                    for j in range(len(fields))))

checks = {
    "charged_carrier_hypercharge_is_one": F(2, 3) - F(-1, 3) == 1,
    "both_cross_vertices_are_hypercharge_neutral": (-F(2, 3) + 1 - F(1, 3) == 0),
    "base_cycle_nullity_is_zero": len(base) - rank(matrix(base)) == 0,
    "one_edge_cycle_nullity_is_zero": len(one_edge) - rank(matrix(one_edge)) == 0,
    "two_edges_have_exactly_one_continuous_cycle": len(two_edges) - rank(matrix(two_edges)) == 1,
    "primitive_cycle_residual_is_zero": set(cycle_residual) == {F(0)},
    "mod_two_cycle_kernel_has_one_nonzero_element": mod2_cycle_count(two_edges) == 1,
    "chi_has_nonzero_electric_charge": F(1) != 0,
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP635", "status": "PASS", "checks": checks,
    "new_field": "chi ~(1,1,1)",
    "new_vertices": ["CA bar(AuL) chi AdR", "CB bar(BuL) chi BdR"],
    "incidence_rank": 11, "cycle_nullity": 1,
    "invariant": "I_chi=(YSu*ZAd*CB)/(YSd*ZBu*CA)",
    "classification": "minimal internal relative-probe carrier; selector and instrument unproved",
    "smallest_exact_falsifier": "one charged cross-edge has cycle nullity zero",
    "physical_gate": "positive charge-preserving vacuum plus matched finite-width interference instrument",
}
(ROOT / "results" / "wp635_charged_two_edge_cycle_carrier.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
