import json

import sympy as sp


z, tau, m = sp.symbols("z tau m", real=True)
S = sp.Rational(1, 2) + m * (z**2 - sp.Rational(1, 4)) * sp.cosh(z)
A = m * (z**2 - sp.Rational(1, 4)) * sp.sinh(z)

collision_equation = (
    2 * tau * sp.cos(tau)
    - (tau**2 + sp.Rational(1, 4)) * sp.sin(tau)
)
tau_star = sp.nsolve(collision_equation, 1, tol=sp.Float("1e-60"), prec=70)
m_star = sp.N(
    sp.Rational(1, 2)
    / ((tau_star**2 + sp.Rational(1, 4)) * sp.cos(tau_star)),
    60,
)

hostile_mass = sp.Rational(1, 2)
hostile_root = sp.nsolve(
    S.subs(m, hostile_mass),
    sp.Float("0.43") - sp.Float("1.08") * sp.I,
    tol=sp.Float("1e-60"),
    prec=70,
)
hostile_A = sp.N(A.subs({m: hostile_mass, z: hostile_root}), 50)

double_value = sp.N(S.subs({m: m_star, z: sp.I * tau_star}), 40)
double_derivative = sp.N(
    sp.diff(S, z).subs({m: m_star, z: sp.I * tau_star}), 40
)

checks = {
    "collision_mass_is_positive": float(m_star) > 0,
    "collision_is_double": abs(complex(double_value)) < 1e-30
    and abs(complex(double_derivative)) < 1e-30,
    "hostile_mass_is_below_collision": float(hostile_mass) < float(m_star),
    "hostile_zero_is_in_open_strip": abs(float(sp.re(hostile_root))) < 0.5,
    "hostile_zero_is_off_seam": abs(float(sp.re(hostile_root))) > 0.4,
    "hostile_scalar_residual_is_small": abs(
        complex(sp.N(S.subs({m: hostile_mass, z: hostile_root}), 30))
    )
    < 1e-25,
    "antisymmetric_real_quadrature_detects_split": abs(float(sp.re(hostile_A)))
    > 0.5,
}

result = {
    "schema": "marici.aspect.one-atom-radial-mass-collision.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "collision_tau": str(sp.N(tau_star, 25)),
    "collision_mass": str(sp.N(m_star, 25)),
    "hostile_zero": str(sp.N(hostile_root, 25)),
    "hostile_antisymmetric_port": str(sp.N(hostile_A, 25)),
    "interpretation": (
        "A scalar radial-mass change in a positive one-atom source splits a "
        "double seam zero into an off-seam quartet."
    ),
}

print(json.dumps(result, indent=2))
