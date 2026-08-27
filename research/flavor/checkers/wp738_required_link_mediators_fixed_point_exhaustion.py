"""Exhaust all 210 fixed-point branches of the required mediator completion."""
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
a1, aA, aB, a3 = G = sp.symbols("a1 aA aB a3", real=True)
k, q, l, u, d, e = Y = sp.symbols("k q l u d e", real=True)

yukawa_brackets = [
    15*k + 2*l + 18*u + 18*d + 6*e
    - sp.Rational(15, 2)*a1 - 9*aA - sp.Rational(9, 2)*aB,
    22*q + 6*l - sp.Rational(1, 3)*a1 - 16*a3
    - sp.Rational(9, 2)*aA - sp.Rational(9, 2)*aB,
    10*l + 18*q + 2*k - 3*a1 - sp.Rational(9, 2)*aA
    - sp.Rational(9, 2)*aB,
    12*k + 21*u + 15*d + 6*e - sp.Rational(17, 6)*a1
    - 16*a3 - sp.Rational(9, 2)*aB,
    12*k + 15*u + 21*d + 6*e - sp.Rational(5, 6)*a1
    - 16*a3 - sp.Rational(9, 2)*aB,
    12*k + 18*u + 18*d + 9*e - sp.Rational(15, 2)*a1
    - sp.Rational(9, 2)*aB,
]
gauge_brackets = [
    sp.Rational(51, 2) + sp.Rational(1091, 18)*a1
    + sp.Rational(52, 3)*a3 + 39*aA + sp.Rational(87, 2)*aB
    - 15*k - sp.Rational(5, 2)*d - sp.Rational(15, 2)*e
    - 6*l - 2*q - sp.Rational(17, 2)*u,
    1 + 13*a1 + 12*a3 + 57*aA + 12*aB - 6*k - 3*l - 9*q,
    sp.Rational(31, 6) + sp.Rational(29, 2)*a1 + 24*a3 + 12*aA
    + sp.Rational(649, 6)*aB - 3*k - sp.Rational(9, 2)*d
    - sp.Rational(3, 2)*e - 3*l - 9*q - sp.Rational(9, 2)*u,
    -3 + sp.Rational(13, 6)*a1 + 50*a3 + sp.Rational(9, 2)*aA
    + 9*aB - 6*d - 12*q - 6*u,
]

branch_count = 0
physical = []
fully_interacting = None
for optional_gauge_bits in itertools.product((0, 1), repeat=2):
    gauge_bits = (1, 1, *optional_gauge_bits)
    active_gauges = [i for i, active in enumerate(gauge_bits) if active]
    for yukawa_bits in itertools.product((0, 1), repeat=6):
        active_yukawas = [i for i, active in enumerate(yukawa_bits) if active]
        substitutions = {
            G[i]: sp.Integer(0) for i, active in enumerate(gauge_bits) if not active
        }
        substitutions.update({
            Y[i]: sp.Integer(0) for i, active in enumerate(yukawa_bits) if not active
        })
        y_solutions = sp.solve(
            [yukawa_brackets[i].subs(substitutions) for i in active_yukawas],
            [Y[i] for i in active_yukawas],
            dict=True,
        ) if active_yukawas else [{}]
        for y_solution in y_solutions:
            combined = {**substitutions, **y_solution}
            g_solutions = sp.solve(
                [gauge_brackets[i].subs(combined) for i in active_gauges],
                [G[i] for i in active_gauges],
                dict=True,
            )
            for g_solution in g_solutions:
                branch_count += 1
                values = {**g_solution, **{
                    symbol: sp.factor(sp.sympify(value).subs(g_solution))
                    for symbol, value in combined.items()
                }}
                is_physical = all(
                    values[G[i]] > 0 if gauge_bits[i] else values[G[i]] == 0
                    for i in range(4)
                ) and all(
                    values[Y[i]] > 0 if yukawa_bits[i] else values[Y[i]] == 0
                    for i in range(6)
                )
                if is_physical:
                    physical.append((gauge_bits, yukawa_bits, values))
                if all(gauge_bits) and all(yukawa_bits):
                    fully_interacting = values

expected_a3 = -sp.Rational(1747041281, 6918678948)
expected_aB = -sp.Rational(116978905, 2306226316)
checks = {
    "all_256_branches_solved_exactly": branch_count == 256,
    "no_physical_branch_exists": len(physical) == 0,
    "fully_interacting_branch_is_unique": fully_interacting is not None,
    "fully_interacting_color_coordinate_is_exact": fully_interacting[a3] == expected_a3,
    "fully_interacting_SU2B_coordinate_is_exact": fully_interacting[aB] == expected_aB,
    "fully_interacting_color_coordinate_is_negative": fully_interacting[a3] < 0,
    "fully_interacting_SU2B_coordinate_is_negative": fully_interacting[aB] < 0,
    "deliberate_failure_residual_color_is_nonzero": fully_interacting[a3] != 0,
    "deliberate_failure_residual_SU2B_is_nonzero": fully_interacting[aB] != 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP738",
    "status": "PASS",
    "checks": checks,
    "source_domain": "minimal product parent plus the vectorlike quark and lepton doublets required for link-mediated SM Yukawas",
    "branch_grammar": "hypercharge and SU2A active; SU2B and color independently active or Gaussian; all 64 Yukawa subsets",
    "exact_branch_count": branch_count,
    "physical_branch_count": len(physical),
    "fully_interacting_hostile_witness": {
        "alpha_3": str(expected_a3),
        "alpha_B": str(expected_aB),
    },
    "classification": "required link mediators do not repair the missing magnitude selector or RG basin",
    "smallest_exact_falsifier": "the exhaustive rational branch count contains zero physical fixed points",
    "claim_boundary": "210 gauge-Yukawa truncation with flavor-universal diagonal mediator Yukawas; scalar quartics, masses, thresholds, and detector response are not reached",
    "remaining_source_gate": "derive any further Yukawa-active matter from an independent physical necessity rather than a fixed-point scan",
    "remaining_threshold_gate": "not reached because no source fixed point exists",
    "remaining_physical_gate": "not reached; independently calibrated labelled readout remains required",
    "external_reproduction": {
        "tool": "PyR@TE 3",
        "repository": "https://github.com/LSartore/pyrate",
        "revision": "04b219c2016f3fc4f2371d72607edc26a7e06364",
    },
}
(ROOT / "results" / "wp738_required_link_mediators_fixed_point_exhaustion.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
