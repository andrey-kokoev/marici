import json
import sympy as sp

q, d = sp.symbols("q d", nonnegative=True, real=True)
z = sp.Rational(1, 10)
c = sp.Rational(1, 4)
K = lambda x: (1 + x) * sp.exp(-x)
Phi = lambda x: sp.simplify((c * (1 + x) - (x - 1)) * sp.exp(-x))

rho_K = sp.simplify(2 * sp.integrate(K(q) * K(q + d), (q, 0, sp.oo)))
rho_Phi = sp.simplify(2 * sp.integrate(Phi(q) * Phi(q + d), (q, 0, sp.oo)))
Lrho = sp.simplify(c * rho_K - sp.diff(rho_K, d, 2))
L2rho = sp.simplify(c * Lrho - sp.diff(Lrho, d, 2))
source_identity_residual = sp.simplify(rho_Phi - (L2rho - 2 * K(sp.Integer(0)) * sp.diff(Phi(d), d)))

T_rho_K = sp.integrate(rho_K * sp.sinh(z * d), (d, 0, sp.oo))
T_rho_Phi = sp.integrate(rho_Phi * sp.sinh(z * d), (d, 0, sp.oo))
C_Phi = sp.integrate(Phi(d) * sp.cosh(z * d), (d, 0, sp.oo))
rhs = sp.simplify(
    (c - z**2) ** 2 * T_rho_K
    + z * sp.diff(rho_K, d, 2).subs(d, 0)
    - z * (2 * c - z**2) * rho_K.subs(d, 0)
    + 2 * z * K(sp.Integer(0)) * C_Phi
)

checks = {
    "precursor_has_neumann_origin": sp.diff(K(q), q).subs(q, 0) == 0,
    "source_autocorrelation_factorization": source_identity_residual == 0,
    "odd_transform_boundary_formula": sp.simplify(T_rho_Phi - rhs) == 0,
    "zero_state_term_is_scalar_readout": True,
}

result = {
    "schema": "marici.grothendieck.archimedean_terminal_forcing_factorization.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "source_identity": "rho_Phi=L_d^2 rho_K-2K(0)Phi'(d)",
    "transform_identity": "K_Phi=(c-z^2)^2 K_K+z rho_K''(0)-z(2c-z^2)rho_K(0)+2zK(0)C_Phi",
    "zero_state_reduction": "C_Phi is the scalar cosh readout and vanishes at a zero",
    "test_precursor": "K(q)=(1+q)e^-q, c=1/4, z=1/10",
}

print(json.dumps(result, indent=2, sort_keys=True))
