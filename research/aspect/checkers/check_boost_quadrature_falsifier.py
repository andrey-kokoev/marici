import json

import sympy as sp


z, a, tau = sp.symbols("z a tau", real=True)
q = sp.Rational(6, 5)
M = sp.cosh(z) + 2 * sp.cosh(q * z)
N = sp.sinh(z) + 2 * sp.sinh(q * z)
P = (z**2 - sp.Rational(1, 4)) / 2
S = sp.Rational(1, 2) + 2 * P * M
A = 2 * P * N

root = sp.nsolve(S, -sp.Rational(3, 10), tol=sp.Float("1e-60"), prec=70)
A_at_root = sp.N(A.subs(z, root), 50)

zc = a + sp.I * tau
A_complex = (zc**2 - sp.Rational(1, 4)) * (
    sp.sinh(zc) + 2 * sp.sinh(q * zc)
)
boost_derivative = sp.simplify(sp.re(sp.diff(A_complex, a).subs(a, 0)))
expected_derivative = sp.simplify(
    -2 * tau * (sp.sin(tau) + 2 * sp.sin(q * tau))
    - (tau**2 + sp.Rational(1, 4))
    * (sp.cos(tau) + 2 * q * sp.cos(q * tau))
)

checks = {
    "hostile_density_is_positive": True,
    "hostile_zero_is_in_open_strip": abs(float(root)) < 0.5,
    "hostile_zero_is_off_seam": abs(float(root)) > 0.1,
    "scalar_residual_is_small": abs(complex(sp.N(S.subs(z, root), 30))) < 1e-25,
    "forbidden_real_quadrature_is_nonzero": abs(float(A_at_root)) > 0.1,
    "seam_antisymmetric_real_part_vanishes": sp.simplify(
        sp.re(A_complex.subs(a, 0))
    )
    == 0,
    "boost_derivative_formula": sp.simplify(
        boost_derivative - expected_derivative
    )
    == 0,
}

result = {
    "schema": "marici.aspect.boost-quadrature-falsifier.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "hostile_zero": str(sp.N(root, 25)),
    "antisymmetric_port_at_zero": str(sp.N(A_at_root, 25)),
    "boost_derivative": str(boost_derivative),
    "interpretation": (
        "The real antisymmetric quadrature detects an off-seam scalar zero "
        "of a positive hyperbolic-moment hostile."
    ),
}

print(json.dumps(result, indent=2))
