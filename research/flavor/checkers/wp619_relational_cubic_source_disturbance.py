"""Exact WP619 lift of relational odd cubics into a physical source action."""

import json
from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

r, lam = sp.symbols("r lambda", real=True)
s = sp.symbols("s", integer=True)

# WP618 lens X(r)=diag(1+r,1-r,-2), with an explicit global sign sheet s.
Q = sp.expand(6 * s * (r**2 - 1))
R = sp.Integer(-6)
cross_energy = sp.expand(-lam * Q * R)
cross_force = sp.diff(cross_energy, r)
target_r = sp.Rational(3, 5)
target_force = sp.simplify(cross_force.subs(r, target_r))

# The abstract simultaneous-reflection quotient.
raw_signs = list(product((-1, 1), repeat=2))
orbits = []
remaining = set(raw_signs)
while remaining:
    state = min(remaining)
    orbit = {state, (-state[0], -state[1])}
    orbits.append(sorted(orbit))
    remaining -= orbit
orbit_products = [orbit[0][0] * orbit[0][1] for orbit in orbits]

# Exact positive Gaussian mediator example. Eliminating mediators produces a
# positive-semidefinite Gram kernel K in the quadratic form -(Q,R)K(Q,R)^T/2.
g_q, g_r, mass_sq = sp.Integer(2), sp.Integer(3), sp.Integer(5)
K = sp.Matrix(
    [
        [g_q**2 / mass_sq, g_q * g_r / mass_sq],
        [g_q * g_r / mass_sq, g_r**2 / mass_sq],
    ]
)
pure_cross = sp.Matrix([[0, 1], [1, 0]])

checks = {
    "quark_cubic_matches_wp618_lens": Q.subs(s, 1) == 6 * (r**2 - 1),
    "reference_cubic_is_nonzero": R == -6,
    "simultaneous_reflection_has_two_orbits": len(orbits) == 2,
    "relative_product_character_is_faithful_on_orbits":
        sorted(orbit_products) == [-1, 1],
    "polynomial_cross_term_moves_target":
        target_force == sp.Rational(216, 5) * lam * s,
    "nonzero_cross_coupling_cannot_leave_target_stationary_by_itself":
        target_force.subs({lam: 1, s: 1}) != 0,
    "gaussian_kernel_is_positive_semidefinite":
        K.det() == 0 and K.trace() > 0 and all(value >= 0 for value in K.eigenvals()),
    "gaussian_cross_saturates_cauchy_bound":
        K[0, 1] ** 2 == K[0, 0] * K[1, 1],
    "pure_cross_kernel_is_not_positive_semidefinite":
        pure_cross.det() == -1 and sorted(pure_cross.eigenvals()) == [-1, 1],
    "pure_cross_has_zero_self_nonzero_cross_and_is_therefore_indefinite":
        not (
            pure_cross[0, 0] > 0
            or pure_cross[1, 1] > 0
        )
        and pure_cross[0, 1] != 0,
}

if not all(checks.values()):
    raise SystemExit(f"WP619 check failed: {checks}")

result = {
    "work_package": "WP619",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "WP618 continuous charge lenses with global sign sheet s, the source-derived H cubic R=-6, and positive-mass Gaussian mediator completions",
    "odd_ports": {
        "quark_lens": "Q(s,r)=6 s (r^2-1)",
        "reference": "R=Tr(H^3)=-6",
    },
    "abstract_contextual_partition": "four raw sign packets reduce to two simultaneous-reflection orbits, separated exactly by sign(QR)",
    "polynomial_source_term": "-lambda Q R",
    "target_force": "d(-lambda Q R)/dr at r=3/5 equals (216/5) lambda s",
    "disturbance_classification": "the cross term selects relative sign on the discrete quotient but generically moves the continuous portal magnitude; it is not a noninvasive selector of the target lens",
    "gaussian_completion": {
        "couplings": ["2", "3"],
        "mass_squared": "5",
        "kernel": [["4/5", "6/5"], ["6/5", "9/5"]],
        "determinant": "0",
        "rule": "positive Gaussian elimination makes the cross kernel a Gram matrix, so a nonzero cross channel requires nonzero self channels",
    },
    "smallest_exact_falsifier": "at r=3/5, every nonzero lambda produces the nonzero force (216/5) lambda s",
    "ordinary_probe": "the WP618 root-vector mass-square ratio measures r and must remain 1:4:9 if the target magnitude is preserved",
    "relational_probe": "a coherent H-referenced interference record measures the relative sign orbit",
    "joint_experiment": "measure the three root-vector masses and the H-referenced interference sign in the same prepared run; sign selection accompanied by a shifted mass ratio falsifies noninvasive orientation",
    "instrument_gate": "derive mediator couplings and self-channel counterterms independently, include finite widths and common lineage calibration, and show target stationarity survives the complete source potential",
    "remaining_source_gate": "supply an independently selected magnitude potential whose stationary equation remains at r=3/5 after the unavoidable relational coupling; fitting its counterforce is target encoding",
}

out = ROOT / "results" / "wp619_relational_cubic_source_disturbance.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
