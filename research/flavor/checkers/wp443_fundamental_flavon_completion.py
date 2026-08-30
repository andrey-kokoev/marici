"""Exact WP443 checker for the minimal fundamental-flavon completion."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp438 = json.loads((root / "results" / "wp438_source_free_vacuum_solution.json").read_text(encoding="utf-8"))
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


def norm_squared(matrix):
    return sp.simplify(sp.trace(matrix.conjugate().T * matrix))


z = sp.symbols("z0:16", real=True)
p = sp.symbols("p0:3", real=True)
q = sp.symbols("q0:3", real=True)
coordinates = list(z)+list(p)+list(q)
A = sum((z[i]*basis[i] for i in range(8)), sp.zeros(3))
D = sum((z[8+i]*basis[i] for i in range(8)), sp.zeros(3))
phi = sp.Matrix([p[i]+I*q[i] for i in range(3)])
R = sp.trace(A*A+D*D)
commutator = A*D-D*A
phi_norm = (phi.conjugate().T*phi)[0]
portal = (phi.conjugate().T*(A*A+D*D)*phi)[0]

# Frozen exact benchmark m^2=lambda=rho=mu^2=kappa=tau=1.
potential = sp.expand(-R/2+R**2-norm_squared(commutator)-phi_norm+phi_norm**2+portal)
vacuum = {coordinate: 0 for coordinate in coordinates}
vacuum[z[2]] = sp.sqrt(sp.Rational(1, 8))
vacuum[z[8]] = sp.sqrt(sp.Rational(1, 8))
vacuum[p[2]] = sp.sqrt(sp.Rational(1, 2))
A0, D0, phi0 = A.subs(vacuum), D.subs(vacuum), phi.subs(vacuum)
hessian = sp.hessian(potential, coordinates).subs(vacuum)
spectrum = hessian.eigenvals()

# Infinitesimal gauge tangents in the same 22 real coordinates.
gauge_tangents = []
for generator in basis:
    delta_a = I*(generator*A0-A0*generator)
    delta_d = I*(generator*D0-D0*generator)
    delta_phi = I*generator*phi0
    vector = []
    for matrix in (delta_a, delta_d):
        vector.extend([sp.simplify(sp.trace(matrix*b)/sp.trace(b*b)) for b in basis])
    vector.extend([sp.re(delta_phi[i]).expand(complex=True) for i in range(3)])
    vector.extend([sp.im(delta_phi[i]).expand(complex=True) for i in range(3)])
    gauge_tangents.append(vector)
gauge_rank = sp.Matrix(gauge_tangents).T.rank()

checks = {
    "wp438_dependency_passed": wp438["passed"],
    "portal_is_positive_gram": sp.simplify(portal-norm_squared(A*phi)-norm_squared(D*phi)) == 0,
    "vacuum_is_stationary_in_all_22_components": all(sp.diff(potential, coordinate).subs(vacuum) == 0 for coordinate in coordinates),
    "vacuum_saturates_separate_global_lower_bounds": sp.simplify(potential.subs(vacuum)+sp.Rational(3, 8)) == 0 and portal.subs(vacuum) == 0,
    "adjoints_are_noncommuting": commutator.subs(vacuum) != sp.zeros(3),
    "fundamental_breaks_residual_generator": basis[7]*phi0 != sp.zeros(3),
    "full_gauge_orbit_has_rank_eight": gauge_rank == 8,
    "hessian_has_exactly_eight_zero_modes": spectrum.get(0) == 8,
    "all_nongauge_hessian_modes_are_positive": all(value > 0 for value in spectrum if value != 0),
    "zero_modes_equal_full_gauge_orbit": spectrum.get(0) == gauge_rank,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP443",
    "state_domain": "Two traceless Hermitian SU(3)_F adjoints plus one complex fundamental scalar.",
    "potential": "V437 - mu^2 phi^dagger phi + kappa(phi^dagger phi)^2 + tau phi^dagger(A^2+D^2)phi",
    "coefficient_domain": "WP437 open domain with mu^2>0, kappa>0, tau>0; exact stability certified at the unit benchmark and hence on a neighborhood by spectral continuity.",
    "vacuum": {"A": "lambda3/sqrt(8)", "D": "lambda1/sqrt(8)", "phi": "e3/sqrt(2)"},
    "minimum_energy": "-3/8",
    "gauge_mass_rank": gauge_rank,
    "breaking_pattern": "SU(3)_F -> discrete stabilizer (continuous gauge rank eight)",
    "hessian_spectrum": {str(value): int(multiplicity) for value, multiplicity in spectrum.items()},
    "instrument": None,
    "classification": "Source-free, globally minimizing, fully Higgsed dynamical flavon vacuum at an exact benchmark with an open stability neighborhood.",
    "smallest_exact_falsifier": "At the unit benchmark, any ninth Hessian zero, negative physical eigenvalue, or nonzero continuous gauge kernel.",
    "remaining_gate": "The dimensionless ratio g_F f/v is still a function of independent Lagrangian masses and couplings; derive or refute its selection before applying flavor-current bounds.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp443_fundamental_flavon_completion.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
