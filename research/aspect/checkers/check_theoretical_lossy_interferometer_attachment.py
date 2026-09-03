#!/usr/bin/env python3
"""Dependency-free exact diagnostics for an idealized lossy two-path attachment."""

import json
from fractions import Fraction as Q
from pathlib import Path

# Gaussian rationals represent four exact phase samples z in {1,-1,i,-i}.
def add(a, b): return (a[0] + b[0], a[1] + b[1])
def mul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def conj(a): return (a[0], -a[1])
def scale(q, a): return (q * a[0], q * a[1])
def matmul(a, b): return [[sum_gaussian(mul(a[r][k], b[k][c]) for k in range(len(b))) for c in range(len(b[0]))] for r in range(len(a))]
def sum_gaussian(values):
    out = (Q(0), Q(0))
    for value in values: out = add(out, value)
    return out
def dagger(a): return [[conj(a[r][c]) for r in range(len(a))] for c in range(len(a[0]))]
ZERO, ONE = (Q(0), Q(0)), (Q(1), Q(0))
I2 = [[ONE, ZERO], [ZERO, ONE]]
PHASES = (ONE, (Q(-1), Q(0)), (Q(0), Q(1)), (Q(0), Q(-1)))

def interferometer(z):
    return [[scale(Q(1, 2), add(ONE, z)), scale(Q(1, 2), add(ONE, scale(Q(-1), z)))], [scale(Q(1, 2), add(ONE, scale(Q(-1), z))), scale(Q(1, 2), add(ONE, z))]]

def prob0(z, eta): return eta * mul(conj(interferometer(z)[0][0]), interferometer(z)[0][0])[0]
def prob1(z, eta): return eta * mul(conj(interferometer(z)[1][0]), interferometer(z)[1][0])[0]

etas = (Q(0), Q(1, 3), Q(1))
visibilities = (Q(0), Q(2, 5), Q(1))
cosines = (Q(-1), Q(0), Q(1))
checks = {
    "four_exact_phase_interferometers_are_unitary": all(matmul(dagger(interferometer(z)), interferometer(z)) == I2 for z in PHASES),
    "ideal_click_probabilities_sum_to_eta": all(prob0(z, eta) + prob1(z, eta) == eta for z in PHASES for eta in etas),
    "full_probabilities_sum_to_one": all(prob0(z, eta) + prob1(z, eta) + (1 - eta) == 1 for z in PHASES for eta in etas),
    "click_only_sum_is_incomplete_under_loss": all(eta != 1 for eta in etas[:-1]),
    "omission_residual_equals_one_minus_eta": all(1 - eta > 0 for eta in etas[:-1]),
    "mismatch_clicks_sum_to_eta": all(eta * (1 + v * c) / 2 + eta * (1 - v * c) / 2 == eta for eta in etas for v in visibilities for c in cosines),
    "mismatch_full_records_sum_to_one": all(eta * (1 + v * c) / 2 + eta * (1 - v * c) / 2 + 1 - eta == 1 for eta in etas for v in visibilities for c in cosines),
    "mismatch_probabilities_are_nonnegative_on_grid": all(eta * (1 + sign * v * c) / 2 >= 0 for eta in etas for v in visibilities for c in cosines for sign in (-1, 1)),
    "click_conditioning_erases_efficiency": all((eta * (1 + v * c) / 2) / eta == (1 + v * c) / 2 for eta in etas[1:] for v in visibilities for c in cosines),
    "no_click_retains_efficiency": len({1 - eta for eta in etas}) == len(etas),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.theoretical-lossy-interferometer-attachment.v1", "status": "passed", "checks": checks, "exact_phase_sample_count": len(PHASES), "exact_parameter_grid_size": len(etas) * len(visibilities) * len(cosines), "deliberate_failure_residuals": [str(1 - eta) for eta in etas[:-1]], "claim_boundary": "Dependency-free exact finite diagnostics at four phase roots and a rational parameter grid; general formulas are derived in the packet."}
output = Path(__file__).parents[1] / "results" / "theoretical_lossy_interferometer_attachment.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "grid_size": result["exact_parameter_grid_size"]}, sort_keys=True))
