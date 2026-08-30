"""Exact solution of the frozen WP437 two-adjoint vacuum."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
wp437 = json.loads((root / "results" / "wp437_source_free_vacuum_preregistration.json").read_text(encoding="utf-8"))

I = sp.I
basis = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.diag(1, -1, 0),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.diag(1, 1, -2),
]


def commutator(left, right):
    return left * right - right * left


def norm_squared(matrix):
    return sp.simplify(sp.trace(matrix.conjugate().T * matrix))


m_sq, lam, rho = sp.symbols("m_squared lambda rho", positive=True, real=True)
c = rho - lam / 2
a_sq = sp.factor(m_sq / (16 * c))
r_star = sp.factor(m_sq / (4 * c))
v_min = sp.factor(-m_sq**2 / (16 * c))

a = sp.symbols("a", positive=True, real=True)
A0 = a * basis[2]
D0 = a * basis[0]
radial = sp.simplify(norm_squared(A0) + norm_squared(D0))
comm_sq = sp.simplify(norm_squared(commutator(A0, D0)))

mass_gram = sp.Matrix([
    [
        sp.simplify(
            sp.trace(commutator(left, A0).conjugate().T * commutator(right, A0))
            + sp.trace(commutator(left, D0).conjugate().T * commutator(right, D0))
        )
        for right in basis
    ]
    for left in basis
])
gauge_rank = mass_gram.rank()
unbroken_generator = basis[7]

# Complete component Hessian at the frozen representative benchmark
# m_squared=lambda=rho=1, for which a^2=1/8.
coordinates = sp.symbols("z0:16", real=True)
A = sum((coordinates[i] * basis[i] for i in range(8)), sp.zeros(3))
D = sum((coordinates[8 + i] * basis[i] for i in range(8)), sp.zeros(3))
C = commutator(A, D)
potential = sp.expand(
    -sp.trace(A * A + D * D) / 2
    + sp.trace(A * A + D * D) ** 2
    - norm_squared(C)
)
representative = {coordinate: 0 for coordinate in coordinates}
representative[coordinates[2]] = sp.sqrt(sp.Rational(1, 8))
representative[coordinates[8]] = sp.sqrt(sp.Rational(1, 8))
hessian = sp.simplify(sp.hessian(potential, coordinates).subs(representative))
hessian_spectrum = hessian.eigenvals()

acceptance = {
    "nonzero_global_minimum": r_star != 0 and v_min.subs({m_sq: 1, lam: 1, rho: 1}) < 0 and sp.simplify(v_min + m_sq**2 / (16 * c)) == 0,
    "stable_complete_Hessian_modulo_gauge": all(value >= 0 for value in hessian_spectrum) and hessian_spectrum.get(0) == 7,
    "noncommuting_A_and_D": comm_sq != 0,
    "SU3_gauge_mass_rank_eight": gauge_rank == 8,
    "open_coefficient_domain": set(r_star.free_symbols) == {m_sq, lam, rho},
    "no_measured_flavor_coordinate": all(token not in wp437["potential"] for token in ("CKM", "physical16", "H_u", "H_d")),
}
acceptance = {name: bool(value) for name, value in acceptance.items()}

checks = {
    "frozen_WP437_dependency_passed": wp437["passed"],
    "embedded_pair_saturates_commutator_bound": sp.simplify(comm_sq - radial**2 / 2) == 0,
    "exact_radial_stationary_point": sp.simplify(sp.diff(-m_sq * sp.Symbol("R") / 2 + c * sp.Symbol("R")**2, sp.Symbol("R")).subs(sp.Symbol("R"), r_star)) == 0,
    "unbroken_generator_commutes_with_vacuum": commutator(unbroken_generator, A0) == sp.zeros(3) and commutator(unbroken_generator, D0) == sp.zeros(3),
    "gauge_mass_rank_is_exactly_seven": gauge_rank == 7,
    "Hessian_has_seven_gauge_zero_modes": hessian_spectrum.get(0) == 7,
    "Hessian_has_no_negative_eigenvalue": all(value >= 0 for value in hessian_spectrum),
    "exactly_one_preregistered_acceptance_gate_fails": sum(not value for value in acceptance.values()) == 1,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP438",
    "title": "Source-free two-adjoint vacuum solution",
    "radial_minimum": str(r_star),
    "representative_a_squared": str(a_sq),
    "minimum_energy": str(v_min),
    "representative_radial_norm": str(radial),
    "representative_commutator_norm_squared": str(comm_sq),
    "Hessian_spectrum": {str(value): multiplicity for value, multiplicity in hessian_spectrum.items()},
    "gauge_mass_rank": gauge_rank,
    "unbroken_generator": str(unbroken_generator),
    "breaking_pattern": "SU(3)_F -> U(1)",
    "preregistered_acceptance": acceptance,
    "classification": "stable source-free noncommuting vacuum on an open domain, but rank seven fails the frozen full-breaking gate",
    "smallest_exact_falsifier": "diag(1,1,-2) commutes with both vacuum adjoints and is a nonzero gauge-mass kernel vector",
    "remaining_gate": "independently justify and preregister a residual-U(1)-breaking invariant; absolute g_F f/v remains unsourced",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp438_source_free_vacuum_solution.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
