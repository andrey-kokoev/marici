"""Exact WP620 coupled-stationarity fiber for the relational cubic source."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

r = sp.symbols("r", real=True)
lam, kap = sp.symbols("lambda kappa", positive=True, real=True)
s = sp.symbols("s", integer=True)
z = sp.expand(36 * s * (1 - r**2))
potential = sp.expand(-lam * z + kap * z**2)
force = sp.factor(sp.diff(potential, r))

target_r = sp.Rational(3, 5)
target_s = sp.Integer(1)
target_z = sp.simplify(z.subs({r: target_r, s: target_s}))
tuned_ratio = sp.simplify(1 / (2 * target_z))
tuned_potential = sp.factor(
    potential.subs(kap, tuned_ratio * lam)
)
tuned_force = sp.factor(force.subs(kap, tuned_ratio * lam))

stationary_minima = [
    (1, sp.Rational(3, 5)),
    (1, sp.Rational(-3, 5)),
    (-1, sp.sqrt(41) / 5),
    (-1, -sp.sqrt(41) / 5),
]
stationary_maxima = [(1, sp.Integer(0)), (-1, sp.Integer(0))]

second_derivative = sp.diff(potential, r, 2)
tuned_second_derivatives = {
    f"s={sheet},r={point}": sp.simplify(
        second_derivative.subs(
            {s: sheet, r: point, kap: tuned_ratio * lam}
        )
    )
    for sheet, point in stationary_minima + stationary_maxima
}

hostile_ratio = sp.Rational(1, 32)
hostile_r = sp.sqrt(sp.Rational(5, 9))
hostile_force = sp.simplify(
    force.subs({s: 1, r: hostile_r, kap: hostile_ratio * lam})
)
target_force_under_hostile_ratio = sp.simplify(
    force.subs({s: 1, r: target_r, kap: hostile_ratio * lam})
)

def mass_squares(point):
    return [
        sp.simplify((2 * point) ** 2),
        sp.simplify((3 - point) ** 2),
        sp.simplify((3 + point) ** 2),
    ]


target_masses = sorted(mass_squares(target_r))
hostile_sheet_r = sp.sqrt(41) / 5
hostile_sheet_masses = mass_squares(hostile_sheet_r)

checks = {
    "target_relational_coordinate_is_exact": target_z == sp.Rational(576, 25),
    "target_stationarity_requires_tuned_ratio":
        tuned_ratio == sp.Rational(25, 1152),
    "tuned_potential_is_complete_square":
        sp.simplify(
            tuned_potential
            - tuned_ratio * lam * (z - target_z) ** 2
            + tuned_ratio * lam * target_z**2
        )
        == 0,
    "all_four_nonzero_stationary_points_are_minima": all(
        value > 0
        for key, value in tuned_second_derivatives.items()
        if ",r=0" not in key
    ),
    "both_zero_points_are_maxima": all(
        value < 0
        for key, value in tuned_second_derivatives.items()
        if ",r=0" in key
    ),
    "full_real_domain_has_hostile_outer_sheet":
        sp.simplify(z.subs({s: -1, r: hostile_sheet_r}) - target_z) == 0,
    "target_support_component_excludes_outer_sheet":
        abs(target_r) < 1 and hostile_sheet_r > 1,
    "cubic_zero_is_domain_boundary":
        sp.solve(sp.Eq(z.subs(s, 1), 0), r) == [-1, 1],
    "hostile_coefficient_moves_minimum":
        hostile_force == 0 and target_force_under_hostile_ratio != 0,
    "target_mass_square_pattern_is_one_four_nine":
        [sp.simplify(value / target_masses[0]) for value in target_masses]
        == [1, 4, 9],
    "outer_sheet_has_distinct_mass_spectrum":
        hostile_sheet_masses != mass_squares(target_r),
}

if not all(checks.values()):
    raise SystemExit(f"WP620 check failed: {checks}")
checks = {key: bool(value) for key, value in checks.items()}

result = {
    "work_package": "WP620",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "the complete real WP619 lens coordinates (s,r), with z=QR=36s(1-r^2), and the smallest bounded polynomial V=-lambda z+kappa z^2",
    "target_coordinate": "z0=576/25 at (s,r)=(1,3/5)",
    "required_coefficient_ratio": "kappa/lambda=25/1152",
    "stationary_minima": [
        {"s": sheet, "r": str(point)}
        for sheet, point in stationary_minima
    ],
    "stationary_maxima": [
        {"s": sheet, "r": str(point)}
        for sheet, point in stationary_maxima
    ],
    "contextual_partition": "on the full real domain the tuned potential has four minima; on the source component s=1 and |r|<1 it has the target pair r=+-3/5, related by the first-two-family permutation",
    "domain_boundary": "Q=0 at |r|=1; crossing it changes the sign-character chart and reaches the hostile s=-1 outer minima r=+-sqrt(41)/5",
    "classification": "conditional coupled magnitude-and-relative-orientation selector only after inserting the exact ratio 25/1152 and restricting to a source-authorized cubic-sign component; otherwise a fitted potential with extra minima",
    "smallest_exact_falsifier": "kappa/lambda=1/32 moves the inner minimum to r=sqrt(5)/3 and gives nonzero force at r=3/5",
    "physical_probe": "same-lineage root-vector masses distinguish the target 1:4:9 spectrum from the outer-sheet spectrum, while H-referenced interference resolves the relational sign component",
    "instrument_gate": "experimentally establish the cubic-sign support component without conditioning on the desired record, resolve all vector masses and interference, and measure the independent mediator parameters determining kappa/lambda",
    "remaining_source_gate": "derive 25/1152 and the |r|<1 support component from a fixed representation or mediator multiplicity; neither follows from the two-adjoint vacuum",
}

out = ROOT / "results" / "wp620_coupled_stationarity_fiber.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
