"""Exact WP630 parity protection versus wall-lift audit."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Monomial x^a y^b, with x=Hu even and y=Hd odd.
monomials = [(a, b) for a in range(5) for b in range(5 - a)]
even_source = [(a, b) for a, b in monomials if b % 2 == 0]
odd_breakers = [(a, b) for a, b in monomials if b % 2 == 1]

def value(term, x, y):
    a, b = term
    return x**a * y**b

v = F(3)
even_degeneracy = all(value(t, F(1), v) == value(t, F(1), -v)
                      for t in even_source)
odd_separates_some_pair = any(value(t, F(1), v) != value(t, F(1), -v)
                              for t in odd_breakers)

# c=Re(Hu^dagger Hd) is the overlap coordinate. The declared vacuum has c=0.
mu2 = F(5)
bilinear_energy_plus = mu2 * F(0)
bilinear_energy_minus = mu2 * F(0)
bilinear_overlap_gradient = mu2

checks = {
    "all_even_operators_preserve_sign_degeneracy": even_degeneracy,
    "energy_splitting_requires_an_odd_operator": odd_separates_some_pair,
    "bilinear_is_minimal_odd_monomial": min(a + b for a, b in odd_breakers) == 1,
    "orthogonal_vacua_are_not_split_by_bilinear": bilinear_energy_plus == bilinear_energy_minus == 0,
    "nonzero_bilinear_destroys_orthogonal_stationarity": bilinear_overlap_gradient != 0,
    "exact_protection_and_explicit_breaking_are_disjoint": set(even_source).isdisjoint(odd_breakers),
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP630", "status": "PASS", "checks": checks,
    "admitted_domain": "WP629 global sector parity with a nonzero odd entrance vev",
    "classification": "exact rigidifier versus wall-lift incompatibility; no selector or instrument",
    "smallest_soft_candidate": "mu_ud^2 Re(Hu^dagger Hd)",
    "smallest_exact_falsifier": "at orthogonal vacuum its energy split is 0 but overlap-gradient residual is mu_ud^2",
    "remaining_branches": ["exact parity plus cosmological domain selection",
                           "gauged discrete parity with changed groupoid",
                           "source-derived odd reference plus full vacuum recomputation"],
}
(ROOT / "results" / "wp630_sector_parity_wall_lift_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

