"""Exact WP601 D5 cubic-versus-shaping generalized-CP tradeoff."""

import json
from pathlib import Path

import sympy as sp


x, y, u, v = sp.symbols("x y u v", real=True)
alpha, beta, gamma = sp.symbols("alpha beta gamma", real=True)
z_phi = x + sp.I * y
z_psi = u + sp.I * v
cubic = sp.expand(sp.re(z_phi * z_psi**2))


def rotation(angle):
    return sp.Matrix(
        [[sp.cos(angle), -sp.sin(angle)], [sp.sin(angle), sp.cos(angle)]]
    )


C = sp.diag(1, -1)
d5_rotation = sp.diag(rotation(2 * sp.pi / 5), rotation(4 * sp.pi / 5))
d5_cp = sp.diag(C, C)
variables = (x, y, u, v)
source_vector = sp.Matrix(variables)


def invariant_under(polynomial, generator):
    transformed = generator * source_vector
    substitution = {
        variable: transformed[index]
        for index, variable in enumerate(variables)
    }
    difference = sp.Poly(
        sp.expand(polynomial.subs(substitution, simultaneous=True) - polynomial),
        *variables,
    )
    return all(
        sp.radsimp(sp.trigsimp(coefficient)) == 0
        for coefficient in difference.coeffs()
    )


cubic_slice = sp.trigsimp(
    cubic.subs(
        {
            x: sp.cos(alpha),
            y: sp.sin(alpha),
            u: sp.cos(beta),
            v: sp.sin(beta),
        }
    )
)
cubic_gradient = sp.simplify(
    sp.Matrix(
        [
            sp.diff(gamma * sp.cos(alpha + 2 * beta), alpha),
            sp.diff(gamma * sp.cos(alpha + 2 * beta), beta),
        ]
    ).subs({alpha: 0, beta: sp.pi / 5})
)

charge_census = []
for q_phi in range(5):
    for q_psi in range(5):
        cubic_charge = (q_phi + 2 * q_psi) % 5
        determinant = (q_psi - 2 * q_phi) % 5
        forbids_cubic = cubic_charge != 0
        independent_from_d5_rotation = determinant != 0
        charge_census.append(
            {
                "q_phi": q_phi,
                "q_psi": q_psi,
                "cubic_charge": cubic_charge,
                "forbids_cubic": forbids_cubic,
                "independent_from_d5_rotation": independent_from_d5_rotation,
            }
        )

forbidding_charges = [item for item in charge_census if item["forbids_cubic"]]
allowing_charges = [item for item in charge_census if not item["forbids_cubic"]]
extremum_pairs = [(m, n) for m in range(10) for n in range(10)]
independent_cp_stabilizers = [
    {
        "angles": (m, n),
        "rotation_powers": (m % 5, n % 5),
        "fixes_pair": (2 * (m % 5) - 2 * m) % 10 == 0
        and (2 * (n % 5) - 2 * n) % 10 == 0,
    }
    for m, n in extremum_pairs
]

checks = {
    "mixed_cubic_is_common_d5_invariant": invariant_under(cubic, d5_rotation),
    "mixed_cubic_is_bare_cp_even": invariant_under(cubic, d5_cp),
    "cubic_real_slice_is_cos_alpha_plus_two_beta": sp.trigsimp(
        cubic_slice - sp.cos(alpha + 2 * beta)
    )
    == 0,
    "cubic_moves_wp600_candidate": sp.simplify(
        cubic_gradient
        - sp.Matrix(
        [
            -gamma * sp.sin(2 * sp.pi / 5),
            -2 * gamma * sp.sin(2 * sp.pi / 5),
        ]
        )
    )
    == sp.zeros(2, 1),
    "twenty_z5_charge_pairs_forbid_cubic": len(forbidding_charges) == 20,
    "every_cubic_forbidding_charge_is_independent": all(
        item["independent_from_d5_rotation"] for item in forbidding_charges
    ),
    "every_dependent_charge_allows_cubic": all(
        not item["independent_from_d5_rotation"] for item in allowing_charges
    ),
    "independent_rotations_stabilize_every_quintic_extremum_pair": len(
        independent_cp_stabilizers
    )
    == 100
    and all(item["fixes_pair"] for item in independent_cp_stabilizers),
}

if not all(checks.values()):
    raise SystemExit(f"WP601 check failed: {checks}")

result = {
    "work_package": "WP601",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "domain": "two faithful D5 doublets of weights one and two, plus one arbitrary diagonal Z5 shaping charge",
    "allowed_cubic": "Re(z_phi*z_psi^2)=cos(alpha+2*beta) on the unit-radius slice",
    "candidate_gradient": ["-gamma*sin(2*pi/5)", "-2*gamma*sin(2*pi/5)"],
    "charge_theorem": "a Z5 charge forbids the cubic exactly only if it is linearly independent of the D5 rotation charge (1,2); together they then generate independent C5 rotations of both doublets",
    "classification": "D5 cubic-versus-generalized-CP shaping tradeoff; the WP600 quartic window does not extend to a complete renormalizable selector",
    "smallest_exact_falsifier": "the unshaped cubic moves the candidate, while every shaping charge that forbids it restores componentwise generalized CP",
    "surviving_architecture_gate": "use a non-diagonal non-abelian selection rule, gauge locality, or collective breaking that forbids the cubic without generating independent rotations",
    "instrument_gate": "unchanged: no source-to-physical16 and threshold joint instrument exists",
    "charge_census": charge_census,
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp601_d5_cubic_shaping_cp_tradeoff.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
